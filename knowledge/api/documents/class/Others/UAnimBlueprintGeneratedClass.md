---
id: "api:class:UAnimBlueprintGeneratedClass"
title: "UAnimBlueprintGeneratedClass"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAnimBlueprintGeneratedClass.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAnimBlueprintGeneratedClass

## Inheritance

`UBlueprintGeneratedClass` -> `IAnimClassInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BakedStateMachines` | `TArray < FBakedAnimationStateMachine >` | - |
| `TargetSkeleton` | `USkeleton *` | Target skeleton for this blueprint class |
| `AnimNotifies` | `TArray < FAnimNotifyEvent >` | A list of anim notifies that state machines (or anything else) may reference |
| `RootAnimNodeIndex` | `int32` | - |
| `OrderedSavedPoseIndices` | `TArray < int32 >` | - |
| `SyncGroupNames` | `TArray < FName >` | - |
| `bFMPrecomputeDone` | `bool` | 预计算标记：编辑器编译蓝图时（PostCompile）扫描并写入，打包后序列化到.uasset，<br>	   运行时加载后直接读取正确值，无需再次扫描。<br>	   编辑器未编译时为false，懒初始化逻辑会在首次CollectFunctionModule时兜底扫描。 |
| `bHasAnyFunctionModule` | `bool` | 预计算缓存：该动画蓝图类（含父类继承链）是否含有任何FunctionModule属性。<br>	   仅在bFMPrecomputeDone为true时有效。打包后序列化到.uasset，运行时直接使用。 |

## Language

`cpp`
