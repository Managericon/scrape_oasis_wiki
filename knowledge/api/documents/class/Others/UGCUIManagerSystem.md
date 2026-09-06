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

### `RegisterViewModel`

```text
RegisterViewModel(VMKey: string, ViewModel: UGCViewModel)
```

会在依赖它的View创建时实例化

**Parameters**

| Name | Type | Description |
|---|---|---|
| `VMKey` | `string` | ViewModel的Key，与UI的Key相互独立 |
| `ViewModel` | `UGCViewModel` | ViewModel原型 |

### `NewViewModel`

```text
NewViewModel() -> UGCViewModel
```

创建新的ViewModel
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `UGCViewModel` | ViewModel实例，在OnInitialize中声明属性 |

### `NewView`

```text
NewView() -> UGCView
```

创建新的View，绑定到指定的ViewModel
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `UGCView` | View实例 |

### `NewItemView`

```text
NewItemView() -> UGCItemView
```

创建新的ItemView（列表项View），用于Collection绑定场景
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `UGCItemView` | ItemView实例，在OnSetup中通过self.VMProperties/self.VMCommands设置绑定 |

### `NewCollectionBinder`

```text
NewCollectionBinder() -> UGCMVVMCollectionBinder
```

创建新的UGCMVVMCollectionBinder，用于派生自定义集合绑定器
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `UGCMVVMCollectionBinder` | CollectionBinder原型，通过View:BindCollection的BinderClass参数使用 |

### `RegisterWidgetUpdater`

```text
RegisterWidgetUpdater(BindType: string, UpdaterFunc: fun(Widget:userdata, Value:any) @更新函数)
```

注册自定义的Widget更新函数
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BindType` | `string` | 自定义的绑定类型名 |
| `UpdaterFunc` | `fun(Widget:userdata, Value:any) @更新函数` | 更新函数 |

### `RegisterConverter`

```text
RegisterConverter(Name: string, ConverterFunc: fun(Value:any, ...:any):any @转换函数)
```

注册自定义值转换器
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Name` | `string` | 转换器名称 |
| `ConverterFunc` | `fun(Value:any, ...:any):any @转换函数` | 转换函数 |

## Language

`lua`
