---
id: "api:class:UStaticMeshSocket"
title: "UStaticMeshSocket"
source: "https://developer.gp.qq.com/api/class/detail/Others/UStaticMeshSocket.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UStaticMeshSocket

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SocketName` | `FName` | Defines a named attachment location on the UStaticMesh. <br>	 	These are set up in editor and used as a shortcut instead of specifying <br>	 	everything explicitly to AttachComponent in the StaticMeshComponent.<br>	 	The Outer of a StaticMeshSocket should always be the UStaticMesh. |
| `RelativeLocation` | `FVector` | - |
| `RelativeRotation` | `FRotator` | - |
| `RelativeScale` | `FVector` | - |
| `Tag` | `FString` | - |
| `bDynamicCreate` | `bool` | - |

## Language

`cpp`
