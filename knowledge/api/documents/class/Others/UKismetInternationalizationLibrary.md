---
id: "api:class:UKismetInternationalizationLibrary"
title: "UKismetInternationalizationLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UKismetInternationalizationLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UKismetInternationalizationLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `SetCurrentCulture`

```text
SetCurrentCulture(Culture: FString &, SaveToConfig: bool) -> bool
```

Set the current culture.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Culture` | `FString &` | The culture to set, as an IETF language tag (eg, "zh-Hans-CN"). |
| `SaveToConfig` | `bool` | If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload. |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the culture was set, false otherwise. |

### `GetCurrentCulture`

```text
GetCurrentCulture() -> FString
```

Get the current culture as an IETF language tag:
	   - A two-letter ISO 639-1 language code (eg, "zh").
	   - An optional four-letter ISO 15924 script code (eg, "Hans").
	   - An optional two-letter ISO 3166-1 country code (eg, "CN").

**Returns**

| Type | Description |
|---|---|
| `FString` | The culture as an IETF language tag (eg, "zh-Hans-CN"). |

### `SetCurrentLanguage`

```text
SetCurrentLanguage(Culture: FString &, SaveToConfig: bool) -> bool
```

Set only the current language (for localization).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Culture` | `FString &` | The language to set, as an IETF language tag (eg, "zh-Hans-CN"). |
| `SaveToConfig` | `bool` | If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload. |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the language was set, false otherwise. |

### `GetCurrentLanguage`

```text
GetCurrentLanguage() -> FString
```

Get the current language (for localization) as an IETF language tag:
	   - A two-letter ISO 639-1 language code (eg, "zh").
	   - An optional four-letter ISO 15924 script code (eg, "Hans").
	   - An optional two-letter ISO 3166-1 country code (eg, "CN").

**Returns**

| Type | Description |
|---|---|
| `FString` | The language as an IETF language tag (eg, "zh-Hans-CN"). |

### `SetCurrentLocale`

```text
SetCurrentLocale(Culture: FString &, SaveToConfig: bool) -> bool
```

Set only the current locale (for internationalization).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Culture` | `FString &` | The locale to set, as an IETF language tag (eg, "zh-Hans-CN"). |
| `SaveToConfig` | `bool` | If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload. |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the locale was set, false otherwise. |

### `GetCurrentLocale`

```text
GetCurrentLocale() -> FString
```

Get the current locale (for internationalization) as an IETF language tag:
	   - A two-letter ISO 639-1 language code (eg, "zh").
	   - An optional four-letter ISO 15924 script code (eg, "Hans").
	   - An optional two-letter ISO 3166-1 country code (eg, "CN").

**Returns**

| Type | Description |
|---|---|
| `FString` | The locale as an IETF language tag (eg, "zh-Hans-CN"). |

### `SetCurrentLanguageAndLocale`

```text
SetCurrentLanguageAndLocale(Culture: FString &, SaveToConfig: bool) -> bool
```

Set the current language (for localization) and locale (for internationalization).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Culture` | `FString &` | The language and locale to set, as an IETF language tag (eg, "zh-Hans-CN"). |
| `SaveToConfig` | `bool` | If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload. |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the language and locale were set, false otherwise. |

### `SetCurrentAssetGroupCulture`

```text
SetCurrentAssetGroupCulture(AssetGroup: FName, Culture: FString &, SaveToConfig: bool) -> bool
```

Set the given asset group category culture from an IETF language tag (eg, "zh-Hans-CN").

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetGroup` | `FName` | The asset group to set the culture for. |
| `Culture` | `FString &` | The culture to set, as an IETF language tag (eg, "zh-Hans-CN"). |
| `SaveToConfig` | `bool` | If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload. |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the culture was set, false otherwise. |

### `GetCurrentAssetGroupCulture`

```text
GetCurrentAssetGroupCulture(AssetGroup: FName) -> FString
```

Get the given asset group category culture.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetGroup` | `FName` | The asset group to get the culture for. |

**Returns**

| Type | Description |
|---|---|
| `FString` | The culture as an IETF language tag (eg, "zh-Hans-CN"). |

### `ClearCurrentAssetGroupCulture`

```text
ClearCurrentAssetGroupCulture(AssetGroup: FName, SaveToConfig: bool) -> void
```

Clear the given asset group category culture.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetGroup` | `FName` | The asset group to clear the culture for. |
| `SaveToConfig` | `bool` | If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
