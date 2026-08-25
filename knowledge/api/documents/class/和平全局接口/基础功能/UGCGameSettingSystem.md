---
id: "api:class:UGCGameSettingSystem"
title: "UGCGameSettingSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%9F%BA%E7%A1%80%E5%8A%9F%E8%83%BD/UGCGameSettingSystem.json"
category: "API Wiki/class/和平全局接口/基础功能"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCGameSettingSystem

游戏配置通用接口库

## Functions

### `GetDeviceLevel`

```text
GetDeviceLevel() -> number
```

获取设备水平（0=低端机，1=中端机，2=高端机）
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `number` | 设备水平级别 |

### `GetRenderQualitySetting`

```text
GetRenderQualitySetting() -> ERenderQuality
```

获取渲染水平设置（画面品质）
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `ERenderQuality` | 渲染水平枚举值 |

### `GetRenderStyleSetting`

```text
GetRenderStyleSetting() -> ERenderStyle
```

获取渲染风格设置（画面风格）
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `ERenderStyle` | 渲染风格枚举值 |

### `AllowSoftwareOcclusion`

```text
AllowSoftwareOcclusion(bEnabled: boolean)
```

是否开启软件遮挡剔除（默认开启）。2D 类游戏建议关闭，否则在手机上层次相近（接近重叠）的物体处，可能会出现（黑屏）闪烁
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnabled` | `boolean` | 是否开启 |

## Language

`lua`
