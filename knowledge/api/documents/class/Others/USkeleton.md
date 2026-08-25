---
id: "api:class:USkeleton"
title: "USkeleton"
source: "https://developer.gp.qq.com/api/class/detail/Others/USkeleton.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# USkeleton

USkeleton : that links between mesh and animation
 		- Bone hierarchy for animations
 		- Bonetrack linkup between mesh and animation
 		- Retargetting related
 		- Mirror table

## Inheritance

`UObject` -> `IInterface_AssetUserData`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoneTree` | `TArray < struct FBoneNode >` | Skeleton bone tree - each contains name and parent index |
| `OverrideBoneTranslationRetargetingModeConfigMap` | `TMap < FName , FOverrideBoneTranslationRetargetingModeConfig >` | - |
| `RefLocalPoses_DEPRECATED` | `TArray < FTransform >` | Reference skeleton poses in local space |
| `VirtualBoneGuid` | `FGuid` | Guid for virtual bones.<br>	   Separate so that we don't have to dirty the original guid when only changing virtual bones |
| `VirtualBones` | `TArray < FVirtualBone >` | Array of this skeletons virtual bones. These are new bones are links between two existing bones<br>	  and are baked into all the skeletons animations |
| `CompatibleSkeletons` | `TArray < TSoftObjectPtr < USkeleton > >` | The list of compatible skeletons.<br>	  This is an array of TSoftObjectPtr in order to prevent all skeletons to be loaded, as we only want to load things on demand.<br>	  As this is EditAnywhere and an array of TSoftObjectPtr, checking validity of pointers is needed. |
| `MultiSkeletonNameMap` | `TMap < TSoftObjectPtr < USkeleton > , FCustomSkeletonName >` | - |
| `CustomSkeletonNameMap` | `TMap < FName , FName >` | key名称对应其他骨骼的名字 做骨骼兼容时 会被当作本骨骼的value使用 |
| `SkeletonNotOffsetName` | `TMap < FName , FBoneOffset >` | 是否要在骨骼兼容后不应用offset |
| `RefBoneNames` | `TArray < FName >` | 该名称对应的骨骼 做骨骼兼容时 只会应用旋转 |
| `ExcludeBoneInfos` | `TArray < FSkinWeightInfoForFPP >` | 该名称对应的骨骼 做骨骼兼容时排除该骨骼的信息 |
| `ExcludeBoneNameForAvatar` | `TArray < FName >` | - |
| `bIsFPPSkeleton` | `bool` | - |
| `Sockets` | `TArray < USkeletalMeshSocket * >` | Array of named socket locations, set up in editor and used as a shortcut instead of specifying <br>	 	everything explicitly to AttachComponent in the SkeletalMeshComponent. |
| `SmartNames` | `FSmartNameContainer` | - |
| `BlendProfiles` | `TArray < UBlendProfile * >` | List of blend profiles available in this skeleton |
| `SlotGroups` | `TArray < FAnimSlotGroup >` | Slot Groups |
| `AssetUserData` | `TArray < UAssetUserData * >` | Array of user data stored with the asset |
| `bSkipGenerateGuidWhenSkeletonHierarchyAdd` | `bool` | 当骨架增加骨骼时，跳过 Guid 更新和 DDC 重新构建 |
| `PreviewSkeletalMesh` | `TSoftObjectPtr < USkeletalMesh >` | The default skeletal mesh to use when previewing this skeleton |
| `AdditionalPreviewSkeletalMeshes` | `TSoftObjectPtr < UDataAsset >` | The additional skeletal meshes to use when previewing this skeleton |
| `RigConfig` | `FRigConfiguration` | - |
| `AnimationNotifies` | `TArray < FName >` | AnimNotifiers that has been created. Right now there is no delete step for this, but in the future we'll supply delete |
| `PreviewAttachedAssetContainer` | `FPreviewAssetAttachContainer` | Attached assets component for this skeleton |

## Functions

### `AddCompatibleSkeleton`

```text
AddCompatibleSkeleton(SourceSkeleton: USkeleton *) -> ENGINE_API void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceSkeleton` | `USkeleton *` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `AddCompatibleSkeletonSoft`

```text
AddCompatibleSkeletonSoft(SourceSkeleton: TSoftObjectPtr < USkeleton > &) -> ENGINE_API void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceSkeleton` | `TSoftObjectPtr < USkeleton > &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

## Language

`cpp`
