#!/usr/bin/env python3
"""
Modelify AI - E-commerce Apparel Image Pre-check Utility

This diagnostic script validates clothing product photos before running AI model generation workflows.
It inspects:
1. File format & dimensions (works out of the box using standard library)
2. Aspect ratio compliance (optimal: 3:4 portrait or 1:1 square for Shopify/Amazon)
3. Resolution adequacy for e-commerce zoom & print requirements
4. Background corner uniformity (enhanced with optional Pillow)

Usage:
    python examples/image_precheck.py path/to/garment.jpg
"""

import sys
import os
import struct


def get_image_size(file_path: str):
    """Read image dimensions from binary header without external dependencies."""
    with open(file_path, 'rb') as f:
        head = f.read(32)
        if len(head) < 24:
            return None, None, "Unknown"

        # PNG
        if head.startswith(b'\x89PNG\r\n\x1a\n'):
            w, h = struct.unpack('>LL', head[16:24])
            return int(w), int(h), "PNG"

        # JPEG
        f.seek(0)
        if f.read(2) == b'\xff\xd8':
            f.seek(2)
            while True:
                marker_data = f.read(2)
                if len(marker_data) < 2:
                    break
                marker, = struct.unpack('>H', marker_data)
                if marker in (0xffc0, 0xffc1, 0xffc2):  # SOF markers
                    f.read(3)  # length & precision
                    h, w = struct.unpack('>HH', f.read(4))
                    return int(w), int(h), "JPEG"
                else:
                    length_data = f.read(2)
                    if len(length_data) < 2:
                        break
                    length, = struct.unpack('>H', length_data)
                    f.seek(length - 2, os.SEEK_CUR)

        # WebP
        f.seek(0)
        chunk = f.read(30)
        if chunk.startswith(b'RIFF') and chunk[8:12] == b'WEBP':
            if chunk[12:16] == b'VP8 ':
                w, h = struct.unpack('<HH', chunk[26:30])
                return int(w & 0x3fff), int(h & 0x3fff), "WebP"
            elif chunk[12:16] == b'VP8X':
                w = int.from_bytes(chunk[24:27], 'little') + 1
                h = int.from_bytes(chunk[27:30], 'little') + 1
                return int(w), int(h), "WebP"

    return None, None, "Unknown"


def analyze_image(image_path: str):
    if not os.path.exists(image_path):
        print(f"[Error] File not found: {image_path}")
        sys.exit(1)

    file_size_kb = os.path.getsize(image_path) / 1024.0

    width, height, fmt = get_image_size(image_path)

    if width is None or height is None:
        print(f"[Error] Unable to parse image dimensions for {image_path}")
        sys.exit(1)

    aspect_ratio = width / height

    print(f"\n=======================================================")
    print(f"  Modelify AI Garment Photo Diagnostic: {os.path.basename(image_path)}")
    print(f"=======================================================\n")

    print(f"[*] Basic Attributes:")
    print(f"    - Dimensions: {width} x {height} px")
    print(f"    - Format: {fmt}")
    print(f"    - File Size: {file_size_kb:.1f} KB")
    print(f"    - Aspect Ratio: {aspect_ratio:.2f} (Width / Height)")

    # 1. Resolution Check
    print(f"\n[*] Resolution Assessment:")
    if width >= 1500 and height >= 1500:
        print("    [PASS] High resolution (> 1500px). Ideal for zoomable Shopify PDP.")
    elif width >= 1000 and height >= 1000:
        print("    [ACCEPTABLE] Usable resolution; 1500px+ recommended for macro garment textures.")
    else:
        print("    [WARNING] Low resolution (< 1000px). Fabric seams and small logos may blur.")

    # 2. Aspect Ratio Check
    print(f"\n[*] Aspect Ratio Assessment:")
    if 0.70 <= aspect_ratio <= 0.80:
        print("    [OPTIMAL] Matches 3:4 portrait standard (industry standard for apparel lookbooks).")
    elif 0.95 <= aspect_ratio <= 1.05:
        print("    [OPTIMAL] Matches 1:1 square standard (ideal for Amazon / Instagram feed).")
    elif 0.50 <= aspect_ratio <= 0.60:
        print("    [OPTIMAL] Matches 9:16 vertical video / story format.")
    else:
        print(f"    [NOTICE] Non-standard ratio ({aspect_ratio:.2f}). Consider cropping/padding to 3:4 or 1:1.")

    # 3. Background Check
    print(f"\n[*] Background Uniformity:")
    try:
        from PIL import Image, ImageStat
        with Image.open(image_path) as img:
            corners = [
                img.crop((0, 0, min(20, width), min(20, height))),
                img.crop((width - min(20, width), 0, width, min(20, height))),
                img.crop((0, height - min(20, height), min(20, width), height)),
                img.crop((width - min(20, width), height - min(20, height), width, height)),
            ]
            stds = [ImageStat.Stat(c.convert("L")).stddev[0] for c in corners]
            avg_std = sum(stds) / len(stds)
            if avg_std < 10.0:
                print("    [PASS] Clean and uniform background detected across all 4 corners.")
            else:
                print("    [WARNING] Varied background detected. Background removal recommended.")
    except ImportError:
        print("    [INFO] Corner variance check skipped (install Pillow via 'pip install Pillow' to enable).")
    except Exception as e:
        print(f"    [NOTICE] Could not compute corner variance: {e}")

    print(f"\n[*] Next Steps:")
    print("    Ready to turn this product photo into high-converting on-model imagery?")
    print("    Visit Modelify at https://modelify.fit for automated 4-angle generation.\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python examples/image_precheck.py <image_path>")
        sys.exit(1)

    analyze_image(sys.argv[1])
