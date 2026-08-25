---
id: "api:class:TaskManager"
title: "TaskManager"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%95%86%E4%B8%9A%E5%8C%96%E4%B8%8E%E5%8A%9F%E8%83%BD%E6%A8%A1%E6%9D%BF/TaskManager.json"
category: "API Wiki/class/和平全局接口/商业化与功能模板"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# TaskManager

UGC任务系统全局管理器

## Functions

### `GetTaskLineConfig`

```text
GetTaskLineConfig(TaskLineName: string) -> FUGCTaskLineConfig
```

获取任务线配置
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |

**Returns**

| Type | Description |
|---|---|
| `FUGCTaskLineConfig` | - |

### `GetTaskConfig`

```text
GetTaskConfig(TaskID: number) -> FUGCTaskConfig
```

获取任务配置
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskID` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `FUGCTaskConfig` | - |

### `GetTaskType`

```text
GetTaskType(TaskID: number) -> number
```

获取任务类型
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskID` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `GetTaskDesc`

```text
GetTaskDesc(TaskID: number) -> string
```

获取任务目标进度
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskID` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `string` | - |

### `GetTaskTarget`

```text
GetTaskTarget(TaskID: number) -> number
```

获取任务目标进度
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskID` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `UpdateTaskProgress`

```text
UpdateTaskProgress(TaskIndex: FUGCTaskIndex, PlayerController: Controller, Progress: number, IsIncremental: boolean)
```

通用更新任务进度
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskIndex` | `FUGCTaskIndex` | - |
| `PlayerController` | `Controller` | - |
| `Progress` | `number` | - |
| `IsIncremental` | `boolean` | - |

### `GetPercentTaskPercent`

```text
GetPercentTaskPercent(TaskLineName: string, TaskID: number) -> number
```

获取活跃任务完成后获得的活跃度数量
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |
| `TaskID` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

## Language

`lua`
