---
id: "api:class:UAsyncTaskDownloadImage"
title: "UAsyncTaskDownloadImage"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAsyncTaskDownloadImage.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAsyncTaskDownloadImage

## Inheritance

`UBlueprintAsyncActionBase`

## Functions

### `DownloadImage`

```text
DownloadImage(URL: FString) -> UAsyncTaskDownloadImage *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `URL` | `FString` | - |

**Returns**

| Type | Description |
|---|---|
| `UAsyncTaskDownloadImage *` | - |

## Delegates

### `OnSuccess`

```text
OnSuccess(Texture: UTexture2DDynamic*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Texture` | `UTexture2DDynamic*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnFail`

```text
OnFail(Texture: UTexture2DDynamic*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Texture` | `UTexture2DDynamic*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
