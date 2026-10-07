# Modelify API Overview

Modelify plans to expose a stable developer-facing API for commerce and automation workflows.

This document describes the intended public surface. It is **not a guarantee that every endpoint shown here is currently available in production**.

## Intended concepts

A public API is expected to revolve around a small set of product concepts:

- Authentication
- Generation requests
- Generation status
- Generated assets
- Webhooks
- Usage / credits

## Illustrative request shape

A future generation request may conceptually look like:

```json
{
  "product_image": "https://example.com/product.jpg",
  "model": "selected-model",
  "options": {
    "output": "ecommerce"
  }
}
```

A corresponding result may contain a request identifier, processing status, and generated asset URL.

## Stability

Internal worker APIs, provider-specific parameters, queue mechanics, generation prompts, and infrastructure endpoints are not part of the intended public contract.

## Access

For current availability and integration discussions, use the official Modelify website:

https://modelify.fit

## SDKs

Official SDKs are intentionally not a prerequisite for the public repository.

Modelify may add JavaScript, Python, or other SDKs when there is enough real external demand to justify maintaining them.
