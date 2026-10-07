# Source Image Preparation

[English](source-image-preparation.md) · [简体中文](source-image-preparation.zh-CN.md)

Good source images dramatically improve the consistency of AI fashion outputs.

## Best source images

Prefer product photos with:

- The full garment visible
- A clean or simple background
- Minimal occlusion
- Accurate colors
- Good lighting
- Enough resolution to preserve texture and construction details
- No large watermarks or text covering the garment

## Flat-lay images

Flat-lay images work best when:

- Sleeves and hems are visible
- The garment is not folded
- The silhouette is easy to understand
- The camera is close to perpendicular to the product
- Strong shadows do not hide construction details

Avoid excessive styling props if the goal is accurate product reconstruction.

## Mannequin or ghost-mannequin images

These can be useful because they preserve structure, but check:

- Neckline shape
- Sleeve length
- Waist position
- Garment length
- Any areas hidden by the mannequin

The clearer the original structure, the easier it is to maintain garment identity.

## Existing model photos

If the source already contains a person, outputs may be more sensitive to pose and occlusion.

Prefer images where:

- The product is clearly visible
- Arms do not cover important details
- Hair does not cover the neckline
- Bags or accessories do not cover the garment
- The pose does not strongly distort the silhouette

## Color accuracy

Before generating:

1. Use the most color-accurate source image available.
2. Avoid strong filters.
3. Avoid heavily compressed screenshots.
4. Compare generated results against the original product, not only against aesthetic expectations.

## Quick checklist

Before uploading, ask:

- Is the full garment visible?
- Can I clearly understand the silhouette?
- Are key details unobstructed?
- Is the color reliable?
- Is the source image sharp enough?

If most answers are yes, the image is usually a much better candidate for generation.
