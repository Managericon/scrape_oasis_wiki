---
id: "api:cppstruct:FAssetBundleEntry"
title: "FAssetBundleEntry"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAssetBundleEntry.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAssetBundleEntry

A struct representing a single AssetBundle

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BundleScope` | `FPrimaryAssetId` | Asset this bundle is saved within. This is empty for global bundles, or in the saved bundle info |
| `BundleName` | `FName` | Specific name of this bundle, should be unique for a given scope |
| `BundleAssets` | `TArray < FSoftObjectPath >` | List of string assets contained in this bundle |
