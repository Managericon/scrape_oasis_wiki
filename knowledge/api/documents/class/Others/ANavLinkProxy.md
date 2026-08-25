---
id: "api:class:ANavLinkProxy"
title: "ANavLinkProxy"
source: "https://developer.gp.qq.com/api/class/detail/Others/ANavLinkProxy.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ANavLinkProxy

## Inheritance

`AActor` -> `INavLinkHostInterface` -> `INavRelevantInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PointLinks` | `TArray < FNavigationLink >` | Navigation links (point to point) added to navigation data |
| `SegmentLinks` | `TArray < FNavigationSegmentLink >` | Navigation links (segment to segment) added to navigation data<br>		@todo hidden from use until we fix segment links. Not really working now |
| `SmartLinkComp` | `UNavLinkCustomComponent *` | Smart link: can affect path following |
| `bSmartLinkIsRelevant` | `bool` | Smart link: toggle relevancy |
| `EdRenderComp` | `UNavLinkRenderingComponent *` | Editor Preview |
| `SpriteComponent` | `UBillboardComponent *` | - |

## Functions

### `ReceiveSmartLinkReached`

```text
ReceiveSmartLinkReached(Agent: AActor *, Destination: FVector &) -> void
```

called when agent reaches smart link during path following, use ResumePathFollowing() to give control back

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Agent` | `AActor *` | - |
| `Destination` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResumePathFollowing`

```text
ResumePathFollowing(Agent: AActor *) -> void
```

resume normal path following

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Agent` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsSmartLinkEnabled`

```text
IsSmartLinkEnabled() -> bool
```

check if smart link is enabled

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetSmartLinkEnabled`

```text
SetSmartLinkEnabled(bEnabled: bool) -> void
```

change state of smart link

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnabled` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HasMovingAgents`

```text
HasMovingAgents() -> bool
```

check if any agent is moving through smart link right now

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Delegates

### `OnSmartLinkReached`

```text
OnSmartLinkReached(MovingActor: AActor*, DestinationPoint: const FVector&) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MovingActor` | `AActor*` | - |
| `DestinationPoint` | `const FVector&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
