---
id: "api:class:UAnimInstance"
title: "UAnimInstance"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAnimInstance.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAnimInstance

## Inheritance

`UObject` -> `IObjectPoolInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CurrentSkeleton` | `USkeleton *` | This is used to extract animation. If Mesh exists, this will be overwritten by Mesh->Skeleton |
| `RootMotionMode` | `TEnumAsByte < ERootMotionMode :: Type >` | - |
| `bRunUpdatesInWorkerThreads_DEPRECATED` | `bool` | DEPRECATED: No longer used.<br>	  Allows this anim instance to update its native update, blend tree, montages and asset players on<br>	  a worker thread. this requires certain conditions to be met:<br>	  - All access of variables in the blend tree should be a direct access of a member variable<br>	  - No BlueprintUpdateAnimation event should be used (i.e. the event graph should be empty). Only native update is permitted. |
| `bCanUseParallelUpdateAnimation_DEPRECATED` | `bool` | DEPRECATED: No longer used.<br>	  Whether we can use parallel updates for our animations.<br>	  Conditions affecting this include:<br>	  - Use of BlueprintUpdateAnimation<br>	  - Use of non 'fast-path' EvaluateGraphExposedInputs in the node graph |
| `bUseMultiThreadedAnimationUpdate` | `bool` | Allows this anim instance to update its native update, blend tree, montages and asset players on<br>	  a worker thread. This flag is propagated from the UAnimBlueprint to this instance by the compiler.<br>	  The compiler will attempt to pick up any issues that may occur with threaded update.<br>	  For updates to run in multiple threads both this flag and the project setting "Allow Multi Threaded<br>	  Animation Update" should be set. |
| `bWarnAboutBlueprintUsage_DEPRECATED` | `bool` | Selecting this option will cause the compiler to emit warnings whenever a call into Blueprint<br>	  is made from the animation graph. This can help track down optimizations that need to be made. |
| `bBlueprintSkipUpdate` | `bool` | - |
| `bUseBlueprintUpdateAnimation` | `uint8` | - |
| `bUseBlueprintPostEvaluateAnimation` | `uint8` | - |
| `AnimAssets_NoGCRef` | `TMap < int64 , UAnimationAsset * >` | - |
| `bQueueMontageEvents` | `bool` | True when Montages are being ticked, and Montage Events should be queued.<br>	  When Montage are being ticked, we queue AnimNotifies and Events. We trigger notifies first, then Montage events. |
| `ForbiddenPlayMontageSlot` | `TArray < FString >` | - |
| `ActiveAnimNotifyState` | `TArray < FAnimNotifyEvent >` | Currently Active AnimNotifyState, stored as a copy of the event as we need to<br>		is removed correctly. |
| `bNeedUpdateNotAttributeCurve` | `bool` | 此动画蓝图是否需要更新非Attribute的Curve数据 |
| `RefCachedSubAnimInstances` | `TArray < UAnimInstance * >` | - |
| `bIsOnlyMasterTriggerNotify` | `bool` | - |
| `bIsMaster` | `bool` | - |
| `bDynamicDisableBoneRetarget` | `bool` | - |
| `CopyPoseFromSkelComp` | `USkeletalMeshComponent *` | - |
| `BoneRetargetSource` | `FName` | - |
| `bUseBoneStateDirtyFeature` | `bool` | - |
| `bBoneStateDirty` | `bool` | - |
| `C_InverseRetargetIgnoreBoneList` | `TArray < int32 >` | - |
| `C_IgnoreRetargetBoneList` | `TArray < FName >` | - |
| `FollowedAnimInstance` | `UAnimInstance *` | 记录被跟随者的动画实例   当该指针为nullptr时，代表启用了自身 Proxy 的 Follow 轨道(即FollowGroupArrays开始记录) |
| `FollowerAnimInstances` | `TArray < TWeakObjectPtr < UAnimInstance > >` | - |
| `ParentAnimInstance` | `TWeakObjectPtr < UAnimInstance >` | - |
| `SubAnimInstances` | `TArray < TWeakObjectPtr < UAnimInstance > >` | - |
| `SubAnimInstancesTempRef` | `TArray < UAnimInstance * >` | - |
| `CachedSwitchNotifySequence` | `TArray < UAnimSequenceBase * >` | - |
| `CachedBoneTransformInfoIndex` | `int64` | - |
| `CachedBoneTransformMapAsync` | `TMap < FName , FCachedBoneTransformInfo >` | - |
| `CachedBoneTransformMapInGame` | `TMap < FName , FCachedBoneTransformInfo >` | - |
| `bIsInPoseUpdate` | `bool` | - |
| `bEnableBoneCacheInGameThread` | `bool` | - |
| `bEnableFastPathExposedNodeTree` | `bool` | - |
| `UpdateConditions` | `TArray < UAnimInstanceUpdateCondition * >` | - |
| `bCheckUpdateConditionResult` | `bool` | - |
| `bEnableAnimBlueprintSkeletonDifferFromMeshSkeleton` | `bool` | - |
| `bEnableFilterForceTriggerNotifyWhenMontageJumpTick` | `bool` | - |
| `MultiSubInstanceTransferDefaultPoseIndex` | `int32` | - |
| `bEnableTriggerAnimNotify` | `bool` | - |
| `InitNodeSourcePropertyLookupTable` | `TMap < FName , UProperty * >` | - |
| `bParentPoseOverride` | `bool` | - |
| `bAutoCopyPose` | `bool` | - |
| `bHasAvatarSlotEvent` | `bool` | - |
| `bRestoreSlotVar` | `bool` | - |
| `bSkipSlotRelevanceCheckForNotifies` | `bool` | - |
| `bEnableAsyncAnimInstance` | `bool` | - |
| `bCanCopyRequiredBones` | `bool` | - |
| `RecordFileName` | `FString` | 回放的录制文件名 |
| `TotalFrames` | `int32` | 总帧数 |
| `CurrentFrame` | `int32` | 当前帧号 |
| `bIsPaused` | `bool` | 暂停 |
| `bRestoreErrorPending` | `bool` | 是否有待游戏线程处理的回放错误（由 ParallelRestoreAnimation 在工作线程设置） |
| `PostCompileValidationClassName` | `FSoftClassPath` | Name of Class to do Post Compile Validation.<br>	 See Class UAnimBlueprintPostCompileValidation. |
| `BoneRetargetBaseRefMesh` | `USkeletalMesh *` | - |

## Functions

### `TryGetPawnOwner`

```text
TryGetPawnOwner() -> APawn *
```

**Returns**

| Type | Description |
|---|---|
| `APawn *` | - |

### `SavePoseSnapshot`

```text
SavePoseSnapshot(SnapshotName: FName) -> void
```

Takes a snapshot of the current skeletal mesh component pose & saves it internally.
	  This snapshot can then be retrieved by name in the animation blueprint for blending.
	  The snapshot is taken at the current LOD, so if for example you took the snapshot at LOD1 and then used it at LOD0 any bones not in LOD1 will use the reference pose

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SnapshotName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SnapshotPose`

```text
SnapshotPose(Snapshot: FPoseSnapshot &) -> void
```

Takes a snapshot of the current skeletal mesh component pose and saves it to the specified snapshot.
	  The snapshot is taken at the current LOD, so if for example you took the snapshot at LOD1
	  and then used it at LOD0 any bones not in LOD1 will use the reference pose

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Snapshot` | `FPoseSnapshot &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetOwningActor`

```text
GetOwningActor() -> AActor *
```

Returns the owning actor of this AnimInstance

**Returns**

| Type | Description |
|---|---|
| `AActor *` | - |

### `GetOwningComponent`

```text
GetOwningComponent() -> USkeletalMeshComponent *
```

**Returns**

| Type | Description |
|---|---|
| `USkeletalMeshComponent *` | - |

### `BlueprintShouldSkipUpdateAnimation`

```text
BlueprintShouldSkipUpdateAnimation(DeltaTimeX: float) -> bool
```

Executed before the Animation is updated, Check custom condition, whether to skip update

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaTimeX` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `BlueprintInitializeAnimation`

```text
BlueprintInitializeAnimation() -> void
```

Executed when the Animation is initialized

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BlueprintUnInitializeAnimation`

```text
BlueprintUnInitializeAnimation() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BlueprintUpdateAnimation`

```text
BlueprintUpdateAnimation(DeltaTimeX: float) -> void
```

Executed when the Animation is updated

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaTimeX` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BlueprintPostEvaluateAnimation`

```text
BlueprintPostEvaluateAnimation() -> void
```

Executed after the Animation is evaluated

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BlueprintBeginPlay`

```text
BlueprintBeginPlay() -> void
```

Executed when begin play is called on the owning component

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PlaySlotAnimation`

```text
PlaySlotAnimation(Asset: UAnimSequenceBase *, SlotNodeName: FName, BlendInTime: float, BlendOutTime: float, InPlayRate: float, LoopCount: int32) -> float
```

SlotAnimation
	 
	 DEPRECATED. Use PlaySlotAnimationAsDynamicMontage instead, it returns the UAnimMontage created instead of time, allowing more control 
	 Play normal animation asset on the slot node. You can only play one asset (whether montage or animsequence) at a time.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Asset` | `UAnimSequenceBase *` | - |
| `SlotNodeName` | `FName` | - |
| `BlendInTime` | `float` | - |
| `BlendOutTime` | `float` | - |
| `InPlayRate` | `float` | - |
| `LoopCount` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `PlaySlotAnimationAsDynamicMontage`

```text
PlaySlotAnimationAsDynamicMontage(Asset: UAnimSequenceBase *, SlotNodeName: FName, BlendInTime: float, BlendOutTime: float, InPlayRate: float, LoopCount: int32, BlendOutTriggerTime: float, InTimeToStartMontageAt: float) -> UAnimMontage *
```

Play normal animation asset on the slot node by creating a dynamic UAnimMontage. You can only play one asset (whether montage or animsequence) at a time per SlotGroup.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Asset` | `UAnimSequenceBase *` | - |
| `SlotNodeName` | `FName` | - |
| `BlendInTime` | `float` | - |
| `BlendOutTime` | `float` | - |
| `InPlayRate` | `float` | - |
| `LoopCount` | `int32` | - |
| `BlendOutTriggerTime` | `float` | - |
| `InTimeToStartMontageAt` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `UAnimMontage *` | - |

### `PlaySlotAnimationAsDynamicMontageCustom`

```text
PlaySlotAnimationAsDynamicMontageCustom(Asset: UAnimSequenceBase *, SlotNodeName: FName, Extra: FCustomMontageAnimInfo, BlendInTime: float, BlendOutTime: float, InPlayRate: float, LoopCount: int32, BlendOutTriggerTime: float, InTimeToStartMontageAt: float) -> UAnimMontage *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Asset` | `UAnimSequenceBase *` | - |
| `SlotNodeName` | `FName` | - |
| `Extra` | `FCustomMontageAnimInfo` | - |
| `BlendInTime` | `float` | - |
| `BlendOutTime` | `float` | - |
| `InPlayRate` | `float` | - |
| `LoopCount` | `int32` | - |
| `BlendOutTriggerTime` | `float` | - |
| `InTimeToStartMontageAt` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `UAnimMontage *` | - |

### `SetMatineeAnimPosition`

```text
SetMatineeAnimPosition(TargetMontage: UAnimMontage *, InPosition: float, Extra: FCustomMontageAnimInfo, Weight: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetMontage` | `UAnimMontage *` | - |
| `InPosition` | `float` | - |
| `Extra` | `FCustomMontageAnimInfo` | - |
| `Weight` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopSlotAnimation`

```text
StopSlotAnimation(InBlendOutTime: float, SlotNodeName: FName) -> void
```

Stops currently playing slot animation slot or all

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBlendOutTime` | `float` | - |
| `SlotNodeName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsPlayingSlotAnimation`

```text
IsPlayingSlotAnimation(Asset: UAnimSequenceBase *, SlotNodeName: FName, bcheckTransientPackage: bool) -> bool
```

Return true if it's playing the slot animation

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Asset` | `UAnimSequenceBase *` | - |
| `SlotNodeName` | `FName` | - |
| `bcheckTransientPackage` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ForceTriggerAnimEndedEvent`

```text
ForceTriggerAnimEndedEvent() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMontageCustomSectionsPlayInfo`

```text
SetMontageCustomSectionsPlayInfo(Montage: UAnimMontage *, InPlayInfo: TArray < FMontageSectionsPlayInfo > &) -> void
```

AnimMontage

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |
| `InPlayInfo` | `TArray < FMontageSectionsPlayInfo > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearMontageCustomSectionsPlayInfo`

```text
ClearMontageCustomSectionsPlayInfo(Montage: UAnimMontage *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Montage_Play`

```text
Montage_Play(MontageToPlay: UAnimMontage *, InPlayRate: float, ReturnValueType: EMontagePlayReturnType, InTimeToStartMontageAt: float) -> float
```

Plays an animation montage. Returns the length of the animation montage in seconds. Returns 0.f if failed to play.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MontageToPlay` | `UAnimMontage *` | - |
| `InPlayRate` | `float` | - |
| `ReturnValueType` | `EMontagePlayReturnType` | - |
| `InTimeToStartMontageAt` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Montage_CustomPlay`

```text
Montage_CustomPlay(MontageToPlay: UAnimMontage *, Extra: FCustomMontageAnimInfo, InPlayRate: float, ReturnValueType: EMontagePlayReturnType, InTimeToStartMontageAt: float) -> float
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MontageToPlay` | `UAnimMontage *` | - |
| `Extra` | `FCustomMontageAnimInfo` | - |
| `InPlayRate` | `float` | - |
| `ReturnValueType` | `EMontagePlayReturnType` | - |
| `InTimeToStartMontageAt` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Montage_Stop`

```text
Montage_Stop(InBlendOutTime: float, Montage: UAnimMontage *) -> void
```

Stops the animation montage. If reference is NULL, it will stop ALL active montages.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBlendOutTime` | `float` | - |
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Montage_StopBySlot`

```text
Montage_StopBySlot(InBlendOutTime: float, SlotName: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBlendOutTime` | `float` | - |
| `SlotName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Montage_CustomStop`

```text
Montage_CustomStop(InBlendOutTime: float, Extra: FCustomMontageAnimInfo, Montage: UAnimMontage *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBlendOutTime` | `float` | - |
| `Extra` | `FCustomMontageAnimInfo` | - |
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Montage_Pause`

```text
Montage_Pause(Montage: UAnimMontage *) -> void
```

Pauses the animation montage. If reference is NULL, it will pause ALL active montages.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Montage_Resume`

```text
Montage_Resume(Montage: UAnimMontage *) -> void
```

Resumes a paused animation montage. If reference is NULL, it will resume ALL active montages.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Montage_JumpToSection`

```text
Montage_JumpToSection(SectionName: FName, Montage: UAnimMontage *) -> void
```

Makes a montage jump to a named section. If Montage reference is NULL, it will do that to all active montages.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SectionName` | `FName` | - |
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Montage_JumpToSectionsEnd`

```text
Montage_JumpToSectionsEnd(SectionName: FName, Montage: UAnimMontage *) -> void
```

Makes a montage jump to the end of a named section. If Montage reference is NULL, it will do that to all active montages.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SectionName` | `FName` | - |
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Montage_SetNextSection`

```text
Montage_SetNextSection(SectionNameToChange: FName, NextSection: FName, Montage: UAnimMontage *) -> void
```

Relink new next section AFTER SectionNameToChange in run-time
	 	You can link section order the way you like in editor, but in run-time if you'd like to change it dynamically,
	 	use this function to relink the next section
	 	For example, you can have Start->Loop->Loop->Loop.... but when you want it to end, you can relink
	 	next section of Loop to be End to finish the montage, in which case, it stops looping by Loop->End.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SectionNameToChange` | `FName` | : This should be the name of the Montage Section after which you want to insert a new next section |
| `NextSection` | `FName` | : new next section |
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Montage_SetPlayRate`

```text
Montage_SetPlayRate(Montage: UAnimMontage *, NewPlayRate: float) -> void
```

Change AnimMontage play rate. NewPlayRate = 1.0 is the default playback rate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |
| `NewPlayRate` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Montage_ReversePlayByAbsRateAndSlot`

```text
Montage_ReversePlayByAbsRateAndSlot(SlotName: FName, AbsPlayRate: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SlotName` | `FName` | - |
| `AbsPlayRate` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Montage_SetDelayFrame`

```text
Montage_SetDelayFrame(Montage: UAnimMontage *, DelayFrame: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |
| `DelayFrame` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Montage_IsActive`

```text
Montage_IsActive(Montage: UAnimMontage *) -> bool
```

Returns true if the animation montage is active. If the Montage reference is NULL, it will return true if any Montage is active.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Montage_IsPlaying`

```text
Montage_IsPlaying(Montage: UAnimMontage *) -> bool
```

Returns true if the animation montage is currently active and playing.
	If reference is NULL, it will return true is ANY montage is currently active and playing.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Montage_IsExisting`

```text
Montage_IsExisting(Montage: UAnimMontage *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `MontageGroup_IsPlaying`

```text
MontageGroup_IsPlaying(GroupName: FName) -> bool
```

判断有无某个组下的蒙太奇正在播放

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GroupName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Montage_GetCurrentSection`

```text
Montage_GetCurrentSection(Montage: UAnimMontage *) -> FName
```

Returns the name of the current animation montage section.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `FName` | - |

### `Montage_GetPosition`

```text
Montage_GetPosition(Montage: UAnimMontage *) -> float
```

Get Current Montage Position

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Montage_SetPosition`

```text
Montage_SetPosition(Montage: UAnimMontage *, NewPosition: float) -> void
```

Set position.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |
| `NewPosition` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Montage_GetIsStopped`

```text
Montage_GetIsStopped(Montage: UAnimMontage *) -> bool
```

return true if Montage is not currently active. (not valid or blending out)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Montage_GetBlendTime`

```text
Montage_GetBlendTime(Montage: UAnimMontage *) -> float
```

Get the current blend time of the Montage.
	If Montage reference is NULL, it will return the current blend time on the first active Montage found.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Montage_GetPlayRate`

```text
Montage_GetPlayRate(Montage: UAnimMontage *) -> float
```

Get PlayRate for Montage.
	If Montage is not playing, 0 is returned.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `IsAnyMontagePlaying`

```text
IsAnyMontagePlaying() -> bool
```

Returns true if any montage is playing currently. Doesn't mean it's active though, it could be blending out.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetCurrentActiveMontage`

```text
GetCurrentActiveMontage() -> UAnimMontage *
```

Get a current Active Montage in this AnimInstance.
		Note that there might be multiple Active at the same time. This will only return the first active one it finds.

**Returns**

| Type | Description |
|---|---|
| `UAnimMontage *` | - |

### `GetCurrentActiveMontages`

```text
GetCurrentActiveMontages() -> TArray < FAnimMontageInstance >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < FAnimMontageInstance >` | - |

### `GetCurMontageBySlot`

```text
GetCurMontageBySlot(SlotName: FName) -> UAnimMontage *
```

Get the UAnimMontage currently running that matches this SlotName.  Will return NULL if no instance is found.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SlotName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `UAnimMontage *` | - |

### `Montage_GetNextSection`

```text
Montage_GetNextSection(Montage: UAnimMontage *, SectionName: FName) -> FName
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |
| `SectionName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `FName` | - |

### `AddAnimAssetNoGCRef`

```text
AddAnimAssetNoGCRef(InAnimAsset: UAnimationAsset *) -> int64
```

添加动画资源到非GC引用列表，返回全局唯一ID

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimAsset` | `UAnimationAsset *` | - |

**Returns**

| Type | Description |
|---|---|
| `int64` | - |

### `RemoveAnimAssetNoGCRef`

```text
RemoveAnimAssetNoGCRef(InAnimAssetNoGCID: int64) -> void
```

从非GC引用列表移除动画资源（通过ID）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimAssetNoGCID` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveAllAnimAssetNoGCRef`

```text
RemoveAllAnimAssetNoGCRef(InAnimAsset: UAnimationAsset *) -> void
```

从非GC引用列表移除所有动画资源（通过资源指针）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimAsset` | `UAnimationAsset *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearAnimAssetsNoGCReferences`

```text
ClearAnimAssetsNoGCReferences() -> void
```

清空非GC引用列表

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopAllMontages`

```text
StopAllMontages(BlendOut: float) -> void
```

Stop all montages that are active

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BlendOut` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearAllMontages`

```text
ClearAllMontages(BlendOut: float) -> void
```

Stop all montages that are active

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BlendOut` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearStoppedMontageInstances`

```text
ClearStoppedMontageInstances(bClearSubAnim: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bClearSubAnim` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetForbiddenPlayMontageSlot`

```text
GetForbiddenPlayMontageSlot() -> TArray < FString >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < FString >` | - |

### `SetForbiddenPlayMontageSlot`

```text
SetForbiddenPlayMontageSlot(bIsAdd: bool, SlotName: FString) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsAdd` | `bool` | - |
| `SlotName` | `FString` | should be GroupName + SlotName |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRootMotionMode`

```text
SetRootMotionMode(Value: TEnumAsByte < ERootMotionMode :: Type >) -> void
```

Set RootMotionMode

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `TEnumAsByte < ERootMotionMode :: Type >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetInstanceAssetPlayerLength`

```text
GetInstanceAssetPlayerLength(AssetPlayerIndex: int32) -> float
```

NOTE: Derived anim getters
	 
	  Anim getter functions can be defined for any instance deriving UAnimInstance.
	  To do this the function must be marked BlueprintPure, and have the AnimGetter metadata entry set to
	  "true". Following the instructions below, getters should appear correctly in the blueprint node context
	  menu for the derived classes
	 
	  A context string can be provided in the GetterContext metadata and can contain any (or none) of the
	  following entries separated by a pipe (|)
	  Transition  - Only available in a transition rule
	  AnimGraph   - Only available in an animgraph (also covers state anim graphs)
	  CustomBlend - Only available in a custom blend graph
	 
	  Anim getters support a number of automatic parameters that will be baked at compile time to be passed
	  to the functions. They will not appear as pins on the graph node. They are as follows:
	  AssetPlayerIndex - Index of an asset player node to operate on, one getter will be added to the blueprint action list per asset node available
	  MachineIndex     - Index of a state machine in the animation blueprint, one getter will be added to the blueprint action list per state machine
	  StateIndex       - Index of a state inside a state machine, also requires MachineIndex. One getter will be added to the blueprint action list per state
	  TransitionIndex  - Index of a transition inside a state machine, also requires MachineIndex. One getter will be added to the blueprint action list per transition
	 
	  Gets the length in seconds of the asset referenced in an asset player node

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetPlayerIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetInstanceAssetPlayerTime`

```text
GetInstanceAssetPlayerTime(AssetPlayerIndex: int32) -> float
```

Get the current accumulated time in seconds for an asset player node

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetPlayerIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetInstanceAssetPlayerTime`

```text
SetInstanceAssetPlayerTime(AssetPlayerIndex: int32, time: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetPlayerIndex` | `int32` | - |
| `time` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetNodeIndexWithTag`

```text
GetNodeIndexWithTag(NodeTag: FName) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeTag` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetInstanceAssetPlayerTime_BP`

```text
GetInstanceAssetPlayerTime_BP(AssetPlayerIndex: int32) -> float
```

Get the current accumulated time in seconds for an asset player node

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetPlayerIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetInstanceAssetPlayerTime_BP`

```text
SetInstanceAssetPlayerTime_BP(AssetPlayerIndex: int32, time: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetPlayerIndex` | `int32` | - |
| `time` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetInstanceAssetPlayerTimeFraction`

```text
GetInstanceAssetPlayerTimeFraction(AssetPlayerIndex: int32) -> float
```

Get the current accumulated time as a fraction for an asset player node

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetPlayerIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetInstanceAssetPlayerTimeFromEnd`

```text
GetInstanceAssetPlayerTimeFromEnd(AssetPlayerIndex: int32) -> float
```

Get the time in seconds from the end of an animation in an asset player node

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetPlayerIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetInstanceAssetPlayerTimeFromEndFraction`

```text
GetInstanceAssetPlayerTimeFromEndFraction(AssetPlayerIndex: int32) -> float
```

Get the time as a fraction of the asset length of an animation in an asset player node

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetPlayerIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetInstanceMachineWeight`

```text
GetInstanceMachineWeight(MachineIndex: int32) -> float
```

Get the blend weight of a specified state machine

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MachineIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetInstanceStateWeight`

```text
GetInstanceStateWeight(MachineIndex: int32, StateIndex: int32) -> float
```

Get the blend weight of a specified state

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MachineIndex` | `int32` | - |
| `StateIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetInstanceCurrentStateElapsedTime`

```text
GetInstanceCurrentStateElapsedTime(MachineIndex: int32) -> float
```

Get the current elapsed time of a state within the specified state machine

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MachineIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetInstanceTransitionCrossfadeDuration`

```text
GetInstanceTransitionCrossfadeDuration(MachineIndex: int32, TransitionIndex: int32) -> float
```

Get the crossfade duration of a specified transition

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MachineIndex` | `int32` | - |
| `TransitionIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetInstanceTransitionTimeElapsed`

```text
GetInstanceTransitionTimeElapsed(MachineIndex: int32, TransitionIndex: int32) -> float
```

Get the elapsed time in seconds of a specified transition

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MachineIndex` | `int32` | - |
| `TransitionIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetInstanceTransitionTimeElapsedFraction`

```text
GetInstanceTransitionTimeElapsedFraction(MachineIndex: int32, TransitionIndex: int32) -> float
```

Get the elapsed time as a fraction of the crossfade duration of a specified transition

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MachineIndex` | `int32` | - |
| `TransitionIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetRelevantAnimTimeRemaining`

```text
GetRelevantAnimTimeRemaining(MachineIndex: int32, StateIndex: int32, NullAnimDefaultValue: float) -> float
```

Get the time remaining in seconds for the most relevant animation in the source state

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MachineIndex` | `int32` | - |
| `StateIndex` | `int32` | - |
| `NullAnimDefaultValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetRelevantAnimTimeRemainingFraction`

```text
GetRelevantAnimTimeRemainingFraction(MachineIndex: int32, StateIndex: int32, NullAnimDefaultValue: float) -> float
```

Get the time remaining as a fraction of the duration for the most relevant animation in the source state

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MachineIndex` | `int32` | - |
| `StateIndex` | `int32` | - |
| `NullAnimDefaultValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetRelevantAnimLength`

```text
GetRelevantAnimLength(MachineIndex: int32, StateIndex: int32, NullAnimDefaultValue: float) -> float
```

Get the length in seconds of the most relevant animation in the source state

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MachineIndex` | `int32` | - |
| `StateIndex` | `int32` | - |
| `NullAnimDefaultValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetRelevantAnimTime`

```text
GetRelevantAnimTime(MachineIndex: int32, StateIndex: int32, NullAnimDefaultValue: float) -> float
```

Get the current accumulated time in seconds for the most relevant animation in the source state

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MachineIndex` | `int32` | - |
| `StateIndex` | `int32` | - |
| `NullAnimDefaultValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetRelevantAnimTimeFraction`

```text
GetRelevantAnimTimeFraction(MachineIndex: int32, StateIndex: int32, NullAnimDefaultValue: float) -> float
```

Get the current accumulated time as a fraction of the length of the most relevant animation in the source state

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MachineIndex` | `int32` | - |
| `StateIndex` | `int32` | - |
| `NullAnimDefaultValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetCurveValue`

```text
GetCurveValue(CurveName: FName, Immediately: bool) -> float
```

Returns the value of a named curve.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CurveName` | `FName` | - |
| `Immediately` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetCurrentStateName`

```text
GetCurrentStateName(MachineIndex: int32) -> FName
```

Returns the name of a currently active state in a state machine.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MachineIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FName` | - |

### `SetMorphTarget`

```text
SetMorphTarget(MorphTargetName: FName, Value: float) -> void
```

Sets a morph target to a certain weight.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MorphTargetName` | `FName` | - |
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearMorphTargets`

```text
ClearMorphTargets() -> void
```

Clears the current morph targets.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CalculateDirection`

```text
CalculateDirection(Velocity: FVector &, BaseRotation: FRotator &) -> float
```

Returns degree of the angle betwee velocity and Rotation forward vector
	  The range of return will be from [-180, 180], and this can be used to feed blendspace directional value

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Velocity` | `FVector &` | - |
| `BaseRotation` | `FRotator &` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `LockAIResources`

```text
LockAIResources(bLockMovement: bool, LockAILogic: bool) -> void
```

locks indicated AI resources of animated pawn
	 	DEPRECATED. Use LockAIResourcesWithAnimation instead

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bLockMovement` | `bool` | - |
| `LockAILogic` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnlockAIResources`

```text
UnlockAIResources(bUnlockMovement: bool, UnlockAILogic: bool) -> void
```

unlocks indicated AI resources of animated pawn. Will unlock only animation-locked resources.
	 	DEPRECATED. Use UnlockAIResourcesWithAnimation instead

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bUnlockMovement` | `bool` | - |
| `UnlockAILogic` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetTimeToClosestMarker`

```text
GetTimeToClosestMarker(SyncGroup: FName, MarkerName: FName, OutMarkerTime: float &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SyncGroup` | `FName` | - |
| `MarkerName` | `FName` | - |
| `OutMarkerTime` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `HasMarkerBeenHitThisFrame`

```text
HasMarkerBeenHitThisFrame(SyncGroup: FName, MarkerName: FName) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SyncGroup` | `FName` | - |
| `MarkerName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsSyncGroupBetweenMarkers`

```text
IsSyncGroupBetweenMarkers(InSyncGroupName: FName, PreviousMarker: FName, NextMarker: FName, bRespectMarkerOrder: bool) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSyncGroupName` | `FName` | - |
| `PreviousMarker` | `FName` | - |
| `NextMarker` | `FName` | - |
| `bRespectMarkerOrder` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetSyncGroupPosition`

```text
GetSyncGroupPosition(InSyncGroupName: FName) -> FMarkerSyncAnimPosition
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSyncGroupName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `FMarkerSyncAnimPosition` | - |

### `TriggerAllSequenceSwitchNotify`

```text
TriggerAllSequenceSwitchNotify() -> void
```

Trigger AnimNotifies

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CheckCanTriggerNotify_AnimIsolation_Outer`

```text
CheckCanTriggerNotify_AnimIsolation_Outer(InAnimNotifyEvent: FAnimNotifyEvent &, InNotify: UAnimNotify *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimNotifyEvent` | `FAnimNotifyEvent &` | - |
| `InNotify` | `UAnimNotify *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `CheckCanTriggerNotifyState_AnimIsolation_Outer`

```text
CheckCanTriggerNotifyState_AnimIsolation_Outer(InAnimNotifyEvent: FAnimNotifyEvent &, InNotifyState: UAnimNotifyState *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimNotifyEvent` | `FAnimNotifyEvent &` | - |
| `InNotifyState` | `UAnimNotifyState *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `CheckCanTriggerAnimNotifyFunction_AnimIsolation_Outer`

```text
CheckCanTriggerAnimNotifyFunction_AnimIsolation_Outer(InAnimNotifyEvent: FAnimNotifyEvent &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimNotifyEvent` | `FAnimNotifyEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ReplaceSubAnimNodeAnimClass`

```text
ReplaceSubAnimNodeAnimClass(SubInstanceSlotName: FName, NewAnimClass: TSubclassOf < UAnimInstance >, BlendTime: float, bEnableNoWaitParallelEvalTask: bool) -> UAnimInstance *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SubInstanceSlotName` | `FName` | - |
| `NewAnimClass` | `TSubclassOf < UAnimInstance >` | - |
| `BlendTime` | `float` | - |
| `bEnableNoWaitParallelEvalTask` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `UAnimInstance *` | - |

### `ReplaceSubAnimNodeAnimClass_EmptyClassDefaut`

```text
ReplaceSubAnimNodeAnimClass_EmptyClassDefaut(SubInstanceSlotName: FName, NewAnimClass: TSubclassOf < UAnimInstance >, BlendTime: float) -> UAnimInstance *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SubInstanceSlotName` | `FName` | - |
| `NewAnimClass` | `TSubclassOf < UAnimInstance >` | - |
| `BlendTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `UAnimInstance *` | - |

### `ResetSubAnimNodeAnimClass`

```text
ResetSubAnimNodeAnimClass(SubInstanceSlotName: FName, FilterAnimClass: TSubclassOf < UAnimInstance >, BlendTime: float, bEnableNoWaitParallelEvalTask: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SubInstanceSlotName` | `FName` | - |
| `FilterAnimClass` | `TSubclassOf < UAnimInstance >` | - |
| `BlendTime` | `float` | - |
| `bEnableNoWaitParallelEvalTask` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetSubAnimNodeAnimClass_EmptyClassDefaut`

```text
ResetSubAnimNodeAnimClass_EmptyClassDefaut(SubInstanceSlotName: FName, FilterAnimClass: TSubclassOf < UAnimInstance >, BlendTime: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SubInstanceSlotName` | `FName` | - |
| `FilterAnimClass` | `TSubclassOf < UAnimInstance >` | - |
| `BlendTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetAllSubAnimNode`

```text
ResetAllSubAnimNode() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearAllSubAnimBlendTime`

```text
ClearAllSubAnimBlendTime() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetAllSubAnimNodePosInertialization`

```text
ResetAllSubAnimNodePosInertialization() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSubAnimInstanceBySlot`

```text
GetSubAnimInstanceBySlot(SubInstanceSlotName: FName) -> UAnimInstance *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SubInstanceSlotName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `UAnimInstance *` | - |

### `IsUseSubAnimInstanceBySlot`

```text
IsUseSubAnimInstanceBySlot(SubInstanceSlotName: FName) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SubInstanceSlotName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetSubAnimNodeEnableBlend`

```text
SetSubAnimNodeEnableBlend(SubInstanceSlotName: FName, bEnable: bool, NewSubAnimBlendTime: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SubInstanceSlotName` | `FName` | - |
| `bEnable` | `bool` | - |
| `NewSubAnimBlendTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddSubAnimNodeAnimClass`

```text
AddSubAnimNodeAnimClass(SubInstanceSlotName: FName, NewAnimClass: TSubclassOf < UAnimInstance >, Priority: int32, BlendTime: float) -> UAnimInstance *
```

同槽多子动画实例

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SubInstanceSlotName` | `FName` | - |
| `NewAnimClass` | `TSubclassOf < UAnimInstance >` | - |
| `Priority` | `int32` | - |
| `BlendTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `UAnimInstance *` | - |

### `RemoveSubAnimNodeAnimClass`

```text
RemoveSubAnimNodeAnimClass(SubInstanceSlotName: FName, FilterClass: TSubclassOf < UAnimInstance >, BlendTime: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SubInstanceSlotName` | `FName` | - |
| `FilterClass` | `TSubclassOf < UAnimInstance >` | - |
| `BlendTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetSubAnimNode_MultiInstanceClass`

```text
ResetSubAnimNode_MultiInstanceClass(SubInstanceSlotName: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SubInstanceSlotName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetAllSubAnimNode_MultiInstance`

```text
ResetAllSubAnimNode_MultiInstance() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddStopTickSubAnimInstance`

```text
AddStopTickSubAnimInstance(Instance: UAnimInstance *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Instance` | `UAnimInstance *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveCachedStopTickSubAnimInstance`

```text
RemoveCachedStopTickSubAnimInstance(Instance: UAnimInstance *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Instance` | `UAnimInstance *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearAllStopTickSubAnimInstance`

```text
ClearAllStopTickSubAnimInstance() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRecycleCachedSubAnimInstances`

```text
OnRecycleCachedSubAnimInstances(bToPersistentPool: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bToPersistentPool` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MarkBoneStateDirty`

```text
MarkBoneStateDirty(InIsDirty: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InIsDirty` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsBoneStateDirty`

```text
IsBoneStateDirty() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsUseBoneStateDirtyFeature`

```text
IsUseBoneStateDirtyFeature() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `HasSlotNode`

```text
HasSlotNode(InSlotName: FName) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSlotName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `UpdateAnimSlotRetargetInfo`

```text
UpdateAnimSlotRetargetInfo(InMontage: UAnimMontage *, InSlotNameRetargetInfo: TMap < FName , FName > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMontage` | `UAnimMontage *` | - |
| `InSlotNameRetargetInfo` | `TMap < FName , FName > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetInverseRetargetIgnoreBoneList`

```text
GetInverseRetargetIgnoreBoneList() -> const TArray < int32 > &
```

**Returns**

| Type | Description |
|---|---|
| `const TArray < int32 > &` | - |

### `SetFollowedAnimInstance`

```text
SetFollowedAnimInstance(InputFollowedInstance: UAnimInstance *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InputFollowedInstance` | `UAnimInstance *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetFollowedAnimInstance`

```text
ResetFollowedAnimInstance() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsFollowing`

```text
IsFollowing(TargetFollowedInstance: UAnimInstance *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetFollowedInstance` | `UAnimInstance *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetDelayPlay`

```text
SetDelayPlay(IsDelay: bool, InputDelayFrames: int) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsDelay` | `bool` | - |
| `InputDelayFrames` | `int` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetParentAnimInstance`

```text
GetParentAnimInstance() -> UAnimInstance *
```

**Returns**

| Type | Description |
|---|---|
| `UAnimInstance *` | - |

### `SetParentAnimInstance`

```text
SetParentAnimInstance(InParentAnimInstance: UAnimInstance *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InParentAnimInstance` | `UAnimInstance *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSubAnimInstances`

```text
GetSubAnimInstances() -> TArray < UAnimInstance * >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < UAnimInstance * >` | - |

### `GetAllSubAnimInstances`

```text
GetAllSubAnimInstances() -> TArray < UAnimInstance * >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < UAnimInstance * >` | - |

### `SwapCachedBoneTransformMap`

```text
SwapCachedBoneTransformMap() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCachedBoneTransform`

```text
GetCachedBoneTransform(InBoneName: FName, OutTransform: FTransform &, forceSync: bool) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBoneName` | `FName` | - |
| `OutTransform` | `FTransform &` | - |
| `forceSync` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetCachedBoneTransformByFlag`

```text
GetCachedBoneTransformByFlag(InBoneName: FName, InCacheFlag: FName, OutTransform: FTransform &, NeedLastFrameCount: int32, forceSync: bool) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBoneName` | `FName` | - |
| `InCacheFlag` | `FName` | - |
| `OutTransform` | `FTransform &` | - |
| `NeedLastFrameCount` | `int32` | - |
| `forceSync` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `CompareCachedBoneTransformByFlag`

```text
CompareCachedBoneTransformByFlag(InBoneName0: FName, InCacheFlag0: FName, InBoneName1: FName, InCacheFlag1: FName) -> int64
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBoneName0` | `FName` | - |
| `InCacheFlag0` | `FName` | - |
| `InBoneName1` | `FName` | - |
| `InCacheFlag1` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `int64` | - |

### `SetTriggerAnimNotify`

```text
SetTriggerAnimNotify(NeedTrigger: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NeedTrigger` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FilterForceTriggerNotifyWhenMontageJumpTick`

```text
FilterForceTriggerNotifyWhenMontageJumpTick(InMontage: UAnimMontage *, bPlayingBackwards: bool, CurrentTrackPos: float, CurrentDeltaSeconds: float, InAnimNotifies: TArray < FAnimNotifyEvent > &, OutForceTriggerAnimNotifies: TArray < FAnimNotifyEvent > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMontage` | `UAnimMontage *` | - |
| `bPlayingBackwards` | `bool` | - |
| `CurrentTrackPos` | `float` | - |
| `CurrentDeltaSeconds` | `float` | - |
| `InAnimNotifies` | `TArray < FAnimNotifyEvent > &` | - |
| `OutForceTriggerAnimNotifies` | `TArray < FAnimNotifyEvent > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetLobbySeqIgnoreNotifyList`

```text
GetLobbySeqIgnoreNotifyList() -> TArray < FString >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < FString >` | - |

### `ResetNotifyQueue`

```text
ResetNotifyQueue() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RestoreAnimation`

```text
RestoreAnimation(InRecordName: FString &) -> void
```

编辑器调用函数，根据录制文件名进行重放，播放第一帧后暂停

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRecordName` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `LogPoseDebug`

```text
LogPoseDebug() -> void
```

输出当前Pose至Log界面

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PauseOrContinueRestore`

```text
PauseOrContinueRestore() -> void
```

暂停或者继续重放

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RestoreNextFrame`

```text
RestoreNextFrame() -> void
```

重放下一帧

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `JumpToGivenFrame`

```text
JumpToGivenFrame() -> void
```

跳转至指定帧

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RestoreClear`

```text
RestoreClear() -> void
```

清空当前回放信息

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RestartAnimation`

```text
RestartAnimation() -> void
```

重新开始回放

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SeekToFrame`

```text
SeekToFrame(FrameIndex: int32) -> void
```

跳转到指定帧并恢复该帧状态（编辑器调用）
	   要求当前处于 RestoreWait 或 RestoreEnd 状态
	   内部设置 DataAr 位置到 RestoreHeader[FrameIndex-1]，
	   下一帧 ParallelRestoreAnimation 将恢复该帧并更新调试数据

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FrameIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SeekToTime`

```text
SeekToTime(TimeInSeconds: float) -> void
```

根据时间跳转到最近帧（编辑器调用）
	   使用估算帧率计算帧索引后调用 SeekToFrame

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TimeInSeconds` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RestorePreviousFrame`

```text
RestorePreviousFrame() -> void
```

回退到前一帧（编辑器调用）

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnMontageBlendingOut`

```text
OnMontageBlendingOut(Montage: UAnimMontage*, bInterrupted: bool) -> void
```

Called when a montage starts blending out, whether interrupted or finished

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage*` | - |
| `bInterrupted` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMontageStarted`

```text
OnMontageStarted(Montage: UAnimMontage*) -> void
```

Called when a montage has started

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMontageEnded`

```text
OnMontageEnded(Montage: UAnimMontage*, bInterrupted: bool) -> void
```

Called when a montage has ended, whether interrupted or finished

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage*` | - |
| `bInterrupted` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMontageRealEnded`

```text
OnMontageRealEnded(Montage: UAnimMontage*, bInterrupted: bool) -> void
```

Called when a montage real ended, whether interrupted or finished

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage*` | - |
| `bInterrupted` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnAllMontageInstancesEnded`

```text
OnAllMontageInstancesEnded() -> void
```

Called when all Montage instances have ended.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
