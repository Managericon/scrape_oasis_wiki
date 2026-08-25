---
id: "api:class:UKismetGuidLibrary"
title: "UKismetGuidLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UKismetGuidLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UKismetGuidLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `EqualEqual_GuidGuid`

```text
EqualEqual_GuidGuid(A: FGuid &, B: FGuid &) -> bool
```

Returns true if the values are equal (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FGuid &` | - |
| `B` | `FGuid &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_GuidGuid`

```text
NotEqual_GuidGuid(A: FGuid &, B: FGuid &) -> bool
```

Returns true if the values are not equal (A != B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FGuid &` | - |
| `B` | `FGuid &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsValid_Guid`

```text
IsValid_Guid(InGuid: FGuid &) -> bool
```

Checks whether the given GUID is valid

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InGuid` | `FGuid &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Invalidate_Guid`

```text
Invalidate_Guid(InGuid: FGuid &) -> void
```

Invalidates the given GUID

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InGuid` | `FGuid &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `NewGuid`

```text
NewGuid() -> FGuid
```

Returns a new unique GUID

**Returns**

| Type | Description |
|---|---|
| `FGuid` | - |

### `Conv_GuidToString`

```text
Conv_GuidToString(InGuid: FGuid &) -> FString
```

Converts a GUID value to a string, in the form 'A-B-C-D'

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InGuid` | `FGuid &` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `Parse_StringToGuid`

```text
Parse_StringToGuid(GuidString: FString &, OutGuid: FGuid &, Success: bool &) -> void
```

Converts a String of format EGuidFormats to a Guid. Returns Guid OutGuid, Returns bool Success

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GuidString` | `FString &` | - |
| `OutGuid` | `FGuid &` | - |
| `Success` | `bool &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
