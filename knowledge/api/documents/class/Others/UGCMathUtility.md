---
id: "api:class:UGCMathUtility"
title: "UGCMathUtility"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGCMathUtility.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCMathUtility

数学工具接口库

## Functions

### `Sin`

```text
Sin(A: number) -> number
```

返回A的正弦值(sin)，结果为弧度制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | sin(A) |

### `Asin`

```text
Asin(A: number) -> number
```

返回A的反正弦值(arcsin)，结果为弧度制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | arcsin(A) |

### `Cos`

```text
Cos(A: number) -> number
```

返回A的余弦值(cos)，结果为弧度制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | cos(A) |

### `Acos`

```text
Acos(A: number) -> number
```

返回A的反余弦值(arccos)，结果为弧度制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | arccos(A) |

### `Tan`

```text
Tan(A: number) -> number
```

返回A的正切值(tan)，结果为弧度制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | tan(A) |

### `Atan`

```text
Atan(A: number) -> number
```

返回A的反正切值(arctan)，结果为弧度制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | arctan(A) |

### `DegSin`

```text
DegSin(A: number) -> number
```

返回A的正弦值(sin)，结果为角度制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | sin(A) |

### `DegAsin`

```text
DegAsin(A: number) -> number
```

返回A的反正弦值(arcsin)，结果为角度制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | arcsin(A) |

### `DegCos`

```text
DegCos(A: number) -> number
```

返回A的余弦值(cos)，结果为角度制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | cos(A) |

### `DegAcos`

```text
DegAcos(A: number) -> number
```

返回A的反余弦值(arccos)，结果为角度制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | arccos(A) |

### `DegTan`

```text
DegTan(A: number) -> number
```

返回A的正切值(tan)，结果为角度制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | tan(A) |

### `DegAtan`

```text
DegAtan(A: number) -> number
```

返回A的反正切值(arctan)，结果为角度制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | arctan(A) |

### `DegAtan2`

```text
DegAtan2(A: number, B: number) -> number
```

返回A/B的反正切值(atan2)，结果为角度制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |
| `B` | `number` | B |

**Returns**

| Type | Description |
|---|---|
| `number` | arctan(A/B) |

### `RandomFloat`

```text
RandomFloat() -> number
```

返回一个介于0和1之间的随机浮点数

**Returns**

| Type | Description |
|---|---|
| `number` | 随机浮点数 |

### `RandomFloatInRange`

```text
RandomFloatInRange(InMin: number, InMax: number) -> number
```

生成一个介于Min和Max之间的随机数

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMin` | `number` | 最小值 |
| `InMax` | `number` | 最大值 |

**Returns**

| Type | Description |
|---|---|
| `number` | 随机数 |

### `Lerp`

```text
Lerp(A: number, B: number, Alpha: number) -> number
```

根据Alpha在A和B之间线性插值（Alpha=0时返回A，Alpha=1时返回B））

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |
| `B` | `number` | B |
| `Alpha` | `number` | Alpha |

**Returns**

| Type | Description |
|---|---|
| `number` | 线性插值 |

### `FClamp`

```text
FClamp(InValue: number, InMin: number, InMax: number) -> number
```

【废弃】请使用 UGCMathUtility.Clamp
返回限制在A和B之间的值（包含A和B）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `number` | 值 |
| `InMin` | `number` | 最小值 |
| `InMax` | `number` | 最大值 |

**Returns**

| Type | Description |
|---|---|
| `number` | 限制后的值 |

### `MapRangeClamped`

```text
MapRangeClamped(InValue: number, InMinIn: number, InMaxIn: number, InMinOut: number, InMaxOut: number) -> number
```

将数值从一个输入范围映射到另一个输出范围（数值会被限制在输入范围内）。（例如：将0.5从0→1范围映射到0→50范围会得到25）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `number` | 值 |
| `InMinIn` | `number` | 输入范围最小值 |
| `InMaxIn` | `number` | 输入范围最大值 |
| `InMinOut` | `number` | 输出范围最小值 |
| `InMaxOut` | `number` | 输出范围最大值 |

**Returns**

| Type | Description |
|---|---|
| `number` | 映射后的值 |

### `NearlyEqualFloat`

```text
NearlyEqualFloat(A: number, B: number, Tolerance: number) -> boolean
```

返回A是否近似等于B（|A - B| < 误差容限）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |
| `B` | `number` | B |
| `Tolerance` | `number` | 误差容限 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否近似等于 |

### `NotEqualFloat`

```text
NotEqualFloat(A: number, B: number) -> boolean
```

如果A不等于B则返回true

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |
| `B` | `number` | B |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否不等于 |

### `Now`

```text
Now() -> FDateTime
```

返回当前计算机的本地日期和时间

**Returns**

| Type | Description |
|---|---|
| `FDateTime` | 当前计算机的本地日期和时间 |

### `Today`

```text
Today() -> FDateTime
```

返回当前计算机的本地日期

**Returns**

| Type | Description |
|---|---|
| `FDateTime` | 当前计算机的本地日期 |

### `UtcNow`

```text
UtcNow() -> FDateTime
```

返回当前计算机的UTC日期和时间

**Returns**

| Type | Description |
|---|---|
| `FDateTime` | 当前计算机的UTC日期和时间 |

### `GetYear`

```text
GetYear(A: FDateTime) -> number
```

返回A的年分量值

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FDateTime` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | 年分量值 |

### `GetMonth`

```text
GetMonth(A: FDateTime) -> number
```

返回A的月分量值

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FDateTime` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | 月分量值 |

### `DaysInMonth`

```text
DaysInMonth(Year: number, Month: number) -> number
```

返回给定年份和月份的天数

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Year` | `number` | 年份 |
| `Month` | `number` | 月份 |

**Returns**

| Type | Description |
|---|---|
| `number` | 天数 |

### `AddVector`

```text
AddVector(A: FVector, B: FVector) -> FVector
```

向量加法

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | A |
| `B` | `FVector` | B |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `AddVector2D`

```text
AddVector2D(A: FVector2D, B: FVector2D) -> FVector2D
```

返回二维向量A和二维向量B的和（A + B）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | A |
| `B` | `FVector2D` | B |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `SubtractVector`

```text
SubtractVector(A: FVector, B: FVector) -> FVector
```

向量减法

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | A |
| `B` | `FVector` | B |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `SubtractVector2D`

```text
SubtractVector2D(A: FVector2D, B: FVector2D) -> FVector2D
```

返回二维向量A和二维向量B的差（A - B）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | A |
| `B` | `FVector2D` | B |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `MultiplyVector`

```text
MultiplyVector(A: FVector, B: number) -> FVector
```

将向量A按B缩放

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | A |
| `B` | `number` | B |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `MultiplyVector2D`

```text
MultiplyVector2D(A: FVector2D, B: number) -> FVector2D
```

将二维向量A按B缩放

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | A |
| `B` | `number` | B |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `VSize`

```text
VSize(A: FVector) -> number
```

返回向量的长度

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `VSize2D`

```text
VSize2D(A: FVector2D) -> number
```

返回二维向量的长度

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `VSizeSquared`

```text
VSizeSquared(A: FVector) -> number
```

返回向量的长度的平方

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `VSizeSquared2D`

```text
VSizeSquared2D(A: FVector2D) -> number
```

返回二维向量的长度的平方

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `EqualVector`

```text
EqualVector(A: FVector, B: FVector, Tolerance: number) -> boolean
```

判断向量A是否在允许误差范围内等于向量B

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | A |
| `B` | `FVector` | B |
| `Tolerance` | `number` | 允许误差，默认为1.e-4f |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `NotEqualVector`

```text
NotEqualVector(A: FVector, B: FVector, Tolerance: number) -> boolean
```

判断向量A是否在允许误差范围内不等于向量B

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | A |
| `B` | `FVector` | B |
| `Tolerance` | `number` | 允许误差，默认为1.e-4f |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `DotVector`

```text
DotVector(A: FVector, B: FVector) -> number
```

返回两个向量的点积

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | A |
| `B` | `FVector` | B |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `CrossVector`

```text
CrossVector(A: FVector, B: FVector) -> FVector
```

返回两个向量的叉积

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | A |
| `B` | `FVector` | B |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `DotVector2D`

```text
DotVector2D(A: FVector2D, B: FVector2D) -> number
```

返回两个二维向量的点积

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | A |
| `B` | `FVector2D` | B |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `CrossVector2D`

```text
CrossVector2D(A: FVector2D, B: FVector2D) -> number
```

返回两个二维向量的叉积

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | A |
| `B` | `FVector2D` | B |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `RotateVector`

```text
RotateVector(A: FVector, B: FRotator) -> FVector
```

返回向量A经过 Rotator B 旋转后的结果

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | A |
| `B` | `FRotator` | B |

**Returns**

| Type | Description |
|---|---|
| `FVector` | Vector |

### `RotateAngleAxis`

```text
RotateAngleAxis(A: FVector, AngleDeg: number, Axis: FVector) -> FVector
```

返回向量A绕Axis轴旋转AngleDeg角度后的结果

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | A |
| `AngleDeg` | `number` | AngleDeg |
| `Axis` | `FVector` | Axis |

**Returns**

| Type | Description |
|---|---|
| `FVector` | Vector |

### `Normal`

```text
Normal(A: FVector) -> FVector
```

返回向量A的单位法向量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | A |

**Returns**

| Type | Description |
|---|---|
| `FVector` | Vector |

### `Normal2D`

```text
Normal2D(A: FVector2D) -> FVector2D
```

返回二维向量A的单位法向量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | A |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | Vector |

### `VLerp`

```text
VLerp(A: FVector, B: FVector, Alpha: number) -> FVector
```

根据Alpha值在向量A和向量B之间线性插值（Alpha=0时返回100%A，Alpha=1时返回100%B）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | A |
| `B` | `FVector` | B |
| `Alpha` | `number` | Alpha |

**Returns**

| Type | Description |
|---|---|
| `FVector` | Vector |

### `RandomUnitVector`

```text
RandomUnitVector() -> FVector
```

返回一个长度为1的随机向量

**Returns**

| Type | Description |
|---|---|
| `FVector` | Vector |

### `RandomPointInBoundingBox`

```text
RandomPointInBoundingBox(Origin: FVector, BoxExtent: FVector) -> FVector
```

返回指定边界框内的随机点

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Origin` | `FVector` | Origin |
| `BoxExtent` | `FVector` | BoxExtent |

**Returns**

| Type | Description |
|---|---|
| `FVector` | Point |

### `ProjectVectorOnToVector`

```text
ProjectVectorOnToVector(V: FVector, Target: FVector) -> FVector
```

将向量V投影到目标向量Target上并返回投影向量，如果Target长度接近零，则返回零向量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `V` | `FVector` | V |
| `Target` | `FVector` | Target |

**Returns**

| Type | Description |
|---|---|
| `FVector` | Vector |

### `FInterpTo`

```text
FInterpTo(Current: number, Target: number, DeltaTime: number, InterpSpeed: number) -> number
```

根据当前值到目标值的插值进行平滑过渡，实现流畅的过度效果

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `number` | 当前值 |
| `Target` | `number` | 目标值 |
| `DeltaTime` | `number` | 平滑时间 |
| `InterpSpeed` | `number` | 插值速度 |

**Returns**

| Type | Description |
|---|---|
| `number` | 新的插值位置 |

### `FInterpConstantTo`

```text
FInterpConstantTo(Current: number, Target: number, DeltaTime: number, InterpSpeed: number) -> number
```

以恒定速率向目标值变换

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `number` | 当前值 |
| `Target` | `number` | 目标值 |
| `DeltaTime` | `number` | 平滑时间 |
| `InterpSpeed` | `number` | 插值速度 |

**Returns**

| Type | Description |
|---|---|
| `number` | Location |

### `VInterpTo`

```text
VInterpTo(Current: FVector, Target: FVector, DeltaTime: number, InterpSpeed: number) -> FVector
```

根据向量表示的当前位置与目标位置的距离平滑地接近目标位置，实现流畅的追踪效果

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `FVector` | 当前位置 |
| `Target` | `FVector` | 目标位置 |
| `DeltaTime` | `number` | 平滑时间 |
| `InterpSpeed` | `number` | 插值速度 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 新的插值位置 |

### `VInterpConstantTo`

```text
VInterpConstantTo(Current: FVector, Target: FVector, DeltaTime: number, InterpSpeed: number) -> FVector
```

以恒定速率向向量表示的目标位置移动

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `FVector` | 当前位置 |
| `Target` | `FVector` | 目标位置 |
| `DeltaTime` | `number` | 平滑时间 |
| `InterpSpeed` | `number` | 插值速度 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | Location |

### `Vector2DInterpTo`

```text
Vector2DInterpTo(Current: FVector2D, Target: FVector2D, DeltaTime: number, InterpSpeed: number) -> FVector2D
```

根据二维向量表示的当前位置与目标位置的距离平滑地接近目标位置，实现流畅的追踪效果

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `FVector2D` | 当前位置 |
| `Target` | `FVector2D` | 目标位置 |
| `DeltaTime` | `number` | 平滑时间 |
| `InterpSpeed` | `number` | 插值速度 |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | 新的插值位置 |

### `Vector2DInterpConstantTo`

```text
Vector2DInterpConstantTo(Current: FVector2D, Target: FVector2D, DeltaTime: number, InterpSpeed: number) -> FVector2D
```

以恒定速率向二维向量表示的目标位置移动

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `FVector2D` | 当前位置 |
| `Target` | `FVector2D` | 目标位置 |
| `DeltaTime` | `number` | 平滑时间 |
| `InterpSpeed` | `number` | 插值速度 |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | Location |

### `RInterpTo`

```text
RInterpTo(Current: FRotator, Target: FRotator, DeltaTime: number, InterpSpeed: number) -> FRotator
```

根据当前旋转角度平滑过渡到目标旋转角度，实现流畅的旋转效果

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `FRotator` | 当前旋转角度 |
| `Target` | `FRotator` | 目标旋转角度 |
| `DeltaTime` | `number` | 平滑时间 |
| `InterpSpeed` | `number` | 插值速度 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 新的插值旋转角度 |

### `RInterpConstantTo`

```text
RInterpConstantTo(Current: FRotator, Target: FRotator, DeltaTime: number, InterpSpeed: number) -> FRotator
```

以恒定速率向目标旋转角度旋转

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `FRotator` | 当前旋转角度 |
| `Target` | `FRotator` | 目标旋转角度 |
| `DeltaTime` | `number` | 平滑时间 |
| `InterpSpeed` | `number` | 插值速度 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | Location |

### `FindClosestPointOnSegment`

```text
FindClosestPointOnSegment(Point: FVector, SegmentStart: FVector, SegmentEnd: FVector) -> FVector
```

查找线段上距离给定点最近的点

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Point` | `FVector` | 需要计算最近点的目标点 |
| `SegmentStart` | `FVector` | 线段起点 |
| `SegmentEnd` | `FVector` | 线段终点 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 线段上距离给定点最近的点 |

### `FindClosestPointOnLine`

```text
FindClosestPointOnLine(Point: FVector, LineOrigin: FVector, LineDirection: FVector) -> FVector
```

找到无限长直线上距离给定点最近的点

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Point` | `FVector` | 需要计算最近点的目标点 |
| `LineOrigin` | `FVector` | 直线上的参考点 |
| `LineDirection` | `FVector` | 直线上的方向向量(无需归一化) |

**Returns**

| Type | Description |
|---|---|
| `FVector` | Point |

### `GetPointDistanceToSegment`

```text
GetPointDistanceToSegment(Point: FVector, SegmentStart: FVector, SegmentEnd: FVector) -> number
```

计算点到线段的最短距离

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Point` | `FVector` | 需要计算最近点的目标点 |
| `SegmentStart` | `FVector` | 线段起点 |
| `SegmentEnd` | `FVector` | 线段终点 |

**Returns**

| Type | Description |
|---|---|
| `number` | 点到线段的最短距离 |

### `GetPointDistanceToLine`

```text
GetPointDistanceToLine(Point: FVector, LineOrigin: FVector, LineDirection: FVector) -> number
```

计算点到无限长直线的最短距离

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Point` | `FVector` | 需要计算距离的目标 |
| `LineOrigin` | `FVector` | 直线上的参考点 |
| `LineDirection` | `FVector` | 直线上的方向向量(无需归一化) |

**Returns**

| Type | Description |
|---|---|
| `number` | 点到直线上的最短距离 |

### `ProjectVectorOnToPlane`

```text
ProjectVectorOnToPlane(V: FVector, PlaneNormal: FVector) -> FVector
```

将向量投影到由法向量定义的平面上

**Parameters**

| Name | Type | Description |
|---|---|---|
| `V` | `FVector` | 需要投影的向量 |
| `PlaneNormal` | `FVector` | 法向量 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 投影后的向量 |

### `NegateVector`

```text
NegateVector(V: FVector) -> FVector
```

向量取反

**Parameters**

| Name | Type | Description |
|---|---|---|
| `V` | `FVector` | 需要取反的向量 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 取反后的向量 |

### `ClampVectorSize`

```text
ClampVectorSize(V: FVector, Min: number, Max: number) -> FVector
```

将向量长度限制在最小值和最大值之间

**Parameters**

| Name | Type | Description |
|---|---|---|
| `V` | `FVector` | 需要限制长度的向量 |
| `Min` | `number` | 最小长度 |
| `Max` | `number` | 最大长度 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 限制长度后的向量 |

### `GetMinElement`

```text
GetMinElement(V: FVector) -> number
```

找出向量中(X, Y或Z)的最小分量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `V` | `FVector` | 需要计算最小分量的向量 |

**Returns**

| Type | Description |
|---|---|
| `number` | 最小分量 |

### `GetMaxElement`

```text
GetMaxElement(V: FVector) -> number
```

找出向量中(X, Y或Z)的最大分量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `V` | `FVector` | 需要计算最大分量的向量 |

**Returns**

| Type | Description |
|---|---|
| `number` | 最大分量 |

### `GetDirectionUnitVector`

```text
GetDirectionUnitVector(From: FVector, To: FVector) -> FVector
```

计算从一个位置指向另一个位置的单位方向向量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `From` | `FVector` | 起点 |
| `To` | `FVector` | 终点 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 单位方向向量 |

### `EqualName`

```text
EqualName(A: string, B: string) -> boolean
```

如果A和B相等则返回true (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `string` | A |
| `B` | `string` | B |

**Returns**

| Type | Description |
|---|---|
| `boolean` | true or false |

### `NotEqualName`

```text
NotEqualName(A: string, B: string) -> boolean
```

如果A和B不相等则返回true (A ~= B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `string` | A |
| `B` | `string` | B |

**Returns**

| Type | Description |
|---|---|
| `boolean` | true or false |

### `MakeBox`

```text
MakeBox(Min: FVector, Max: FVector) -> FBox
```

通过最小点和最大点创建一个FBox，并将IsValid设为true

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Min` | `FVector` | 最小点 |
| `Max` | `FVector` | 最大点 |

**Returns**

| Type | Description |
|---|---|
| `FBox` | FBox |

### `MakeBox2D`

```text
MakeBox2D(Min: FVector2D, Max: FVector2D) -> FBox2D
```

通过最小点和最大点创建一个FBox2D，并将IsValid设为true

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Min` | `FVector2D` | 最小点 |
| `Max` | `FVector2D` | 最大点 |

**Returns**

| Type | Description |
|---|---|
| `FBox2D` | FBox2D |

### `MakeVector`

```text
MakeVector(X: number, Y: number, Z: number) -> FVector
```

创建一个向量 {X, Y, Z}

**Parameters**

| Name | Type | Description |
|---|---|---|
| `X` | `number` | X |
| `Y` | `number` | Y |
| `Z` | `number` | Z |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 向量 |

### `BreakVector`

```text
BreakVector(V: FVector) -> number,number,number
```

将向量分解为X、Y和Z分量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `V` | `FVector` | 向量 |

**Returns**

| Type | Description |
|---|---|
| `number,number,number` | X,Y,Z |

### `MakeVector2D`

```text
MakeVector2D(X: number, Y: number) -> FVector2D
```

创建一个二维向量 {X, Y}

**Parameters**

| Name | Type | Description |
|---|---|---|
| `X` | `number` | X |
| `Y` | `number` | Y |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | 向量 |

### `BreakVector2D`

```text
BreakVector2D(V: FVector2D) -> number,number
```

将二维向量分解为X和Y分量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `V` | `FVector2D` | 向量 |

**Returns**

| Type | Description |
|---|---|
| `number,number` | X,Y |

### `GetForwardVector`

```text
GetForwardVector(InRot: FRotator) -> FVector
```

按给定旋转角度旋转世界前向向量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRot` | `FRotator` | 旋转角度 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 矩阵 |

### `GetRightVector`

```text
GetRightVector(InRot: FRotator) -> FVector
```

按给定旋转角度旋转世界右向量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRot` | `FRotator` | 旋转角度 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 矩阵 |

### `GetUpVector`

```text
GetUpVector(InRot: FRotator) -> FVector
```

按给定旋转角度旋转世界上向量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRot` | `FRotator` | 旋转角度 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 矩阵 |

### `GetYawPitchFromVector`

```text
GetYawPitchFromVector(V: FVector) -> number,number
```

将向量分解为Yaw(偏航角)和Pitch(俯仰角)旋转值(角度制，不限制范围)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `V` | `FVector` | 向量 |

**Returns**

| Type | Description |
|---|---|
| `number,number` | Yaw,Pitch |

### `MakeRotator`

```text
MakeRotator(Roll: number, Pitch: number, Yaw: number) -> FRotator
```

使用以度数为单位提供的旋转值创建旋转器{Roll, Pitch, Yaw}

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Roll` | `number` | Roll |
| `Pitch` | `number` | Pitch |
| `Yaw` | `number` | Yaw |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 矩阵 |

### `FindLookAtRotation`

```text
FindLookAtRotation(Start: FVector, Target: FVector) -> FRotator
```

查找一个物体在起始位置指向目标位置所需的旋转角度

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Start` | `FVector` | 起始位置 |
| `Target` | `FVector` | 目标位置 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 矩阵 |

### `MakeRotFromX`

```text
MakeRotFromX(XAxis: FVector) -> FRotator
```

仅使用X轴构建Rotator。Y和Z轴未指定但将保持正交归一。X轴无需归一化

**Parameters**

| Name | Type | Description |
|---|---|---|
| `XAxis` | `FVector` | X轴 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 矩阵 |

### `MakeRotFromY`

```text
MakeRotFromY(YAxis: FVector) -> FRotator
```

仅使用Y轴构建Rotator。X和Z轴未指定但将保持正交归一。Y轴无需归一化

**Parameters**

| Name | Type | Description |
|---|---|---|
| `YAxis` | `FVector` | Y轴 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 矩阵 |

### `MakeRotFromZ`

```text
MakeRotFromZ(ZAxis: FVector) -> FRotator
```

仅使用Z轴构建Rotator。X和Y轴未指定但将保持正交归一。Z轴无需归一化

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ZAxis` | `FVector` | Z轴 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 矩阵 |

### `MakeRotFromXY`

```text
MakeRotFromXY(XAxis: FVector, YAxis: FVector) -> FRotator
```

使用给定的X和Y轴构建矩阵。X轴保持不变，Y轴会微调以确保正交性。Z轴将被计算得出。输入向量无需归一化

**Parameters**

| Name | Type | Description |
|---|---|---|
| `XAxis` | `FVector` | X轴 |
| `YAxis` | `FVector` | Y轴 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 矩阵 |

### `MakeRotFromXZ`

```text
MakeRotFromXZ(XAxis: FVector, ZAxis: FVector) -> FRotator
```

使用给定的X和Z轴构建矩阵。X轴保持不变，Z轴会微调以确保正交性。Y轴将被计算得出。输入向量无需归一化

**Parameters**

| Name | Type | Description |
|---|---|---|
| `XAxis` | `FVector` | X轴 |
| `ZAxis` | `FVector` | Z轴 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 矩阵 |

### `MakeRotFromYX`

```text
MakeRotFromYX(YAxis: FVector, XAxis: FVector) -> FRotator
```

使用给定的Y和X轴构建矩阵。Y轴保持不变，X轴会微调以确保正交性。Z轴将被计算得出。输入向量无需归一化

**Parameters**

| Name | Type | Description |
|---|---|---|
| `YAxis` | `FVector` | Y轴 |
| `XAxis` | `FVector` | X轴 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 矩阵 |

### `MakeRotFromYZ`

```text
MakeRotFromYZ(YAxis: FVector, ZAxis: FVector) -> FRotator
```

使用给定的Y和Z轴构建矩阵。Y轴保持不变，Z轴会微调以确保正交性。X轴将被计算得出。输入向量无需归一化

**Parameters**

| Name | Type | Description |
|---|---|---|
| `YAxis` | `FVector` | Y轴 |
| `ZAxis` | `FVector` | Z轴 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 矩阵 |

### `MakeRotFromZX`

```text
MakeRotFromZX(ZAxis: FVector, XAxis: FVector) -> FRotator
```

使用给定的Z和X轴构建矩阵。Z轴保持不变，X轴会微调以确保正交性。Y轴将被计算得出。输入向量无需归一化

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ZAxis` | `FVector` | Z轴 |
| `XAxis` | `FVector` | X轴 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 矩阵 |

### `MakeRotFromZY`

```text
MakeRotFromZY(ZAxis: FVector, YAxis: FVector) -> FRotator
```

使用给定的Z和Y轴构建矩阵。Z轴保持不变，Y轴会微调以确保正交性。X轴将被计算得出。输入向量无需归一化

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ZAxis` | `FVector` | Z轴 |
| `YAxis` | `FVector` | Y轴 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 矩阵 |

### `BreakRotator`

```text
BreakRotator(Rotator: FRotator) -> number,number,number
```

将Rotator分解为{Roll, Pitch, Yaw}角度值(单位:度)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rotator` | `FRotator` | Rotator |

**Returns**

| Type | Description |
|---|---|
| `number,number,number` | Roll,Pitch,Yaw |

### `MakeTransform`

```text
MakeTransform(Location: FVector, Rotation: FRotator, Scale: FVector) -> FTransform
```

根据位置、旋转和缩放创建Transform

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Location` | `FVector` | 位置 |
| `Rotation` | `FRotator` | 旋转 |
| `Scale` | `FVector` | 缩放 |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | transformFVecto |

### `BreakTransform`

```text
BreakTransform(Transform: FTransform) -> FVector,FRotator,FVector
```

将transform分解为{Location, Rotation, Scale}值

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Transform` | `FTransform` | Transform |

**Returns**

| Type | Description |
|---|---|
| `FVector,FRotator,FVector` | Location,Rotation,Scale |

### `Conv_VectorToLinearColor`

```text
Conv_VectorToLinearColor(Vector: FVector) -> FLinearColor
```

将向量转换为LinearColor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vector` | `FVector` | 向量 |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | LinearColor |

### `Conv_ColorToLinearColor`

```text
Conv_ColorToLinearColor(Color: FColor) -> FLinearColor
```

将Color转换为LinearColor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Color` | `FColor` | Color |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | LinearColor |

### `Conv_LinearColorToColor`

```text
Conv_LinearColorToColor(LinearColor: FLinearColor) -> FColor
```

将LinearColor转换为Color

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LinearColor` | `FLinearColor` | LinearColor |

**Returns**

| Type | Description |
|---|---|
| `FColor` | Color |

### `Conv_VectorToVector2D`

```text
Conv_VectorToVector2D(Vector: FVector) -> FVector2D
```

将向量转换为二维向量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vector` | `FVector` | 向量 |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | 二维向量 |

### `Conv_Vector2DToVector`

```text
Conv_Vector2DToVector(Vector2D: FVector2D) -> FVector
```

将二维向量转换为向量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vector2D` | `FVector2D` | 二维向量 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 向量 |

### `HSVToRGB`

```text
HSVToRGB(H: number, S: number, V: number, A: number) -> FLinearColor
```

根据HSV分量创建颜色

**Parameters**

| Name | Type | Description |
|---|---|---|
| `H` | `number` | 色相 |
| `S` | `number` | 饱和度 |
| `V` | `number` | 明度 |
| `A` | `number` | 透明度 |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | Color |

### `RGBToHSV`

```text
RGBToHSV(Color: FLinearColor) -> number,number,number,number
```

将颜色分解为单独的HSV分量（以及透明度）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Color` | `FLinearColor` | Color |

**Returns**

| Type | Description |
|---|---|
| `number,number,number,number` | H,S,V,A |

### `Conv_HSVToRGB`

```text
Conv_HSVToRGB(HSV: FLinearColor) -> FLinearColor
```

将HSV线性颜色转换为RGB颜色（其中H在R分量，S在G分量，V在B分量）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HSV` | `FLinearColor` | HSV |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | RGB |

### `Conv_RGBToHSV`

```text
Conv_RGBToHSV(RGB: FLinearColor) -> FLinearColor
```

将RGB线性颜色转换为HSV（其中H存储在R分量，S存储在G分量，V存储在B分量）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RGB` | `FLinearColor` | RGB |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | HSV |

### `HexToRGB`

```text
HexToRGB(HexString: string, bSRGB: boolean) -> FLinearColor
```

将十六进制颜色字符串转换为RGB

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HexString` | `string` | 十六进制颜色字符串 |
| `bSRGB` | `boolean` | 是否使用sRGB颜色空间 |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | RGB |

### `RGBToHex`

```text
RGBToHex(RGB: FLinearColor, bSRGB: boolean) -> string
```

将RGB颜色转换为十六进制字符串

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RGB` | `FLinearColor` | RGB |
| `bSRGB` | `boolean` | 是否使用sRGB颜色空间 |

**Returns**

| Type | Description |
|---|---|
| `string` | 十六进制颜色字符串 |

### `Conv_VectorToRotator`

```text
Conv_VectorToRotator(XAxis: FVector) -> FRotator
```

创建一个使X轴朝向指定方向向量的Rotator

**Parameters**

| Name | Type | Description |
|---|---|---|
| `XAxis` | `FVector` | X轴 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | Rotator |

### `Conv_RotatorToVector`

```text
Conv_RotatorToVector(Rotator: FRotator) -> FVector
```

获取旋转后的X轴方向向量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rotator` | `FRotator` | Rotator |

**Returns**

| Type | Description |
|---|---|
| `FVector` | X轴 |

### `TransformLocation`

```text
TransformLocation(T: FTransform, Location: FVector) -> FVector
```

使用指定的变换矩阵转换位置坐标
例如：若T是某物体的变换矩阵，此操作会将局部坐标系的位置转换到世界坐标系

**Parameters**

| Name | Type | Description |
|---|---|---|
| `T` | `FTransform` | 变换矩阵 |
| `Location` | `FVector` | 局部坐标系下的位置 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 世界坐标系下的位置 |

### `TransformDirection`

```text
TransformDirection(T: FTransform, Direction: FVector) -> FVector
```

使用指定的变换矩阵转换方向向量 - 不会改变向量长度
例如：若T是某物体的变换矩阵，此操作会将局部坐标系的方向向量转换到世界坐标系

**Parameters**

| Name | Type | Description |
|---|---|---|
| `T` | `FTransform` | 变换矩阵 |
| `Direction` | `FVector` | 局部坐标系下的方向向量 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 世界坐标系下的方向向量 |

### `TransformRotation`

```text
TransformRotation(T: FTransform, Rotation: FRotator) -> FRotator
```

使用指定的变换矩阵转换Rotator
例如：若T是某物体的变换矩阵，此操作会将局部坐标系的旋转转换到世界坐标系

**Parameters**

| Name | Type | Description |
|---|---|---|
| `T` | `FTransform` | 变换矩阵 |
| `Rotation` | `FRotator` | 局部坐标系下的旋转 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 世界坐标系下的旋转 |

### `RandomBool`

```text
RandomBool() -> boolean
```

随机返回 true 或 false，概率各占 50%

**Returns**

| Type | Description |
|---|---|
| `boolean` | true或false |

### `RandomBoolWithWeight`

```text
RandomBoolWithWeight(Weight: number) -> boolean
```

根据指定权重获取随机概率结果。权重范围为 0.0 - 1.0
例如：权重 = 0.6，返回值将有 60% 的概率为 True

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Weight` | `number` | 权重 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | true或false |

### `RandomInteger`

```text
RandomInteger(Max: number) -> number
```

返回一个随机数，范围在0到Max - 1之间，每个数出现的概率相同

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Max` | `number` | 最大值 |

**Returns**

| Type | Description |
|---|---|
| `number` | 随机数 |

### `Clamp`

```text
Clamp(Value: number, Min: number, Max: number) -> number
```

返回限制在A和B之间的值(包含A和B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `number` | 值 |
| `Min` | `number` | 最小值 |
| `Max` | `number` | 最大值 |

**Returns**

| Type | Description |
|---|---|
| `number` | 限制后的值 |

### `RandomIntegerInRange`

```text
RandomIntegerInRange(Min: number, Max: number) -> number
```

返回Min和Max之间的随机整数(包含Min和Max)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Min` | `number` | 最小值 |
| `Max` | `number` | 最大值 |

**Returns**

| Type | Description |
|---|---|
| `number` | 随机整数 |

### `IsPointInBox`

```text
IsPointInBox(Point: FVector, BoxOrigin: FVector, BoxExtent: FVector) -> boolean
```

判断给定点是否在盒子内（包括在盒子边界上的点）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Point` | `FVector` | 要测试的点 |
| `BoxOrigin` | `FVector` | 盒子的原点 |
| `BoxExtent` | `FVector` | 盒子在各个轴上的范围（从原点出发的距离） |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 如果点在盒子内则返回true；否则返回false |

### `IsPointInBoxWithTransform`

```text
IsPointInBoxWithTransform(Point: FVector, BoxWorldTransform: FTransform, BoxExtent: FVector) -> boolean
```

判断给定点是否在具有特定变换的盒子内（包含边界点)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Point` | `FVector` | 要测试的点 |
| `BoxWorldTransform` | `FTransform` | 盒子从组件空间到世界空间的变换 |
| `BoxExtent` | `FVector` | 盒子在组件空间中的范围（各轴距原点的距离） |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 如果点在盒子内则返回true；否则返回false |

### `EqualRotator`

```text
EqualRotator(A: FRotator, B: FRotator, ErrorTolerance: number) -> boolean
```

检查Rotator A 和 B 是否在指定误差范围内相等 (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FRotator` | 旋转量A |
| `B` | `FRotator` | 旋转量B |
| `ErrorTolerance` | `number` | 误差范围 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 如果旋转量A和B在误差范围内相等则返回true；否则返回false |

### `NotEqualRotator`

```text
NotEqualRotator(A: FRotator, B: FRotator, ErrorTolerance: number) -> boolean
```

检查Rotator A 和 B 是否在指定误差范围内不相等 (A != B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FRotator` | 旋转量A |
| `B` | `FRotator` | 旋转量B |
| `ErrorTolerance` | `number` | 误差范围 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 如果旋转量A和B在误差范围内不相等则返回true；否则返回false |

### `ComposeRotators`

```text
ComposeRotators(A: FRotator, B: FRotator) -> FRotator
```

组合两个旋转，返回先应用A再应用B的结果旋转

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FRotator` | 旋转量A |
| `B` | `FRotator` | 旋转量B |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 先应用A再应用B的结果旋转 |

### `GetAxes`

```text
GetAxes(Rotator: FRotator) -> FVector,FVector,FVector
```

获取该旋转对应的前向、右向和上向三个基准方向向量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rotator` | `FRotator` | 旋转量 |

**Returns**

| Type | Description |
|---|---|
| `FVector,FVector,FVector` | 前向向量,右向向量,上向向量 |

### `NormalRotator`

```text
NormalRotator(A: FRotator) -> FRotator
```

标准化Rotator

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FRotator` | 旋转量 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 标准化后的旋转量 |

### `RandomRotator`

```text
RandomRotator(bRoll: boolean) -> FRotator
```

生成一个随机旋转角度，可选择是否包含绕Z轴的随机旋转

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bRoll` | `boolean` | 是否包含绕Z轴的随机旋转 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 随机旋转量 |

### `RLerp`

```text
RLerp(A: FRotator, B: FRotator, Alpha: number, bShortestPath: boolean) -> FRotator
```

基于Alpha值在A和B之间线性插值（Alpha=0时返回100%A，Alpha=1时返回100%B）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FRotator` | 起始旋转量 |
| `B` | `FRotator` | 目标旋转量 |
| `Alpha` | `number` | 插值比例（0-1） |
| `bShortestPath` | `boolean` | 是否采用最短路径插值 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 线性插值后的值 |

## Language

`lua`
