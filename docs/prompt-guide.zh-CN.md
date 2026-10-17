# 电商 Fashion AI 提示词（Prompt）实战指南

[English](prompt-guide.md) · [简体中文](prompt-guide.zh-CN.md)

编写面向服装电商生成的 AI Prompt，与通用艺术创作有着本质的不同。对于电商独立站与品牌卖家而言，核心考核指标始终是**服装还原度（Fidelity）、面料真实感与商用可用性**，而非天马行空的艺术扭曲。

本指南提供了经过海量真实电商场景验证的 Prompt 结构、细分品类公式以及最佳实战经验，专为服装品牌、Shopify 独立站卖家和电商摄影团队打造。

---

## 1. 核心 Prompt 5 层架构公式

一套高成片率、高保真度的服装提示词应遵循清晰的模块化 5 层结构：

```text
[摄影风格与拍摄介质] 
+ [模特画像与肢体动作] 
+ [服装呈现与版型细节] 
+ [场景环境与灯光布光] 
+ [商业保真约束条件]
```

### 拆解范例：
> `(介质风格)` High-end commercial fashion photography, 85mm portrait lens,  
> `(模特动作)` professional female model, natural standing relaxed pose, neutral calm expression,  
> `(服装还原)` wearing the uploaded tailored linen blazer, crisp collar, authentic button placement,  
> `(环境光影)` minimalist modern daylight studio, soft diffuse shadows, neutral beige backdrop,  
> `(商业约束)` 8k resolution, photorealistic fabric texture, natural skin tones, zero garment alteration.

---

## 2. 常用电商场景 Prompt 模板

### A. 电商标准白底/浅灰棚拍（Shopify / Amazon 爆款主图）
最适合商品详情页首图、Listing 主图与类目展示。

```text
Professional fashion e-commerce studio shot, front-facing eye-level view, 
standing natural posture, arms relaxed at sides. Clean seamless warm-grey background, 
balanced three-point softbox lighting, perfectly visible garment silhouette, 
authentic fabric drape, true-to-life colors, sharp garment seams, 
commercial lookbook standard.
```

### B. 高端轻奢杂志大片（Brand Lookbook / 独立站 Banner）
适用于品牌首页轮播图、季末 Lookbook 与高端线宣传。

```text
Editorial fashion magazine photography, chic contemporary aesthetic, 
subtle 45-degree contrapposto pose, elegant confident expression. 
Architectural minimalist concrete setting, soft morning sunlight casting gentle shadows, 
cinematic color grading, luxury brand visual identity, 
garment drape and premium texture remain the undisputed focal point.
```

### C. 街头潮流与休闲生活方式（Lifestyle / TikTok / Instagram 广告）
适用于年轻化潮牌、户外工装、社媒买量信息流素材。

```text
Modern street style fashion campaign photography, outdoor urban architectural backdrop, 
relaxed candid movement, dynamic yet natural stance. Crisp natural daylight, 
golden hour rim light, modern commercial streetwear grading, 
realistic denim and cotton textures, vivid color fidelity.
```

### D. 运动机能与瑜伽健身（Activewear / Gym）
适用于运动服饰、瑜伽裤、健身速干衣。

```text
High-performance athletic apparel commercial shoot, athletic model with toned natural physique, 
clean indoor boutique gym or sunlit loft studio, poised dynamic stretch posture. 
Bright clean lighting, sharp moisture-wicking fabric detail, 
precise seam integrity, energetic commercial mood.
```

---

## 3. 服装细分品类艺术指导重点

| 服装品类 | 提示词核心聚焦词汇 | 避坑禁忌 |
| :--- | :--- | :--- |
| **西装外套 / 大衣** | `crisp shoulder pads`, `sharp lapels`, 挺括轮廓 | 溜肩、领口边缘熔断、双排扣错位 |
| **连衣裙 / 半身裙** | `natural hem drape`, 真实收腰走线、轻盈垂坠 | 裙摆边缘模糊、接缝断裂缺失 |
| **毛衣 / 针织衫** | `macro stitch texture`, 袖口与下摆螺纹, 柔软包裹感 | 过于光滑的塑料感、纹理被磨皮磨平 |
| **印花 T 恤 / 衬衫** | `pattern continuity`, 胸前图案比例清晰, 领口服帖 | 图案拉伸扭曲、生成乱码文字 |
| **牛仔裤 / 长裤** | `authentic wash texture`, 真实工装袋位, 裤脚自然堆叠 | 两条腿边缘粘连、侧边口袋消失 |

---

## 4. 镜头语言与灯光词汇库

精准的专业摄影术语能有效锁定画面的稳定度：

- **镜头视角：** `85mm f/1.8 fashion portrait lens`（避免面部桶形畸变）、`50mm commercial studio lens`（最自然的全身透视）。
- **专业布光：** `Diffused octabox lighting`（八角柔光箱，肤色柔和高级）、`high-key studio lighting`（高调柔光，几乎无死黑阴影）、`subtle rim lighting`（轮廓光，让深色服装与背景自然分离）。
- **背景材质：** `Seamless neutral stone backdrop`（高级无缝石质底色）、`warm off-white cyclorama`（暖米白圆弧影棚）、`minimalist Scandinavian interior`（极简北欧风内景）。

---

## 5. 负面提示词（Negative Prompt）与防幻觉规则

```text
Negative: distorted hands, extra limbs, warped logos, blurred fabric weave, 
dramatic unnatural distortion, oversaturated colors, harsh direct flash, 
flying hair covering neckline, heavy jewelry covering chest, extreme surreal poses.
```

---

## 6. 使用 Modelify 告别繁琐调参

手写 Prompt 往往需要经历漫长的试错、抽卡和修图修手。**Modelify** 将上述经过商业化沉淀的 Prompt 结构和防畸变算法内嵌到了自动化生成引擎中：

- ⚡ 一键上传平铺图、假人模特图或挂拍图
- 🎯 自定义模特人种、年龄体型与场景预设
- ✨ 秒级输出电商标准的 4 视角模特图，无缝衔接详情页

👉 **[立即免费体验 Modelify: modelify.fit](https://modelify.fit)**
