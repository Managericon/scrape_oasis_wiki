---
id: "api:class:UGCActorComponentUtility"
title: "UGCActorComponentUtility"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%9F%BA%E7%A1%80%E5%8A%9F%E8%83%BD/UGCActorComponentUtility.json"
category: "API Wiki/class/和平全局接口/基础功能"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCActorComponentUtility

Actor接口库

## Functions

### `SpawnActor`

```text
SpawnActor(WorldContextObject: UObject, ActorClass: UClass, Location: Vector, Rotation: Rotator, Scale3D: Vector, Owner: Actor) -> Actor
```

在游戏世界中生成指定类型的 Actor
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `ActorClass` | `UClass` | 要生成的 Actor 类型，需通过 UGCObjectUtility.LoadClass 加载类引用 |
| `Location` | `Vector` | 生成位置坐标，推荐使用 {X=1,Y=1,Z=1} 构造 |
| `Rotation` | `Rotator` | 生成旋转角度，推荐使用 {X=0,Y=0,Z=0} 构造 |
| `Scale3D` | `Vector` | 可生成缩放比例，推荐使用 {X=1,Y=1,Z=1} 构造，默认值: Vector(0,0,0)，建议使用Vector(1,1,1)保持原始比例 |
| `Owner` | `Actor` | 新生成 Actor 的所属对象 |

**Returns**

| Type | Description |
|---|---|
| `Actor` | 新生成的 Actor 实例 |

### `DestroyActor`

```text
DestroyActor(InActor: AActor)
```

销毁Actor
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |

### `ToString`

```text
ToString(InActor: AActor) -> string
```

获取Actor的ToString
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |

**Returns**

| Type | Description |
|---|---|
| `string` | ToString |

### `GetOwner`

```text
GetOwner(InActor: AActor) -> AActor
```

获取Actor的Owner
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |

**Returns**

| Type | Description |
|---|---|
| `AActor` | Owner |

### `SetOwner`

```text
SetOwner(InActor: AActor, InOwner: AActor)
```

设置Actor的Owner
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |
| `InOwner` | `AActor` | Owner |

### `GetUltimateOwnerActor`

```text
GetUltimateOwnerActor(InActor: AActor) -> AActor
```

获取技能，武器，Buff等持有者acotr
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |

**Returns**

| Type | Description |
|---|---|
| `AActor` | Owner |

### `GetUltimateController`

```text
GetUltimateController(InActor: AActor) -> AActor
```

获取技能，武器，Buff等持有者的Controller
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |

**Returns**

| Type | Description |
|---|---|
| `AActor` | Owner |

### `AttachToActor`

```text
AttachToActor(InActor: AActor, InAttachTo: AActor, LocationRule: EAttachmentRule, RotationRule: EAttachmentRule, ScaleRule: EAttachmentRule, InSocketName: string)
```

附着到Actor上
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |
| `InAttachTo` | `AActor` | 需要附着到的Actor |
| `LocationRule` | `EAttachmentRule` | 附着位置规则 |
| `RotationRule` | `EAttachmentRule` | 附着旋转规则 |
| `ScaleRule` | `EAttachmentRule` | 附着缩放规则 |
| `InSocketName` | `string` | 需要附着到的SocketName |

### `AttachToComponent`

```text
AttachToComponent(InActor: AActor, InAttachTo: USceneComponent, LocationRule: EAttachmentRule, RotationRule: EAttachmentRule, ScaleRule: EAttachmentRule, InSocketName: string, bWeldSimulatedBodies: boolean)
```

附着到Component上
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |
| `InAttachTo` | `USceneComponent` | 需要附着到的Actor |
| `LocationRule` | `EAttachmentRule` | 附着位置规则 |
| `RotationRule` | `EAttachmentRule` | 附着旋转规则 |
| `ScaleRule` | `EAttachmentRule` | 附着缩放规则 |
| `InSocketName` | `string` | 需要附着到的SocketName |
| `bWeldSimulatedBodies` | `boolean` | 是否保持相对位置不变/是否焊接为模拟刚体 |

### `DetachFromParent`

```text
DetachFromParent(InComponent: USceneComponent, bMaintainWorldPosition: boolean, bCallModify: boolean)
```

将Component从父Actor上拆离
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InComponent` | `USceneComponent` | Actor |
| `bMaintainWorldPosition` | `boolean` | 是否保持位置不变 |
| `bCallModify` | `boolean` | 是否调用Modify |

### `GetRootComponent`

```text
GetRootComponent(InActor: AActor) -> USceneComponent
```

获取根组件
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |

**Returns**

| Type | Description |
|---|---|
| `USceneComponent` | 根组件 |

### `GetComponentsByOwner`

```text
GetComponentsByOwner(InActor: AActor) -> UActorComponent[]
```

获取Actor上的所有Component
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |

**Returns**

| Type | Description |
|---|---|
| `UActorComponent[]` | Actor上的所有Component |

### `GetComponentsByClass`

```text
GetComponentsByClass(InActor: AActor, InComonentClass: UClass) -> UActorComponent[]
```

获取Actor上指定类的Component
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |
| `InComonentClass` | `UClass` | 指定Component的Class |

**Returns**

| Type | Description |
|---|---|
| `UActorComponent[]` | Actor上特定类型的Components |

### `GetComponentsByTag`

```text
GetComponentsByTag(InActor: AActor, InComonentClass: UClass, Tag: string) -> UActorComponent[]
```

获取Actor上指定Tag的Component
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |
| `InComonentClass` | `UClass` | ComponentClass |
| `Tag` | `string` | Tag |

**Returns**

| Type | Description |
|---|---|
| `UActorComponent[]` | Components |

### `GetAllActorsOfClass`

```text
GetAllActorsOfClass(WorldContextObject: UObject, ActorClass: UClass) -> AActor[]
```

获取指定Class在场景里的所有Actor
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | WorldContextObject |
| `ActorClass` | `UClass` | ActorClass |

**Returns**

| Type | Description |
|---|---|
| `AActor[]` | Actor列表 |

### `GetAllActorsWithTag`

```text
GetAllActorsWithTag(WorldContextObject: UObject, Tag: string) -> AActor[]
```

获取指定Tag在场景里的所有Actor
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | WorldContextObject |
| `Tag` | `string` | Tag |

**Returns**

| Type | Description |
|---|---|
| `AActor[]` | Actor列表 |

### `GetActorTransform`

```text
GetActorTransform(InActor: AActor) -> FTransform
```

获取Actor的Transform
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | Transform |

### `GetSceneComponentWorldTransform`

```text
GetSceneComponentWorldTransform(InSceneComponent: USceneComponent) -> FTransform
```

获取场景组件的世界Transform
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSceneComponent` | `USceneComponent` | 场景组件 |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | Transform |

### `SetActorTransform`

```text
SetActorTransform(InActor: AActor, InTransform: FTransform)
```

设置Actor的Transform
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |
| `InTransform` | `FTransform` | Transform |

### `HasAuthority`

```text
HasAuthority(InActor: AActor) -> boolean
```

判断是否为权威端
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 当前端是否为权威端 |

### `CreateAndRegisterComponent`

```text
CreateAndRegisterComponent(InComponentClass: UClass, InOuter: UObject, InComponentName: string)
```

创建并注册组件
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InComponentClass` | `UClass` | 要创建组件对应的Class |
| `InOuter` | `UObject` | Outer |
| `InComponentName` | `string` | 要创建组件对应的Class对应的ObjectName |

### `DestroyComponent`

```text
DestroyComponent(InActor: AActor, InComponent: UActorComponent)
```

销毁组件
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |
| `InComponent` | `UActorComponent` | 要销毁的组件 |

### `GetOverlappingActorsWithPrimitiveComponent`

```text
GetOverlappingActorsWithPrimitiveComponent(InPrimitiveComponent: UPrimitiveComponent, Transform: FTransform, ObjectTypes: ESceneQueryType[], ActorClassFilter: UClass, ActorsToIgnore: AActor[]) -> AActor[]
```

获取与PrimitiveComponent重叠的Actor
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPrimitiveComponent` | `UPrimitiveComponent` | 组件 |
| `Transform` | `FTransform` | 组件的Transform |
| `ObjectTypes` | `ESceneQueryType[]` | 对象类型列表 |
| `ActorClassFilter` | `UClass` | 要检测的Actor类型（默认值：nil为全部类型的Actor） |
| `ActorsToIgnore` | `AActor[]` | 需要忽略的Actor列表 |

**Returns**

| Type | Description |
|---|---|
| `AActor[]` | 与目标Actor重叠的Actor列表 |

### `GetActorByActorInstancePath`

```text
GetActorByActorInstancePath(InstancePath: string) -> AActor
```

在运行时通过Actor实例路径获取Actor，对关卡编辑器实例列表里任意Actor右键，选择GetActorInstancePath即可获取路径
生效范围：客户端&服务器
路径格式：PackageName.ObjectPath，例如：UGCmap.test_8

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstancePath` | `string` | 实例路径 |

**Returns**

| Type | Description |
|---|---|
| `AActor` | Actor实例 |

### `SetActorTickEnabled`

```text
SetActorTickEnabled(Actor: AActor, bEnabled: boolean)
```

启用或禁用 Actor 的 Tick
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 目标 Actor |
| `bEnabled` | `boolean` | 是否启用 Tick |

### `IsActorTickEnabled`

```text
IsActorTickEnabled(Actor: AActor) -> @Tick
```

查询 Actor 的 Tick 是否启用
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 目标 Actor |

**Returns**

| Type | Description |
|---|---|
| `@Tick` | 是否启用 |

### `SetActorLocation`

```text
SetActorLocation(Actor: AActor, Location: Vector)
```

设置 Actor 的世界坐标位置
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 目标 Actor |
| `Location` | `Vector` | 新坐标位置 |

### `GetActorLocation`

```text
GetActorLocation(Actor: AActor) -> Vector
```

获取 Actor 的世界坐标位置
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 目标 Actor |

**Returns**

| Type | Description |
|---|---|
| `Vector` | 当前位置 |

### `SetActorRotation`

```text
SetActorRotation(Rotation: Rotator)
```

设置 Actor 的世界旋转
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rotation` | `Rotator` | 新旋转角度 |

### `GetActorRotation`

```text
GetActorRotation() -> Rotator
```

获取 Actor 的世界旋转
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `Rotator` | 当前旋转 |

### `SetActorScale`

```text
SetActorScale(Actor: AActor, Scale: Vector)
```

设置 Actor 的缩放
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 目标 Actor |
| `Scale` | `Vector` | 新的缩放值 |

### `GetActorScale`

```text
GetActorScale() -> Vector
```

获取 Actor 的缩放
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `Vector` | 当前缩放 |

### `SetActorVisible`

```text
SetActorVisible(Actor: AActor, bVisible: boolean)
```

设置 Actor 的可见性
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 目标 Actor |
| `bVisible` | `boolean` | 是否可见 |

### `IsActorVisible`

```text
IsActorVisible(Actor: AActor) -> boolean
```

查询 Actor 当前是否可见
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 目标 Actor |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否可见 |

### `GetComponentOwner`

```text
GetComponentOwner(Component: UComponent) -> AActor
```

获取组件所属的 Actor
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UComponent` | 任意组件 |

**Returns**

| Type | Description |
|---|---|
| `AActor` | 所属 Actor |

### `ActivateComponent`

```text
ActivateComponent(Component: UActorComponent, bReset: boolean)
```

激活已停用的组件，恢复其逐帧更新及组件自身功能
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UActorComponent` | 要激活的组件 |
| `bReset` | `boolean` | 是否强制重新执行组件的激活逻辑，默认 false；为 true 时即使组件已激活也会再次执行激活流程 |

### `DeactivateComponent`

```text
DeactivateComponent(Component: UActorComponent)
```

停用已激活的组件并停止其逐帧更新，用于暂停粒子、移动等可激活组件
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UActorComponent` | 要停用的组件 |

### `IsComponentActive`

```text
IsComponentActive(Component: UActorComponent) -> boolean
```

查询组件当前是否处于激活状态
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UActorComponent` | 目标组件；无效组件返回 false |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 当前调用端的组件激活状态；仅反映激活或停用状态，不代表可见性、物理模拟或有效性 |

### `GetActorBounds`

```text
GetActorBounds(Actor: AActor, bOnlyCollidingComponents: boolean) -> Vector, Vector
```

获取 Actor 的包围盒中心与半尺寸，用于空间定位与范围判断
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 目标 Actor |
| `bOnlyCollidingComponents` | `boolean` | 是否只统计启用碰撞的组件，默认 false；为 false 时统计全部组件（含无碰撞的视觉组件） |

**Returns**

| Type | Description |
|---|---|
| `Vector` | 世界空间包围盒中心；不含子 Actor 组件；Actor 无效时为零向量 |
| `Vector` | 包围盒半尺寸，各轴为完整尺寸的一半；Actor 无效时为零向量 |

### `SetComponentRelativeTransform`

```text
SetComponentRelativeTransform(Component: USceneComponent, RelativeTransform: FTransform)
```

设置组件相对于父级的 Transform，用于调整部件偏移、朝向与缩放（如挂点微调）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `USceneComponent` | 目标场景组件 |
| `RelativeTransform` | `FTransform` | 相对父级的位置、旋转与缩放 |

### `GetComponentRelativeTransform`

```text
GetComponentRelativeTransform(Component: USceneComponent) -> FTransform
```

获取组件相对于父级的 Transform，用于读取当前偏移、朝向与缩放（如缓存原值以便恢复）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `USceneComponent` | 目标场景组件 |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | 相对父级的位置、旋转与缩放；Component 无效时返回 nil |

### `GetAttachedActors`

```text
GetAttachedActors(Actor: AActor, bRecursive: boolean) -> AActor[]
```

获取 Actor 的子 Actor（可选递归取全部后代），用于遍历附着层级（如查询挂载的武器、道具）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 目标 Actor |
| `bRecursive` | `boolean` | 是否沿附着层级递归获取全部后代，默认 false；为 false 时仅返回直接子级 |

**Returns**

| Type | Description |
|---|---|
| `AActor[]` | 已附着的 Actor 列表（同一 Actor 只出现一次）；无子 Actor 或 Actor 无效时返回空列表 |

### `AddActorOffset`

```text
AddActorOffset(Actor: AActor, Delta: Vector)
```

立即沿世界空间平移 Actor 一段距离，用于逐步移动或位置校正（如落地对齐）；连续移动需每帧重复调用
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 目标 Actor |
| `Delta` | `Vector` | 世界空间位移增量 |

### `GetComponentMobility`

```text
GetComponentMobility(Component: USceneComponent) -> EComponentMobility
```

获取场景组件移动性
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `USceneComponent` | 目标组件 |

**Returns**

| Type | Description |
|---|---|
| `EComponentMobility` | 组件移动性；Component 无效时返回 nil |

### `IsComponentVisible`

```text
IsComponentVisible(Component: USceneComponent) -> boolean
```

查询组件是否可见，用于判断（如 3D 名牌、模型部件）当前是否展示
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `USceneComponent` | 目标组件（任意场景组件，含 3D 控件组件） |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否可见；Component 无效时返回 false |

### `SetComponentMobility`

```text
SetComponentMobility(Component: USceneComponent, Mobility: EComponentMobility)
```

设置场景组件移动性
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `USceneComponent` | 目标组件 |
| `Mobility` | `EComponentMobility` | 移动性：Static, Stationary, Movable |

### `SetComponentVisible`

```text
SetComponentVisible(Component: USceneComponent, bVisible: boolean)
```

设置组件的可见性，用于隐藏/显示单个组件（如 3D 名牌、模型部件）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `USceneComponent` | 目标组件（任意场景组件，含 3D 控件组件） |
| `bVisible` | `boolean` | 是否可见 |

## Language

`lua`
