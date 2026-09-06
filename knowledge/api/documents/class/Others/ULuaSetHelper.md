---
id: "api:class:ULuaSetHelper"
title: "ULuaSetHelper"
source: "https://developer.gp.qq.com/api/class/detail/Others/ULuaSetHelper.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ULuaSetHelper

集合帮助类

## Functions

### `Add`

```text
Add(Item: any) -> number
```

添加一个元素

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Item` | `any` | 需要添加的元素 |

**Returns**

| Type | Description |
|---|---|
| `number` | 索引 |

### `Remove`

```text
Remove(Item: any) -> number
```

移除一个元素

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Item` | `any` | 需要移除的元素 |

**Returns**

| Type | Description |
|---|---|
| `number` | 移除的元素数量 |

### `RemoveAt`

```text
RemoveAt(Index: number)
```

根据索引移除一个元素

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `number` | 索引 |

### `Get`

```text
Get(Index: number) -> any
```

根据索引获取一个元素

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `number` | 索引 |

**Returns**

| Type | Description |
|---|---|
| `any` | 元素 |

### `Set`

```text
Set(Index: number, Item: any) -> number
```

设置一个元素

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `number` | 索引 |
| `Item` | `any` | 元素 |

**Returns**

| Type | Description |
|---|---|
| `number` | 索引 |

### `Find`

```text
Find(Item: any) -> number
```

查找一个元素

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Item` | `any` | 元素 |

**Returns**

| Type | Description |
|---|---|
| `number` | 索引 |

### `Contains`

```text
Contains(Item: any) -> number
```

判断集合是否包含某个元素

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Item` | `any` | 元素 |

**Returns**

| Type | Description |
|---|---|
| `number` | 是否包含 |

### `IsValidIndex`

```text
IsValidIndex(Index: number) -> number
```

判断指定索引是否合法

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `number` | 索引 |

**Returns**

| Type | Description |
|---|---|
| `number` | 是否合法 |

### `Empty`

```text
Empty()
```

清空集合

### `Reset`

```text
Reset(ExpectedSize: number)
```

重置集合

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ExpectedSize` | `number` | 期望的集合长度（可选） |

### `Num`

```text
Num() -> number
```

获取集合长度

**Returns**

| Type | Description |
|---|---|
| `number` | 集合长度 |

## Language

`lua`
