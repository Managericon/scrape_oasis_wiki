---
id: "api:cppstruct:FDockTabStyle"
title: "FDockTabStyle"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FDockTabStyle.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FDockTabStyle

Represents the appearance of an SDockTab

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CloseButtonStyle` | `FButtonStyle` | Style used for the close button |
| `NormalBrush` | `FSlateBrush` | Brush used when this tab is in its normal state |
| `ActiveBrush` | `FSlateBrush` | Brush used when this tab is in its active state |
| `ColorOverlayTabBrush` | `FSlateBrush` | Brush used to overlay a given color onto this tab |
| `ColorOverlayIconBrush` | `FSlateBrush` | Brush used to overlay a given color onto this tab |
| `ForegroundBrush` | `FSlateBrush` | Brush used when this tab is in the foreground |
| `HoveredBrush` | `FSlateBrush` | Brush used when this tab is hovered over |
| `ContentAreaBrush` | `FSlateBrush` | Brush used by the SDockingTabStack to draw the content associated with this tab; Documents, Apps, and Tool Panels have different backgrounds |
| `TabWellBrush` | `FSlateBrush` | Brush used by the SDockingTabStack to draw the content associated with this tab; Documents, Apps, and Tool Panels have different backgrounds |
| `TabPadding` | `FMargin` | Padding used around this tab |
| `OverlapWidth` | `float` | The width that this tab will overlap with side-by-side tabs |
| `FlashColor` | `FSlateColor` | Color used when flashing this tab |
