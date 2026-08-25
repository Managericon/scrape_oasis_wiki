---
id: "api:class:UGCGameplayTagSystem"
title: "UGCGameplayTagSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%B7%A5%E5%85%B7%E5%BA%93/UGCGameplayTagSystem.json"
category: "API Wiki/class/和平全局接口/工具库"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCGameplayTagSystem

GameplayTag接口库

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UGCGameplayTagSystem.Tags.PawnState` | `-` | - |

## Functions

### `RequestGameplayTag`

```text
RequestGameplayTag(TagString: string) -> FGameplayTag
```

根据字符串获取FGameplayTag
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagString` | `string` | Tag的字符串 |

**Returns**

| Type | Description |
|---|---|
| `FGameplayTag` | 是否为合法的Tag |

### `IsValidTag`

```text
IsValidTag(Tag: UGCGameplayTag|string|FGameplayTag) -> boolean
```

检查一个Tag是否合法
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Tag` | `UGCGameplayTag\|string\|FGameplayTag` | Tag |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否为合法的Tag |

### `IsUGCGameplayTag`

```text
IsUGCGameplayTag(Tag: UGCGameplayTag) -> boolean
```

检查一个Tag是否是UGCGameplayTag
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Tag` | `UGCGameplayTag` | UGCGameplayTag的lua对象 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否为UGCGameplayTag |

### `MatchesTag`

```text
MatchesTag(TagA: UGCGameplayTag|string|FGameplayTag, TagB: UGCGameplayTag|string|FGameplayTag, bExactMatch: boolean) -> boolean
```

检查TagA是否与TagB匹配
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagA` | `UGCGameplayTag\|string\|FGameplayTag` | Tag |
| `TagB` | `UGCGameplayTag\|string\|FGameplayTag` | Tag |
| `bExactMatch` | `boolean` | 是否精确匹配 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否匹配 |

### `EqualsTag`

```text
EqualsTag(TagA: UGCGameplayTag|string|FGameplayTag, TagB: UGCGameplayTag|string|FGameplayTag) -> boolean
```

检查TagA是否与TagB相等
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagA` | `UGCGameplayTag\|string\|FGameplayTag` | Tag |
| `TagB` | `UGCGameplayTag\|string\|FGameplayTag` | Tag |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否相等 |

### `CreateGameplayTagContainer`

```text
CreateGameplayTagContainer() -> FGameplayTagContainer
```

创建一个空的FFGameplayTagContainer
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `FGameplayTagContainer` | 空的FGameplayTagContainer |

### `CreateGameplayTagContainerFromTag`

```text
CreateGameplayTagContainerFromTag(SingleTag: UGCGameplayTag|string|FGameplayTag) -> FGameplayTagContainer
```

创建一个包含指定FGameplayTag的FGameplayTagContainer
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SingleTag` | `UGCGameplayTag\|string\|FGameplayTag` | 传入FGameplayTagContainer中的FGameplayTag |

**Returns**

| Type | Description |
|---|---|
| `FGameplayTagContainer` | 包含传入FGameplayTag的GameplayTagContainer |

### `CreateGameplayTagContainerFromArray`

```text
CreateGameplayTagContainerFromArray(GameplayTags: FGameplayTag[]) -> FGameplayTagContainer
```

创建一个包含一组FGameplayTag的FGameplayTagContainer
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GameplayTags` | `FGameplayTag[]` | 传入FGameplayTagContainer中的FGameplayTags |

**Returns**

| Type | Description |
|---|---|
| `FGameplayTagContainer` | 包含传入FGameplayTags的GameplayTagContainer |

### `AddGameplayTagToContainer`

```text
AddGameplayTagToContainer(TagContainer: FGameplayTagContainer, Tag: FGameplayTag)
```

将单个FGameplayTag添加到传入的FGameplayTagContainer中
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagContainer` | `FGameplayTagContainer` | 要追加到的FGameplayTagContainer |
| `Tag` | `FGameplayTag` | 要添加到FGameplayTagContainer中的FGameplayTag |

### `RemoveGameplayTagFromContainer`

```text
RemoveGameplayTagFromContainer(TagContainer: FGameplayTagContainer, Tag: FGameplayTag) -> boolean
```

从传入的FGameplayTagContainer中移除单个FGameplayTag，若找到并移除则返回 true ，否则返回 false
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagContainer` | `FGameplayTagContainer` | 要从中移除的FGameplayTagContainer |
| `Tag` | `FGameplayTag` | 要从FGameplayTagContainer中移除的FGameplayTag |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否成功移除 |

### `HasTag`

```text
HasTag(TagContainer: FGameplayTagContainer, Tag: FGameplayTag, bExactMatch: boolean) -> boolean
```

检查FGameplayTagContainer是否包含特定的FGameplayTag
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagContainer` | `FGameplayTagContainer` | 要从中查找指定FGameplayTag的FGameplayTagContainer |
| `Tag` | `FGameplayTag` | 要从FGameplayTagContainer中检查的FGameplayTag |
| `bExactMatch` | `boolean` | 是否精确匹配 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否包含Tag |

## Language

`lua`
