---
id: "api:cppstruct:FScreenMessageString"
title: "FScreenMessageString"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FScreenMessageString.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FScreenMessageString

On-screen debug message handling 
 Helper struct for tracking on screen messages.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Key` | `uint64` | The 'key' for this message. |
| `ScreenMessage` | `FString` | The message to display. |
| `DisplayColor` | `FColor` | The color to display the message in. |
| `TimeToDisplay` | `float` | The number of frames to display it. |
| `CurrentTimeDisplayed` | `float` | The number of frames it has been displayed so far. |
| `TextScale` | `FVector2D` | Scale of text |
| `IsUGCMsg` | `bool` | Is ugc message |
