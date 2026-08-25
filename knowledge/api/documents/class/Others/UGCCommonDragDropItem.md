---
id: "api:class:UGCCommonDragDropItem"
title: "UGCCommonDragDropItem"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGCCommonDragDropItem.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCCommonDragDropItem

拖拽控件

## Functions

### `SetDragWidget`

```text
SetDragWidget(Widget: UUserWidget|Class, bCreate: boolean)
```

设置拖拽时的控件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget\|Class` | 拖拽时的控件实例 或 类 |
| `bCreate` | `boolean` | 是否创建控件，传入Class则创建控件实例 |

### `SetDragDirectionMode`

```text
SetDragDirectionMode(DirectionMode: EDragDirectionMode)
```

设置拖拽方向模式

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DirectionMode` | `EDragDirectionMode` | 拖拽方向模式 |

### `SetDragDropMode`

```text
SetDragDropMode(DragDropMode: EDragDropMode)
```

设置拖拽模式

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DragDropMode` | `EDragDropMode` | 拖拽模式 |

### `RegisterDragDropData`

```text
RegisterDragDropData(DragDropData: table, DragDropMode: EDragDropMode, InDragWidgetClass: FSoftClassPath|string)
```

注册拖拽(入口), 仅执行一次有效

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DragDropData` | `table` | 拖拽数据，在拖拽响应事件中传递 |
| `DragDropMode` | `EDragDropMode` | 拖拽模式 |
| `InDragWidgetClass` | `FSoftClassPath\|string` | 可选，自定义拖拽控件类 |

### `SetData`

```text
SetData(Data: table)
```

设置拖拽数据

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Data` | `table` | 拖拽数据 |

## Language

`lua`
