---
id: "api:globalfunc:GetAsyncLoadObjectPromiseFuture"
title: "GetAsyncLoadObjectPromiseFuture"
source: "https://developer.gp.qq.com/api/globalfunc/detail/GetAsyncLoadObjectPromiseFuture.json"
category: "API Wiki/globalfunc"
kind: "globalfunc"
api_root: "https://developer.gp.qq.com/api/"
---

# GetAsyncLoadObjectPromiseFuture

使用 PromiseFuture 异步加载资源并创建对象实例
用法：GetAsyncLoadObjectPromiseFuture(PlayerController, ObjectPath):Then(function (PromiseFuture) local Obj = PromiseFuture:Get() end):AutoResume()
生效范围：服务器&客户端

## Functions

### `GetAsyncLoadObjectPromiseFuture`

```text
GetAsyncLoadObjectPromiseFuture(Outer: UObject, FullPath: string) -> @PromiseFuture
```

使用 PromiseFuture 异步加载资源并创建对象实例
用法：GetAsyncLoadObjectPromiseFuture(PlayerController, ObjectPath):Then(function (PromiseFuture) local Obj = PromiseFuture:Get() end):AutoResume()
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Outer` | `UObject` | Outer 对象，一般为 PlayerController |
| `FullPath` | `string` | 资源路径 |

**Returns**

| Type | Description |
|---|---|
| `@PromiseFuture` | 对象 |
