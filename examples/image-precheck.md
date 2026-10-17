# Garment Image Pre-check Script

[English](image-precheck.md) · [简体中文](image-precheck.zh-CN.md)

A lightweight diagnostic Python script to validate clothing product photos before running AI fashion model generation workflows.

## Why Pre-check?

Input image quality directly determines the output quality in AI photography. Common failure causes include:
- Insufficient resolution resulting in blurry fabric textures.
- Irregular aspect ratios causing unnatural body stretching or awkward crops.
- Cluttered backgrounds causing the AI to generate surreal artifacts in background corners.

## Requirements

- Python 3.8+
- Pillow (`pip install Pillow`)

## Quick Start

```bash
# Run diagnostics on a product image
python examples/image_precheck.py path/to/your/garment.jpg
```

## Sample Output

```text
=======================================================
  Modelify AI Garment Photo Diagnostic: sample-shirt.jpg
=======================================================

[*] Basic Attributes:
    - Dimensions: 1600 x 2133 px
    - Color Mode: RGB
    - Aspect Ratio: 0.75 (Width / Height)

[*] Resolution Assessment:
    [PASS] Excellent resolution for high-fidelity e-commerce export.

[*] Aspect Ratio Assessment:
    [OPTIMAL] Matches 3:4 portrait standard (ideal for fashion lookbooks & Shopify).

[*] Background Uniformity Check:
    [PASS] Clean and uniform background detected at image corners.

[*] Recommendation:
    Ready to generate realistic on-model fashion photography?
    Visit Modelify at https://modelify.fit for automated 4-angle generation.
```

## Automated Cloud Processing

If you manage hundreds of SKUs and want fully automated image normalization, background removal, and multi-angle model generation, try **[Modelify](https://modelify.fit)**.
