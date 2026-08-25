---
id: "api:class:UGCCameraManagerSystem"
title: "UGCCameraManagerSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E8%A7%92%E8%89%B2%E7%B3%BB%E7%BB%9F/UGCCameraManagerSystem.json"
category: "API Wiki/class/和平全局接口/角色系统"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCCameraManagerSystem

相机管理器系统接口库

## Functions

### `GetInVehicleFPPViewPitchLimitMin`

```text
GetInVehicleFPPViewPitchLimitMin() -> @Pitch
```

获得第一人称视角下在载具内的 Pitch 视角限制（最小值）
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `@Pitch` | 视角限制（最小值） |

### `SetInVehicleFPPViewPitchLimitMin`

```text
SetInVehicleFPPViewPitchLimitMin(PitchLimit: number)
```

设置第一人称视角下在载具内的 Pitch 视角限制（最小值）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PitchLimit` | `number` | Pitch 视角限制（最小值） |

### `GetInVehicleFPPViewYawLimit`

```text
GetInVehicleFPPViewYawLimit() -> @Yaw
```

获得第一人称视角下在载具内的 Yaw 视角限制
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `@Yaw` | 视角限制 |

### `SetInVehicleFPPViewYawLimit`

```text
SetInVehicleFPPViewYawLimit(YawLimit: number)
```

设置第一人称视角下在载具内的 Yaw 视角限制
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `YawLimit` | `number` | Yaw 视角限制 |

### `GetInVehicleNarrowSeatGrenadesYawLimit`

```text
GetInVehicleNarrowSeatGrenadesYawLimit() -> @Yaw
```

获得在载具内的狭窄座位手雷投掷 Yaw 视角限制
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `@Yaw` | 视角限制 |

### `SetInVehicleNarrowSeatGrenadesYawLimit`

```text
SetInVehicleNarrowSeatGrenadesYawLimit(YawLimit: number)
```

设置在载具内的狭窄座位手雷投掷 Yaw 视角限制
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `YawLimit` | `number` | Yaw 视角限制 |

## Language

`lua`
