---
id: "api:class:UInvalidationBox"
title: "UInvalidationBox"
source: "https://developer.gp.qq.com/api/class/detail/Others/UInvalidationBox.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UInvalidationBox

Invalidate
   Single Child
   Caching  Performance

## Inheritance

`UContentWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bCanCache` | `bool` | Should the invalidation panel cache the widgets?  Making this false makes it so the invalidation<br>	  panel stops acting like an invalidation panel, just becomes a simple container widget. |
| `CacheRelativeTransforms` | `bool` | Caches the locations for child draw elements relative to the invalidation box,<br>	  this adds extra overhead to drawing them every frame.  However, in cases where<br>	  the position of the invalidation boxes changes every frame this can be a big savings. |

## Functions

### `InvalidateCache`

```text
InvalidateCache() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCanCache`

```text
GetCanCache() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetCanCache`

```text
SetCanCache(CanCache: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CanCache` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
