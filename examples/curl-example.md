# cURL Integration Example

[English](curl-example.md) · [简体中文](curl-example.zh-CN.md)

This example demonstrates the **shape of a future Modelify API integration**.

It is illustrative and should not be treated as a currently supported production endpoint unless the official API documentation explicitly says otherwise.

```bash
curl -X POST "https://api.example.modelify/generations" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "product_image": "https://example.com/product.jpg",
    "model": "selected-model"
  }'
```

## Expected workflow

A typical integration would:

1. Submit a generation request.
2. Receive a request identifier.
3. Poll for status or receive a webhook.
4. Read the completed generated asset.

For current API availability, refer to the official Modelify website:

https://modelify.fit
