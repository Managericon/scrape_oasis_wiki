---
id: "api:cppstruct:FPESkillCDWapper"
title: "FPESkillCDWapper"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FPESkillCDWapper.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FPESkillCDWapper

技能CD信息

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CDType` | `EPESkillCDType` | 技能CD类型 |
| `CDRecoveryTime` | `float` | CD能量充能时间 |
| `AllowRecoveryDuringActivation` | `bool` | 技能激活期间恢复CD能量 |
| `MaxLayer` | `int` | 最大充能次数 |
| `CDEnergyConsume` | `float` | 持续消耗型每秒扣除速率，如果不选energy，就是直接扣完一层的所有能量 |
| `AllowConsumeMinEnergy` | `float` | 能开始消耗能量的最小百分比 |
