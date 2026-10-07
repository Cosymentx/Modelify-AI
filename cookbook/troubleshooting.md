# Troubleshooting AI Fashion Images

[English](troubleshooting.md) · [简体中文](troubleshooting.zh-CN.md)

Common problems and practical things to try before assuming a generation model cannot handle the product.

## Garment shape changed

Try:

- A cleaner source image
- A more front-facing source
- Less aggressive posing
- Fewer styling instructions
- A simpler background
- A prompt that explicitly prioritizes garment silhouette

## Color drift

Try:

- A source image without filters
- Better white balance
- A cleaner background
- Avoiding strongly colored ambient lighting in the requested scene
- Regenerating with a simpler studio setup

Always compare against the real product.

## Logo or print changed

Fine graphics and typography are difficult for image-generation systems.

Try:

- Higher-resolution source imagery
- Less body rotation
- More frontal views
- Keeping the printed area unobstructed

For legally or commercially critical text/logos, review carefully before publishing.

## Sleeves, hands, or accessories cover the product

Try:

- A neutral standing pose
- Arms relaxed at the sides
- Minimal accessories
- Explicitly asking for the garment to remain fully visible

## Output looks good but not suitable for a product page

Reduce art direction.

Try:

- Neutral background
- Even lighting
- Front or three-quarter pose
- Less dramatic styling
- Consistent framing

A catalog image has a different job from a campaign image.

## Results are inconsistent across a collection

Standardize:

- Source image style
- Prompt template
- Model choice
- Background
- Lighting direction
- Crop
- Aspect ratio

Consistency is usually a workflow problem as much as a generation problem.
