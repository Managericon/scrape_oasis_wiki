---
id: "api:cppstruct:FUGCItemTransferResult"
title: "FUGCItemTransferResult"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FUGCItemTransferResult.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FUGCItemTransferResult

物品转移结果

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CanTransfer` | `bool` | 转移是否成功 |
| `TransferErrorReason` | `TArray < FName >` | 如果转移失败，失败原因来自于转移者 |
| `ItemErrorReason` | `TMap < FItemDefineID , FName >` | 如果转移失败，失败原因来自于物品 |
