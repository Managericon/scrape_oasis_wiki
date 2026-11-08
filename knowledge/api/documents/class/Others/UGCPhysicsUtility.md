---
id: "api:class:UGCPhysicsUtility"
title: "UGCPhysicsUtility"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGCPhysicsUtility.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCPhysicsUtility

统一物理能力接口库

## Functions

### `AddBeginOverlapDelegate`

```text
AddBeginOverlapDelegate(Component: UPrimitiveComponent, Callback: function, Callback_self: UObject)
```

注册组件开始重叠事件回调，用于检测物体开始接触（如角色走入触发区域）
生效范围：服务器&客户端
      回调签名：(OverlappedComponent, OtherActor, OtherComp, OtherBodyIndex, bFromSweep, SweepResult)；
      绑定方式：Component.OnComponentBeginOverlap:Add(Callback, Callback_self)；
      移除方式：UGCPhysicsUtility.RemoveBeginOverlapDelegate(Component, Callback, Callback_self)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent` | 目标组件；双方组件均需生成重叠事件才会触发回调 |
| `Callback` | `function` | 回调函数，参数为 OverlappedComponent、OtherActor、OtherComp、OtherBodyIndex；如需扫掠细节，可多声明两个参数接收 bFromSweep、SweepResult |
| `Callback_self` | `UObject` | 冒号形式回调的 self，可选；带冒号定义时传入 self，不带冒号时传 nil |

### `AddEndOverlapDelegate`

```text
AddEndOverlapDelegate(Component: UPrimitiveComponent, Callback: function, Callback_self: UObject)
```

注册组件结束重叠事件回调，用于检测物体停止接触（如角色走出触发区域）
生效范围：服务器&客户端
      回调签名：(OverlappedComponent, OtherActor, OtherComp, OtherBodyIndex)；
      绑定方式：Component.OnComponentEndOverlap:Add(Callback, Callback_self)；
      移除方式：UGCPhysicsUtility.RemoveEndOverlapDelegate(Component, Callback, Callback_self)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent` | 目标组件；双方组件均需生成重叠事件才会触发回调 |
| `Callback` | `function` | 回调函数，参数为 OverlappedComponent、OtherActor、OtherComp、OtherBodyIndex |
| `Callback_self` | `UObject` | 冒号形式回调的 self，可选；带冒号定义时传入 self，不带冒号时传 nil |

### `ApplyAngularImpulse`

```text
ApplyAngularImpulse(Component: UPrimitiveComponent, AngularImpulse: Vector, BoneName: string, bVelChange: boolean)
```

对物理组件施加角冲量，用于瞬间改变物体旋转（如受击打转、旋转击飞）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent` | 目标物理组件；需已启用物理模拟 |
| `AngularImpulse` | `Vector` | 角冲量，单位为度；方向为旋转轴 |
| `BoneName` | `string` | 骨骼名称，可选；不传则作用于整体刚体 |
| `bVelChange` | `boolean` | 是否按角速度变化施加，默认 false；为 true 时不受质量影响 |

### `ApplyForce`

```text
ApplyForce(Component: UPrimitiveComponent, Force: Vector, BoneName: string, bAccelChange: boolean)
```

对物理组件施加作用力，每帧调用可实现持续推动（如推进器、风力）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent` | 目标物理组件；需已启用物理模拟 |
| `Force` | `Vector` | 世界空间作用力；按质量换算为加速度变化 |
| `BoneName` | `string` | 骨骼名称，可选；不传则作用于整体刚体 |
| `bAccelChange` | `boolean` | 是否按加速度变化施加，默认 false；为 true 时不受质量影响 |

### `ApplyImpulse`

```text
ApplyImpulse(Component: UPrimitiveComponent, Impulse: Vector, BoneName: string, bVelChange: boolean)
```

对物理组件施加线性冲量，用于击飞、弹射等瞬时加速
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent` | 目标物理组件；需已启用物理模拟 |
| `Impulse` | `Vector` | 世界空间冲量；按质量换算为速度变化 |
| `BoneName` | `string` | 骨骼名称，可选；不传则作用于整体刚体 |
| `bVelChange` | `boolean` | 是否按速度变化施加，默认 false；为 true 时不受质量影响 |

### `ApplyImpulseAtLocation`

```text
ApplyImpulseAtLocation(Component: UPrimitiveComponent, Impulse: Vector, Location: Vector, BoneName: string)
```

在指定世界位置对物理组件施加冲量，用于制造偏心撞击（如击中边缘时推移并打转）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent` | 目标物理组件；需已启用物理模拟 |
| `Impulse` | `Vector` | 世界空间冲量；按质量换算为速度变化 |
| `Location` | `Vector` | 世界空间作用位置 |
| `BoneName` | `string` | 骨骼名称，可选；不传则作用于整体刚体 |

### `GetAngularVelocity`

```text
GetAngularVelocity(Component: UPrimitiveComponent) -> Vector
```

获取物理组件角速度
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent` | 目标组件 |

**Returns**

| Type | Description |
|---|---|
| `Vector` | 角速度，单位为度每秒；Component 无效时返回零向量 |

### `GetCenterOfMass`

```text
GetCenterOfMass(Component: UPrimitiveComponent) -> Vector
```

获取物理组件质心位置
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent` | 目标组件 |

**Returns**

| Type | Description |
|---|---|
| `Vector` | 世界空间质心位置；Component 无效时返回零向量 |

### `GetLinearVelocity`

```text
GetLinearVelocity(Component: UPrimitiveComponent, BoneName: string) -> Vector
```

获取物理组件线速度
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent` | 目标组件 |
| `BoneName` | `string` | 骨骼名称，可选；不传则取整体刚体 |

**Returns**

| Type | Description |
|---|---|
| `Vector` | 线速度；Component 无效时返回零向量 |

### `GetMass`

```text
GetMass(Component: UPrimitiveComponent) -> number
```

获取物理组件的质量（千克），用于按重量计算受力、浮力等物理效果
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent` | 目标组件 |

**Returns**

| Type | Description |
|---|---|
| `number` | 质量（千克）；组件无效或尚无物理体时返回 0 |

### `GetVelocityAtPoint`

```text
GetVelocityAtPoint(Component: UPrimitiveComponent, Point: Vector) -> Vector
```

获取物理组件指定世界位置的线速度
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent` | 目标组件 |
| `Point` | `Vector` | 世界空间采样点 |

**Returns**

| Type | Description |
|---|---|
| `Vector` | 采样点线速度；Component 无效时返回零向量 |

### `IsActorCollisionEnabled`

```text
IsActorCollisionEnabled(Actor: Actor) -> boolean
```

查询 Actor 是否启用碰撞
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | 目标 Actor |

**Returns**

| Type | Description |
|---|---|
| `boolean` | Actor 级碰撞开关是否开启；关闭时该 Actor 的所有组件均不参与碰撞，开启时各组件仍受自身碰撞设置约束；Actor 无效时返回 false |

### `IsOverlapEventsEnabled`

```text
IsOverlapEventsEnabled(Component: UPrimitiveComponent) -> boolean
```

查询组件是否生成重叠事件
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent` | 目标组件 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否生成重叠事件；需双方组件都开启，重叠事件才会触发；Component 无效时返回 false |

### `IsSimulatingPhysics`

```text
IsSimulatingPhysics(Component: UPrimitiveComponent, BoneName: string) -> boolean
```

查询组件是否正在模拟物理，用于判断物体当前是否由物理驱动
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent` | 目标组件 |
| `BoneName` | `string` | 骨骼名称，可选；不传则查询整体刚体 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 组件（或指定骨骼）当前是否处于物理模拟状态；组件无效、无物理体或骨骼名无效时返回 false |

### `GetOverlappingActors`

```text
GetOverlappingActors(Actor: Actor, ActorClassFilter: UClass) -> Actor[]
```

获取当前与 Actor 接触的所有 Actor，用于即时查询接触状态（如判断角色是否已在触发区域内）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | 目标 Actor；双方组件均需生成重叠事件才会出现在结果中（编辑器新建的组件默认关闭，可用 SetOverlapEventsEnabled 开启） |
| `ActorClassFilter` | `UClass` | 可选，按类过滤返回的重叠 Actor |

**Returns**

| Type | Description |
|---|---|
| `Actor[]` | 当前重叠的 Actor 列表（同一 Actor 只出现一次）；无重叠或 Actor 无效时返回空列表 |

### `RemoveBeginOverlapDelegate`

```text
RemoveBeginOverlapDelegate(Component: UPrimitiveComponent, Callback: function, Callback_self: UObject)
```

移除组件开始重叠事件回调，用于停止接触检测（如对象销毁前解除订阅）
生效范围：服务器&客户端
      移除方式：Component.OnComponentBeginOverlap:Remove(Callback, Callback_self)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent` | 目标组件 |
| `Callback` | `function` | Add 时注册的回调函数 |
| `Callback_self` | `UObject` | Add 时传入的 self，可选；需与注册时一致 |

### `RemoveEndOverlapDelegate`

```text
RemoveEndOverlapDelegate(Component: UPrimitiveComponent, Callback: function, Callback_self: UObject)
```

移除组件结束重叠事件回调，用于停止离开检测（如对象销毁前解除订阅）
生效范围：服务器&客户端
      移除方式：Component.OnComponentEndOverlap:Remove(Callback, Callback_self)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent` | 目标组件 |
| `Callback` | `function` | Add 时注册的回调函数 |
| `Callback_self` | `UObject` | Add 时传入的 self，可选；需与注册时一致 |

### `SetActorCollisionEnabled`

```text
SetActorCollisionEnabled(Actor: Actor, bEnabled: boolean)
```

设置 Actor 是否参与碰撞
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | 目标 Actor |
| `bEnabled` | `boolean` | 是否启用碰撞 |

### `SetOverlapEventsEnabled`

```text
SetOverlapEventsEnabled(Component: UPrimitiveComponent, bEnabled: boolean)
```

设置物理组件是否生成重叠事件，用于按需开启或关闭该组件的接触检测
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent` | 目标组件 |
| `bEnabled` | `boolean` | 是否生成重叠事件；需双方组件都开启，重叠事件才会触发；UGC 编辑器新建组件默认关闭，需显式开启 |

### `SetSimulatePhysics`

```text
SetSimulatePhysics(Component: UPrimitiveComponent, bSimulate: boolean)
```

设置物理组件是否模拟物理，用于让物体开始或停止受重力与碰撞驱动（如击飞下落、落地固定）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent` | 目标组件；需为带物理体的非静态（Movable）组件 |
| `bSimulate` | `boolean` | 是否启用物理模拟；启用时会先解除该组件与父级的附着（保持世界变换），关闭后恢复为固定（运动学）状态 |

### `SetAngularVelocity`

```text
SetAngularVelocity(Component: UPrimitiveComponent, AngularVelocity: Vector)
```

设置物理组件角速度
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent` | 目标组件 |
| `AngularVelocity` | `Vector` | 角速度，单位为度每秒 |

### `SetLinearVelocity`

```text
SetLinearVelocity(Component: UPrimitiveComponent, Velocity: Vector)
```

设置物理组件线速度
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent` | 目标组件 |
| `Velocity` | `Vector` | 线速度 |

### `SetMass`

```text
SetMass(Component: UPrimitiveComponent, Mass: number)
```

设置物理组件的质量（千克），用于按重量调整受力、浮力等物理表现
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent` | 目标组件 |
| `Mass` | `number` | 质量（千克），必须为大于 0 的有限数值；设置后该组件质量固定为此值，不再随网格缩放或物理材质密度自动变化 |

## Language

`lua`
