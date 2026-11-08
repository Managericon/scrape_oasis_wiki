---
id: "api:class:UGCUIManagerSystem"
title: "UGCUIManagerSystem"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGCUIManagerSystem.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCUIManagerSystem

UI管理器（客户端）

## Functions

### `RegisterUI`

```text
RegisterUI(Key: string, Config: UGCUIConfig)
```

注册 UI 配置，供后续通过 Key 加载和打开界面。
重复注册同一个 Key 会先注销旧配置并销毁旧实例；默认仅保存配置，bPreload=true 时自动预加载。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `string` | 非空的 UI 唯一标识，后续 Open、Close 等接口均使用此标识 |
| `Config` | `UGCUIConfig` | 必须提供 WidgetClassPath；其余字段的默认值见 UGCUIConfig |

### `UnregisterUI`

```text
UnregisterUI(Key: string)
```

注销 UI 配置并销毁已加载的实例，同时取消尚未完成的打开操作。
已打开的 UI 会先调用 OnClose；注销后需重新 RegisterUI 才能打开。Key 未注册时不做处理。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `string` | UI 注册时使用的唯一标识 |

### `IsRegistered`

```text
IsRegistered(Key: string) -> boolean
```

查询是否存在此 Key 的 UI 配置，与界面是否已加载或打开无关。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `string` | UI 注册时使用的唯一标识 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 已注册返回 true，否则返回 false |

### `RegisterViewModel`

```text
RegisterViewModel(VMKey: string, ViewModel: UGCViewModel)
```

注册共享 ViewModel 的原型，首次 GetViewModel 时通过原型的 New 方法创建实例。
同一个 VMKey 的多个 View 共用一个实例；重复注册只更新原型，已有实例继续使用到被回收。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `VMKey` | `string` | 非空的 ViewModel 唯一标识，与 UI 的 Key 相互独立 |
| `ViewModel` | `UGCViewModel` | 用于创建实例的原型，需提供 New 方法；可用 NewViewModel 创建后定义 OnInitialize |

### `GetViewModel`

```text
GetViewModel(VMKey: string, View: UGCView) -> UGCViewModel|nil
```

获取或创建共享 ViewModel，并记录当前 View 对它的引用。
同一个 View 重复获取同一个 VMKey 只计一次引用；View 的 Destruct 执行后释放引用。
最后一个引用释放时销毁实例，保留注册原型，下次获取时重新创建。仅隐藏 View 不释放引用。
此接口只获取实例并管理引用；属性和命令绑定仍需调用 SetupViewModel、BindProperty 等方法设置。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `VMKey` | `string` | 通过 RegisterViewModel 注册的标识 |
| `View` | `UGCView` | 使用该实例的有效 View 控件，通常传入控件脚本中的 self，不可传普通 Lua 表 |

**Returns**

| Type | Description |
|---|---|
| `UGCViewModel\|nil` | 共享实例；未注册、View 无效或原型 New 返回 nil 时返回 nil |

### `GetViewModelIfExists`

```text
GetViewModelIfExists(VMKey: string) -> UGCViewModel|nil
```

查询已经创建的共享 ViewModel，不创建实例，也不增加引用计数。
适合业务逻辑临时读取或更新已有实例；实例可能随最后一个引用它的 View 销毁而被回收。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `VMKey` | `string` | ViewModel 注册时使用的唯一标识 |

**Returns**

| Type | Description |
|---|---|
| `UGCViewModel\|nil` | 当前实例；未注册、尚未创建或已被回收时返回 nil |

### `Preload`

```text
Preload(Key: string) -> PromiseFuture
```

异步加载 UI 类并创建隐藏的缓存实例，供后续 Open 复用；不调用 OnOpen。
会等待本地 PlayerController 就绪；已有有效实例时直接复用，不改变其显示状态。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `string` | 已注册的 UI 标识 |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 已启动的异步任务，完成结果为 UUserWidget；未注册、加载失败或加载期间注册被移除、替换时为 nil |

### `PreloadAll`

```text
PreloadAll(Keys: string[]) -> PromiseFuture
```

并行预加载多个 UI，等待所有已注册项的加载任务结束；未注册的 Key 会被跳过。
任务结束不代表每个 UI 都加载成功，可通过 GetWidget 分别检查实例。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Keys` | `string[]` | 需要预加载的 UI 标识数组 |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 已启动的异步任务，仅表示批量加载结束，不返回实例列表 |

### `Open`

```text
Open(Key: string, ...: any) -> PromiseFuture
```

异步打开 UI：按需加载实例和层容器，关闭同互斥组的其他界面，再显示并调用 Widget:OnOpen(...)。
已打开时会移到所在层的最上方并再次调用 OnOpen；正在打开时复用原任务，后续传入的参数不生效。
可在异步上下文中用 UGCAsyncUtility.Await 等待返回的任务，或通过任务的 Then 方法接收结果。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `string` | 已注册的 UI 标识 |
| `...` | `any` | 传给 Widget:OnOpen(...) 的参数 |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 已启动的异步任务；打开完成后返回 Widget，未注册、打开失败或被取消时返回 nil |

### `Close`

```text
Close(Key: string, bDestroy: boolean|nil)
```

关闭已打开的 UI，先调用 OnClose，再隐藏或销毁实例；注册配置仍然保留。
默认隐藏为 Collapsed 并缓存复用。正在打开但尚未显示时只取消打开，加载本身可能继续完成并留下缓存。
对其他未打开的 UI 不做处理，包括已预加载的缓存；若要移除缓存及配置，请调用 UnregisterUI。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `string` | UI 注册时使用的唯一标识 |
| `bDestroy` | `boolean\|nil` | 可选，true 强制销毁已打开的实例；false 或 nil 仍按配置 bDestroyOnClose 决定是否销毁 |

### `Toggle`

```text
Toggle(Key: string, ...: any) -> boolean
```

已打开时调用 Close，否则调用 Open；正在打开时仍走 Open，不会取消打开。
返回值只表示选择的操作。需要等待打开结果时请直接调用 Open，查询当前打开状态请用 IsOpen。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `string` | 已注册的 UI 标识 |
| `...` | `any` | 仅在打开分支传给 Widget:OnOpen(...) 的参数 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | true 表示调用了 Open，不保证最终成功；false 表示调用了 Close |

### `CloseAll`

```text
CloseAll(bDestroy: boolean|nil)
```

关闭所有当前已打开的 UI，逐个执行 Close；不处理正在加载或仅缓存的 UI。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bDestroy` | `boolean\|nil` | 可选，true 强制销毁；false 或 nil 按各 UI 的 bDestroyOnClose 配置处理 |

### `CloseLayer`

```text
CloseLayer(Layer: EUGCUILayer, bDestroy: boolean|nil)
```

关闭指定层中当前已打开的全部 UI，逐个执行 Close。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Layer` | `EUGCUILayer` | 要关闭的 UI 层，例如 EUGCUILayer.Popup |
| `bDestroy` | `boolean\|nil` | 可选，true 强制销毁；false 或 nil 按各 UI 的 bDestroyOnClose 配置处理 |

### `CloseGroup`

```text
CloseGroup(GroupName: string, bDestroy: boolean|nil)
```

关闭属于指定互斥组且当前已打开的 UI，逐个执行 Close。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GroupName` | `string` | 注册配置 MutexGroups 中使用的组名；组不存在时不做处理 |
| `bDestroy` | `boolean\|nil` | 可选，true 强制销毁；false 或 nil 按各 UI 的 bDestroyOnClose 配置处理 |

### `IsOpen`

```text
IsOpen(Key: string) -> boolean
```

查询管理器是否已将此 UI 标记为打开；不检查控件被外部代码隐藏等情况。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `string` | UI 注册时使用的唯一标识 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 状态为 Open 时返回 true；未注册、正在加载或已关闭时返回 false |

### `GetWidget`

```text
GetWidget(Key: string) -> UUserWidget|nil
```

获取当前有效的 UI 实例，不触发加载，也不等待正在进行的打开操作。
预加载或关闭后缓存的实例也会返回；拿到实例不代表 UI 已打开。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `string` | UI 注册时使用的唯一标识 |

**Returns**

| Type | Description |
|---|---|
| `UUserWidget\|nil` | 已创建且有效的实例；未注册、尚未创建或实例已失效时返回 nil |

### `GetState`

```text
GetState(Key: string) -> EUGCUIState
```

查询 UI 的当前管理状态，可与 EUGCUIState.Open 等枚举值比较。
Unloaded：未加载；Loading：正在加载实例；Cached：实例已缓存但未打开；Open：已打开。
等待层容器就绪时可能仍为 Cached；此状态不能单独判断是否有 Open 任务正在执行。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `string` | UI 注册时使用的唯一标识 |

**Returns**

| Type | Description |
|---|---|
| `EUGCUIState` | UI 状态枚举值；未注册返回 EUGCUIState.Unloaded，可用 IsRegistered 区分 |

### `GetTopWidget`

```text
GetTopWidget(Layer: EUGCUILayer) -> string|nil, UUserWidget|nil
```

获取指定层最上方的已打开 UI；同层最后打开或再次打开的 UI 位于栈顶。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Layer` | `EUGCUILayer` | 要查询的 UI 层 |

**Returns**

| Type | Description |
|---|---|
| `string\|nil` | 栈顶 UI 的 Key；该层没有已打开 UI 时返回 nil |
| `UUserWidget\|nil` | 栈顶 UI 的有效实例；实例失效或栈为空时返回 nil |

### `GetOpennedKeys`

```text
GetOpennedKeys(Layer: EUGCUILayer|nil) -> string[]
```

获取当前已打开 UI 的 Key 列表，可按层筛选。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Layer` | `EUGCUILayer\|nil` | 可选，指定层时按从底到顶的顺序返回；不传则返回所有层的已打开 UI，顺序不固定 |

**Returns**

| Type | Description |
|---|---|
| `string[]` | UI Key 数组副本；没有符合条件的 UI 时返回空数组 |

### `NewViewModel`

```text
NewViewModel() -> UGCViewModel
```

创建 ViewModel 对象，可作为自定义原型，定义 OnInitialize 后传给 RegisterViewModel。
管理器首次 GetViewModel 时会调用该原型的 New 创建共享实例，并执行 OnInitialize 声明属性。
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `UGCViewModel` | 新的 ViewModel 对象；本接口不会自动注册到管理器 |

### `NewView`

```text
NewView() -> UGCView
```

创建 View 的 Lua 对象，供 UI 控件脚本扩展使用；不创建 UUserWidget，也不自动绑定 ViewModel。
在控件中获取 ViewModel 后，调用 self:SetupViewModel(ViewModel) 设置绑定上下文。
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `UGCView` | 新的 View 对象，包含属性、命令和集合的绑定接口 |

### `NewItemView`

```text
NewItemView() -> UGCItemView
```

创建列表项 View 的 Lua 对象，用于集合绑定和列表项复用；不创建 UUserWidget。
后续由 SetupWithViewModel 设置或切换 ViewModel，并调用 OnSetup 声明绑定。
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `UGCItemView` | 新的列表项 View 对象，在 OnSetup 中通过 self.VMProperties/self.VMCommands 设置绑定 |

### `NewCollectionBinder`

```text
NewCollectionBinder() -> UGCMVVMCollectionBinder
```

创建继承 UGCMVVMCollectionBinder 的原型，用于实现自定义列表控件的集合绑定器。
将该原型传给 View:BindCollection 的 BinderClass 参数，由 BindCollection 创建并绑定实例。
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `UGCMVVMCollectionBinder` | 自定义集合绑定器原型 |

### `RegisterWidgetUpdater`

```text
RegisterWidgetUpdater(BindType: string)
```

注册控件更新函数，供 View:BindProperty 等属性绑定接口按 BindType 调用。
属性同步时将控件和值传给更新函数；配置了转换器时，Value 为转换后的值。同名注册会覆盖旧函数。
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BindType` | `string` | 绑定类型名，在属性绑定时使用同一个名称 |

### `RegisterConverter`

```text
RegisterConverter(Name: string)
```

注册属性值转换函数，供 View:BindProperty 等接口的 Converter 参数按名称引用。
转换后的返回值会传给控件更新函数；同名注册会覆盖旧转换器。
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Name` | `string` | 非空的转换器名称，可作为绑定接口的 Converter 参数 |

## Language

`lua`
