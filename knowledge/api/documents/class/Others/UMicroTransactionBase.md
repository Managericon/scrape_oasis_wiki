---
id: "api:class:UMicroTransactionBase"
title: "UMicroTransactionBase"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMicroTransactionBase.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMicroTransactionBase

## Inheritance

`UPlatformInterfaceBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AvailableProducts` | `TArray < struct FPurchaseInfo >` | The list of products available to purchase, filled out by the time a MTD_PurchaseQueryComplete is fired |
| `LastError` | `FString` | In case of errors, this will describe the most recent error |
| `LastErrorSolution` | `FString` | In case of errors, this will describe possible solutions (if there are any) |

## Language

`cpp`
