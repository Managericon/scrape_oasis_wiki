---
id: "api:class:UMaterialExpressionNamedRerouteDeclaration"
title: "UMaterialExpressionNamedRerouteDeclaration"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionNamedRerouteDeclaration.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMaterialExpressionNamedRerouteDeclaration

## Inheritance

`UMaterialExpressionRerouteBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Name` | `FName` | 此 Named Reroute 的显示名称 |
| `NodeColor` | `FLinearColor` | 节点标题颜色，Declaration 和所有 Usage 共享 |
| `VariableGuid` | `FGuid` | 全局唯一标识，用于 Usage 查找 Declaration，以及复制粘贴后重连 |
| `Input` | `FExpressionInput` | 输入引脚：接收上游数据 |

## Language

`cpp`
