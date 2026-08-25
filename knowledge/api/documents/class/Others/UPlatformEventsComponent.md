---
id: "api:class:UPlatformEventsComponent"
title: "UPlatformEventsComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPlatformEventsComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPlatformEventsComponent

Component to handle receiving notifications from the OS about platform events.

## Inheritance

`UActorComponent`

## Functions

### `IsInLaptopMode`

```text
IsInLaptopMode() -> bool
```

Check whether a convertible laptop is laptop mode.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if in laptop mode, false otherwise or if not a convertible laptop. |

### `IsInTabletMode`

```text
IsInTabletMode() -> bool
```

Check whether a convertible laptop is laptop mode.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if in tablet mode, false otherwise or if not a convertible laptop. |

### `SupportsConvertibleLaptops`

```text
SupportsConvertibleLaptops() -> bool
```

Check whether the platform supports convertible laptops.
	 
	  Note: This does not necessarily mean that the platform is a convertible laptop.
	  For example, convertible laptops running Windows 7 or older will return false,
	  and regular laptops running Windows 8 or newer will return true.

**Returns**

| Type | Description |
|---|---|
| `bool` | true for convertible laptop platforms, false otherwise. |

## Delegates

### `PlatformChangedToLaptopModeDelegate`

```text
PlatformChangedToLaptopModeDelegate() -> void
```

This is called when a convertible laptop changed into laptop mode.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PlatformChangedToTabletModeDelegate`

```text
PlatformChangedToTabletModeDelegate() -> void
```

This is called when a convertible laptop changed into tablet mode.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
