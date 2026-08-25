---
id: "api:class:UPendingNetGame"
title: "UPendingNetGame"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPendingNetGame.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPendingNetGame

## Inheritance

`UObject` -> `FNetworkNotify`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NetDriver` | `UNetDriver *` | Net driver created for contacting the new server<br>	  Transferred to world on successful connection |
| `DemoNetDriver` | `UDemoNetDriver *` | Demo Net driver created for loading demos, but we need to go through pending net game<br>	  Transferred to world on successful connection |

## Language

`cpp`
