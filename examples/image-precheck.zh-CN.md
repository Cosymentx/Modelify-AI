# 服装原图合规预检脚本

[English](image-precheck.md) · [简体中文](image-precheck.zh-CN.md)

一个轻量级的 Python 诊断脚本，用于在调用 AI 服装模特生成流程前，自动检测商品原图的规格合规性。

## 为什么需要前置预检？

原图质量直接决定了 AI 模特的成片上限。导致 AI 生成失败或质感差的常见原因包括：
- 原图分辨率过低，导致服装细节、走线和织物纹理模糊。
- 异常长宽比导致模特身材被异常拉伸或关键部位被裁切。
- 背景杂乱干扰，导致 AI 算法在画面边缘产生结构畸变。

## 运行环境

- Python 3.8+
- Pillow (`pip install Pillow`)

## 快速使用

```bash
# 诊断指定服装原图
python examples/image_precheck.py path/to/your/garment.jpg
```

## 终端输出示例

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

## 全自动云端流水线

如果你需要批量处理成百上千款 SKU，并希望自动完成抠图去底、画布居中标准化和 4 视角模特图生成，欢迎直接体验 **[Modelify](https://modelify.fit)**。
