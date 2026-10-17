# 时尚电商 AI Cookbook

[English](README.md) · [简体中文](README.zh-CN.md)

这里整理了一套面向 AI 时尚商品摄影的实用工作流、Prompt 和原图准备方法。

目标很简单：让 AI 生成的时尚商品图更稳定、更适合电商使用，也更容易重复获得高品质效果。

## 实战指南与核心资源

- [原图准备指南](source-image-preparation.zh-CN.md) — 如何拍摄和准备更适合 AI 生成的服装平铺/人台图
- [Fashion Prompt Library](prompt-library.zh-CN.md) — Catalog、Editorial、Streetwear 等可复用高成片率 Prompt
- [多角度一致性生成指南](multi-angle-generation.zh-CN.md) — 正面、45° 斜侧面、正侧面与背面视角一致性解决方案
- [Shopify 商品图工作流](shopify-workflow.zh-CN.md) — 从单个 SKU 到全店发布的可重复标准化流程
- [常见失败问题排查](troubleshooting.zh-CN.md) — 解决服装变形、颜色偏移、Logo 扭曲与多图不一致

## 进阶深度文档

- [电商 Prompt 实战指南](../docs/prompt-guide.zh-CN.md) — 核心 5 层架构公式与各服装品类提示词拆解
- [全链路落地工作流](../docs/ai-fashion-workflow.zh-CN.md) — 从原图到详情页上线的 5 步全流程流水线
- [商业落地场景与 ROI 指南](../docs/ecommerce-use-cases.zh-CN.md) — 传统棚拍对比、测款策略与转化率提升实操
- [出海增长与全渠道内容飞轮](../docs/growth-guide.zh-CN.md) — 3x3 广告买量矩阵、图片 SEO 与内容规模化

## 推荐生产工作流

```text
干净的商品原图
      │
      ▼
明确生成目标风格
      │
      ▼
4 视角一致性批量生成
      │
      ▼
核验服装细节还原度
      │
      ▼
终审选图 / 微调重算
      │
      ▼
WebP 压缩并同步到店铺
```

## 电商商用核心原则

做时尚电商时，最好看的艺术图往往不一定是最具转化力的商品图。

必须严格遵循以下质量优先级：

1. **服装细节保真度**（严格保留版型、缝线、领型与印花）
2. **廓形轮廓清晰利落**
3. **色彩精准**（严防色差色漂，对标实物样卡）
4. **影棚光影与地平线一致**
5. **模特肢体动作自然**
6. **同一款商品全视角比例连贯**

## 每个 SKU 推荐的详情页黄金图片组合

一个具备高转化潜力的标准商详页建议包含：

- 1 张正面大身主图（Hero Shot）
- 1 张 45° 斜侧面上身立体图
- 1 张正侧面线条剖面图
- 1 张背后全景与后腰细节图
- 1 张生活方式（Lifestyle）场景氛围图
- 1 张纽扣/拉链/面料微距特写

不是每个商品都需要一次性上全，整套图片的一致性远比盲目追求数量更重要。

## Modelify

Modelify 专为这套严苛的电商多角度工作流而构建，开箱即用，免去繁琐的人工调参试错。

👉 **[立即在 modelify.fit 免费体验](https://modelify.fit)**
