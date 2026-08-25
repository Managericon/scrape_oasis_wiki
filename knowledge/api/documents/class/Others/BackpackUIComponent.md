---
id: "api:class:BackpackUIComponent"
title: "BackpackUIComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/BackpackUIComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# BackpackUIComponent

UGC V2背包UI组件

需启用及配合新背包系统使用，具体参见https://developer.gp.qq.com/wikieditor/#/catalog/20104

## Functions

### `GetBackpackDragDropWidget`

```text
GetBackpackDragDropWidget() -> FSoftClassPath|nil
```

获取背包拖拽控件类
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `FSoftClassPath\|nil` | 拖拽控件类，未配置则返回nil |

### `CloseLobbyPanel`

```text
CloseLobbyPanel()
```

关闭大厅背包界面(已废弃)
生效范围：客户端

### `OpenLobbyBackpackMainUI`

```text
OpenLobbyBackpackMainUI(Mode: number)
```

打开大厅背包界面(已废弃)
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Mode` | `number` | 1:背包+装备栏 2:背包+仓库 3:背包+装备栏+仓库 |

### `OnOpenBattleMainPanel`

```text
OnOpenBattleMainPanel(Panel: UUserWidget)
```

背包UI打开后执行

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Panel` | `UUserWidget` | 背包主界面控件 |

### `OnCloseBattleMainPanel`

```text
OnCloseBattleMainPanel(Panel: UUserWidget)
```

背包UI关闭后执行

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Panel` | `UUserWidget` | 背包主界面控件 |

### `OnOpenDeletePanel`

```text
OnOpenDeletePanel(Panel: UUserWidget)
```

当打开删除弹窗时调用（仅作为通知钩子，内核已用AddToSlot挂载，此处不处理AddToViewport）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Panel` | `UUserWidget` | 面板控件 |

### `OnOpenSavePanel`

```text
OnOpenSavePanel(Panel: UUserWidget)
```

当打开存入仓库确认弹窗时调用（仅作为通知钩子，内核已用AddToSlot挂载，此处不处理AddToViewport）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Panel` | `UUserWidget` | 面板控件 |

### `OnOpenTakeOutPanel`

```text
OnOpenTakeOutPanel(Panel: UUserWidget)
```

当打开存入背包确认弹窗时调用（仅作为通知钩子，内核已用AddToSlot挂载，此处不处理AddToViewport）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Panel` | `UUserWidget` | 面板控件 |

### `ClickLockBackpackItem`

```text
ClickLockBackpackItem(type: number) -> UUserWidget
```

点击上锁格子的响应函数
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `type` | `number` | 类型 [0:背包数据, 1:仓库数据] |

**Returns**

| Type | Description |
|---|---|
| `UUserWidget` | 弹窗控件 |

### `OnClickLockBackpackItem`

```text
OnClickLockBackpackItem(Panel: UUserWidget)
```

点击上锁格子后回调(重写ClickLockBackpackItem后不会执行)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Panel` | `UUserWidget` | 弹窗面板，取自ClickLockBackpackItem返回值，可能为nil |

### `IsDiscardAreaVisible`

```text
IsDiscardAreaVisible() -> boolean
```

是否显示丢弃区域
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否显示丢弃区域 |

### `OnOpenSaveOrWithDrawPanel`

```text
OnOpenSaveOrWithDrawPanel(Panel: UUserWidget)
```

当打开存入取出代币时调用（仅作为通知钩子，内核已用AddToSlot挂载，此处不处理AddToViewport）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Panel` | `UUserWidget` | 面板控件 |

### `OnOpenDropItemPanel`

```text
OnOpenDropItemPanel(Panel: UUserWidget)
```

当打开丢弃物品弹窗时调用（仅作为通知钩子，内核已用AddToSlot挂载，此处不处理AddToViewport）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Panel` | `UUserWidget` | 面板控件 |

### `GetUGCAvailableServerRPCs`

```text
GetUGCAvailableServerRPCs() -> table
```

获取RPC列表 (注意不要使用GetAvailableServerRPCs)

**Returns**

| Type | Description |
|---|---|
| `table` | RPC函数名列表 |

### `CompareQuality`

```text
CompareQuality(Data1: table, Data2: table) -> boolean
```

默认排序函数
生效范围: 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Data1` | `table` | 物品数据1 {DefineID:物品DefineID, Idx:格子索引} |
| `Data2` | `table` | 物品数据2 {DefineID:物品DefineID, Idx:格子索引} |

**Returns**

| Type | Description |
|---|---|
| `boolean` | true:物品1在前, false:物品2在前 |

## Language

`lua`
