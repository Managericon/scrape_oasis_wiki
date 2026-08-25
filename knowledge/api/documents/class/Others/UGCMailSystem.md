---
id: "api:class:UGCMailSystem"
title: "UGCMailSystem"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGCMailSystem.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCMailSystem

邮件系统库

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UGCMailSystem.MailListUpdateDelegate` | `-` | 玩家邮件列表更新时触发<br>非PIE时，仅在玩家刚进入玩法时触发一次，玩家在局内时后台发送的邮件，会在下一局进入时更新<br>@param UID int @UID<br>@param MailList UGCMailInfo[] @邮件列表 |
| `UGCMailSystem.ClaimMailsResultDelegate` | `-` | 收到领取邮件奖励结果后触发 @param UID int @UID @param ItemList table @奖励物品列表 @param ClaimedMailIDs int[] @已领取的邮件ID数组 @param FailedResults table @失败邮件 |
| `UGCMailSystem.ReadMailsResultDelegate` | `-` | 收到标记邮件已阅读结果后触发 @param UID int @UID @param ReadMailIDs int[] @已阅读的邮件ID数组 @param FailedResults table @失败邮件 |
| `UGCMailSystem.DeleteReadMailsResultDelegate` | `-` | 收到删除已读邮件结果后触发 @param UID int @UID @param DeletedMailIDs int[] @已删除的邮件ID数组 @param FailedResults table @失败邮件 |

## Functions

### `IsMailSystemEnabled`

```text
IsMailSystemEnabled() -> boolean
```

获取邮件系统是否开启，PIE下默认开启
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `boolean` | 邮件系统是否开启 |

### `GetMailList`

```text
GetMailList(UID: int) -> UGCMailInfo[]
```

获取指定玩家的邮件列表
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `int` | UID |

**Returns**

| Type | Description |
|---|---|
| `UGCMailInfo[]` | 邮件列表 |

### `GetMailInfo`

```text
GetMailInfo(UID: int, MailID: int) -> UGCMailInfo
```

获取指定玩家的邮件信息
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `int` | UID |
| `MailID` | `int` | 邮件ID |

**Returns**

| Type | Description |
|---|---|
| `UGCMailInfo` | 邮件信息，如果不存在则返回 nil |

### `ClaimMailAward`

```text
ClaimMailAward(UID: int, MailIDs: int[])
```

请求领取指定玩家的邮件奖励
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `int` | UID |
| `MailIDs` | `int[]` | 邮件ID数组 |

### `ReadMail`

```text
ReadMail(UID: int, MailIDs: int[])
```

请求标记指定玩家的邮件已读
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `int` | UID |
| `MailIDs` | `int[]` | 邮件ID数组 |

### `DeleteReadMail`

```text
DeleteReadMail(UID: int, MailIDs: int[])
```

请求删除指定玩家的已读邮件
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `int` | UID |
| `MailIDs` | `int[]` | 邮件ID数组 |

### `PIESendMail`

```text
PIESendMail(UID: int, Title: string, Content: string, ExpireTime: int, Attachments: table)
```

发送邮件, 仅PIE环境有效
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `int` | UID |
| `Title` | `string` | 邮件标题 |
| `Content` | `string` | 邮件内容 |
| `ExpireTime` | `int` | 过期时间 |
| `Attachments` | `table` | 附件 {[ItemID]=Count, ...} |

## Language

`lua`
