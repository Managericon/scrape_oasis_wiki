---
id: "api:class:UPESkillPassiveSkill"
title: "UPESkillPassiveSkill"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPESkillPassiveSkill.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPESkillPassiveSkill

被动技能实体

## Inheritance

`UPersistEffectSkill`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaxActivationCount` | `int32` | 最大激活次数，-1表示无限制 |

## Events

### `OnStackChange_BP`

```text
OnStackChange_BP(PreNum: int32, CurrentNum: int32) -> void
```

生效范围：服务器&客户端
	  当 被动技能 堆叠层数变化时调用，比如技能被合并时

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PreNum` | `int32` | 上一次的堆叠层数 |
| `CurrentNum` | `int32` | 当前的堆叠层数 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanClientRPCActivate_BP`

```text
CanClientRPCActivate_BP() -> bool
```

生效范围：服务器
	  当 pes.BlockPassiveSkillClientRPC 开关关闭时，由蓝图决定是否允许客户端 RPC 激活被动技能

**Returns**

| Type | Description |
|---|---|
| `bool` | true 允许激活，false 拒绝激活 |

## Language

`cpp`
