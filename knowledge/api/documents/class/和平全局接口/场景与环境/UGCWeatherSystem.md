---
id: "api:class:UGCWeatherSystem"
title: "UGCWeatherSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%9C%BA%E6%99%AF%E4%B8%8E%E7%8E%AF%E5%A2%83/UGCWeatherSystem.json"
category: "API Wiki/class/和平全局接口/场景与环境"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCWeatherSystem

天气系统接口库

## Functions

### `LoadWeatherSequence`

```text
LoadWeatherSequence(PlayerController: PlayerController, WeatherSequence: WeatherSequence, BlendTime: number)
```

加载天气序列
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |
| `WeatherSequence` | `WeatherSequence` | 天气序列资源 |
| `BlendTime` | `number` | 过渡时间 |

### `UnloadWeatherSequence`

```text
UnloadWeatherSequence(PlayerController: PlayerController, WeatherSequence: WeatherSequence)
```

卸载天气序列
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |
| `WeatherSequence` | `WeatherSequence` | 天气序列资源 |

### `SeekWeatherSequence`

```text
SeekWeatherSequence(PlayerController: PlayerController, WeatherSequence: WeatherSequence, Time: number)
```

设置天气序列播放进度
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |
| `WeatherSequence` | `WeatherSequence` | 天气序列资源 |
| `Time` | `number` | 目标时间 |

### `PauseWeatherSequence`

```text
PauseWeatherSequence(PlayerController: PlayerController, WeatherSequence: WeatherSequence)
```

暂停天气序列
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |
| `WeatherSequence` | `WeatherSequence` | 天气序列资源 |

### `ResumeWeatherSequence`

```text
ResumeWeatherSequence(PlayerController: PlayerController, WeatherSequence: WeatherSequence)
```

继续天气序列
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |
| `WeatherSequence` | `WeatherSequence` | 天气序列资源 |

### `GetCurrentWeatherSequence`

```text
GetCurrentWeatherSequence(PlayerController: PlayerController) -> WeatherSequence
```

获取当前天气序列
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `WeatherSequence` | 天气序列资源 |

### `GetCurrentWeatherPlayPercentage`

```text
GetCurrentWeatherPlayPercentage(PlayerController: PlayerController) -> number
```

获取当前天气播放进度
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `number` | 播放进度（0~1） |

### `GetCurrentWeatherTime`

```text
GetCurrentWeatherTime(PlayerController: PlayerController) -> number
```

获取当前天气时间
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `number` | 天气时间（0~24） |

## Language

`lua`
