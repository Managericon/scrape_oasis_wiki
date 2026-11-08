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
| `FGeometry` | 几何信息；Widget 无效或未上屏（无缓存几何）时返回 nil |

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

获取控件的本地尺寸（Slate 单位，未乘 DPI 与渲染变换）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Geometry` | `FGeometry` | 控件几何信息 |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | 本地尺寸（局部空间） |

### `GetAbsoluteSize`

```text
GetAbsoluteSize(Geometry: FGeometry) -> FVector2D
```

获取控件的渲染空间尺寸（含渲染变换；布局占位尺寸请用槽位尺寸接口）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Geometry` | `FGeometry` | 控件几何信息 |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | 绝对尺寸（渲染空间，含渲染缩放；旋转或剪切时不是轴对齐包围盒） |

### `GetAbsolutePosition`

```text
GetAbsolutePosition(Geometry: FGeometry) -> FVector2D
```

获取控件的绝对位置（渲染空间，含渲染变换）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Geometry` | `FGeometry` | 控件几何信息 |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | 绝对位置（渲染空间；默认 pivot 在中心，缩放会使左上角位置变化） |

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

设置控件的 slot 尺寸（仅 CanvasPanel 槽位；非 CanvasPanel 槽位调用仅记录日志并返回）
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

获取控件的 slot 尺寸（仅 CanvasPanel 槽位）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | - |

**Returns**

| Type | Description |
|---|---|
| `Vector2D` | 尺寸；Widget 无效或不在 CanvasPanel 槽位时返回 (0, 0) |

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

### `AddToViewport`

```text
AddToViewport(Widget: UUserWidget, ZOrder: number)
```

把用户控件添加到视口显示（可指定显示层级）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 已创建的用户控件；须没有父容器（仍在槽位中的控件请先 RemoveFromSlot） |
| `ZOrder` | `number` | 显示层级，数值越大越靠上；不传默认 0；挂载后无法再改，需移除后重新挂载 |

### `RemoveFromViewport`

```text
RemoveFromViewport(Widget: UUserWidget)
```

从视口移除用户控件（对槽位挂载的控件同样有效）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 目标用户控件；视口挂载与槽位挂载的控件都可移除 |

### `SetWidgetPositionInViewport`

```text
SetWidgetPositionInViewport(Widget: UUserWidget, Position: Vector2D, bRemoveDPIScale: boolean)
```

设置用户控件在视口中的位置（仅对视口挂载的控件生效）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 已挂载到视口的用户控件 |
| `Position` | `Vector2D` | 视口位置（相对视口左上角）；调用后定位锚点重置为左上角 |
| `bRemoveDPIScale` | `boolean` | 是否由接口自动移除 DPI 缩放；true（默认）时按视口 DPI 对坐标做逆缩放 |

### `FindComboBoxOptionIndex`

```text
FindComboBoxOptionIndex(ComboBoxWidget: UComboBoxString, Option: string) -> number
```

查找下拉菜单中指定选项的索引（对外 1 基）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ComboBoxWidget` | `UComboBoxString` | 下拉菜单控件 |
| `Option` | `string` | 选项文本；空字符串也是合法选项（引擎按字符串相等匹配） |

**Returns**

| Type | Description |
|---|---|
| `number` | 从 1 开始的选项索引；未找到返回 0 |

### `GetScrollBoxOffset`

```text
GetScrollBoxOffset(ScrollBox: UScrollBox) -> number
```

获取滚动框当前偏移
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ScrollBox` | `UScrollBox` | 滚动框 |

**Returns**

| Type | Description |
|---|---|
| `number` | 滚动偏移，单位为 Slate Unit；ScrollBox 无效时返回 0 |

### `SetScrollBoxOffset`

```text
SetScrollBoxOffset(ScrollBox: UScrollBox, Offset: number)
```

设置滚动框滚动到指定偏移
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ScrollBox` | `UScrollBox` | 滚动框 |
| `Offset` | `number` | 滚动偏移，单位为 Slate Unit |

### `ScrollBoxToStart`

```text
ScrollBoxToStart(ScrollBox: UScrollBox)
```

滚动框内容到顶部（立即生效）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ScrollBox` | `UScrollBox` | 滚动框 |

### `GetSizeBoxSize`

```text
GetSizeBoxSize(SizeBox: USizeBox) -> table|nil
```

获取尺寸约束容器的固定尺寸
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SizeBox` | `USizeBox` | 尺寸约束容器 |

**Returns**

| Type | Description |
|---|---|
| `table\|nil` | 固定尺寸表 {X=宽, Y=高}；仅某一轴固定时该轴为数值、另一轴为 nil；宽高均未固定时整体返回 nil（与设置接口的取消语义对称） |

### `SetSizeBoxSize`

```text
SetSizeBoxSize(SizeBox: USizeBox, Size: Vector2D|table|nil)
```

设置尺寸约束容器的固定尺寸（改布局占位）：固定后尺寸不随内容变化
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SizeBox` | `USizeBox` | 尺寸约束容器 |
| `Size` | `Vector2D\|table\|nil` | 固定尺寸；传 {X=宽, Y=高} 表时某一轴为 nil（或不传该键）则单独取消该轴固定，也可传 Vector2D（两轴一体生效）；整体传 nil 取消全部固定 |

### `GetTextBoxHintText`

```text
GetTextBoxHintText(TextBox: UEditableTextBox) -> string
```

获取文本框的占位文本
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TextBox` | `UEditableTextBox` | 文本框 |

**Returns**

| Type | Description |
|---|---|
| `string` | 占位文本；TextBox 无效时返回空字符串 |

### `SetTextBoxHintText`

```text
SetTextBoxHintText(TextBox: UEditableTextBox, Text: string)
```

设置文本框的占位文本，用于输入为空时提示输入内容
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TextBox` | `UEditableTextBox` | 文本框 |
| `Text` | `string` | 占位文本，输入为空时显示 |

### `IsTextBoxReadOnly`

```text
IsTextBoxReadOnly(TextBox: UEditableTextBox) -> boolean
```

查询文本框是否为只读
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TextBox` | `UEditableTextBox` | 文本框 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否只读；TextBox 无效时返回 false |

### `SetTextBoxReadOnly`

```text
SetTextBoxReadOnly(TextBox: UEditableTextBox, bReadOnly: boolean)
```

设置文本框是否为只读，用于禁止用户编辑输入
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TextBox` | `UEditableTextBox` | 文本框 |
| `bReadOnly` | `boolean` | 是否只读 |

### `GetTextWidgetStyle`

```text
GetTextWidgetStyle(TextWidget: UTextBlock) -> table|nil
```

查询文本控件的字体、颜色、对齐、换行、描边与阴影设置
生效范围：客户端
   Font table @字体，含 FontObject、Size、TypefaceFontName、FontMaterial、OutlineSettings(OutlineSize、OutlineColor、OutlineMaterial、bSeparateFillAlpha)
   Color table @颜色，{R, G, B, A}；原控件取色规则非指定色时附带 ColorUseRule 字段，回传 SetTextWidgetStyle 时保持该规则
   Justification ETextJustify @水平对齐
   VerticalJustification ETextVerticalJustify @垂直对齐
   WrapTextAt number @控件当前生效的换行宽度
   Shadow table @阴影，含 Offset({X, Y})、Color({R, G, B, A})
 TextWidget 无效时返回 nil

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TextWidget` | `UTextBlock` | 文本控件 |

**Returns**

| Type | Description |
|---|---|
| `table\|nil` | 样式表（结构同 SetTextWidgetStyle 的 Style，可直接回传给它）： |

### `SetTextWidgetStyle`

```text
SetTextWidgetStyle(TextWidget: UTextBlock, Style: table)
```

批量设置文本控件字体、颜色、对齐、换行、描边与阴影
生效范围：客户端
   Font table @字体，字段：FontObject(UObject)、Size(number)、TypefaceFontName(string)、FontMaterial(UObject)、OutlineSettings(table, 字段：OutlineSize、OutlineColor、OutlineMaterial、bSeparateFillAlpha)
   Color table|string @颜色表 {R,G,B,A}（可携带 ColorUseRule 保持原取色规则），也可传 sRGB 十六进制字符串（如 FFFFFF 或 FFFFFFFF，RGB 分量按 sRGB 转线性）
   Justification ETextJustify @水平对齐
   VerticalJustification ETextVerticalJustify @垂直对齐
   WrapTextAt number @按该宽度换行，0 表示不按固定宽度换行
   Shadow table @阴影，字段：Offset(Vector2D)、Color(LinearColor)
   Outline table @描边，字段同 Font.OutlineSettings；与 Font.OutlineSettings 同时传入时以 Outline 为准

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TextWidget` | `UTextBlock` | 文本控件 |
| `Style` | `table` | 样式表，仅支持以下键（均为可选）： |

### `SetWidgetRenderRotation`

```text
SetWidgetRenderRotation(Widget: UWidget, Angle: number)
```

设置控件的局部渲染旋转角度
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget` | 目标控件 |
| `Angle` | `number` | 渲染旋转角度，单位为度 |

### `GetWidgetRenderRotation`

```text
GetWidgetRenderRotation(Widget: UWidget) -> number
```

获取控件的局部渲染旋转角度
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget` | 目标控件 |

**Returns**

| Type | Description |
|---|---|
| `number` | 渲染旋转角度（度）；Widget 无效时返回 0 |

### `SetWidgetRenderScale`

```text
SetWidgetRenderScale(Widget: UWidget, Scale: Vector2D)
```

设置控件的渲染缩放（只改绘制比例，不改布局占位）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget` | 目标控件 |
| `Scale` | `Vector2D` | 二维渲染缩放倍数（1 为原始比例；围绕 RenderTransformPivot 缩放，默认基准点为控件中心；负值可镜像翻转绘制） |

### `GetWidgetRenderScale`

```text
GetWidgetRenderScale(Widget: UWidget) -> Vector2D
```

获取控件的渲染缩放（绘制比例，非布局尺寸）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget` | 目标控件 |

**Returns**

| Type | Description |
|---|---|
| `Vector2D` | 二维渲染缩放（不改布局占位）；Widget 无效时返回 (0, 0) |

### `SetWidgetFocus`

```text
SetWidgetFocus(Widget: UWidget)
```

设置控件的键盘焦点（仅可聚焦控件生效）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget` | 目标控件；需可聚焦（UserWidget 请先设 bIsFocusable = true） |

### `IsWidgetFocused`

```text
IsWidgetFocused(Widget: UWidget) -> boolean
```

查询控件是否拥有键盘焦点
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget` | 目标控件 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否拥有键盘焦点；Widget 无效时返回 false |

### `SetWidgetPadding`

```text
SetWidgetPadding(Widget: UUserWidget, Padding: FMargin)
```

设置控件内边距
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 用户控件 |
| `Padding` | `FMargin` | 内容内边距，可传 {Left, Top, Right, Bottom} |

### `GetWidgetComponentUserWidget`

```text
GetWidgetComponentUserWidget(WidgetComponent: UWidgetComponent) -> UUserWidget|nil
```

获取世界空间控件组件承载的用户控件实例
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetComponent` | `UWidgetComponent` | 世界空间控件组件 |

**Returns**

| Type | Description |
|---|---|
| `UUserWidget\|nil` | 用户控件实例；组件尚未创建控件时为 nil |

### `SetWidgetComponentTint`

```text
SetWidgetComponentTint(WidgetComponent: UWidgetComponent, Tint: LinearColor)
```

设置世界空间控件组件的颜色与透明度
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetComponent` | `UWidgetComponent` | 世界空间控件组件 |
| `Tint` | `LinearColor` | 颜色与透明度，可传 {R, G, B, A} |

### `RequestWidgetComponentRedraw`

```text
RequestWidgetComponentRedraw(WidgetComponent: UWidgetComponent)
```

请求世界空间控件组件重绘
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetComponent` | `UWidgetComponent` | 世界空间控件组件；仅在组件为手动重绘模式（bManuallyRedraw 为 true）时有意义 |

### `IsWidgetAnimationPlaying`

```text
IsWidgetAnimationPlaying(Widget: UUserWidget, Animation: UWidgetAnimation) -> boolean
```

查询控件动画是否播放中，常用于播放前判断
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |
| `Animation` | `UWidgetAnimation` | 控件动画 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否播放中；控件或动画无效时返回 false |

### `PlayWidgetAnimation`

```text
PlayWidgetAnimation(Widget: UUserWidget, Animation: UWidgetAnimation, StartAtTime: number, NumLoopsToPlay: number, PlayMode: EUMGSequencePlayMode, PlaybackSpeed: number)
```

播放控件动画
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |
| `Animation` | `UWidgetAnimation` | 控件动画 |
| `StartAtTime` | `number` | 起始时间（秒），默认 0；可传入 PauseWidgetAnimation 的返回值用于续播 |
| `NumLoopsToPlay` | `number` | 循环次数，默认 1；0 表示无限循环 |
| `PlayMode` | `EUMGSequencePlayMode` | 播放模式，默认 Forward |
| `PlaybackSpeed` | `number` | 播放速率，默认 1 |

### `PauseWidgetAnimation`

```text
PauseWidgetAnimation(Widget: UUserWidget, Animation: UWidgetAnimation) -> number
```

暂停控件动画
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |
| `Animation` | `UWidgetAnimation` | 控件动画 |

**Returns**

| Type | Description |
|---|---|
| `number` | 暂停时的动画时间（相对起始位置），可作为 PlayWidgetAnimation 的 StartAtTime 续播；从未播放或播放器已清理时返回 0 |

### `StopWidgetAnimation`

```text
StopWidgetAnimation(Widget: UUserWidget, Animation: UWidgetAnimation)
```

停止控件动画
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |
| `Animation` | `UWidgetAnimation` | 控件动画 |

### `SetWidgetAnimationPlaybackSpeed`

```text
SetWidgetAnimationPlaybackSpeed(Widget: UUserWidget, Animation: UWidgetAnimation, PlaybackSpeed: number)
```

设置正在播放的控件动画速率
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |
| `Animation` | `UWidgetAnimation` | 控件动画 |
| `PlaybackSpeed` | `number` | 播放速率，默认 1 |

### `TweenWidgetSlotPosition`

```text
TweenWidgetSlotPosition(Widget: UWidget, TargetPosition: Vector2D, Duration: number, Easing: EEasingType, Config: FUnrealTweenConfig) -> FTweenHandle|nil
```

缓动控件槽位位置（仅 CanvasPanel 槽位有效）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget` | 目标控件 |
| `TargetPosition` | `Vector2D` | 目标槽位位置；仅 CanvasPanel 槽位有效 |
| `Duration` | `number` | 动画时长（秒） |
| `Easing` | `EEasingType` | 缓动类型（EEasingType 枚举），不传默认 Linear |
| `Config` | `FUnrealTweenConfig` | 高级配置（可用 UGCTweenSystem.MakeConfig() 创建，不传则使用默认值） |

**Returns**

| Type | Description |
|---|---|
| `FTweenHandle\|nil` | 动画句柄；参数无效、非 CanvasPanel 槽位或底层缓动未建立时返回 nil |

### `TweenWidgetSlotSize`

```text
TweenWidgetSlotSize(Widget: UWidget, TargetSize: Vector2D, Duration: number, Easing: EEasingType, Config: FUnrealTweenConfig) -> FTweenHandle|nil
```

缓动控件槽位尺寸（改布局占位，非渲染缩放；仅 CanvasPanel 槽位有效）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget` | 目标控件 |
| `TargetSize` | `Vector2D` | 目标槽位尺寸（宽度，高度）；仅 CanvasPanel 槽位有效 |
| `Duration` | `number` | 动画时长（秒） |
| `Easing` | `EEasingType` | 缓动类型（EEasingType 枚举），不传默认 Linear |
| `Config` | `FUnrealTweenConfig` | 高级配置（可用 UGCTweenSystem.MakeConfig() 创建，不传则使用默认值） |

**Returns**

| Type | Description |
|---|---|
| `FTweenHandle\|nil` | 动画句柄；参数无效、非 CanvasPanel 槽位或底层缓动未建立时返回 nil |

## Language

`lua`
