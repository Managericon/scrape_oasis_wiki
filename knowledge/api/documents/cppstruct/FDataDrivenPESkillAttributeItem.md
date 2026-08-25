---
id: "api:cppstruct:FDataDrivenPESkillAttributeItem"
title: "FDataDrivenPESkillAttributeItem"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FDataDrivenPESkillAttributeItem.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FDataDrivenPESkillAttributeItem

属性修改项（DataDriven 版本，带 CustomizedSerialize）
  复制自 FPESkillAttributeItem，针对移动端简化：
  - GameAttribute: FGameAttributeContainer → FString（移动端无编辑器下拉选择器）
  - 移除 OptionalModifyItemNameID（移动端不需要）
  - ModifierValueWrapper: FGameMagnitudeWrapper → float（移动端仅使用常量值）
  用于 Mobile 序列化，不影响主干逻辑

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Method` | `FPESkillAttributeModifyMethod` | 修改方式 |
| `GameAttribute` | `FString` | 要修改的属性名 |
| `ModifierOp` | `EAttrOperator` | 属性修改操作类型（非永久修改） |
| `ModifierOp_DoChange` | `EAttrOperator_DoChange` | 属性修改操作类型（永久修改） |
| `ModifierValue` | `float` | 操作数值 |
| `bRepAttrModify` | `bool` | 是否同步客户端 |
