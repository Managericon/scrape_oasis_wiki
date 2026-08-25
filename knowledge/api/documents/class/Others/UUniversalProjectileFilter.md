---
id: "api:class:UUniversalProjectileFilter"
title: "UUniversalProjectileFilter"
source: "https://developer.gp.qq.com/api/class/detail/Others/UUniversalProjectileFilter.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UUniversalProjectileFilter

过滤器

## Inheritance

`UObject`

## Events

### `Filter`

```text
Filter(InActor: AActor *, Causer: AActor *, Instigator: AController *) -> bool
```

过滤器的过滤方法
	 生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor *` | 当前判断过滤的对象 |
| `Causer` | `AActor *` | 发起过滤的对象（可能为抛体，法术场等） |
| `Instigator` | `AController *` | 发起过滤的对象的Controller（一般在服务端使用） |

**Returns**

| Type | Description |
|---|---|
| `bool` | bool 过滤结果 |

## Language

`cpp`
