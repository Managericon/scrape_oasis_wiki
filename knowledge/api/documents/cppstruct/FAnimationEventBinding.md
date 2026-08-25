---
id: "api:cppstruct:FAnimationEventBinding"
title: "FAnimationEventBinding"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimationEventBinding.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimationEventBinding

Used to manage different animation event bindings that users want callbacks on.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Delegate` | `FWidgetAnimationDynamicEvent` | The callback. |
| `Animation` | `UWidgetAnimation *` | The animation to look for. |
| `AnimationEvent` | `EWidgetAnimationEvent` | The type of animation event. |
| `UserTag` | `FName` | A user tag used to only get callbacks for specific runs of the animation. |
