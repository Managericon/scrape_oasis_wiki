---
id: "api:class:UPESkillWidget"
title: "UPESkillWidget"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPESkillWidget.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPESkillWidget

技能UI基类

## Inheritance

`UUAEUserWidget` -> `ILuaInterface`

## Functions

### `BindToSlot`

```text
BindToSlot(Comp: UPersistBaseComponent *, SlotName: FGameplayTag) -> void
```

将技能绑定到指定PE组件的指定Slot上
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Comp` | `UPersistBaseComponent *` | 绑定的组件 |
| `SlotName` | `FGameplayTag` | 绑定的槽位 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCurrentSkill`

```text
GetCurrentSkill() -> UPersistEffectSkill *
```

获取当前绑定的技能
	  生效范围C

**Returns**

| Type | Description |
|---|---|
| `UPersistEffectSkill *` | 当前绑定的技能 |

### `BindImageAndTextForSkillNameAndIcon`

```text
BindImageAndTextForSkillNameAndIcon(IconImage: UImage *, NameText: UTextBlock *, DescribeText: UTextBlock *) -> void
```

绑定用于显示技能图标、名字、描述的控件
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IconImage` | `UImage *` | 图标控件 |
| `NameText` | `UTextBlock *` | 名字控件 |
| `DescribeText` | `UTextBlock *` | 描述控件 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RefreshSkillUI`

```text
RefreshSkillUI() -> void
```

刷新当前UI绑定的控件的内容
	  生效范围C

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSkillName`

```text
GetSkillName() -> FName
```

获取技能名字
	  生效范围C

**Returns**

| Type | Description |
|---|---|
| `FName` | 技能名字 |

### `GetSkillDetail`

```text
GetSkillDetail() -> FString
```

获取技能描述
	  生效范围C

**Returns**

| Type | Description |
|---|---|
| `FString` | 技能描述 |

### `GetSkillIcon`

```text
GetSkillIcon() -> FSoftObjectPath
```

获取技能图标
	  生效范围C

**Returns**

| Type | Description |
|---|---|
| `FSoftObjectPath` | 技能图标 |

### `InitButton`

```text
InitButton(IconImage: UImage *, NameText: UTextBlock *, ClickButton: UButton *) -> void
```

绑定技能按钮控件
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IconImage` | `UImage *` | 图标控件 |
| `NameText` | `UTextBlock *` | 名字控件 |
| `ClickButton` | `UButton *` | 按钮控件 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `InitLayer`

```text
InitLayer(LayerText: UTextBlock *, LayerPanel: UPanelWidget *) -> void
```

绑定技能使用层数控件
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LayerText` | `UTextBlock *` | 技能层数 |
| `LayerPanel` | `UPanelWidget *` | 技能层数的Panel控件，控制层数的显隐 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `InitCDProgress`

```text
InitCDProgress(CDText: UTextBlock *, CDProgressImage: UImage *, CDProgressPanel: UPanelWidget *) -> void
```

绑定技能CD控件
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CDText` | `UTextBlock *` | 技能CD时间 |
| `CDProgressImage` | `UImage *` | @技能CD进度条 |
| `CDProgressPanel` | `UPanelWidget *` | 整个CD的Panel控件，控制CD的显隐 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `InitEnergyProgress`

```text
InitEnergyProgress(EnergyProgressImage: UImage *, EnergyCanvasPanel: UPanelWidget *) -> void
```

绑定技能能量控件
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EnergyProgressImage` | `UImage *` | 技能能量进度条 |
| `EnergyCanvasPanel` | `UPanelWidget *` | 技能能量Panel控件，控制能量进度条的显隐 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `InitTagDisableState`

```text
InitTagDisableState(TagDisableCanvasPanel: UPanelWidget *) -> void
```

绑定技能显示TagDisable状态的控件
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagDisableCanvasPanel` | `UPanelWidget *` | 技能TagDisable状态的Panel控件，控制TagDisable状态的显隐 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `InitEnableState`

```text
InitEnableState(EnableCanvasPanel: UPanelWidget *) -> void
```

绑定技能显示Enable状态的控件
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EnableCanvasPanel` | `UPanelWidget *` | 技能Enable状态的Panel控件，控制Enable状态的显隐 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `InitVirtualJoystick`

```text
InitVirtualJoystick(VirtualJoystickPanel: UPanelWidget *, VirtualJoystick: UPESkillVirtualJoystick *) -> void
```

绑定技能摇杆输入控件
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `VirtualJoystickPanel` | `UPanelWidget *` | - |
| `VirtualJoystick` | `UPESkillVirtualJoystick *` | 技能技能摇杆控件，控制摇杆的生效和失效 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Events

### `OnSkillBound_BP`

```text
OnSkillBound_BP(InOwnerSkill: UPersistEffectSkill *) -> void
```

当控件绑定到新的技能时触发
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOwnerSkill` | `UPersistEffectSkill *` | 当前绑定的技能 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UpdateCD_BP`

```text
UpdateCD_BP(Delta: float) -> void
```

每帧触发，用于更新CD显示
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Delta` | `float` | 每帧的时间 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnCDStateChange_BP`

```text
OnCDStateChange_BP(bIsCD: bool) -> void
```

当控件绑定的技能CD状态变化时触发
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsCD` | `bool` | 技能是否处在CD状态 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnSkillUIInfoChange_BP`

```text
OnSkillUIInfoChange_BP() -> void
```

当控件绑定的技能的UI信息变化时触发
	  生效范围C

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnEnableChange_BP`

```text
OnEnableChange_BP(bIsEnable: bool) -> void
```

当控件绑定的技能Enable状态变化时触发
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsEnable` | `bool` | 技能是否Enable |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTagDisableChange_BP`

```text
OnTagDisableChange_BP(bIsDisable: bool) -> void
```

当控件绑定的技能被禁用Tag(PawnState.ActivatingSkill)导致无法激活时触发
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsDisable` | `bool` | 技能是否被Tag禁用 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnSkillDirectionInputEnableChange_BP`

```text
OnSkillDirectionInputEnableChange_BP(bEnable: bool) -> void
```

当控件绑定的技能的摇杆输入生效或失效时触发
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
