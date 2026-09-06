---
id: "api:class:UGCWidgetUtility"
title: "UGCWidgetUtility"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGCWidgetUtility.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCWidgetUtility

UI控件工具接口库

## Functions

### `CreateWidgetAsync`

```text
CreateWidgetAsync(WidgetClassPath: string|FSoftObjectPath, OnCreatedCallback: fun(Widget:UUserWidget))
```

异步创建一个控件，返回控件实例

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetClassPath` | `string\|FSoftObjectPath` | 控件类路径 |
| `OnCreatedCallback` | `fun(Widget:UUserWidget)` | 创建完成回调 |

### `CreateWidget`

```text
CreateWidget(WidgetClass: UClass) -> UUserWidget
```

创建一个控件，返回控件实例

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetClass` | `UClass` | 控件蓝图类 |

**Returns**

| Type | Description |
|---|---|
| `UUserWidget` | 控件实例 |

### `DestroyWidget`

```text
DestroyWidget(Widget: UUserWidget)
```

销毁一个控件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |

### `SetWidgetLayout`

```text
SetWidgetLayout(LayoutPath: string)
```

异步加载并设置当前的 WidgetLayout，同时只能设置一个，旧的 WidgetLayout 会被卸载。传入 “Default” 可卸载 WidgetLayout 回到默认状态。（主要用于可视化屏蔽玩法中不需要的和平 UI，UI 会强制隐藏）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LayoutPath` | `string` | WidgetLayout 引用路径 |

### `GetUserWidgetByWidgetLayout`

```text
GetUserWidgetByWidgetLayout(WidgetLayoutPath: string, UserWidgetName: string) -> UserWidget
```

获取通过WidgetLayout加载的自定义UserWidget
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetLayoutPath` | `string` | 控件 ClassPath, 控件需继承自 UUserWidgetLayout |
| `UserWidgetName` | `string` | 控件 Name |

**Returns**

| Type | Description |
|---|---|
| `UserWidget` | - |

### `AddToSlot`

```text
AddToSlot(Widget: UUserWidget, SlotName: string, ZOrder: number, AnchorData: FAnchorData)
```

添加一个控件到指定 UI 挂点槽位

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |
| `SlotName` | `string` | 控件槽位名称，默认为 UI.UISlot.MainUISlot_Low |
| `ZOrder` | `number` | 控件层级，默认为 0 |
| `AnchorData` | `FAnchorData` | 控件锚点，默认为 { Anchors = { Minimum = Vector2D.New(0, 0), Maximum = Vector2D.New(1, 1) } } |

### `RemoveFromSlot`

```text
RemoveFromSlot(Widget: UUserWidget)
```

从 UI 挂点槽位移除控件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |

### `IsWidgetAddedToSlot`

```text
IsWidgetAddedToSlot(Widget: UUserWidget) -> boolean
```

判断一个控件是否已经挂载在 UI 挂点上

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否已经挂载 |

### `ShowWidget`

```text
ShowWidget(Widget: UUserWidget)
```

显示一个控件，需要控件已经挂载到挂点槽上

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |

### `HideWidget`

```text
HideWidget(Widget: UUserWidget)
```

隐藏一个控件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |

### `SetWidgetVisible`

```text
SetWidgetVisible(Widget: UUserWidget, bVisible: boolean)
```

设置控件的显示或隐藏状态
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |
| `bVisible` | `boolean` | 是否可见 |

### `IsWidgetVisible`

```text
IsWidgetVisible(Widget: UUserWidget) -> boolean
```

判断一个控件是否可见

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否可见 |

### `GetSubWidget`

```text
GetSubWidget(Widget: UUserWidget, SubWidgetName: string) -> UWidget
```

获取子控件，可用于获取 UMG 蓝图里的子控件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |
| `SubWidgetName` | `string` | 子控件名称 |

**Returns**

| Type | Description |
|---|---|
| `UWidget` | 子控件实例 |

### `GetAllWidgetsOfClass`

```text
GetAllWidgetsOfClass(WidgetClass: UClass, bAddedToSlotOnly: boolean) -> UUserWidget[]
```

获取指定类别的所有控件，可筛选只获取已被添加到挂点的控件
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetClass` | `UClass` | 控件类（UUserWidget） |
| `bAddedToSlotOnly` | `boolean` | 是否只获取已添加到挂点的控件 |

**Returns**

| Type | Description |
|---|---|
| `UUserWidget[]` | 控件实例列表 |

### `AddChildToTochButton`

```text
AddChildToTochButton(Widget: UserWidget)
```

把自定义 UI 挂到和平 UI 上并应用自定义布局
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UserWidget` | - |

### `ProjectWorldLocationToWidgetPosition`

```text
ProjectWorldLocationToWidgetPosition(WorldLocation: FVector) -> FVector2D
```

将世界坐标转换为控件坐标
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldLocation` | `FVector` | 世界坐标 |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | 控件坐标 |

### `SlotAsCanvasSlot`

```text
SlotAsCanvasSlot(Widget: UUserWidget) -> UCanvasPanelSlot
```

获取 Canvas 插槽
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |

**Returns**

| Type | Description |
|---|---|
| `UCanvasPanelSlot` | Canvas 插槽实例 |

### `SlotAsOverlaySlot`

```text
SlotAsOverlaySlot(Widget: UUserWidget) -> @Overlay
```

获取 Overlay 插槽
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |

**Returns**

| Type | Description |
|---|---|
| `@Overlay` | 插槽实例 |

### `SlotAsVerticalBoxSlot`

```text
SlotAsVerticalBoxSlot(Widget: UUserWidget) -> @HorizontalBox
```

获取 HorizontalBox 插槽
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |

**Returns**

| Type | Description |
|---|---|
| `@HorizontalBox` | 插槽实例 |

### `GetViewportScale`

```text
GetViewportScale() -> number
```

获取视口缩放比例
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `number` | 缩放比例 |

### `GetViewportSize`

```text
GetViewportSize() -> FVector2D
```

获取视口尺寸
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | 视口尺寸 |

### `GetViewportWidgetGeometry`

```text
GetViewportWidgetGeometry() -> FGeometry
```

获取视口 Widget 几何信息
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `FGeometry` | 几何信息 |

### `GetWidgetGeometry`

```text
GetWidgetGeometry(Widget: UUserWidget) -> FGeometry
```

获取控件的几何信息（可用于坐标转换等）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |

**Returns**

| Type | Description |
|---|---|
| `FGeometry` | 几何信息 |

### `AbsoluteToLocal`

```text
AbsoluteToLocal(Geometry: FGeometry, AbsoluteCoordinate: FVector2D) -> FVector2D
```

绝对坐标转本地坐标
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Geometry` | `FGeometry` | 控件几何信息 |
| `AbsoluteCoordinate` | `FVector2D` | 绝对坐标 |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | 本地坐标 |

### `LocalToAbsolute`

```text
LocalToAbsolute(Geometry: FGeometry, LocalCoordinate: FVector2D) -> FVector2D
```

本地坐标转绝对坐标
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Geometry` | `FGeometry` | 控件几何信息 |
| `LocalCoordinate` | `FVector2D` | 本地坐标 |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | 绝对坐标 |

### `GetLocalSize`

```text
GetLocalSize(Geometry: FGeometry) -> FVector2D
```

获取控件的本地尺寸
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Geometry` | `FGeometry` | 控件几何信息 |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | 本地尺寸 |

### `GetAbsoluteSize`

```text
GetAbsoluteSize(Geometry: FGeometry) -> FVector2D
```

获取控件的绝对尺寸
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Geometry` | `FGeometry` | 控件几何信息 |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | 绝对尺寸 |

### `GetAbsolutePosition`

```text
GetAbsolutePosition(Geometry: FGeometry) -> FVector2D
```

获取控件的绝对位置
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Geometry` | `FGeometry` | 控件几何信息 |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | 绝对位置 |

### `SetWidgetOpacity`

```text
SetWidgetOpacity(Widget: UUserWidget, Opacity: number)
```

设置控件的不透明度
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |
| `Opacity` | `number` | 不透明度(0全透明~1不透明) |

### `GetWidgetOpacity`

```text
GetWidgetOpacity(Widget: UUserWidget) -> number
```

获取控件当前不透明度
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |

**Returns**

| Type | Description |
|---|---|
| `number` | 不透明度值 |

### `SetWidgetColor`

```text
SetWidgetColor(Widget: UUserWidget, HexString: string)
```

设置控件的颜色和透明度（颜色与不透明度组合设置）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |
| `HexString` | `string` | 设置字符串色值sRGB（含Alpha通道控制透明度），例：FB5AF9FF |

### `AddChildWidget`

```text
AddChildWidget(ParentWidget: UPanelWidget, ChildWidget: UUserWidget)
```

添加子控件到指定Panel父控件上（非Panel控件无效）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParentWidget` | `UPanelWidget` | Panel父控件 |
| `ChildWidget` | `UUserWidget` | 要添加的子控件 |

### `RemoveChildWidget`

```text
RemoveChildWidget(ParentWidget: UPanelWidget, ChildWidget: UUserWidget)
```

从Panel父控件移除指定子控件（非Panel控件无效）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParentWidget` | `UPanelWidget` | Panel父控件 |
| `ChildWidget` | `UUserWidget` | 需要移除的子控件 |

### `RemoveAllChildWidgets`

```text
RemoveAllChildWidgets(ParentWidget: UPanelWidget)
```

清空Panel父控件下所有子控件（非Panel控件无效）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParentWidget` | `UPanelWidget` | Panel父控件 |

### `SetWidgetSlotPosition`

```text
SetWidgetSlotPosition(Widget: UUserWidget, Position: FVector2D)
```

设置控件在slot上的位置（相对于父控件）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |
| `Position` | `FVector2D` | slot坐标位置 |

### `GetWidgetSlotPosition`

```text
GetWidgetSlotPosition(Widget: UUserWidget) -> FVector2D
```

获取控件当前slot位置（相对于父控件）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | slot位置 |

### `SetWidgetSlotSize`

```text
SetWidgetSlotSize(Widget: UUserWidget, Size: Vector2D)
```

设置控件的slot尺寸
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |
| `Size` | `Vector2D` | 尺寸（宽度，高度） |

### `GetWidgetSlotSize`

```text
GetWidgetSlotSize(Widget: UUserWidget) -> Vector2D
```

获取控件slot尺寸
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | - |

**Returns**

| Type | Description |
|---|---|
| `Vector2D` | 尺寸 |

### `SetActiveWidgetIndex`

```text
SetActiveWidgetIndex(Container: UUserWidget, Index: integer)
```

设置容器控件（如 WidgetSwitcher）当前显示的页面索引
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Container` | `UUserWidget` | 容器控件（需为WidgetSwitcher或类似） |
| `Index` | `integer` | 页面索引（从1开始） |

### `GetActiveWidgetIndex`

```text
GetActiveWidgetIndex(Container: UUserWidget) -> integer
```

获取容器当前显示的页面索引（从1开始）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Container` | `UUserWidget` | - |

**Returns**

| Type | Description |
|---|---|
| `integer` | 当前显示的页面索引，失败或无效时返回 -1 |

### `GetActiveWidget`

```text
GetActiveWidget() -> UUserWidget
```

获取容器当前显示的页面控件
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `UUserWidget` | 当前的页面控件实例 |

### `SetWidgetEnabled`

```text
SetWidgetEnabled(Widget: UUserWidget, bEnabled: boolean)
```

设置控件是否可交互（启用/禁用输入）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |
| `bEnabled` | `boolean` | 是否启用 |

### `SetCheckBoxChecked`

```text
SetCheckBoxChecked(bChecked: boolean)
```

设置复选框的勾选状态
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bChecked` | `boolean` | 是否勾选 |

### `IsCheckBoxChecked`

```text
IsCheckBoxChecked(CheckBoxWidget: UUserWidget) -> boolean
```

查询复选框是否勾选
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CheckBoxWidget` | `UUserWidget` | 复选框控件 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否勾选 |

### `SetComboBoxSelectedOption`

```text
SetComboBoxSelectedOption(ComboBoxWidget: UUserWidget, Option: string)
```

设置下拉菜单当前选中的选项
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ComboBoxWidget` | `UUserWidget` | 下拉菜单控件实例 |
| `Option` | `string` | 选项文本 |

### `GetComboBoxSelectedOption`

```text
GetComboBoxSelectedOption(ComboBoxWidget: UUserWidget) -> string
```

获取下拉菜单当前选中的选项文本
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ComboBoxWidget` | `UUserWidget` | 下拉菜单控件实例 |

**Returns**

| Type | Description |
|---|---|
| `string` | 选项文本，若获取失败返回空字符串 |

### `GetComboBoxOptionAtIndex`

```text
GetComboBoxOptionAtIndex(ComboBoxWidget: UUserWidget, Index: integer) -> string
```

获取下拉菜单指定索引的选项文本
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ComboBoxWidget` | `UUserWidget` | 下拉菜单控件实例 |
| `Index` | `integer` | 选项索引 |

**Returns**

| Type | Description |
|---|---|
| `string` | 选项文本 |

### `SetWidgetProgress`

```text
SetWidgetProgress(ProgressWidget: UUserWidget, Percent: number) -> nil
```

设置进度条控件的当前进度值
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ProgressWidget` | `UUserWidget` | - |
| `Percent` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `nil` | - |

### `SetImageTexture`

```text
SetImageTexture(Image: UImage, TexturePath: string)
```

设置Image控件的图像/纹理（通过资源路径）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Image` | `UImage` | 图像控件 |
| `TexturePath` | `string` | 纹理资源引用路径 |

### `ScrollBoxToEnd`

```text
ScrollBoxToEnd()
```

滚动容器内容到底部
生效范围：客户端

### `SetWidgetText`

```text
SetWidgetText(Widget: UWidget, Text: string)
```

设置控件（文本控件）的显示文本
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget` | 控件实例 |
| `Text` | `string` | 文本内容 |

### `GetWidgetText`

```text
GetWidgetText(Widget: UWidget) -> string
```

获取控件（文本控件）的显示文本
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget` | 文本控件 |

**Returns**

| Type | Description |
|---|---|
| `string` | 文本内容 |

## Language

`lua`
