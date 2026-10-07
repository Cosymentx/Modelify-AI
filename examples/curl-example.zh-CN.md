# cURL 集成示例

[English](curl-example.md) · [简体中文](curl-example.zh-CN.md)

这个示例用于展示**未来 Modelify API 集成的大致形式**。

除非官方 API 文档明确说明某个接口已经正式开放，否则不要把下面的地址当作当前可用的生产接口。

```bash
curl -X POST "https://api.example.modelify/generations" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "product_image": "https://example.com/product.jpg",
    "model": "selected-model"
  }'
```

## 预期工作流

典型集成流程可能是：

1. 提交生成请求。
2. 获得任务 ID。
3. 轮询任务状态，或者通过 Webhook 获取状态变化。
4. 获取最终生成资源。

关于当前 API 可用性，请参考 Modelify 官网：

https://modelify.fit
