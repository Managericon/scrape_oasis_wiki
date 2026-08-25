---
id: "api:class:UBlueprintGameplayTagLibrary"
title: "UBlueprintGameplayTagLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBlueprintGameplayTagLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBlueprintGameplayTagLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `MatchesTag`

```text
MatchesTag(TagOne: FGameplayTag, TagTwo: FGameplayTag, bExactMatch: bool) -> bool
```

Determine if TagOne matches against TagTwo

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagOne` | `FGameplayTag` | Tag to check for match |
| `TagTwo` | `FGameplayTag` | Tag to check match against |
| `bExactMatch` | `bool` | If true, the tag has to be exactly present, if false then TagOne will include it's parent tags while matching |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if TagOne matches TagTwo |

### `MatchesAnyTags`

```text
MatchesAnyTags(TagOne: FGameplayTag, OtherContainer: FGameplayTagContainer &, bExactMatch: bool) -> GAMEPLAYTAGS_API bool
```

Determine if TagOne matches against any tag in OtherContainer

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagOne` | `FGameplayTag` | Tag to check for match |
| `OtherContainer` | `FGameplayTagContainer &` | Container to check against. |
| `bExactMatch` | `bool` | If true, the tag has to be exactly present, if false then TagOne will include it's parent tags while matching |

**Returns**

| Type | Description |
|---|---|
| `GAMEPLAYTAGS_API bool` | True if TagOne matches any tags explicitly present in OtherContainer |

### `EqualEqual_GameplayTag`

```text
EqualEqual_GameplayTag(A: FGameplayTag, B: FGameplayTag) -> bool
```

Returns true if the values are equal (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FGameplayTag` | - |
| `B` | `FGameplayTag` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_GameplayTag`

```text
NotEqual_GameplayTag(A: FGameplayTag, B: FGameplayTag) -> bool
```

Returns true if the values are not equal (A != B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FGameplayTag` | - |
| `B` | `FGameplayTag` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsGameplayTagValid`

```text
IsGameplayTagValid(GameplayTag: FGameplayTag) -> bool
```

Returns true if the passed in gameplay tag is non-null

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GameplayTag` | `FGameplayTag` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetTagName`

```text
GetTagName(GameplayTag: FGameplayTag &) -> FName
```

Returns FName of this tag

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GameplayTag` | `FGameplayTag &` | - |

**Returns**

| Type | Description |
|---|---|
| `FName` | - |

### `MakeLiteralGameplayTag`

```text
MakeLiteralGameplayTag(Value: FGameplayTag) -> FGameplayTag
```

Creates a literal FGameplayTag

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `FGameplayTag` | - |

**Returns**

| Type | Description |
|---|---|
| `FGameplayTag` | - |

### `GetNumGameplayTagsInContainer`

```text
GetNumGameplayTagsInContainer(TagContainer: FGameplayTagContainer &) -> int32
```

Get the number of gameplay tags in the specified container

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagContainer` | `FGameplayTagContainer &` | Tag container to get the number of tags from |

**Returns**

| Type | Description |
|---|---|
| `int32` | The number of tags in the specified container |

### `HasTag`

```text
HasTag(TagContainer: FGameplayTagContainer &, Tag: FGameplayTag, bExactMatch: bool) -> bool
```

Check if the tag container has the specified tag

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagContainer` | `FGameplayTagContainer &` | Container to check for the tag |
| `Tag` | `FGameplayTag` | Tag to check for in the container |
| `bExactMatch` | `bool` | If true, the tag has to be exactly present, if false then TagContainer will include it's parent tags while matching |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the container has the specified tag, false if it does not |

### `HasAnyTags`

```text
HasAnyTags(TagContainer: FGameplayTagContainer &, OtherContainer: FGameplayTagContainer &, bExactMatch: bool) -> bool
```

Check if the specified tag container has ANY of the tags in the other container

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagContainer` | `FGameplayTagContainer &` | Container to check if it matches any of the tags in the other container |
| `OtherContainer` | `FGameplayTagContainer &` | Container to check against. |
| `bExactMatch` | `bool` | If true, the tag has to be exactly present, if false then TagContainer will include it's parent tags while matching |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the container has ANY of the tags in the other container |

### `HasAllTags`

```text
HasAllTags(TagContainer: FGameplayTagContainer &, OtherContainer: FGameplayTagContainer &, bExactMatch: bool) -> bool
```

Check if the specified tag container has ALL of the tags in the other container

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagContainer` | `FGameplayTagContainer &` | Container to check if it matches all of the tags in the other container |
| `OtherContainer` | `FGameplayTagContainer &` | Container to check against. If this is empty, the check will succeed |
| `bExactMatch` | `bool` | If true, the tag has to be exactly present, if false then TagContainer will include it's parent tags while matching |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the container has ALL of the tags in the other container |

### `DoesContainerMatchTagQuery`

```text
DoesContainerMatchTagQuery(TagContainer: FGameplayTagContainer &, TagQuery: FGameplayTagQuery &) -> bool
```

Check if the specified tag container matches the given Tag Query

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagContainer` | `FGameplayTagContainer &` | Container to check if it matches all of the tags in the other container |
| `TagQuery` | `FGameplayTagQuery &` | Query to match against |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the container matches the query, false otherwise. |

### `GetAllActorsOfClassMatchingTagQuery`

```text
GetAllActorsOfClassMatchingTagQuery(WorldContextObject: UObject *, ActorClass: TSubclassOf < AActor >, GameplayTagQuery: FGameplayTagQuery &, OutActors: TArray < AActor * > &) -> void
```

Get an array of all actors of a specific class (or subclass of that class) which match the specified gameplay tag query.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `ActorClass` | `TSubclassOf < AActor >` | Class of actors to fetch |
| `GameplayTagQuery` | `FGameplayTagQuery &` | Query to match against |
| `OutActors` | `TArray < AActor * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddGameplayTag`

```text
AddGameplayTag(TagContainer: FGameplayTagContainer &, Tag: FGameplayTag) -> void
```

Adds a single tag to the passed in tag container

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagContainer` | `FGameplayTagContainer &` | - |
| `Tag` | `FGameplayTag` | The tag to add to the container |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveGameplayTag`

```text
RemoveGameplayTag(TagContainer: FGameplayTagContainer &, Tag: FGameplayTag) -> bool
```

Remove a single tag from the passed in tag container, returns true if found

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagContainer` | `FGameplayTagContainer &` | - |
| `Tag` | `FGameplayTag` | The tag to add to the container |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `AppendGameplayTagContainers`

```text
AppendGameplayTagContainers(InOutTagContainer: FGameplayTagContainer &, InTagContainer: FGameplayTagContainer &) -> void
```

Appends all tags in the InTagContainer to InOutTagContainer

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOutTagContainer` | `FGameplayTagContainer &` | The container that will be appended too. |
| `InTagContainer` | `FGameplayTagContainer &` | The container to append. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EqualEqual_GameplayTagContainer`

```text
EqualEqual_GameplayTagContainer(A: FGameplayTagContainer &, B: FGameplayTagContainer &) -> bool
```

Returns true if the values are equal (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FGameplayTagContainer &` | - |
| `B` | `FGameplayTagContainer &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_GameplayTagContainer`

```text
NotEqual_GameplayTagContainer(A: FGameplayTagContainer &, B: FGameplayTagContainer &) -> bool
```

Returns true if the values are not equal (A != B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FGameplayTagContainer &` | - |
| `B` | `FGameplayTagContainer &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `MakeLiteralGameplayTagContainer`

```text
MakeLiteralGameplayTagContainer(Value: FGameplayTagContainer) -> FGameplayTagContainer
```

Creates a literal FGameplayTagContainer

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `FGameplayTagContainer` | - |

**Returns**

| Type | Description |
|---|---|
| `FGameplayTagContainer` | - |

### `MakeGameplayTagContainerFromArray`

```text
MakeGameplayTagContainerFromArray(GameplayTags: TArray < FGameplayTag > &) -> FGameplayTagContainer
```

Creates a FGameplayTagContainer from the array of passed in tags

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GameplayTags` | `TArray < FGameplayTag > &` | - |

**Returns**

| Type | Description |
|---|---|
| `FGameplayTagContainer` | - |

### `MakeGameplayTagContainerFromTag`

```text
MakeGameplayTagContainerFromTag(SingleTag: FGameplayTag) -> FGameplayTagContainer
```

Creates a FGameplayTagContainer containing a single tag

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SingleTag` | `FGameplayTag` | - |

**Returns**

| Type | Description |
|---|---|
| `FGameplayTagContainer` | - |

### `BreakGameplayTagContainer`

```text
BreakGameplayTagContainer(GameplayTagContainer: FGameplayTagContainer &, GameplayTags: TArray < FGameplayTag > &) -> void
```

Breaks tag container into explicit array of tags

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GameplayTagContainer` | `FGameplayTagContainer &` | - |
| `GameplayTags` | `TArray < FGameplayTag > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MakeGameplayTagQuery`

```text
MakeGameplayTagQuery(TagQuery: FGameplayTagQuery) -> FGameplayTagQuery
```

Creates a literal FGameplayTagQuery

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagQuery` | `FGameplayTagQuery` | value to set the FGameplayTagQuery to |

**Returns**

| Type | Description |
|---|---|
| `FGameplayTagQuery` | The literal FGameplayTagQuery |

### `HasAllMatchingGameplayTags`

```text
HasAllMatchingGameplayTags(TagContainerInterface: TScriptInterface < IGameplayTagAssetInterface >, OtherContainer: FGameplayTagContainer &) -> bool
```

Check Gameplay tags in the interface has all of the specified tags in the tag container (expands to include parents of asset tags)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagContainerInterface` | `TScriptInterface < IGameplayTagAssetInterface >` | An Interface to a tag container |
| `OtherContainer` | `FGameplayTagContainer &` | A Tag Container |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the tagcontainer in the interface has all the tags inside the container. |

### `DoesTagAssetInterfaceHaveTag`

```text
DoesTagAssetInterfaceHaveTag(TagContainerInterface: TScriptInterface < IGameplayTagAssetInterface >, Tag: FGameplayTag) -> bool
```

Check if the specified tag container has the specified tag, using the specified tag matching types

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagContainerInterface` | `TScriptInterface < IGameplayTagAssetInterface >` | An Interface to a tag container |
| `Tag` | `FGameplayTag` | Tag to check for in the container |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the container has the specified tag, false if it does not |

### `NotEqual_TagTag`

```text
NotEqual_TagTag(A: FGameplayTag, B: FString) -> bool
```

Checks if a gameplay tag's name and a string are not equal to one another

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FGameplayTag` | - |
| `B` | `FString` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_TagContainerTagContainer`

```text
NotEqual_TagContainerTagContainer(A: FGameplayTagContainer, B: FString) -> bool
```

Checks if a gameplay tag containers's name and a string are not equal to one another

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FGameplayTagContainer` | - |
| `B` | `FString` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetDebugStringFromGameplayTagContainer`

```text
GetDebugStringFromGameplayTagContainer(TagContainer: FGameplayTagContainer &) -> FString
```

Returns an FString listing all of the gameplay tags in the tag container for debugging purposes.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagContainer` | `FGameplayTagContainer &` | The tag container to get the debug string from. |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `GetDebugStringFromGameplayTag`

```text
GetDebugStringFromGameplayTag(GameplayTag: FGameplayTag) -> FString
```

Returns an FString representation of a gameplay tag for debugging purposes.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GameplayTag` | `FGameplayTag` | The tag to get the debug string from. |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

## Language

`cpp`
