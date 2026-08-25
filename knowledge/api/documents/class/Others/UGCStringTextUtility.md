---
id: "api:class:UGCStringTextUtility"
title: "UGCStringTextUtility"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGCStringTextUtility.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCStringTextUtility

文本系统接口库

## Functions

### `ExportText`

```text
ExportText(Object: string) -> string
```

导出对象文本，会根据传入的对象类型打印关键信息

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `string` | 文本对象 |

**Returns**

| Type | Description |
|---|---|
| `string` | 文本字符串 |

### `TrimStartOrEnd`

```text
TrimStartOrEnd(InStr: string, TrimStart: boolean, TrimEnd: boolean) -> string
```

修剪字符串的起始和结尾，根据传入的TrimStart和TrimEnd去除字符串头尾的空白字符

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStr` | `string` | 字符串 |
| `TrimStart` | `boolean` | 是否修剪起始 |
| `TrimEnd` | `boolean` | 是否修剪结尾 |

**Returns**

| Type | Description |
|---|---|
| `string` | 修剪后的字符串 |

### `SplitToArray`

```text
SplitToArray(InStr: string, Separator: string) -> table
```

将字符串按照分隔符分割成数组

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStr` | `string` | 字符串 |
| `Separator` | `string` | 分隔符 |

**Returns**

| Type | Description |
|---|---|
| `table` | 数组 |

### `StartsWith`

```text
StartsWith(InStr: string, InPrefix: string, SearchCase: ESearchCase) -> boolean
```

判断字符串是否以指定的前缀开头

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStr` | `string` | 字符串 |
| `InPrefix` | `string` | 前缀 |
| `SearchCase` | `ESearchCase` | 是否区分大小写 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否以指定的前缀开头 |

### `EndWith`

```text
EndWith(InStr: string, InSuffix: string, SearchCase: ESearchCase) -> boolean
```

判断字符串是否以指定的后缀结尾

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStr` | `string` | 字符串 |
| `InSuffix` | `string` | 后缀 |
| `SearchCase` | `ESearchCase` | 是否区分大小写 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否以指定的后缀结尾 |

### `InsertIntoString`

```text
InsertIntoString(SourceStr: string, Content: string, Position: number) -> string
```

在字符串的指定位置插入内容

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceStr` | `string` | 源字符串 |
| `Content` | `string` | 插入内容 |
| `Position` | `number` | 插入位置 |

**Returns**

| Type | Description |
|---|---|
| `string` | 字符串 |

### `JoinArrayIntoString`

```text
JoinArrayIntoString(InStrArray: table, Separator: string) -> string
```

将字符串数组连接成字符串

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStrArray` | `table` | 字符串数组 |
| `Separator` | `string` | 分隔符 |

**Returns**

| Type | Description |
|---|---|
| `string` | 字符串 |

### `SplitToCharArray`

```text
SplitToCharArray(InStr: string) -> table
```

将字符串分割成字符数组

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStr` | `string` | 字符串 |

**Returns**

| Type | Description |
|---|---|
| `table` | 字符数组 |

### `ComposedOfDigits`

```text
ComposedOfDigits(InStr: string) -> boolean
```

判断字符串是否由数字组成

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStr` | `string` | 字符串 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否由数字组成 |

### `LeftChop`

```text
LeftChop(InStr: string, Count: number) -> string
```

截断字符串的前n个字符

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStr` | `string` | 字符串 |
| `Count` | `number` | 字符数 |

**Returns**

| Type | Description |
|---|---|
| `string` | 字符串 |

### `LeftPad`

```text
LeftPad(InStr: string, StrLen: number) -> string
```

在字符串的左侧填充空白字符使得字符串长度达到指定的长度

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStr` | `string` | 字符串 |
| `StrLen` | `number` | 指定的长度 |

**Returns**

| Type | Description |
|---|---|
| `string` | 字符串 |

### `RightChop`

```text
RightChop(InStr: string, Count: number) -> string
```

截断字符串的后n个字符

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStr` | `string` | 字符串 |
| `Count` | `number` | 字符数 |

**Returns**

| Type | Description |
|---|---|
| `string` | 字符串 |

### `RightPad`

```text
RightPad(InStr: string, StrLen: number) -> string
```

在字符串的右侧填充空白字符使得字符串长度达到指定的长度

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStr` | `string` | 字符串 |
| `StrLen` | `number` | 指定的长度 |

**Returns**

| Type | Description |
|---|---|
| `string` | 字符串 |

### `LogTree`

```text
LogTree(Desc: string, Var: any)
```

打印变量,特别是对table类型做树形输出,仅DEV打印

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Desc` | `string` | 变量描述 |
| `Var` | `any` | 要输出的变量,可以是任何类型table, bool, number, nil |

## Language

`lua`
