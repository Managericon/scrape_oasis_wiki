---
id: "api:class:UGCActivitySystem"
title: "UGCActivitySystem"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGCActivitySystem.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCActivitySystem

活动系统库（需要启用活动GamePart）

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UGCActivitySystem.OnActivityInfoReadyDelegate` | `-` | 活动信息准备好时触发的委托<br>生效范围：客户端&&服务器 |
| `UGCActivitySystem.OnUpdateValidActivityIDsDelegate` | `-` | 更新有效活动时触发的委托<br>活动系统会按照每个活动配置的生效周期来定期更新有效活动<br>生效范围：客户端&&服务器 |

## Functions

### `IsActivityInfoReady`

```text
IsActivityInfoReady() -> bool
```

活动信息是否已准备好
生效范围：客户端&&服务器

**Returns**

| Type | Description |
|---|---|
| `bool` | 活动信息是否已准备好 |

### `GetAllActivityInfos`

```text
GetAllActivityInfos() -> UGCActivityInfo[]
```

获取所有活动的信息
生效范围：客户端&&服务器

**Returns**

| Type | Description |
|---|---|
| `UGCActivityInfo[]` | 所有活动信息 |

### `GetActivityInfo`

```text
GetActivityInfo(ActivityID: int) -> UGCActivityInfo
```

获取指定活动ID的活动信息
生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActivityID` | `int` | 活动ID |

**Returns**

| Type | Description |
|---|---|
| `UGCActivityInfo` | 活动信息 |

### `GetValidActivityIDs`

```text
GetValidActivityIDs() -> int[]
```

获取所有有效的活动ID
生效范围：客户端&&服务器

**Returns**

| Type | Description |
|---|---|
| `int[]` | - |

### `GetNearestPeriodIndex`

```text
GetNearestPeriodIndex(ActivityID: int) -> int
```

获取指定活动距当前时间最近的生效周期序号，
如果已经没有符合条件的开启周期，则返回最后一个生效周期的序号
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActivityID` | `int` | 活动ID |

**Returns**

| Type | Description |
|---|---|
| `int` | 活动开启周期序号, 0表示永久时间，-1表示活动不存在或未开启 |

## Language

`lua`
