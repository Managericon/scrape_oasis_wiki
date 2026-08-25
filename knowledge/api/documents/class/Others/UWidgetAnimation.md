---
id: "api:class:UWidgetAnimation"
title: "UWidgetAnimation"
source: "https://developer.gp.qq.com/api/class/detail/Others/UWidgetAnimation.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UWidgetAnimation

## Inheritance

`UMovieSceneSequence`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MovieScene` | `UMovieScene *` | Pointer to the movie scene that controls this animation. |
| `AnimationBindings` | `TArray < FWidgetAnimationBinding >` | - |

## Functions

### `GetStartTime`

```text
GetStartTime() -> UMG_API float
```

Get the start time of this animation.

**Returns**

| Type | Description |
|---|---|
| `UMG_API float` | Start time in seconds. |

### `GetEndTime`

```text
GetEndTime() -> UMG_API float
```

Get the end time of this animation.

**Returns**

| Type | Description |
|---|---|
| `UMG_API float` | End time in seconds. |

### `BindToAnimationStarted`

```text
BindToAnimationStarted(Widget: UUserWidget *, Delegate: FWidgetAnimationDynamicEvent) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget *` | - |
| `Delegate` | `FWidgetAnimationDynamicEvent` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnbindFromAnimationStarted`

```text
UnbindFromAnimationStarted(Widget: UUserWidget *, Delegate: FWidgetAnimationDynamicEvent) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget *` | - |
| `Delegate` | `FWidgetAnimationDynamicEvent` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnbindAllFromAnimationStarted`

```text
UnbindAllFromAnimationStarted(Widget: UUserWidget *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BindToAnimationFinished`

```text
BindToAnimationFinished(Widget: UUserWidget *, Delegate: FWidgetAnimationDynamicEvent) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget *` | - |
| `Delegate` | `FWidgetAnimationDynamicEvent` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnbindFromAnimationFinished`

```text
UnbindFromAnimationFinished(Widget: UUserWidget *, Delegate: FWidgetAnimationDynamicEvent) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget *` | - |
| `Delegate` | `FWidgetAnimationDynamicEvent` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnbindAllFromAnimationFinished`

```text
UnbindAllFromAnimationFinished(Widget: UUserWidget *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnAnimationStarted`

```text
OnAnimationStarted() -> void
```

Fires when the widget animation starts playing. compatible for lua, to be deleted

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnAnimationFinished`

```text
OnAnimationFinished() -> void
```

Fires when the widget animation is finished. compatible for lua, to be deleted

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
