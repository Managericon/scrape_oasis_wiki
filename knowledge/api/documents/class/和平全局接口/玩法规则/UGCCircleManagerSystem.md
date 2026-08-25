---
id: "api:class:UGCCircleManagerSystem"
title: "UGCCircleManagerSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E6%B3%95%E8%A7%84%E5%88%99/UGCCircleManagerSystem.json"
category: "API Wiki/class/和平全局接口/玩法规则"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCCircleManagerSystem

信号圈系统接口库

## Functions

### `GetBlueCircleCenter`

```text
GetBlueCircleCenter() -> Vector2D
```

获取当前蓝圈中心
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `Vector2D` | 蓝圈中心 {X，Y} |

### `GetWhiteCircleCenter`

```text
GetWhiteCircleCenter() -> Vector2D
```

获取当前白圈中心
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `Vector2D` | 白圈中心 {X，Y} |

### `GetBlueCircleRadius`

```text
GetBlueCircleRadius() -> number
```

获取当前蓝圈半径
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `number` | 半径 |

### `GetWhiteCircleRadius`

```text
GetWhiteCircleRadius() -> number
```

获取当前白圈半径
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `number` | 半径 |

### `GetCurrentCircleIndex`

```text
GetCurrentCircleIndex() -> number
```

获得当前运行到的信号圈序号
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `number` | 信号圈序号 缩圈结束时，返回最后一个信号圈序号 |

### `GetAllCircleConfig`

```text
GetAllCircleConfig() -> FCirCleCfg[]
```

获得所有信号圈配置
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `FCirCleCfg[]` | 所有信号圈配置 |

### `GetCurrentConfigCircle`

```text
GetCurrentConfigCircle() -> FCirCleCfg
```

获取当前信号圈配置
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `FCirCleCfg` | 当前信号圈配置 |

### `GetNextConfigCircle`

```text
GetNextConfigCircle() -> FCirCleCfg
```

获取下一信号圈配置
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `FCirCleCfg` | 下一信号圈配置 |

### `TogglePoisonCircle`

```text
TogglePoisonCircle() -> boolean
```

开启或者关闭信号圈（关闭状态则开启，开启状态则关闭）
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `boolean` | 调用后状态为开启或者关闭 |

### `StartCircle`

```text
StartCircle()
```

启用信号圈
生效范围：服务器

### `StopCircle`

```text
StopCircle()
```

关闭信号圈
生效范围：服务器

### `PauseCircle`

```text
PauseCircle()
```

暂停信号圈
生效范围：服务器

### `ResumeCircle`

```text
ResumeCircle()
```

恢复暂停信号圈
生效范围：服务器

## Language

`lua`
