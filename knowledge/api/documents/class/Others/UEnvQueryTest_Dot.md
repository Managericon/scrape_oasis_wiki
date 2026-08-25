---
id: "api:class:UEnvQueryTest_Dot"
title: "UEnvQueryTest_Dot"
source: "https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryTest_Dot.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UEnvQueryTest_Dot

## Inheritance

`UEnvQueryTest`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LineA` | `FEnvDirection` | defines direction of first line used by test |
| `LineB` | `FEnvDirection` | defines direction of second line used by test |
| `TestMode` | `EEnvTestDot` | - |
| `bAbsoluteValue` | `bool` | If true, this test uses the absolute value of the dot product rather than the dot product itself.  Useful<br>	   when you want to compare "how lateral" something is.  I.E. values closer to zero are further to the side, <br>	   and values closer to 1 are more in front or behind (without distinguishing forwardbackward). |

## Language

`cpp`
