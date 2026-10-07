# Modelify API 概览

[English](api-overview.md) · [简体中文](api-overview.zh-CN.md)

Modelify 计划提供稳定、面向开发者的 API，用于电商和自动化工作流。

本文档描述的是计划中的公共接口边界，**并不代表其中展示的所有接口现在都已经可以在生产环境使用**。

## 计划中的核心概念

公开 API 预计会围绕以下能力展开：

- 身份认证
- Generation Request
- Generation Status
- Generated Assets
- Webhooks
- Usage / Credits

## 示例请求结构

未来的生成请求在概念上可能类似：

```json
{
  "product_image": "https://example.com/product.jpg",
  "model": "selected-model",
  "options": {
    "output": "ecommerce"
  }
}
```

对应的响应可能包含任务标识、处理状态以及最终生成资源 URL。

## 稳定性边界

内部 Worker API、Provider 专属参数、队列机制、生成 Prompt 以及基础设施接口不会作为公共 API 契约的一部分。

## 当前接入方式

关于目前可用的集成能力，请访问 Modelify 官网：

https://modelify.fit

## SDK

官方 SDK 并不是当前公开仓库的前置目标。

只有当 JavaScript、Python 或其他语言 SDK 出现足够明确的真实外部需求时，Modelify 才会投入长期维护。
