---
id: "api:cppenum:EUGCCommonDelegateType"
title: "EUGCCommonDelegateType"
source: "https://developer.gp.qq.com/api/cppenum/detail/EUGCCommonDelegateType.json"
category: "API Wiki/cppenum"
kind: "cppenum"
api_root: "https://developer.gp.qq.com/api/"
---

# EUGCCommonDelegateType

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Normal` | `0` | 普通委托：可以多次广播，每次广播只通知已订阅者 |
| `Sticky` | `1` | 粘滞委托：可以多次广播，每次广播会通知已订阅者，之后新加入的订阅者会收到上一次广播的结果 |
| `Latched` | `2` | 锁存委托：只能广播一次，第一次广播会通知已订阅者，之后新加入的订阅者会收到第一次广播的结果，之后的广播会直接忽略 |
