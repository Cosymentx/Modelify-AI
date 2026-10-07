# Modelify 架构概览

[English](architecture.md) · [简体中文](architecture.zh-CN.md)

本文档从较高层级介绍 Modelify 的整体架构。

目标是帮助用户和集成方理解产品如何组织，同时避免暴露生产环境中的专有实现细节。

## 高层流程

```text
用户 / 电商店铺
      │
      ▼
Modelify Web Experience
      │
      ▼
Modelify Cloud Services
      │
      ├── 身份认证与账户服务
      ├── 商品与生成请求
      ├── 生成任务编排
      ├── 图片处理
      ├── 结果持久化
      └── 结果交付
      │
      ▼
AI Generation Providers
```

## 生成生命周期

从概念上看，一次生成任务通常会经过以下阶段：

1. 用户提交商品图片以及生成选项。
2. Modelify 校验请求并准备输入。
3. 请求进入 Modelify 私有生成基础设施。
4. 生成结果经过处理并准备交付。
5. 最终资源被持久化，并通过产品界面返回给用户。

## 保持私有的部分

以下内容不会公开实现细节：

- AI Provider 路由
- Provider 凭证与配置
- Prompt 与生成参数调优
- 图片预处理策略
- Queue 与 Worker 实现
- Retry 与 Fallback 逻辑
- 并发控制策略
- 成本优化
- Billing 与积分计算
- 生产数据库结构
- 内部管理系统

这些都属于 Modelify 商业化生产平台的一部分。

## 公共集成边界

长期来看，公开集成会围绕稳定的产品级能力，而不是内部基础设施：

- 创建生成请求
- 查询生成状态
- 获取生成结果
- 通过 Webhook 集成
- 连接电商工作流

当前 API 方向请参考 [api-overview.zh-CN.md](api-overview.zh-CN.md)。
