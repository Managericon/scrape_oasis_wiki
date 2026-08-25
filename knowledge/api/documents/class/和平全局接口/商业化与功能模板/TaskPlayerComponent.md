---
id: "api:class:TaskPlayerComponent"
title: "TaskPlayerComponent"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%95%86%E4%B8%9A%E5%8C%96%E4%B8%8E%E5%8A%9F%E8%83%BD%E6%A8%A1%E6%9D%BF/TaskPlayerComponent.json"
category: "API Wiki/class/和平全局接口/商业化与功能模板"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# TaskPlayerComponent

UGC任务系统玩家组件

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TaskPlayerComponent.OnTaskLineAwardInfoChangeDelegate` | `-` | 生效范围：客户端<br>任务线奖励状态变更回调<br>@param TaskLineName string @任务线名称<br>@param Index number @奖励索引 |
| `TaskPlayerComponent.OnTaskInfoChangeDelegate` | `-` | 生效范围：客户端<br>任务数据变更回调<br>@param Index UGCTaskIndex @榜单周期 |
| `TaskPlayerComponent.OnTaskLineProgressChangeDelegate` | `-` | 生效范围：客户端&服务端<br>任务线进度变更回调<br>@param TaskLineName string @任务线名称 |

## Functions

### `ResetPercentTaskLine`

```text
ResetPercentTaskLine(TaskLineName: string)
```

重置活跃任务线
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |

### `ClaimLevelTaskAward`

```text
ClaimLevelTaskAward(TaskLineName: string, LevelIndex: number, TaskIndex: number)
```

领取成长任务奖励
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |
| `LevelIndex` | `number` | - |
| `TaskIndex` | `number` | - |

### `ClaimPercentTaskAward`

```text
ClaimPercentTaskAward(TaskLineName: string, TaskIndex: number)
```

领取活跃任务奖励
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |
| `TaskIndex` | `number` | - |

### `GetTaskLineProgress`

```text
GetTaskLineProgress(TaskLineName: string) -> number
```

获取任务线进度
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `GetLevelTaskInfoList`

```text
GetLevelTaskInfoList(TaskLineName: string) -> FUGCLevelTaskPlayerData[]
```

获取成长任务线的任务信息列表
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |

**Returns**

| Type | Description |
|---|---|
| `FUGCLevelTaskPlayerData[]` | - |

### `GetPercentTaskInfoList`

```text
GetPercentTaskInfoList(TaskLineName: string) -> FUGCTaskInfo[]
```

获取活跃任务线的任务信息列表
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |

**Returns**

| Type | Description |
|---|---|
| `FUGCTaskInfo[]` | - |

### `GetPercentTaskLineAwardStateList`

```text
GetPercentTaskLineAwardStateList(TaskLineName: string) -> table
```

获取活跃任务线的奖励状态列表
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |

**Returns**

| Type | Description |
|---|---|
| `table` | - |

### `GetTaskLineAwardState`

```text
GetTaskLineAwardState(TaskLineName: string, Index: number) -> EUGCTaskLineAwardState
```

获取任务线奖励状态
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |
| `Index` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `EUGCTaskLineAwardState` | - |

### `ClaimAllAward`

```text
ClaimAllAward(TaskLineName: string)
```

领取任务线的全部奖励
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |

### `ClaimTaskLineAward`

```text
ClaimTaskLineAward(TaskLineName: string, Index: number)
```

领取任务线奖励
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |
| `Index` | `number` | - |

### `SetTaskLineProgress`

```text
SetTaskLineProgress(TaskLineName: string, Progress: number)
```

设置任务线进度
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |
| `Progress` | `number` | - |

### `GetPercentTaskProgress`

```text
GetPercentTaskProgress(TaskLineName: string, Index: number) -> number
```

获取活跃任务进度
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |
| `Index` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `GetPercentTaskState`

```text
GetPercentTaskState(TaskLineName: string, Index: number) -> EUGCTaskState
```

获取活跃任务状态
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |
| `Index` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `EUGCTaskState` | - |

### `GetLevelTaskProgress`

```text
GetLevelTaskProgress(TaskLineName: string, LevelIndex: number, TaskIndex: number) -> number
```

获取成长任务进度
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |
| `LevelIndex` | `number` | - |
| `TaskIndex` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `GetLevelTaskState`

```text
GetLevelTaskState(TaskLineName: string, LevelIndex: number, TaskIndex: number) -> EUGCTaskState
```

获取成长任务状态
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |
| `LevelIndex` | `number` | - |
| `TaskIndex` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `EUGCTaskState` | - |

### `GetTaskManager`

```text
GetTaskManager() -> TaskManager
```

**Returns**

| Type | Description |
|---|---|
| `TaskManager` | - |

### `SetTaskLineTime`

```text
SetTaskLineTime(TaskLineName: string, BeginTime: number, EndTime: number)
```

设置任务线和任务线下所有任务的开始/结束时间
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |
| `BeginTime` | `number` | - |
| `EndTime` | `number` | - |

## Language

`lua`
