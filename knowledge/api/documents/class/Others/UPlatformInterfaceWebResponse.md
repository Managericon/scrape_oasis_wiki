---
id: "api:class:UPlatformInterfaceWebResponse"
title: "UPlatformInterfaceWebResponse"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPlatformInterfaceWebResponse.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPlatformInterfaceWebResponse

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OriginalURL` | `FString` | This holds the original requested URL |
| `ResponseCode` | `int32` | Result code from the response (200=OK, 404=Not Found, etc) |
| `Tag` | `int32` | A user-specified tag specified with the request |
| `StringResponse` | `FString` | For string results, this is the response |
| `BinaryResponse` | `TArray < uint8 >` | For non-string results, this is the response |

## Functions

### `GetNumHeaders`

```text
GetNumHeaders() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | the number of headervalue pairs |

### `GetHeader`

```text
GetHeader(HeaderIndex: int32, Header: FString &, Value: FString &) -> void
```

Retrieve the header and value for the given index of headervalue pair

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HeaderIndex` | `int32` | - |
| `Header` | `FString &` | - |
| `Value` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetHeaderValue`

```text
GetHeaderValue(HeaderName: FString &) -> FString
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HeaderName` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | the value for the given header (or "" if no matching header) |

## Language

`cpp`
