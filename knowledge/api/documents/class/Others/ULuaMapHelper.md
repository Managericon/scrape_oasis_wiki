---
id: "api:class:ULuaMapHelper"
title: "ULuaMapHelper"
source: "https://developer.gp.qq.com/api/class/detail/Others/ULuaMapHelper.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ULuaMapHelper

映射帮助类

## Functions

### `Add`

```text
Add(Key: any, Value: any) -> boolean
```

添加一个键值对

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `any` | 键 |
| `Value` | `any` | 值 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否更新成功 |

### `Remove`

```text
Remove(Key: any) -> number
```

根据键移除一个元素

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `any` | 键 |

**Returns**

| Type | Description |
|---|---|
| `number` | 移除的元素数量 |

### `Get`

```text
Get(Key: any) -> any
```

根据键获取值

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `any` | 键 |

**Returns**

| Type | Description |
|---|---|
| `any` | 值 |

### `Set`

```text
Set(Key: any, Value: any) -> boolean
```

更新键值对

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `any` | 键 |
| `Value` | `any` | 值 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否更新成功 |

### `Find`

```text
Find(Key: any) -> any
```

根据键获取值

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `any` | 键 |

**Returns**

| Type | Description |
|---|---|
| `any` | 值 |

### `Empty`

```text
Empty()
```

清空哈希表

### `Reset`

```text
Reset(ExpectedSize: number)
```

重置哈希表

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ExpectedSize` | `number` | 期望的哈希表长度（可选） |

### `Num`

```text
Num() -> number
```

获取哈希表长度

**Returns**

| Type | Description |
|---|---|
| `number` | 长度 |

## Language

`lua`
