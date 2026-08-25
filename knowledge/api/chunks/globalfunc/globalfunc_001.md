---
id: "api-chunk:globalfunc:1"
title: "Oasis API globalfunc chunk 1"
source: "https://developer.gp.qq.com/api/"
category: "API Wiki/globalfunc"
kind: "api_chunk"
---

<!-- Source: https://developer.gp.qq.com/api/globalfunc/detail/GetAsyncLoadObjectPromiseFuture.json -->

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


---

<!-- Source: https://developer.gp.qq.com/api/globalfunc/detail/TagLogFormatPrint.json -->

# TagLogFormatPrint

输出格式化的日志（注意：format 使用  XML占位符格式，不是 %s/%d） 有三种使用方式： 格式1（纯字符串，无额外参数）：TagLogFormatPrint(log) 示例：TagLogFormatPrint("something happened") 格式2（带Tag占位符的格式化字符串 + 参数，使用默认Category "LogTagLog"、默认Verbosity Log）： TagLogFormatPrint(format, ...) 示例：TagLogFormatPrint("player= score=", playerName, score) 格式3（指定已注册的LogCategory + ELogVerbosity + 带Tag占位符的格式化字符串 + 参数）： TagLogFormatPrint(category, verbosity, format, ...) 示例：TagLogFormatPrint("LogPESkill", ELogVerbosity.Log, ": damage=", character, damage) 占位符类型： 等，按顺序对应后续参数 注意：format 中必须包含  占位符才能传递额外参数，否则会被拒绝输出！ 错误用法：TagLogFormatPrint("type=%s", val) -- 不支持 %s 格式！ 生效范围：服务器&客户端

## Functions

### `TagLogFormatPrint`

```text
TagLogFormatPrint(...: any)
```

输出格式化的日志（注意：format 使用  XML占位符格式，不是 %s/%d） 有三种使用方式： 格式1（纯字符串，无额外参数）：TagLogFormatPrint(log) 示例：TagLogFormatPrint("something happened") 格式2（带Tag占位符的格式化字符串 + 参数，使用默认Category "LogTagLog"、默认Verbosity Log）： TagLogFormatPrint(format, ...) 示例：TagLogFormatPrint("player= score=", playerName, score) 格式3（指定已注册的LogCategory + ELogVerbosity + 带Tag占位符的格式化字符串 + 参数）： TagLogFormatPrint(category, verbosity, format, ...) 示例：TagLogFormatPrint("LogPESkill", ELogVerbosity.Log, ": damage=", character, damage) 占位符类型： 等，按顺序对应后续参数 注意：format 中必须包含  占位符才能传递额外参数，否则会被拒绝输出！ 错误用法：TagLogFormatPrint("type=%s", val) -- 不支持 %s 格式！ 生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `...` | `any` | 输入参数 格式1 string log；格式2 string format, vararg params；格式3 string category, ELogVerbosity verbosity, string format, vararg params |


---

<!-- Source: https://developer.gp.qq.com/api/globalfunc/detail/TagLogRawPrint.json -->

# TagLogRawPrint

输出原始日志

## Functions

### `TagLogRawPrint`

```text
TagLogRawPrint(LogCategory: string, LogVerbosity: ELogVerbosity, LogContent: string)
```

输出原始日志

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LogCategory` | `string` | 日志类别 |
| `LogVerbosity` | `ELogVerbosity` | 日志详细级别 |
| `LogContent` | `string` | 日志内容 |

