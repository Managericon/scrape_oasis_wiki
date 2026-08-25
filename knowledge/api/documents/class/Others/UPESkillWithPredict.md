---
id: "api:class:UPESkillWithPredict"
title: "UPESkillWithPredict"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPESkillWithPredict.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPESkillWithPredict

带主端预测的技能实,目前暂未有技能实装，待测试

## Inheritance

`UPersistEffectSkill`

## Functions

### `ActivateSkillWithPredict`

```text
ActivateSkillWithPredict() -> void
```

生效范围：SC
	  释放技能带主端预测

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `JumpToStateWithPredict`

```text
JumpToStateWithPredict(StateName: FName, EnterTime: float, bPause: bool) -> void
```

生效范围：SC
	  跳转状态带主端预测

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StateName` | `FName` | - |
| `EnterTime` | `float` | - |
| `bPause` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
