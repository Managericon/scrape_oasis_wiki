---
id: "api:class:UGCGunSystem"
title: "UGCGunSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81%E4%B8%8E%E8%83%8C%E5%8C%85/UGCGunSystem.json"
category: "API Wiki/class/和平全局接口/物品与背包"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCGunSystem

枪械系统接口库

## Functions

### `StartFire`

```text
StartFire(Gun: STExtraShootWeapon)
```

开火
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

### `StopFire`

```text
StopFire(Gun: STExtraShootWeapon)
```

停止开火
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

### `EnableInfiniteBullets`

```text
EnableInfiniteBullets(Gun: STExtraShootWeapon, IsEnable: boolean)
```

启用/停用无限子弹（无需换弹）
启用后，弹夹容量无限，一直开火也无需换弹
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `IsEnable` | `boolean` | 启用/停用 |

### `EnableClipInfiniteBullets`

```text
EnableClipInfiniteBullets(Gun: STExtraShootWeapon, IsEnable: boolean)
```

启用/停用弹夹无限子弹（需要换弹一次）
启用后，子弹容量无限，开火会打空弹夹触发换弹
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `IsEnable` | `boolean` | 启用/停用 |

### `ForceReloadAndEnableInfiniteBullets`

```text
ForceReloadAndEnableInfiniteBullets(Gun: STExtraShootWeapon, IsEnable: boolean)
```

启用/停用无限子弹（无需换弹）并且强制换弹
启用后，强制换弹弹夹容量无限，一直开火也无需换弹，避免弹夹内子弹为0时触发检查
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `IsEnable` | `boolean` | 启用/停用 |

### `SetMaxBulletNumInOneClip`

```text
SetMaxBulletNumInOneClip(Gun: STExtraShootWeapon, MaxBulletNumInOneClip: number)
```

设置弹夹容量
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `MaxBulletNumInOneClip` | `number` | 弹夹容量 |

### `GetMaxBulletNumInOneClip`

```text
GetMaxBulletNumInOneClip(Gun: STExtraShootWeapon) -> number
```

获取弹夹容量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `number` | 弹夹容量 |

### `SetBulletFireSpeed`

```text
SetBulletFireSpeed(Gun: STExtraShootWeapon, BulletFireSpeed: number)
```

设置子弹飞行速度
例：60000代表1秒飞行600米
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `BulletFireSpeed` | `number` | 飞行速度 |

### `GetBulletFireSpeed`

```text
GetBulletFireSpeed(Gun: STExtraShootWeapon) -> number
```

获取子弹飞行速度
例：60000代表1秒飞行600米
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `number` | 当前飞行速度 |

### `SetShootIntervalTime`

```text
SetShootIntervalTime(Gun: STExtraShootWeapon, ShootIntervalTime: number)
```

设置射击间隔时间
例：0.1代表0.1秒射击一次
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `ShootIntervalTime` | `number` | 射击间隔时间 |

### `GetShootIntervalTime`

```text
GetShootIntervalTime(Gun: STExtraShootWeapon) -> number
```

获取射击间隔时间
例：0.1代表0.1秒射击一次
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `number` | 射击间隔时间 |

### `SetBulletRange`

```text
SetBulletRange(Gun: STExtraShootWeapon, BulletRange: number)
```

设置子弹射程
例：60000射程为600米
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `BulletRange` | `number` | 子弹射程 |

### `GetBulletRange`

```text
GetBulletRange(Gun: STExtraShootWeapon) -> number
```

获取子弹射程
例：60000射程为600米
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `number` | 子弹射程 |

### `SetBulletBaseDamage`

```text
SetBulletBaseDamage(Gun: STExtraShootWeapon, BulletBaseDamage: number)
```

设置子弹基础伤害
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `BulletBaseDamage` | `number` | 基础伤害 |

### `GetBulletBaseDamage`

```text
GetBulletBaseDamage(Gun: STExtraShootWeapon) -> number
```

获取子弹基础伤害
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `number` | 基础伤害 |

### `SetBulletMinimumDamage`

```text
SetBulletMinimumDamage(Gun: STExtraShootWeapon, BulletMinimumDamage: number)
```

设置子弹最低伤害（子弹经过穿透，距离等衰减后）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `BulletMinimumDamage` | `number` | 最低伤害 |

### `GetBulletMinimumDamage`

```text
GetBulletMinimumDamage(Gun: STExtraShootWeapon) -> number
```

获取子弹最低伤害（子弹经过穿透，距离等衰减后）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `number` | 最低伤害 |

### `SetBulletImpulse`

```text
SetBulletImpulse(Gun: STExtraShootWeapon, BulletImpulse: number)
```

设置子弹命中冲量
冲量越大，击退击飞效果越大
参考：破片手雷最大造成冲量为2500
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `BulletImpulse` | `number` | 冲量 |

### `GetBulletImpulse`

```text
GetBulletImpulse(Gun: STExtraShootWeapon) -> number
```

获取子弹命中冲量
冲量越大，击退击飞效果越大
参考：破片手雷最大造成冲量为2500
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `number` | 冲量 |

### `SetReloadTime`

```text
SetReloadTime(Gun: STExtraShootWeapon, ReloadTime: number)
```

设置换弹时间
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `ReloadTime` | `number` | 换弹时间 |

### `GetReloadTime`

```text
GetReloadTime(Gun: STExtraShootWeapon) -> number
```

获取换弹时间                 
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `number` | 换弹时间 |

### `SetTacticalReloadTime`

```text
SetTacticalReloadTime(Gun: STExtraShootWeapon, TacticalReloadTime: number)
```

设置战术换弹时间（弹夹子弹数不为0）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `TacticalReloadTime` | `number` | 换弹时间 |

### `GetTacticalReloadTime`

```text
GetTacticalReloadTime(Gun: STExtraShootWeapon) -> number
```

获取战术换弹时间（弹夹子弹数不为0）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `number` | 换弹时间 |

### `SetVerticalRecoilScale`

```text
SetVerticalRecoilScale(Gun: STExtraShootWeapon, VerticalRecoilScale: number)
```

设置垂直后坐力倍率
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `VerticalRecoilScale` | `number` | 倍率 |

### `GetVerticalRecoilScale`

```text
GetVerticalRecoilScale(Gun: STExtraShootWeapon) -> number
```

获取垂直后坐力倍率
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `number` | 倍率 |

### `SetHorizontalRecoilScale`

```text
SetHorizontalRecoilScale(Gun: STExtraShootWeapon, HorizontalRecoilScale: number)
```

设置水平后坐力倍率
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `HorizontalRecoilScale` | `number` | 倍率 |

### `GetHorizontalRecoilScale`

```text
GetHorizontalRecoilScale(Gun: STExtraShootWeapon) -> number
```

获取水平后坐力倍率
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `number` | 倍率 |

### `SetDeviationScale`

```text
SetDeviationScale(Gun: STExtraShootWeapon, DeviationScale: number)
```

设置扩散值倍率
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `DeviationScale` | `number` | 倍率 |

### `GetDeviationScale`

```text
GetDeviationScale(Gun: STExtraShootWeapon) -> number
```

获取扩散值倍率
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `number` | 倍率 |

### `Reload`

```text
Reload(PlayerPawn: PlayerPawn)
```

玩家当前武器换弹
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

### `OpenScope`

```text
OpenScope(PlayerPawn: PlayerPawn, IsOpenScope: boolean)
```

玩家当前武器开镜/关镜
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `IsOpenScope` | `boolean` | 开镜/关镜 |

### `GetIsAutoAimEnabled`

```text
GetIsAutoAimEnabled(PlayerPawn: PlayerPawn) -> boolean
```

获取辅助瞄准是否启用 
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 启用/关闭 |

### `SetIsAutoAimEnabled`

```text
SetIsAutoAimEnabled(PlayerPawn: PlayerPawn, IsAutoAimEnabled: boolean)
```

设置自动瞄准是否启用 
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `IsAutoAimEnabled` | `boolean` | 启用/关闭 |

### `AddGunAttachment`

```text
AddGunAttachment(Gun: STExtraShootWeapon, ItemDefineID: ItemDefineID)
```

武器添加指定配件
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `ItemDefineID` | `ItemDefineID` | 物品DefineID |

### `CreateAndAddGunAttachment`

```text
CreateAndAddGunAttachment(Gun: STExtraShootWeapon, ItemID: number)
```

创建新配件并且直接添加到武器
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `ItemID` | `number` | 物品ID |

### `RemoveGunAttachmentBySocketType`

```text
RemoveGunAttachmentBySocketType(Gun: STExtraShootWeapon, SocketType: WeaponAttachmentSocketType)
```

卸载武器指定部位配件
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `SocketType` | `WeaponAttachmentSocketType` | 配件槽位 |

### `GetWeaponAttachmentIDBySocketType`

```text
GetWeaponAttachmentIDBySocketType(Gun: STExtraShootWeapon, SocketType: WeaponAttachmentSocketType) -> ItemDefineID
```

获取特定槽位的配件ItemDefineID
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `SocketType` | `WeaponAttachmentSocketType` | 配件槽位 |

**Returns**

| Type | Description |
|---|---|
| `ItemDefineID` | - |

### `GetAvailableWeaponAttachmentSocketTypeList`

```text
GetAvailableWeaponAttachmentSocketTypeList(Gun: STExtraShootWeapon) -> @AttachmentSocketType
```

获取枪械可用的配件槽位
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `@AttachmentSocketType` | 列表 |

### `GetAvailableWeaponAttachment`

```text
GetAvailableWeaponAttachment(Gun: STExtraShootWeapon) -> @AvailableWeaponAttachment
```

获取武器可用配件(需要武器加载出来才能使用，不能在武器初始化时调用)
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `@AvailableWeaponAttachment` | 列表 |

### `DisuseAllWeaponAttachmentsOnServer`

```text
DisuseAllWeaponAttachmentsOnServer(Gun: STExtraShootWeapon)
```

卸载武器所有配件
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

### `GetWeaponAllAttachmentIDList`

```text
GetWeaponAllAttachmentIDList(Gun: STExtraShootWeapon) -> @AttachmentDefineID
```

获取武器上的所有配件
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `@AttachmentDefineID` | 列表 |

### `SetCurrentBulletNumInClip`

```text
SetCurrentBulletNumInClip(Gun: STExtraShootWeapon, Count: int)
```

设置武器弹匣内弹药
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `Count` | `int` | 枪械 |

## Language

`lua`
