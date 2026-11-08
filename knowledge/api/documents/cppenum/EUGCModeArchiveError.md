---
id: "api:cppenum:EUGCModeArchiveError"
title: "EUGCModeArchiveError"
source: "https://developer.gp.qq.com/api/cppenum/detail/EUGCModeArchiveError.json"
category: "API Wiki/cppenum"
kind: "cppenum"
api_root: "https://developer.gp.qq.com/api/"
---

# EUGCModeArchiveError

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Success` | `0` | 成功 |
| `LocalNotServer` | `-1` | [本地] 非服务器环境调用（接口仅服务器生效，未发包） |
| `LocalInvalidParam` | `-2` | [本地] 参数校验失败（请求未发出） |
| `LocalNotSupported` | `-3` | [本地] 当前环境不支持（UGCMobile 玩法调用本接口，需求范围仅限 UGC 端游） |
| `LocalTimeout` | `-4` | [本地] 本地兜底超时（默认约 10 秒，防止底层发送失败等异常导致请求永久挂起） |
| `InvalidParam` | `9935128` | 参数非法（后台校验：biz_name / value_info / delta；或对局无有效 sub_mode） |
| `DbError` | `9935129` | 数据库（Redis）操作失败 |
| `KeyLimitExceeded` | `9935130` | key 数量超限（单玩法上限 1000 个 BizName） |
| `RateLimited` | `9935131` | QPS 限流触发（单玩法总 QPS 约 5000，可重试或降频） |
| `NotExist` | `9935132` | key 不存在（delete 仅删存在 key / get 查询不存在 key 时） |
| `KeyAlreadyExists` | `9935133` | key 已存在（create 接口固定"仅当不存在时创建"，key 已存在时返回本错误码） |
| `PendingFull` | `9935134` | 待冲刷队列已满（协议 v2 已移除聚合模式：后台保留该错误码仅为数值对齐兼容，正常不会再返回） |
| `TypeMismatch` | `9935135` | 类型不匹配（int / float 混用；float 标记不可逆） |
