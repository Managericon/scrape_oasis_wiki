---
id: "api:class:ULuaArrayHelper"
title: "ULuaArrayHelper"
source: "https://developer.gp.qq.com/api/class/detail/Others/ULuaArrayHelper.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ULuaArrayHelper

数组帮助类

## Functions

### `Add`

```text
Add(Item: any)
```

添加元素

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Item` | `any` | 需要添加的元素 |

### `AddUnique`

```text
AddUnique(Item: any)
```

往数组里添加一个元素，如果已存在则不压入

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Item` | `any` | 需要添加的元素 |

### `Push`

```text
Push(Item: any)
```

往数组里压入一个元素

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Item` | `any` | 需要添加的元素 |

### `Insert`

```text
Insert(Index: number, Item: any)
```

在指定位置插入一个元素

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `number` | 需要插入的元素索引 |
| `Item` | `any` | 需要添加的元素 |

### `Remove`

```text
Remove(Item: any)
```

移除一个元素

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Item` | `any` | 需要移除的元素 |

### `RemoveAt`

```text
RemoveAt(Index: number)
```

根据索引移除一个元素

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `number` | 索引 |

### `Pop`

```text
Pop() -> any
```

弹出最后一个元素

**Returns**

| Type | Description |
|---|---|
| `any` | 移除的元素 |

### `Get`

```text
Get(Index: number)
```

跟据索引获取一个元素

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `number` | 索引 |

### `Set`

```text
Set(Index: number, Item: any)
```

设置一个元素

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `number` | 索引 |
| `Item` | `any` | 元素 |

### `Find`

```text
Find(Item: any)
```

查找一个元素

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Item` | `any` | 元素 |

### `Contains`

```text
Contains(Item: any)
```

判断数组是否包含某个元素

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Item` | `any` | 元素 |

### `Empty`

```text
Empty()
```

清空数组

### `Reset`

```text
Reset(ExpectedSize: number)
```

重置数组

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ExpectedSize` | `number` | 数组容量（可选） |

### `Num`

```text
Num() -> number
```

获取数组长度

**Returns**

| Type | Description |
|---|---|
| `number` | 数组长度 |

## Language

`lua`
