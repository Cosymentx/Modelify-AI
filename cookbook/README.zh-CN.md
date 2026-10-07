# 时尚电商 AI Cookbook

[English](README.md) · [简体中文](README.zh-CN.md)

这里整理了一套面向 AI 时尚商品摄影的实用工作流、Prompt 和原图准备方法。

目标很简单：让 AI 生成的时尚商品图更稳定、更适合电商使用，也更容易重复获得类似效果。

## 指南

- [原图准备指南](source-image-preparation.zh-CN.md)
- [Prompt Library](prompt-library.zh-CN.md)
- [Shopify 商品图工作流](shopify-workflow.zh-CN.md)
- [常见失败问题排查](troubleshooting.zh-CN.md)

## 推荐工作流

```text
干净的商品原图
      │
      ▼
明确生成目标
      │
      ▼
小批量生成
      │
      ▼
检查服装还原度
      │
      ▼
选择 / 重新生成
      │
      ▼
导出用于店铺
```

## 应该优先关注什么

做时尚电商时，最好看的图片不一定是最好的商品图。

优先级建议：

1. 服装还原度
2. 轮廓清晰
3. 颜色准确
4. 光线一致
5. 模特姿势自然
6. 同一商品组的构图一致

## 每个 SKU 推荐的图片组合

一个实用的商品详情页通常可以包含：

- 1 张正面主图
- 1 张 3/4 角度模特图
- 1 张侧面或强调细节的图片
- 1 张偏生活方式的场景图
- 1 张重要服装细节特写

不是每个商品都需要全部类型。相比数量，整套图片的一致性更加重要。

## Modelify

Modelify 正是围绕这类工作流构建的。

体验地址：https://modelify.fit
