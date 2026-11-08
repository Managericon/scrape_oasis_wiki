---
id: "api:class:UGCModeArchiveSystem"
title: "UGCModeArchiveSystem"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGCModeArchiveSystem.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCModeArchiveSystem

UGC 玩法存档系统（ModeArchive）：玩法（mode）维度存档数据的异步存取接口，全部接口仅在服务器生效

## Functions

### `AsyncCreateIntKey`

```text
AsyncCreateIntKey(BizName: string, InitValue: number, ExpireDays?: number) -> UGCPromiseFuture
```

异步创建整型 key
注意：固定"仅当不存在时创建"语义（最小接口集，禁止无条件覆盖存档数据）：
  key 已存在时返回 KeyAlreadyExists，原值不受影响；未被 float 标记的
  key 需要重置请显式先 AsyncDeleteKey 再 AsyncCreateIntKey（非原子两步；
  float 标记不可逆，曾被 float 接口写入的 key 删除后重建 int 仍返回 TypeMismatch）
注意：float 标记不可逆，若该 key 曾被 float 接口写入，将返回 TypeMismatch
用法：UGCAsyncUtility.AsyncRun(UGCModeArchiveSystem.AsyncCreateIntKey("TotalKills", 0)):Then(function(Task) local ErrCode = Task:Get() end)
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BizName` | `string` | 业务键名，非空且不超过 128 字符，同一玩法内全局唯一 |
| `InitValue` | `number` | 初始值，必须为整数 |
| `ExpireDays?` | `number` | 可选，过期天数，非负数（默认 0 表示永不过期） |

**Returns**

| Type | Description |
|---|---|
| `UGCPromiseFuture` | 结果 (ErrCode) |

### `AsyncCreateFloatKey`

```text
AsyncCreateFloatKey(BizName: string, InitValue: number, ExpireDays?: number) -> UGCPromiseFuture
```

异步创建浮点型 key
注意：固定"仅当不存在时创建"语义（最小接口集，禁止无条件覆盖存档数据）：
  key 已存在时返回 KeyAlreadyExists，原值不受影响；需要重置请显式先
  AsyncDeleteKey 再 AsyncCreateFloatKey（非原子两步）
注意：创建后该 key 永久标记为 float，后续必须使用 float 接口（AsyncModifyFloatValue）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BizName` | `string` | 业务键名，非空且不超过 128 字符，同一玩法内全局唯一 |
| `InitValue` | `number` | 初始值（任意有限数值） |
| `ExpireDays?` | `number` | 可选，过期天数，非负数（默认 0 表示永不过期） |

**Returns**

| Type | Description |
|---|---|
| `UGCPromiseFuture` | 结果 (ErrCode) |

### `AsyncGetKey`

```text
AsyncGetKey(BizName: string) -> UGCPromiseFuture
```

异步查询指定 key 的当前值
协议 v2 直通模式：get 直读 Redis 当前值（modify 即时落盘，无聚合缓存）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BizName` | `string` | 业务键名 |

**Returns**

| Type | Description |
|---|---|
| `UGCPromiseFuture` | 结果 (ErrCode, Value)：成功时 Value 为 number（超出 number 精度范围的超大整数会透传后台原始 string）；key 不存在时 ErrCode=NotExist 且 Value=nil |

### `AsyncDeleteKey`

```text
AsyncDeleteKey(BizName: string) -> UGCPromiseFuture
```

异步删除指定 key（仅当 key 存在时删除）
key 不存在时返回 NotExist；float 类型标记不随删除清除（永久不可逆语义）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BizName` | `string` | 业务键名 |

**Returns**

| Type | Description |
|---|---|
| `UGCPromiseFuture` | 结果 (ErrCode) |

### `AsyncModifyIntValue`

```text
AsyncModifyIntValue(BizName: string, Delta: number) -> UGCPromiseFuture
```

异步增量修改整型 key（直通强一致：即时执行 Redis INCRBY 原子自增并落盘）
key 不存在时按 Redis INCRBY 语义从 0 起算（隐式创建，占用 key 数量配额）
注意：float 标记不可逆，若该 key 曾被 float 接口写入，将返回 TypeMismatch
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BizName` | `string` | 业务键名 |
| `Delta` | `number` | 增量，必须为整数（可为负数） |

**Returns**

| Type | Description |
|---|---|
| `UGCPromiseFuture` | 结果 (ErrCode, NewValue)：成功时 NewValue 为修改后的最新值（Redis 原子返回值，天然包含其他对局的并发修改；超出 number 精度范围的超大整数会透传后台原始 string）；错误路径 NewValue 为 nil |

### `AsyncModifyFloatValue`

```text
AsyncModifyFloatValue(BizName: string, Delta: number) -> UGCPromiseFuture
```

异步增量修改浮点型 key（直通强一致：即时执行 Redis INCRBYFLOAT 原子自增并落盘）
key 不存在时按 Redis INCRBYFLOAT 语义从 0 起算（隐式创建，占用 key 数量配额）
注意：修改后该 key 永久标记为 float，后续 int 接口将返回 TypeMismatch
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BizName` | `string` | 业务键名 |
| `Delta` | `number` | 增量（任意有限数值，可为负数） |

**Returns**

| Type | Description |
|---|---|
| `UGCPromiseFuture` | 结果 (ErrCode, NewValue)：成功时 NewValue 为修改后的最新值（Redis 原子返回值，天然包含其他对局的并发修改）；错误路径 NewValue 为 nil |

## Language

`lua`
