---
id: "api-chunk:cppstruct:1"
title: "Oasis API cppstruct chunk 1"
source: "https://developer.gp.qq.com/api/"
category: "API Wiki/cppstruct"
kind: "api_chunk"
---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FA2CSPose.json -->

# FA2CSPose

Component space poses.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ComponentSpaceFlags` | `TArray < uint8 >` | Once evaluated to be mesh space, this flag will be set. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FA2Pose.json -->

# FA2Pose

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Bones` | `TArray < FTransform >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FACESParameter.json -->

# FACESParameter

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TintColor` | `FLinearColor` | - |
| `Bright` | `float` | - |
| `Gray` | `float` | - |
| `ShoulderStrength` | `float` | - |
| `ToeStrength` | `float` | - |
| `LinearStrength` | `float` | - |
| `LinearAngle` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FActionBindingCluster.json -->

# FActionBindingCluster

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ActionBindingInfos` | `TArray < FActionBindingInfo >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FActionBindingInfo.json -->

# FActionBindingInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InputEvent` | `EActorInputEvent` | - |
| `ActionName` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FActionCluster.json -->

# FActionCluster

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ClusterID` | `int32` | - |
| `ClusterActionNames` | `TArray < FName >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FActiveForceFeedbackEffect.json -->

# FActiveForceFeedbackEffect

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ForceFeedbackEffect` | `UForceFeedbackEffect *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FActiveHapticFeedbackEffect.json -->

# FActiveHapticFeedbackEffect

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `HapticEffect` | `UHapticFeedbackEffect_Base *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FActorPerceptionBlueprintInfo.json -->

# FActorPerceptionBlueprintInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Target` | `AActor *` | - |
| `LastSensedStimuli` | `TArray < FAIStimulus >` | - |
| `bIsHostile` | `uint32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FActorSet.json -->

# FActorSet

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Actors` | `TArray < AActor * >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAdditionalRescanRootEntry.json -->

# FAdditionalRescanRootEntry

One entry of UWorldComposition extra scan roots.
  Allows a persistent map to pull in tiles from directories outside its own folder
  (e.g. shared tile libraries), with per-root include  exclude filtering.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RootPath` | `FString` | Long Package Path (must be a registered content mount), e.g. "GameCommonSharedTiles".<br>	  Leading and trailing slashes are normalized automatically. |
| `IncludeTiles` | `TArray < FString >` | If non-empty, ONLY tiles produced by RootPath whose long package name matches one of these<br>	  patterns are kept. Pattern syntax:<br>	    "Forest"                              -> folder prefix relative to RootPath<br>	    "ForestTile_X1_Y1"                    -> exact tile, relative to RootPath<br>	    "GameCommonSharedTilesForest"     -> absolute folder prefix<br>	    "GameCommonSharedTilesForestTile_X1_Y1" -> absolute exact tile<br>	  Folder patterns must end with ''. |
| `ExcludeTiles` | `TArray < FString >` | Same syntax as IncludeTiles. Tiles matching any pattern here are dropped.<br>	  Applied AFTER IncludeTiles, so a tile must (pass include) AND (not match exclude) to survive. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAggregatedCollision.json -->

# FAggregatedCollision

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BodySetup` | `UBodySetup *` | - |
| `BodySetupName` | `FString` | - |
| `Transforms` | `TArray < FTransform >` | - |
| `BodyInstances` | `TArray < FBodyInstance >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAIDamageEvent.json -->

# FAIDamageEvent

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Amount` | `float` | Damage taken by DamagedActor.<br>	 	@Note 0-damage events do not get ignored |
| `Location` | `FVector` | Event's "Location", or what will be later treated as the perceived location for this sense.<br>	 	If not set, HitLocation will be used, if that is unset too DamagedActor's location |
| `HitLocation` | `FVector` | Event's additional spatial information<br>	 	@TODO document |
| `DamagedActor` | `AActor *` | Damaged actor |
| `Instigator` | `AActor *` | Actor that instigated damage. Can be None |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAIDataProviderBoolValue.json -->

# FAIDataProviderBoolValue

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefaultValue` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAIDataProviderFloatValue.json -->

# FAIDataProviderFloatValue

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefaultValue` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAIDataProviderIntValue.json -->

# FAIDataProviderIntValue

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefaultValue` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAIDataProviderTypedValue.json -->

# FAIDataProviderTypedValue

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PropertyType` | `TSubclassOf < UProperty >` | type of value |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAIDataProviderValue.json -->

# FAIDataProviderValue

AIDataProvider is an object that can provide collection of properties
  associated with bound pawn owner or request Id.
 
  Editable properties are used to set up provider instance,
  creating additional filters or ways of accessing data (e.g. gameplay tag of ability)
 
  Non editable properties are holding data

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CachedProperty` | `UProperty *` | cached uproperty of provider |
| `DataBinding` | `UAIDataProvider *` | (optional) provider for dynamic data binding |
| `DataField` | `FName` | name of provider's value property |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAIMoveRequest.json -->

# FAIMoveRequest

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GoalActor` | `AActor *` | move goal: actor |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAINoiseEvent.json -->

# FAINoiseEvent

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NoiseLocation` | `FVector` | if not set Instigator's location will be used |
| `Loudness` | `float` | Loudness modifier of the sound.<br>	  If MaxRange is non-zero, this modifies the range (by multiplication).<br>	  If there is no MaxRange, then if Square(DistanceToSound) <= Square(HearingRange)  Loudness, the sound is heard, false otherwise. |
| `MaxRange` | `float` | Max range at which the sound can be heard. Multiplied by Loudness.<br>	  A value of 0 indicates that there is no range limit, though listeners are still limited by their own hearing range. |
| `Instigator` | `AActor *` | Actor triggering the sound. |
| `Tag` | `FName` | Named identifier for the noise. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAIPredictionEvent.json -->

# FAIPredictionEvent

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Requestor` | `AActor *` | - |
| `PredictedActor` | `AActor *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAIRequestID.json -->

# FAIRequestID

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RequestID` | `uint32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAISenseAffiliationFilter.json -->

# FAISenseAffiliationFilter

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bDetectEnemies` | `uint32` | - |
| `bDetectNeutrals` | `uint32` | - |
| `bDetectFriendlies` | `uint32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAISightEvent.json -->

# FAISightEvent

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SeenActor` | `AActor *` | - |
| `Observer` | `AActor *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAIStimulus.json -->

# FAIStimulus

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Age` | `float` | - |
| `ExpirationAge` | `float` | - |
| `Strength` | `float` | - |
| `StimulusLocation` | `FVector` | - |
| `ReceiverLocation` | `FVector` | - |
| `Tag` | `FName` | - |
| `bSuccessfullySensed` | `uint32` | - |
| `bExpired` | `uint32` | this means the stimulus was originally created with a "time limit" and this time has passed. <br>	 	Expiration also results in calling MarkNoLongerSensed |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAITeamStimulusEvent.json -->

# FAITeamStimulusEvent

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Broadcaster` | `AActor *` | - |
| `Enemy` | `AActor *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAITouchEvent.json -->

# FAITouchEvent

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TouchReceiver` | `AActor *` | - |
| `OtherActor` | `AActor *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAmbientCube.json -->

# FAmbientCube

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Saturation` | `float` | - |
| `Faces` | `FAmbientCubeFace` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAmbientCube2.json -->

# FAmbientCube2

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bUseCustomCapture` | `bool` | - |
| `Saturation` | `float` | - |
| `Face_PosX_Tint` | `FLinearColor` | - |
| `Face_NegX_Tint` | `FLinearColor` | - |
| `Face_PosY_Tint` | `FLinearColor` | - |
| `Face_NegY_Tint` | `FLinearColor` | - |
| `Face_PosZ_Tint` | `FLinearColor` | - |
| `Face_NegZ_Tint` | `FLinearColor` | - |
| `Face_PosX` | `FLinearColor` | - |
| `Face_NegX` | `FLinearColor` | - |
| `Face_PosY` | `FLinearColor` | - |
| `Face_NegY` | `FLinearColor` | - |
| `Face_PosZ` | `FLinearColor` | - |
| `Face_NegZ` | `FLinearColor` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAmbientCubeFace.json -->

# FAmbientCubeFace

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Color` | `FColor` | - |
| `Tint` | `FLinearColor` | - |
| `FaceSaturation` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnchorData.json -->

# FAnchorData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Offsets` | `FMargin` | Offset. |
| `Anchors` | `FAnchors` | Anchors. |
| `Alignment` | `FVector2D` | Alignment is the pivot point of the widget.  Starting in the upper left at (0,0),<br>	  ending in the lower right at (1,1).  Moving the alignment point allows you to move<br>	  the origin of the widget. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnchors.json -->

# FAnchors

Describes how a widget is anchored.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Minimum` | `FVector2D` | Holds the minimum anchors, left + top. |
| `Maximum` | `FVector2D` | Holds the maximum anchors, right + bottom. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAngularDriveConstraint.json -->

# FAngularDriveConstraint

Angular Drive

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TwistDrive` | `FConstraintDrive` | Controls the twist (roll) constraint drive between current orientationvelocity and target orientationvelocity. This is available as long as the twist limit is set to free or limited. |
| `SwingDrive` | `FConstraintDrive` | Controls the cone constraint drive between current orientationvelocity and target orientationvelocity. This is available as long as there is at least one swing limit set to free or limited. |
| `SlerpDrive` | `FConstraintDrive` | Controls the SLERP (spherical lerp) drive between current orientationvelocity and target orientationvelocity. NOTE: This is only available when all three angular limits are either free or limited. Locking any angular limit will turn off the drive implicitly. |
| `OrientationTarget` | `FRotator` | Target orientation relative to the the body reference frame. |
| `AngularVelocityTarget` | `FVector` | Target angular velocity relative to the body reference frame. |
| `AngularDriveMode` | `TEnumAsByte < enum EAngularDriveMode :: Type >` | Whether motors use SLERP (spherical lerp) or decompose into a Swing motor (cone constraints) and Twist motor (roll constraints). NOTE: SLERP will NOT work if any of the angular constraints are locked. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimationActiveTransitionEntry.json -->

# FAnimationActiveTransitionEntry

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BlendProfile` | `UBlendProfile *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimationEventBinding.json -->

# FAnimationEventBinding

Used to manage different animation event bindings that users want callbacks on.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Delegate` | `FWidgetAnimationDynamicEvent` | The callback. |
| `Animation` | `UWidgetAnimation *` | The animation to look for. |
| `AnimationEvent` | `EWidgetAnimationEvent` | The type of animation event. |
| `UserTag` | `FName` | A user tag used to only get callbacks for specific runs of the animation. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimationGroupReference.json -->

# FAnimationGroupReference

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GroupName` | `FName` | - |
| `GroupRole` | `TEnumAsByte < EAnimGroupRole :: Type >` | - |
| `bNeedAnimNotifyWhenNotLeader` | `bool` | - |
| `bShouldSortWithTimeAccumulator` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimationRecordingSettings.json -->

# FAnimationRecordingSettings

Settings describing how to record an animation

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bRecordInWorldSpace` | `bool` | Whether to record animation in world space, defaults to true |
| `bRemoveRootAnimation` | `bool` | Whether to remove the root bone transform from the animation |
| `bAutoSaveAsset` | `bool` | Whether to auto-save asset when recording is completed. Defaults to false |
| `SampleRate` | `float` | Sample rate of the recorded animation (in Hz) |
| `Length` | `float` | Maximum length of the animation recorded (in seconds). If zero the animation will keep on recording until stopped. |
| `InterpMode` | `TEnumAsByte < ERichCurveInterpMode >` | Interpolation mode for the recorded keys. |
| `TangentMode` | `TEnumAsByte < ERichCurveTangentMode >` | Tangent mode for the recorded keys. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimationState.json -->

# FAnimationState

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Transitions` | `TArray < FAnimationTransitionRule >` | - |
| `StateRootNodeIndex` | `int32` | - |
| `StartNotify` | `int32` | - |
| `EndNotify` | `int32` | - |
| `FullyBlendedNotify` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimationStateBase.json -->

# FAnimationStateBase

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StateName` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimationTransitionBetweenStates.json -->

# FAnimationTransitionBetweenStates

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PreviousState` | `int32` | - |
| `NextState` | `int32` | - |
| `CrossfadeDuration` | `float` | - |
| `StartNotify` | `int32` | - |
| `EndNotify` | `int32` | - |
| `InterruptNotify` | `int32` | - |
| `BlendMode` | `EAlphaBlendOption` | - |
| `CustomCurve` | `UCurveFloat *` | - |
| `BlendProfile` | `UBlendProfile *` | - |
| `LogicType` | `TEnumAsByte < ETransitionLogicType :: Type >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimationTransitionRule.json -->

# FAnimationTransitionRule

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RuleToExecute` | `FName` | - |
| `TransitionReturnVal` | `bool` | What RuleToExecute must return to take transition (for bidirectional transitions) |
| `TransitionIndex` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimControlTrackKey.json -->

# FAnimControlTrackKey

Structure used for holding information for one animation played on the Anim Control track.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StartTime` | `float` | Position in the Matinee sequence to start playing this animation. |
| `AnimSeq` | `UAnimSequence *` | Animation Sequence to play |
| `AnimStartOffset` | `float` | Time to start playing AnimSequence at. |
| `AnimEndOffset` | `float` | Time to end playing the AnimSequence at. |
| `AnimPlayRate` | `float` | Playback speed of this animation. |
| `bLooping` | `uint32` | Should this animation loop. |
| `bReverse` | `uint32` | Whether to play the animation in reverse or not. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimGroupInfo.json -->

# FAnimGroupInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Name` | `FName` | - |
| `Color` | `FLinearColor` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimGroupInstance.json -->

# FAnimGroupInstance

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ActivePlayers` | `TArray < FAnimTickRecord >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimLegIKDefinition.json -->

# FAnimLegIKDefinition

Per foot definitions

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `IKFootBone` | `FBoneReference` | - |
| `FKFootBone` | `FBoneReference` | - |
| `NumBonesInLimb` | `int32` | - |
| `FootBoneForwardAxis` | `TEnumAsByte < EAxis :: Type >` | Forward Axis for Foot bone. |
| `bEnableRotationLimit` | `bool` | If enabled, we prevent the leg from bending backwards and enforce a min compression angle |
| `MinRotationAngle` | `float` | Only used if bEnableRotationLimit is enabled. Prevents the leg from folding onto itself,<br>	 and forces at least this angle between Parent and Child bone. |
| `bEnableKneeTwistCorrection` | `bool` | Enable Knee Twist correction, by comparing Foot FK with Foot IK orientation. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimLinkableElement.json -->

# FAnimLinkableElement

Used to describe an element that can be linked to a segment in a montage or sequence.
 	Usage: 
 		Inherit from FAnimLinkableElement and make sure to call LinkMontage or LinkSequence
 		both on creation and on loading the element. From there SetTime and GetTime should be
 		used to control where this element is in the montage or sequence.
 	
 		For more advanced usage, see this implementation used in FAnimNotifyEvent where
 		we have a secondary link to handle a duration
 		@see FAnimNotifyEvent

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LinkedMontage` | `UAnimMontage *` | The montage that this element is currently linked to |
| `SlotIndex` | `int32` | The slot index we are currently using within LinkedMontage |
| `SegmentIndex` | `int32` | The index of the segment we are linked to within the slot we are using |
| `LinkMethod` | `TEnumAsByte < EAnimLinkMethod :: Type >` | The method we are using to calculate our times |
| `CachedLinkMethod` | `TEnumAsByte < EAnimLinkMethod :: Type >` | Cached link method used to transform the time when LinkMethod changes, always relates to the currently stored time |
| `SegmentBeginTime` | `float` | The absolute time in the montage that our currently linked segment begins |
| `SegmentLength` | `float` | The absolute length of our currently linked segment |
| `LinkValue` | `float` | The time of this montage. This will differ depending upon the method we are using to link the time for this element |
| `LinkedSequence` | `UAnimSequenceBase *` | The Animation Sequence that this montage element will link to, when the sequence changes<br>	  in either length or rate; the element will correctly place itself in relation to the sequence |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimMontageInstance.json -->

# FAnimMontageInstance

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |
| `MontageNoGCID` | `int64` | - |
| `bPlaying` | `bool` | - |
| `bIsStopping` | `bool` | - |
| `DefaultBlendTimeMultiplier` | `float` | - |
| `IgnoreNotifyType` | `TArray < FString >` | - |
| `CustomSectionsPlayInfo` | `TArray < FMontageSectionsPlayInfo >` | - |
| `NextSections` | `TArray < int32 >` | - |
| `PrevSections` | `TArray < int32 >` | - |
| `ActiveStateBranchingPoints` | `TArray < FAnimNotifyEvent >` | Currently Active AnimNotifyState, stored as a copy of the event as we need to<br>		is removed correctly. |
| `Position` | `float` | - |
| `PlayRate` | `float` | - |
| `Blend` | `FAlphaBlend` | - |
| `DisableRootMotionCount` | `int32` | - |
| `RandomJumpTimes` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_AimOffsetLookAt.json -->

# FAnimNode_AimOffsetLookAt

This node uses a source transform of a socket on the skeletal mesh to automatically calculate
  Yaw and Pitch directions for a referenced aim offset given a point in the world to look at.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BasePose` | `FPoseLink` | - |
| `LODThreshold` | `int32` | Max LOD that this node is allowed to run<br>	 For example if you have LODThreadhold to be 2, it will run until LOD 2 (based on 0 index)<br>	 when the component LOD becomes 3, it will stop updateevaluate<br>	 currently transition would be issue and that has to be re-visited |
| `bIsLODEnabled` | `bool` | - |
| `LookAtLocation` | `FVector` | Location, in world space to look at |
| `SourceSocketName` | `FName` | Socket to treat as the look at source |
| `PivotSocketName` | `FName` | Socket to treat as the look at pivot (optional). This will overwrite the translation of the source socket transform to better match the lookat direction |
| `SocketAxis` | `FVector` | Axis in the socket transform to consider the 'forward' or look at axis |
| `Alpha` | `float` | Amount of this node to blend into the output pose |
| `SocketBoneReference` | `FBoneReference` | Cached reference to the source socket's bone |
| `SocketLocalTransform` | `FTransform` | Cached local transform of the source socket |
| `PivotSocketBoneReference` | `FBoneReference` | Cached reference to the pivot socket's bone |
| `PivotSocketLocalTransform` | `FTransform` | Cached local transform of the pivot socket |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_AnimDynamics.json -->

# FAnimNode_AnimDynamics

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bUseLazyChange` | `bool` | - |
| `LazyChangeInterval` | `float` | - |
| `LazyChangeCurve` | `UCurveFloat *` | - |
| `bLazySimulate_Location` | `bool` | - |
| `bLazySimulate_Location_OnlyRoot` | `bool` | - |
| `LazySimulateAlpha_Location` | `float` | - |
| `bLazySimulate_Rotation` | `bool` | - |
| `bLazySimulate_Rotation_OnlyRoot` | `bool` | - |
| `LazySimulateAlpha_Rotation` | `float` | - |
| `SimulationSpace` | `AnimPhysSimSpaceType` | The space used to run the simulation |
| `RelativeSpaceBone` | `FBoneReference` | When in BoneRelative sim space, the simulation will use this bone as the origin |
| `bChain` | `bool` | Set to true to use the solver to simulate a connected chain |
| `BoundBone` | `FBoneReference` | The bone to attach the physics body to, if bChain is true this is the top of the chain |
| `ChainEnd` | `FBoneReference` | If bChain is true this is the bottom of the chain, otherwise ignored |
| `BoxExtents` | `FVector` | Extents of the box to use for simulation |
| `LocalJointOffset` | `FVector` | Vector relative to the body being simulated to attach the constraint to |
| `OldLocalJointOffset` | `FVector` | - |
| `GravityScale` | `float` | Scale for gravity, higher values increase forces due to gravity |
| `bLinearSpring` | `bool` | If true the body will attempt to spring back to its initial position |
| `bAngularSpring` | `bool` | If true the body will attempt to align itself with the specified angular target |
| `LinearSpringConstant` | `float` | Spring constant to use when calculating linear springs, higher values mean a stronger spring. |
| `AngularSpringConstant` | `float` | Spring constant to use when calculating angular springs, higher values mean a stronger spring |
| `bEnableWind` | `bool` | Whether or not wind is enabled for the bodies in this simulation |
| `bWindWasEnabled` | `bool` | - |
| `WindScale` | `float` | Scale to apply to calculated wind velocities in the solver |
| `bOverrideLinearDamping` | `bool` | If true, the override value will be used for linear damping |
| `LinearDampingOverride` | `float` | Overridden linear damping value |
| `bOverrideAngularDamping` | `bool` | If true, the override value will be used for angular damping |
| `AngularDampingOverride` | `float` | Overridden angular damping value |
| `bOverrideAngularBias` | `bool` | If true, the override value will be used for the angular bias for bodies in this node. <br>	   Angular bias is essentially a twist reduction for chain forces and defaults to a value to keep chains stability<br>	   in check. When using single-body systems sometimes angular forces will look like they are "catching-up" with<br>	   the mesh, if that's the case override this and push it towards 1.0f until it settles correctly |
| `AngularBiasOverride` | `float` | Overridden angular bias value<br>	   Angular bias is essentially a twist reduction for chain forces and defaults to a value to keep chains stability<br>	   in check. When using single-body systems sometimes angular forces will look like they are "catching-up" with<br>	   the mesh, if that's the case override this and push it towards 1.0f until it settles correctly |
| `bDoUpdate` | `bool` | If true we will perform physics update, otherwise skip - allows visualisation of the initial state of the bodies |
| `bDoEval` | `bool` | If true we will perform bone transform evaluation, otherwise skip - allows visualisation of the initial anim state compared to the physics sim |
| `NumSolverIterationsPreUpdate` | `int32` | Number of update passes on the linear and angular limits before we solve the position of the bodies recommended to be four times the value of NumSolverIterationsPostUpdate |
| `NumSolverIterationsPostUpdate` | `int32` | Number of update passes on the linear and angular limits after we solve the position of the bodies, recommended to be around a quarter of NumSolverIterationsPreUpdate |
| `ConstraintSetup` | `FAnimPhysConstraintSetup` | Data describing the constraints we will apply to the body |
| `bUseDynamicAngularLimits` | `bool` | if set, will use Dynamic_AngularLimits as ConstraintSetup.AngularLimits when UpdateLimits |
| `Dynamic_AngularLimitsMin` | `FVector` | if bUseDynamicAngularLimits set, will use Dynamic_AngularLimitsMin as ConstraintSetup.AngularLimitsMin when UpdateLimits |
| `Dynamic_AngularLimitsMax` | `FVector` | if bUseDynamicAngularLimits set, will use Dynamic_AngularLimitsMax as ConstraintSetup.AngularLimitsMax when UpdateLimits |
| `bUsePlanarLimit` | `bool` | Whether to evaluate planar limits |
| `PlanarLimits` | `TArray < FAnimPhysPlanarLimit >` | List of available planar limits for this node |
| `bUseSphericalLimits` | `bool` | Whether to evaluate spherical limits |
| `SphericalLimits` | `TArray < FAnimPhysSphericalLimit >` | List of available spherical limits for this node |
| `CollisionType` | `AnimPhysCollisionType` | Resolution method for planar limits |
| `SphereCollisionRadius` | `float` | Radius to use if CollisionType is set to CustomSphere |
| `NonEvaluateFrameNum` | `int32` | Non Evaluate frame from start |
| `ExternalForce` | `FVector` | An external force to apply to all bodies in the simulation when ticked, specified in world space |
| `BoneShiftTolerenceChecker` | `FAnimNodeBoneShiftTolerenceChecker` | Bone Shift Tolerence Check Start |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_AnimDynamics_UE5.json -->

# FAnimNode_AnimDynamics_UE5

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LinearDampingOverride` | `float` | Overridden linear damping value. The default is 0.7. Values below 0.7 won't have an effect. |
| `AngularDampingOverride` | `float` | Overridden angular damping value. The default is 0.7. Values below 0.7 won't have an effect. |
| `RelativeSpaceBone` | `FBoneReference` | When in BoneRelative sim space, the simulation will use this bone as the origin |
| `BoundBone` | `FBoneReference` | The bone to attach the physics body to, if bChain is true this is the top of the chain |
| `ChainEnd` | `FBoneReference` | If bChain is true this is the bottom of the chain, otherwise ignored |
| `PhysicsBodyDefinitions` | `TArray < FAnimPhysBodyDefinition_UE5 >` | - |
| `GravityScale` | `float` | Scale for gravity, higher values increase forces due to gravity |
| `GravityOverride` | `FVector` | Gravity Override Value |
| `LinearSpringConstant` | `float` | Spring constant to use when calculating linear springs, higher values mean a stronger spring.<br>	  You need to enable the Linear Spring checkbox for this to have an effect. |
| `AngularSpringConstant` | `float` | Spring constant to use when calculating angular springs, higher values mean a stronger spring.<br>	  You need to enable the Angular Spring checkbox for this to have an effect.<br>	  Note: Make sure to also set the Angular Target Axis and Angular Target in the Constraint Setup for this to have an effect. |
| `WindScale` | `float` | Scale to apply to calculated wind velocities in the solver |
| `ComponentLinearAccScale` | `FVector` | When using non-world-space sim, this controls how much of the components world-space acceleration is passed on to the local-space simulation. |
| `ComponentLinearVelScale` | `FVector` | When using non-world-space sim, this applies a 'drag' to the bodies in the local space simulation, based on the components world-space velocity. |
| `ComponentAppliedLinearAccClamp` | `FVector` | When using non-world-space sim, this is an overall clamp on acceleration derived from ComponentLinearAccScale and ComponentLinearVelScale, to ensure it is not too large. |
| `AngularBiasOverride` | `float` | Overridden angular bias value<br>	   Angular bias is essentially a twist reduction for chain forces and defaults to a value to keep chains stability<br>	  in check. When using single-body systems sometimes angular forces will look like they are "catching-up" with<br>	  the mesh, if that's the case override this and push it towards 1.0f until it settles correctly |
| `NumSolverIterationsPreUpdate` | `int32` | Number of update passes on the linear and angular limits before we solve the position of the bodies recommended to be four times the value of NumSolverIterationsPostUpdate |
| `NumSolverIterationsPostUpdate` | `int32` | Number of update passes on the linear and angular limits after we solve the position of the bodies, recommended to be around a quarter of NumSolverIterationsPreUpdate |
| `SphericalLimits` | `TArray < FAnimPhysSphericalLimit_UE5 >` | List of available spherical limits for this node |
| `ExternalForce` | `FVector` | An external force to apply to all bodies in the simulation when ticked, specified in world space |
| `PlanarLimits` | `TArray < FAnimPhysPlanarLimit_UE5 >` | List of available planar limits for this node |
| `SimulationSpace` | `AnimPhysSimSpaceType_UE5` | The space used to run the simulation |
| `bUseSphericalLimits` | `uint8` | Whether to evaluate spherical limits |
| `bUsePlanarLimit` | `uint8` | Whether to evaluate planar limits |
| `bDoUpdate` | `uint8` | If true we will perform physics update, otherwise skip - allows visualization of the initial state of the bodies |
| `bDoEval` | `uint8` | If true we will perform bone transform evaluation, otherwise skip - allows visualization of the initial anim state compared to the physics sim |
| `bOverrideLinearDamping` | `uint8` | If true, the override value will be used for linear damping |
| `bOverrideAngularBias` | `uint8` | If true, the override value will be used for the angular bias for bodies in this node. <br>	   Angular bias is essentially a twist reduction for chain forces and defaults to a value to keep chains stability<br>	   in check. When using single-body systems sometimes angular forces will look like they are "catching-up" with<br>	   the mesh, if that's the case override this and push it towards 1.0f until it settles correctly |
| `bOverrideAngularDamping` | `uint8` | If true, the override value will be used for angular damping |
| `bEnableWind` | `uint8` | Whether or not wind is enabled for the bodies in this simulation |
| `bUseGravityOverride` | `uint8` | Use gravity override value vs gravity scale |
| `bGravityOverrideInSimSpace` | `uint8` | If true the gravity override value is defined in simulation space, by default it is in world space |
| `bLinearSpring` | `uint8` | If true the body will attempt to spring back to its initial position |
| `bAngularSpring` | `uint8` | If true the body will attempt to align itself with the specified angular target |
| `bChain` | `uint8` | Set to true to use the solver to simulate a connected chain |
| `BoxExtents_DEPRECATED` | `FVector` | - |
| `LocalJointOffset_DEPRECATED` | `FVector` | - |
| `ConstraintSetup_DEPRECATED` | `FAnimPhysConstraintSetup_UE5` | - |
| `CollisionType_DEPRECATED` | `AnimPhysCollisionType` | - |
| `SphereCollisionRadius_DEPRECATED` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_ApplyAdditive.json -->

# FAnimNode_ApplyAdditive

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Base` | `FPoseLink` | - |
| `Additive` | `FPoseLink` | - |
| `Alpha` | `float` | - |
| `AlphaScaleBias` | `FInputScaleBias` | - |
| `LODThreshold` | `int32` | Max LOD that this node is allowed to run<br>	  For example if you have LODThreadhold to be 2, it will run until LOD 2 (based on 0 index)<br>	  when the component LOD becomes 3, it will stop updateevaluate<br>	  currently transition would be issue and that has to be re-visited |
| `ActualAlpha` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_ApplyMeshSpaceAdditive.json -->

# FAnimNode_ApplyMeshSpaceAdditive

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Base` | `FPoseLink` | - |
| `Additive` | `FPoseLink` | - |
| `Alpha` | `float` | - |
| `AlphaScaleBias` | `FInputScaleBias` | - |
| `LODThreshold` | `int32` | Max LOD that this node is allowed to run<br>	 For example if you have LODThreadhold to be 2, it will run until LOD 2 (based on 0 index)<br>	 when the component LOD becomes 3, it will stop updateevaluate<br>	 currently transition would be issue and that has to be re-visited |
| `ActualAlpha` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_AssetPlayerBase.json -->

# FAnimNode_AssetPlayerBase

Base class for any asset playing anim node

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bIgnoreForRelevancyTest` | `bool` | If true, "Relevant anim" nodes that look for the highest weighted animation in a state will ignore<br>	   this node |
| `GroupIndex` | `int32` | - |
| `GroupName` | `FName` | - |
| `GroupRole` | `TEnumAsByte < EAnimGroupRole :: Type >` | - |
| `bNeedAnimNotifyWhenNotLeader` | `bool` | - |
| `bShouldSortWithTimeAccumulator` | `bool` | - |
| `BlendWeight` | `float` | Last encountered blendweight for this node |
| `InternalTimeAccumulator` | `float` | Accumulated time used to reference the asset in this node |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_Base.json -->

# FAnimNode_Base

This is the base of all runtime animation nodes
 
  To create a new animation node:
    Create a struct derived from FAnimNode_Base - this is your runtime node
    Create a class derived from UAnimGraphNode_Base, containing an instance of your runtime node as a member - this is your visualeditor-only node

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NodeUID` | `int32` | - |
| `EvaluateGraphExposedInputs` | `FExposedValueHandler` | - |
| `bEnableAsyncInitNode` | `bool` | - |
| `bSkipAnimNodeEnabled` | `bool` | - |
| `SkipAnimNodeThresholdOverride` | `float` | - |
| `NodeTag` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_BlendBoneByChannel.json -->

# FAnimNode_BlendBoneByChannel

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `A` | `FPoseLink` | - |
| `B` | `FPoseLink` | - |
| `Alpha` | `float` | - |
| `AlphaScaleBias` | `FInputScaleBias` | - |
| `BoneDefinitions` | `TArray < FBlendBoneByChannelEntry >` | - |
| `TransformsSpace` | `TEnumAsByte < EBoneControlSpace >` | Space to convert transforms into prior to copying channels |
| `InternalBlendAlpha` | `float` | - |
| `bBIsRelevant` | `bool` | - |
| `ValidBoneEntries` | `TArray < FBlendBoneByChannelEntry >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_BlendListBase.json -->

# FAnimNode_BlendListBase

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BlendPose` | `TArray < FPoseLink >` | - |
| `BlendTime` | `TArray < float >` | - |
| `TransitionType` | `EBlendListTransitionType` | - |
| `BlendType` | `EAlphaBlendOption` | - |
| `CustomBlendCurve` | `UCurveFloat *` | - |
| `BlendProfile` | `UBlendProfile *` | - |
| `ResetFrameCountSubValue` | `int32` | - |
| `LastFrameCount` | `uint64` | - |
| `Blends` | `TArray < struct FAlphaBlend >` | - |
| `BlendWeights` | `TArray < float >` | - |
| `RemainingBlendTimes` | `TArray < float >` | - |
| `LastActiveChildIndex` | `int32` | - |
| `PerBoneSampleData` | `TArray < FBlendSampleData >` | - |
| `bResetChildOnActivation` | `bool` | This reinitializes child pose when re-activated. For example, when active child changes |
| `bResetChildOnBlendListChange` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_BlendListByBool.json -->

# FAnimNode_BlendListByBool

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bActiveValue` | `bool` | - |
| `ActiveValueWhenSkipAnimNode` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_BlendListByEnum.json -->

# FAnimNode_BlendListByEnum

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EnumToPoseIndex` | `TArray < int32 >` | - |
| `ActiveEnumValue` | `uint8` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_BlendListByInt.json -->

# FAnimNode_BlendListByInt

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ActiveChildIndex` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_BlendListBySlot.json -->

# FAnimNode_BlendListBySlot

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ActiveSlotName` | `FName` | - |
| `bUseList` | `bool` | - |
| `ActiveSlotNameList` | `TArray < FName >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_BlendListBySlots.json -->

# FAnimNode_BlendListBySlots

多个蒙太奇Slot播放检测过渡融合

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CheckActiveSlotNames` | `TArray < FName >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_BlendSpaceEvaluator.json -->

# FAnimNode_BlendSpaceEvaluator

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NormalizedTime` | `float` | Normalized time between [0,1]. The actual length of a blendspace is dynamic based on the coordinate, so it is exposed as a normalized value. |
| `CheckReTickFrameCounterSubValue` | `int32` | - |
| `bEnableTriggerNotify` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_BlendSpacePlayer.json -->

# FAnimNode_BlendSpacePlayer

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `X` | `float` | - |
| `Y` | `float` | - |
| `Z` | `float` | - |
| `PlayRate` | `float` | - |
| `bLoop` | `bool` | - |
| `StartPosition` | `float` | - |
| `BlendSpace` | `UBlendSpaceBase *` | - |
| `bResetPlayTimeWhenBlendSpaceChanges` | `bool` | - |
| `bResetPlayTimeWhenBlendSpaceReactive` | `bool` | - |
| `bResetSampleCacheWhenBlendSpaceChanges` | `bool` | - |
| `BlendFilter` | `FBlendFilter` | - |
| `BlendSampleDataCache` | `TArray < FBlendSampleData >` | - |
| `PreviousBlendSpace` | `UBlendSpaceBase *` | - |
| `EnableBSBlend` | `bool` | - |
| `BSBlendOutTime` | `float` | - |
| `BSBlendOutBlendOption` | `EAlphaBlendOption` | - |
| `BSBlendMode` | `EBSBlendMode` | - |
| `BSBlendBySyncGroup` | `bool` | - |
| `BSBlendResetNewTimeAccumulator` | `bool` | - |
| `BSBlendOutWeightScale` | `float` | - |
| `bClearBlendOutPoseWhenBlendSpaceReactive` | `bool` | - |
| `BSBlendOutTime_Counter` | `float` | - |
| `BSBlendOutTime_Alpha` | `float` | - |
| `BSBlendOutWeight` | `float` | - |
| `LastBlendSpace` | `UBlendSpaceBase *` | - |
| `BlendOutPlayers_Cache` | `TArray < UBlendSpaceBase * >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_BoneBlendFilter.json -->

# FAnimNode_BoneBlendFilter

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FilterWithBlackList` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_BoneDrivenController.json -->

# FAnimNode_BoneDrivenController

This is the runtime version of a bone driven controller, which maps part of the state from one bone to another (e.g., 2  source.x -> target.z)

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceBone` | `FBoneReference` | - |
| `SourceComponent` | `TEnumAsByte < EComponentType :: Type >` | - |
| `DrivingCurve` | `UCurveFloat *` | Curve used to map from the source attribute to the driven attributes if present (otherwise the Multiplier will be used) |
| `Multiplier` | `float` | - |
| `bUseRange` | `bool` | - |
| `RangeMin` | `float` | - |
| `RangeMax` | `float` | - |
| `RemappedMin` | `float` | - |
| `RemappedMax` | `float` | - |
| `DestinationMode` | `EDrivenDestinationMode` | - |
| `ParameterName` | `FName` | Name of Morph Target to drive using the source attribute |
| `TargetBone` | `FBoneReference` | - |
| `TargetComponent_DEPRECATED` | `TEnumAsByte < EComponentType :: Type >` | - |
| `bAffectTargetTranslationX` | `uint32` | - |
| `bAffectTargetTranslationY` | `uint32` | - |
| `bAffectTargetTranslationZ` | `uint32` | - |
| `bAffectTargetRotationX` | `uint32` | - |
| `bAffectTargetRotationY` | `uint32` | - |
| `bAffectTargetRotationZ` | `uint32` | - |
| `bAffectTargetScaleX` | `uint32` | - |
| `bAffectTargetScaleY` | `uint32` | - |
| `bAffectTargetScaleZ` | `uint32` | - |
| `ModificationMode` | `EDrivenBoneModificationMode` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_BoneFollowChain.json -->

# FAnimNode_BoneFollowChain

make bone list move like snake

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BasePose` | `FPoseLink` | - |
| `ToParentDisTolerence` | `int32` | - |
| `ToParentMaxDisTolerence` | `int32` | - |
| `bLeaderBoneMoveFromAnim` | `bool` | - |
| `bClearParentBonePathWhenNoMove` | `bool` | - |
| `bEnableTerrainAdaptFeature` | `bool` | - |
| `TerrainTraceStart` | `float` | - |
| `TerrainTraceEnd` | `float` | - |
| `ToParentRotationScale` | `float` | - |
| `bLerpBoneRotaion` | `bool` | - |
| `bLerpBoneRotaionCalcCurFrameBoneTransform` | `bool` | - |
| `MaxBonePathRecordBufferSize` | `int32` | - |
| `LeaderBone` | `FBoneReference` | - |
| `FollowBoneList` | `TArray < FBoneReference >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_BoneMirror.json -->

# FAnimNode_BoneMirror

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Source` | `FPoseLink` | The source pose |
| `AutoLRConfigs` | `TArray < FBoneMirrorConfig_AutoLR >` | - |
| `GivenNameConfigs` | `TArray < FBoneMirrorConfig_GivenName >` | - |
| `Configs` | `TArray < FBoneMirrorConfig >` | - |
| `PreviewBoneMirrorMapData` | `TArray < FBoneMirrorMapData >` | 程序自动生成的镜像骨骼对，仅用于编辑器下检查是否符合预期，不可修改。<br>	  骨骼名字以_INVALID结尾说明没有对应的镜像骨骼，这些都不会被列入实际镜像列表中 |
| `bMirror` | `bool` | - |
| `bResetChild` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_BoneRetarget.json -->

# FAnimNode_BoneRetarget

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BasePose` | `FPoseLink` | - |
| `bUseRetargetFeature` | `bool` | - |
| `bAssignedInverseRetargetMode` | `bool` | - |
| `bIgnoreAssignedRefPose` | `bool` | - |
| `AssignedInverseRetargetMesh` | `USkeletalMesh *` | - |
| `InverseRetargetBoneDiffTolerance` | `float` | - |
| `InverseRetargetTraceBoneList` | `TArray < FName >` | - |
| `bInverseRetargetDynamicMontage_AdjustCoreBone` | `bool` | - |
| `InverseRetargetDynamicMontage_CoreBone` | `FName` | - |
| `InverseRetargetDynamicMontage_TipBone` | `FName` | - |
| `bConsiderMasterPoseRetarget` | `bool` | - |
| `bForceUseBaseSkeletonAsRetargetSource` | `bool` | - |
| `OverrideBoneTranslationRetargetingModeKey` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_CachedBoneTransform.json -->

# FAnimNode_CachedBoneTransform

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Source` | `FPoseLink` | - |
| `BoneToCache` | `FBoneReference` | - |
| `CacheFlagName` | `FName` | - |
| `bSaveCacheToRootAnimIns` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_CCDIK.json -->

# FAnimNode_CCDIK

Controller which implements the CCDIK IK approximation algorithm

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EffectorLocation` | `FVector` | Coordinates for target location of tip bone - if EffectorLocationSpace is bone, this is the offset from Target Bone to use as target location |
| `EffectorLocationSpace` | `TEnumAsByte < enum EBoneControlSpace >` | Reference frame of Effector Transform. |
| `EffectorTarget` | `FBoneSocketTarget` | If EffectorTransformSpace is a bone, this is the bone to use. |
| `TipBone` | `FBoneReference` | Name of tip bone |
| `RootBone` | `FBoneReference` | Name of the root bone |
| `Precision` | `float` | Tolerance for final tip location delta from EffectorLocation |
| `MaxIterations` | `int32` | Maximum number of iterations allowed, to control performance. |
| `bStartFromTail` | `bool` | Toggle drawing of axes to debug joint rotation |
| `bEnableRotationLimit` | `bool` | Tolerance for final tip location delta from EffectorLocation |
| `RotationLimitPerJoints` | `TArray < float >` | symmetry rotation limit per joint. Index 0 matches with root bone and last index matches with tip bone. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_CompnentPoseBase.json -->

# FAnimNode_CompnentPoseBase

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bActiveNode` | `bool` | Engine Modify<br>	 Enable Node to be ignored at runtime but keep alpha value no change<br>	 false will ignore (do no or skip) evaluate, but no affect on update |
| `Alpha` | `float` | - |
| `AlphaScaleBias` | `FInputScaleBias` | - |
| `LODThreshold` | `int32` | Max LOD that this node is allowed to run<br>	 For example if you have LODThreadhold to be 2, it will run until LOD 2 (based on 0 index)<br>	 when the component LOD becomes 3, it will stop updateevaluate<br>	 currently transition would be issue and that has to be re-visited |
| `ActualAlpha` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_Constraint.json -->

# FAnimNode_Constraint

Constraint node to parent or world transform for rotationtranslation

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoneToModify` | `FBoneReference` | Name of bone to control. This is the main bone chain to modify from. |
| `ConstraintSetup` | `TArray < FConstraint >` | List of constraints |
| `ConstraintWeights` | `TArray < float >` | Weight data - post edit syncs up to ConstraintSetups |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_ConvertComponentToLocalSpace.json -->

# FAnimNode_ConvertComponentToLocalSpace

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ComponentPose` | `FComponentSpacePoseLink` | - |
| `bBypassForced` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_ConvertLocalToComponentSpace.json -->

# FAnimNode_ConvertLocalToComponentSpace

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LocalPose` | `FPoseLink` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_CopyBone.json -->

# FAnimNode_CopyBone

Simple controller to copy a bone's transform to another one.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceBone` | `FBoneReference` | Source Bone Name to get transform from |
| `TargetBone` | `FBoneReference` | Name of bone to control. This is the main bone chain to modify from. |
| `bCopyTranslation` | `bool` | If Translation should be copied |
| `bCopyRotation` | `bool` | If Rotation should be copied |
| `bCopyScale` | `bool` | If Scale should be copied |
| `ControlSpace` | `TEnumAsByte < EBoneControlSpace >` | Space to convert transforms into prior to copying components |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_CopyBoneDelta.json -->

# FAnimNode_CopyBoneDelta

Simple controller to copy a transform relative to the ref pose to the target bone,
 	instead of the copy bone node which copies the absolute transform

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceBone` | `FBoneReference` | - |
| `TargetBone` | `FBoneReference` | - |
| `bCopyTranslation` | `bool` | - |
| `bCopyRotation` | `bool` | - |
| `bCopyScale` | `bool` | - |
| `CopyMode` | `CopyBoneDeltaMode` | - |
| `TranslationMultiplier` | `float` | - |
| `RotationMultiplier` | `float` | - |
| `ScaleMultiplier` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_CopyBonesFromPose.json -->

# FAnimNode_CopyBonesFromPose

Simple controller to copy a bone's transform to another one.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ToPose` | `FComponentSpacePoseLink` | - |
| `FromPose` | `FComponentSpacePoseLink` | - |
| `CopeBones` | `TArray < FAnimNode_CopyBonesFromPose_Config >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_CopyBonesFromPose_Config.json -->

# FAnimNode_CopyBonesFromPose_Config

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Bone` | `FBoneReference` | Source Bone Name to get transform from |
| `bCopyTranslation` | `bool` | If Translation should be copied |
| `bCopyRotation` | `bool` | If Rotation should be copied |
| `bCopyRotation_Roll` | `bool` | - |
| `bCopyRotation_Pitch` | `bool` | - |
| `bCopyRotation_Yaw` | `bool` | - |
| `bCopyScale` | `bool` | - |
| `ControlSpace` | `TEnumAsByte < EBoneControlSpace >` | Space to convert transforms into prior to copying components |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_CopyMotion.json -->

# FAnimNode_CopyMotion

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BasePose` | `FComponentSpacePoseLink` | - |
| `BasePoseReference` | `FComponentSpacePoseLink` | - |
| `bUseBasePose` | `bool` | - |
| `PoseHistoryTag` | `FName` | - |
| `Delay` | `float` | - |
| `SourceBone` | `FBoneReference` | - |
| `BoneToModify` | `FBoneReference` | Name of bone to control. This is the main bone chain to modify from. |
| `CopySpace` | `FBoneReference` | Bone to use as the reference framespace for our copied transform delta.<br>	If no reference frame is used, the source bone motion will be copied in component space. |
| `ApplySpace` | `FBoneReference` | Bone to use as the reference framespace for our applied transform delta.<br>		If no reference frame is used, the source bone motion will be applied in component space. |
| `TranslationOffset` | `FRotator` | Offset to use before applying the translation deltas (in degrees).<br>		This is useful for changing the direction of motion, relative to our reference framebone |
| `RotationOffset` | `FRotator` | Rotation offset (in degrees) to apply before the rotation deltas.<br>		This is useful for changing the direction of motion, relative to our reference framebone |
| `RotationPivot` | `FVector` | Pivot offset (in local space) to use when applying the rotation.<br>		Any non-zero value will cause the target bone to rotate around the pivot, effectively introducing additional translation. |
| `CurvePrefix` | `FName` | Curve prefix used for the animation curves. Format matches those generated by the LayeringMotionExtractorModifier |
| `TargetCurveName` | `FName` | Name of the curve we're outputting motion to. |
| `TargetCurveScale` | `float` | Which component of motion we're outputting to the curve. |
| `TargetCurveComponent` | `ECopyMotion_Component` | Which component of motion we're outputting to the curve. |
| `TargetCurveRotationAxis` | `TEnumAsByte < EAxis :: Type >` | Axis around which to consider the rotation angle for the curve output. |
| `TranslationX_CurveName` | `FName` | - |
| `TranslationY_CurveName` | `FName` | - |
| `TranslationZ_CurveName` | `FName` | - |
| `RotationRoll_CurveName` | `FName` | - |
| `RotationPitch_CurveName` | `FName` | - |
| `RotationYaw_CurveName` | `FName` | - |
| `TranslationScale` | `FVector` | - |
| `TranslationRemapCurve` | `UCurveVector *` | - |
| `RotationScale` | `float` | - |
| `RotationRemapCurve` | `UCurveFloat *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_CopyPoseFromMesh.json -->

# FAnimNode_CopyPoseFromMesh

Simple controller to copy a bone's transform to another one.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceMeshComponent` | `TWeakObjectPtr < USkeletalMeshComponent >` | This is used by default if it's valid |
| `bUseAttachedParent` | `bool` | If SourceMeshComponent is not valid, and if this is true, it will look for attahced parent as a source |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_CopyPoseFromRemapping.json -->

# FAnimNode_CopyPoseFromRemapping

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceMeshComponent` | `TWeakObjectPtr < USkeletalMeshComponent >` | This is used by default if it's valid |
| `bUseAttachedParent` | `bool` | If SourceMeshComponent is not valid, and if this is true, it will look for attahced parent as a source |
| `bIkGunValid` | `bool` | - |
| `bParentPoseOffset` | `bool` | - |
| `NewFPPPoseOffset` | `FNewFPPPoseOffset` | - |
| `BoneNeedRelevant` | `TMap < FName , FName >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_CurveSource.json -->

# FAnimNode_CurveSource

Supply curves from some external source (e.g. audio)

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourcePose` | `FPoseLink` | - |
| `SourceBinding` | `FName` | The binding of the curve source we want to bind to.<br>	  We will bind to an object that implements ICurveSourceInterface. First we check <br>	  the actor that owns this (if any), then we check each of its components to see if we should<br>	  bind to the source that matches this name. |
| `Alpha` | `float` | How much we wan to blend the curve in by |
| `CurveSource` | `TScriptInterface < ICurveSourceInterface >` | Our bound source |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_EmoteSwitchAdapt.json -->

# FAnimNode_EmoteSwitchAdapt

面部表情骨骼吸附节点
 
  功能：
  - 自动检测当前帧下哪个表情骨骼最接近RefPose位置
  - 将该骨骼吸附到RefPose位置，确保至少有一个完整表情显示
  - 用于解决Linear插值模式下表情切换时的"半表情"问题

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EmoteShowBoneRef` | `FBoneReference` | - |
| `EmoteAdaptBones` | `TArray < FEmoteBoneAdaptConfig >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_Fabrik.json -->

# FAnimNode_Fabrik

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EffectorTransform` | `FTransform` | Coordinates for target location of tip bone - if EffectorLocationSpace is bone, this is the offset from Target Bone to use as target location |
| `EffectorTransformSpace` | `TEnumAsByte < enum EBoneControlSpace >` | Reference frame of Effector Transform. |
| `EffectorTransformBone_DEPRECATED` | `FBoneReference` | If EffectorTransformSpace is a bone, this is the bone to use. |
| `EffectorTarget` | `FBoneSocketTarget` | If EffectorTransformSpace is a bone, this is the bone to use. |
| `EffectorRotationSource` | `TEnumAsByte < enum EBoneRotationSource >` | - |
| `TipBone` | `FBoneReference` | Name of tip bone |
| `RootBone` | `FBoneReference` | Name of the root bone |
| `Precision` | `float` | Tolerance for final tip location delta from EffectorLocation |
| `MaxIterations` | `int32` | Maximum number of iterations allowed, to control performance. |
| `bEnableDebugDraw` | `bool` | Toggle drawing of axes to debug joint rotation |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_HandIKRetargeting.json -->

# FAnimNode_HandIKRetargeting

Node to handle re-targeting of Hand IK bone chain.
  It looks at position in Mesh Space of Left and Right IK bones, and moves Left and Right IK bones to those.
  based on HandFKWeight. (0 = favor left hand, 1 = favor right hand, 0.5 = equal weight).
  This is used so characters of different proportions can handle the same props.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RightHandFK` | `FBoneReference` | Bone for Right Hand FK |
| `LeftHandFK` | `FBoneReference` | Bone for Left Hand FK |
| `RightHandIK` | `FBoneReference` | Bone for Right Hand IK |
| `LeftHandIK` | `FBoneReference` | Bone for Left Hand IK |
| `IKBonesToMove` | `TArray < FBoneReference >` | IK Bones to move. |
| `HandFKWeight` | `float` | Which hand to favor. 0.5 is equal weight for both, 1 = right hand, 0 = left hand. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_HandIKRetargeting_UE5.json -->

# FAnimNode_HandIKRetargeting_UE5

Node to handle re-targeting of Hand IK bone chain.
  It looks at position in Mesh Space of Left and Right IK bones, and moves Left and Right IK bones to those.
  based on HandFKWeight. (0 = favor left hand, 1 = favor right hand, 0.5 = equal weight).
  This is used so characters of different proportions can handle the same props.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RightHandFK` | `FBoneReference` | Bone for Right Hand FK |
| `LeftHandFK` | `FBoneReference` | Bone for Left Hand FK |
| `RightHandIK` | `FBoneReference` | Bone for Right Hand IK |
| `LeftHandIK` | `FBoneReference` | Bone for Left Hand IK |
| `IKBonesToMove` | `TArray < FBoneReference >` | IK Bones to move. |
| `HandFKWeight` | `float` | Which hand to favor. 0.5 is equal weight for both, 1 = right hand, 0 = left hand. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_HeadDodging.json -->

# FAnimNode_HeadDodging

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `HeadBone` | `FBoneReference` | Name of bone to control. This is the main bone chain to modify from. |
| `Depth` | `int` | - |
| `SphereRadius` | `float` | - |
| `CenterOffset` | `FVector` | - |
| `ControlPointOffset` | `float` | - |
| `FarPointLength` | `float` | - |
| `LerpSpeed` | `float` | - |
| `bEnable` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_Inertialization.json -->

# FAnimNode_Inertialization

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Source` | `FPoseLink` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_LayeredBoneBlend.json -->

# FAnimNode_LayeredBoneBlend

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BasePose` | `FPoseLink` | The source pose |
| `BlendPoses` | `TArray < FPoseLink >` | Each layer's blended pose |
| `LayerSetup` | `TArray < FInputBlendPose >` | Configuration for the parts of the skeleton to blend for each layer. Allows<br>	  certain parts of the tree to be blended out or omitted from the pose. |
| `BlendWeights` | `TArray < float >` | The weights of each layer |
| `bMeshSpaceRotationBlend` | `bool` | Whether to blend bone rotations in mesh space or in local space |
| `CurveBlendOption` | `TEnumAsByte < enum ECurveBlendOption :: Type >` | How to blend the layers together |
| `bBlendRootMotionBasedOnRootBone` | `bool` | Whether to incorporate the per-bone blend weight of the root bone when lending root motion |
| `bHasRelevantPoses` | `bool` | - |
| `PerBoneBlendWeights` | `TArray < FPerBoneBlendWeight >` | - |
| `SkeletonGuid` | `FGuid` | - |
| `VirtualBoneGuid` | `FGuid` | - |
| `DesiredBoneBlendWeightsInitMesh` | `TWeakObjectPtr < USkeletalMesh >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_LegIK.json -->

# FAnimNode_LegIK

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ReachPrecision` | `float` | Tolerance for reaching IK Target, in unreal units. |
| `MaxIterations` | `int32` | Max Number of Iterations. |
| `LegsDefinition` | `TArray < FAnimLegIKDefinition >` | - |
| `LegsData` | `TArray < FAnimLegIKData >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_LookAt.json -->

# FAnimNode_LookAt

Simple controller that make a bone to look at the point or another bone

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoneToModify` | `FBoneReference` | Name of bone to control. This is the main bone chain to modify from. |
| `LookAtBone_DEPRECATED` | `FBoneReference` | Target Bone to look at - You can use  LookAtLocation if you need offset from this point. That location will be used in their local space. |
| `LookAtSocket_DEPRECATED` | `FName` | - |
| `LookAtTarget` | `FBoneSocketTarget` | Target socket to look at. Used if LookAtBone is empty. - You can use  LookAtLocation if you need offset from this point. That location will be used in their local space. |
| `LookAtLocation` | `FVector` | Target Offset. It's in world space if LookAtBone is empty or it is based on LookAtBone or LookAtSocket in their local space |
| `LookAtAxis_DEPRECATED` | `TEnumAsByte < EAxisOption :: Type >` | Look at axis, which axis to align to look at point |
| `CustomLookAtAxis_DEPRECATED` | `FVector` | Custom look up axis in local space. Only used if LookAtAxis==EAxisOption::Custom |
| `LookAt_Axis` | `FAxis` | - |
| `bUseLookUpAxis` | `bool` | Whether or not to use Look up axis |
| `LookUpAxis_DEPRECATED` | `TEnumAsByte < EAxisOption :: Type >` | Look up axis in local space |
| `CustomLookUpAxis_DEPRECATED` | `FVector` | Custom look up axis in local space. Only used if LookUpAxis==EAxisOption::Custom |
| `LookUp_Axis` | `FAxis` | - |
| `LookAtClamp` | `float` | Look at Clamp value in degree - if you're look at axis is Z, only X, Y degree of clamp will be used |
| `InterpolationType` | `TEnumAsByte < EInterpolationBlend :: Type >` | - |
| `InterpolationTime` | `float` | - |
| `InterpolationTriggerThreashold` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_MakeDynamicAdditive.json -->

# FAnimNode_MakeDynamicAdditive

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Base` | `FPoseLink` | - |
| `Additive` | `FPoseLink` | - |
| `bMeshSpaceAdditive` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_ModifyBone.json -->

# FAnimNode_ModifyBone

Simple controller that replaces or adds to the translationrotation of a single bone.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoneToModify` | `FBoneReference` | Name of bone to control. This is the main bone chain to modify from. |
| `Translation` | `FVector` | New translation of bone to apply. |
| `Rotation` | `FRotator` | New rotation of bone to apply. |
| `Scale` | `FVector` | New Scale of bone to apply. This is only worldspace. |
| `TranslationMode` | `TEnumAsByte < EBoneModificationMode >` | Whether and how to modify the translation of this bone. |
| `RotationMode` | `TEnumAsByte < EBoneModificationMode >` | Whether and how to modify the translation of this bone. |
| `ScaleMode` | `TEnumAsByte < EBoneModificationMode >` | Whether and how to modify the translation of this bone. |
| `TranslationSpace` | `TEnumAsByte < enum EBoneControlSpace >` | Reference frame to apply Translation in. |
| `RotationSpace` | `TEnumAsByte < enum EBoneControlSpace >` | Reference frame to apply Rotation in. |
| `ScaleSpace` | `TEnumAsByte < enum EBoneControlSpace >` | Reference frame to apply Scale in. |
| `TranslationCoefficient` | `FVector` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_ModifyBoneList.json -->

# FAnimNode_ModifyBoneList

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoneListTransforms` | `FBoneListTransforms` | - |
| `SpaceMode` | `EBatchModifySpace` | - |
| `bEnableTranslation` | `bool` | - |
| `bEnableRotation` | `bool` | - |
| `bEnableScale` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_ModifyBoneTransforms.json -->

# FAnimNode_ModifyBoneTransforms

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoneTransforms` | `FBonesTransfroms` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_ModifyBoneWithFunction.json -->

# FAnimNode_ModifyBoneWithFunction

此动画节点可调用指定的动画蓝图函数，用于热更修复动画Pose
  用法：
  1、添加ModifyBoneWithFunction动画节点，
  2、配置CallFunctionName指定函数名（不可与现有函数重名），点编译回创建出指定函数
  3、进入函数进行骨骼数据修改，注：
 		 函数输入的Context可用于获取某个骨骼的数据（GetBoneTransformLocalSpace、GetBoneTransformComponentSpace）
 		 函数输入的Additional Pose BPContext可用于获取附加Pose里的数据（节点支持额外输入多个附加Pose）
 		 函数输出为需要修改的骨骼数组，每个元素为骨骼名和其对应的ComponentSpaceTransform
 		 输出的骨骼数据需要按骨骼Index正向排序（即按骨架中的骨骼从上到下的顺序排序）

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AdditionalPoses` | `TArray < FComponentSpacePoseLink >` | Each layer's blended pose |
| `FunctionName` | `FName` | - |
| `CachedPrototypeFunction` | `UFunction *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_ModifyCurve.json -->

# FAnimNode_ModifyCurve

Easy way to modify curve values on a pose

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourcePose` | `FPoseLink` | - |
| `ApplyMode` | `EModifyCurveApplyMode` | - |
| `CurveValues` | `TArray < float >` | - |
| `CurveNames` | `TArray < FName >` | - |
| `Alpha` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_MoveAdditiveLayering.json -->

# FAnimNode_MoveAdditiveLayering

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BasePose` | `FPoseLink` | - |
| `TargetPose` | `FPoseLink` | - |
| `RefPose` | `FPoseLink` | - |
| `bFixRootRotation` | `bool` | - |
| `ArmMeshSpaceAlphaL` | `float` | - |
| `ArmMeshSpaceAlphaR` | `float` | - |
| `ArmSwayAlphaL` | `float` | - |
| `ArmSwayAlphaR` | `float` | - |
| `HandAlphaL` | `float` | - |
| `HandAlphaR` | `float` | - |
| `UpperPoseOverrideLayerSetup` | `TArray < FInputBlendPose >` | Configuration for the parts of the skeleton to blend for each layer. Allows<br>	  certain parts of the tree to be blended out or omitted from the pose. |
| `SpineLocalSpaceAdditiveLayerSetup` | `TArray < FInputBlendPose >` | - |
| `MeshSpaceAdditiveLayerSetup_Left` | `TArray < FInputBlendPose >` | - |
| `MeshSpaceAdditiveLayerSetup_Right` | `TArray < FInputBlendPose >` | - |
| `ArmLocalSpaceAdditiveLayerSetup` | `TArray < FInputBlendPose >` | - |
| `bEvaluateLayer0` | `bool` | - |
| `bEvaluateLayer1` | `bool` | - |
| `bEvaluateLayer2` | `bool` | - |
| `bEvaluateLayer3` | `bool` | - |
| `SkeletonGuid` | `FGuid` | - |
| `VirtualBoneGuid` | `FGuid` | - |
| `UpperPoseOverrideData` | `FMoveAdditiveLayeringData` | - |
| `SpineLocalSpaceAdditiveData` | `FMoveAdditiveLayeringData` | - |
| `MeshSpaceAdditiveData_Left` | `FMoveAdditiveLayeringData` | - |
| `MeshSpaceAdditiveData_Right` | `FMoveAdditiveLayeringData` | - |
| `ArmLocalSpaceAdditiveData` | `FMoveAdditiveLayeringData` | - |
| `bOutputTargetPose` | `bool` | - |
| `bOutputRefPose` | `bool` | - |
| `bOutputLocalSpaceAdditivePose` | `bool` | - |
| `bOutputMeshSpaceAdditivePose` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_MultiWayBlend.json -->

# FAnimNode_MultiWayBlend

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Poses` | `TArray < FPoseLink >` | - |
| `DesiredAlphas` | `TArray < float >` | - |
| `bAdditiveNode` | `bool` | - |
| `bNormalizeAlpha` | `bool` | - |
| `AlphaScaleBias` | `FInputScaleBias` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_ObserveBone.json -->

# FAnimNode_ObserveBone

Debugging node that displays the current value of a bone in a specific space.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoneToObserve` | `FBoneReference` | Name of bone to observe. |
| `DisplaySpace` | `TEnumAsByte < EBoneControlSpace >` | Reference frame to display the bone transform in. |
| `bRelativeToRefPose` | `bool` | Show the difference from the reference pose? |
| `Translation` | `FVector` | Translation of the bone being observed. |
| `Rotation` | `FRotator` | Rotation of the bone being observed. |
| `Scale` | `FVector` | Scale of the bone being observed. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_PoseBlendNode.json -->

# FAnimNode_PoseBlendNode

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourcePose` | `FPoseLink` | - |
| `BlendOption` | `EAlphaBlendOption` | Type of blending used (Linear, Cubic, etc.) |
| `CustomCurve` | `UCurveFloat *` | If you're using Custom BlendOption, you can specify curve |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_PoseByName.json -->

# FAnimNode_PoseByName

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PoseName` | `FName` | - |
| `PoseWeight` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_PoseDriver.json -->

# FAnimNode_PoseDriver

RBF based orientation driver

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourcePose` | `FPoseLink` | Bones to use for driving parameters based on their transform |
| `SourceBones` | `TArray < FBoneReference >` | Bone to use for driving parameters based on its orientation |
| `bOnlyDriveSelectedBones` | `bool` | If we should filter bones to be driven using the DrivenBonesFilter array |
| `OnlyDriveBones` | `TArray < FBoneReference >` | If bFilterDrivenBones is specified, only these bones will be modified by this node |
| `EvalSpaceBone` | `FBoneReference` | Optional other bone space to use when reading SourceBone transform.<br>	 	If not specified, we just use local space of SourceBone (ie relative to parent bone) |
| `RBFParams` | `FRBFParams` | Parameters used by RBF solver |
| `DriveSource` | `EPoseDriverSource` | Which part of the transform is read |
| `DriveOutput` | `EPoseDriverOutput` | Whether we should drive poses or curves |
| `PoseTargets` | `TArray < FPoseDriverTarget >` | Targets used to compare with current pose and drive morphsposes |
| `SourceBone_DEPRECATED` | `FBoneReference` | - |
| `TwistAxis_DEPRECATED` | `TEnumAsByte < EBoneAxis >` | - |
| `Type_DEPRECATED` | `EPoseDriverType` | - |
| `RadialScaling_DEPRECATED` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_PoseHandler.json -->

# FAnimNode_PoseHandler

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PoseAsset` | `UPoseAsset *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_PoseSnapshot.json -->

# FAnimNode_PoseSnapshot

Provide a snapshot pose, either from the internal named pose cache or via a supplied snapshot

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Mode` | `ESnapshotSourceMode` | How to access the snapshot |
| `SnapshotName` | `FName` | The name of the snapshot previously stored with SavePoseSnapshot |
| `Snapshot` | `FPoseSnapshot` | Snapshot to use. This should be populated at first by calling SnapshotPose |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_QuadrupedTerrainAdapting.json -->

# FAnimNode_QuadrupedTerrainAdapting

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bEnable` | `bool` | - |
| `bDrawDebug` | `bool` | - |
| `RayTrace_SphereRadius` | `float` | - |
| `RayTrace_MaxGroundAngle` | `float` | - |
| `RayTrace_LHandBottom` | `FBoneSocketTarget` | - |
| `RayTrace_RHandBottom` | `FBoneSocketTarget` | - |
| `RayTrace_LFootBottom` | `FBoneSocketTarget` | - |
| `RayTrace_RFootBottom` | `FBoneSocketTarget` | - |
| `bActorAdjustRotationFloor` | `bool` | - |
| `bEnableSlopeAdapting` | `bool` | - |
| `bResetSlopeAdaptingOnSkipCal` | `bool` | - |
| `bEaseSlopeAdaptingOnDisable` | `bool` | - |
| `bEnableLionDanceSlopeAdapting` | `bool` | - |
| `bEnableUpdateChildrenComps` | `bool` | - |
| `UpdateChildrenCompsFrequency` | `int32` | - |
| `SlopeAdapting_Pelvis` | `FBoneReference` | - |
| `SlopeAdapting_Pelvis1` | `FBoneReference` | - |
| `SlopeAdapting_Pelvis2` | `FBoneReference` | - |
| `SlopeAdapting_LClavicle` | `FBoneReference` | - |
| `SlopeAdapting_RClavicle` | `FBoneReference` | - |
| `SlopeAdapting_LThigh` | `FBoneReference` | - |
| `SlopeAdapting_RThigh` | `FBoneReference` | - |
| `SlopeAdapting_Root` | `FBoneReference` | - |
| `TraceDownLength` | `float` | - |
| `SlopeAdapting_PelvisLimitHeight` | `float` | - |
| `SlopeAdapting_LimitSlopeAngle` | `float` | - |
| `SlopeAdapting_PositionLerpSpeed` | `float` | - |
| `SlopeAdapting_RotationLerpSpeed` | `float` | - |
| `SlopeAdapting_BehindLegModifyFactor` | `float` | - |
| `BoneToFlooroffset` | `float` | - |
| `bEnableLegAdapting` | `bool` | - |
| `LegAdapting_IKLerpSpeed` | `float` | - |
| `LegAdapting_IKMaxHeight` | `float` | - |
| `LegAdapting_LHand` | `FAnimNode_TwoBoneIK` | - |
| `LegAdapting_RHand` | `FAnimNode_TwoBoneIK` | - |
| `LegAdapting_LFoot` | `FAnimNode_TwoBoneIK` | - |
| `LegAdapting_RFoot` | `FAnimNode_TwoBoneIK` | - |
| `fSlopeAdaptOffset` | `float` | - |
| `bApplySlopeAdaptingPelvisPositiontNoMove` | `bool` | ApplySlopeAdapting的时候，是否不调整盆骨的高度（调试用：只走旋转、不做几何补偿，<br>	 用于对比验证旋转方案在不做位置补偿时的效果） |
| `SlopeAdaptingMode` | `ESlopeAdaptingMode` | 斜坡适配方案选择。默认 Legacy 走原逻辑，与现有四足资产完全兼容。<br>	 选 CapsuleCenterRotation_LongLegShortLeg 时走新方案AB（绕胶囊中心整体旋转的等价实现）。<br>	 选 CapsuleCenterRotation_LongLeg的话，推荐开启EnableLegAdapting |
| `bAutoCalculateLegLength` | `bool` | 仅方案A使用：是否自动从骨架默认姿态计算腿长（取 max(前腿平均, 后腿平均)）。<br>	 自动模式下首次计算后会缓存。关闭后使用下面 SlopeAdapting_LegLengthForCompensation 手填值。 |
| `SlopeAdapting_LegLengthForCompensation` | `float` | 仅方案A使用：手填腿长（仅当 bAutoCalculateLegLength=false 时生效）。<br>	 用于补偿 4 腿反向 Roll 后产生的脚浮空：ΔZ = -L  (1 - cos(α))。 |
| `bEnableRollAdapting` | `bool` | 仅方案AB使用：是否启用绕 ActorForward 轴的 Roll 适配（左右侧坡度）。<br>	 默认关闭：仅做 Pitch（前后坡度）。启用后会额外计算并叠加左右侧坡的 Roll 旋转。 |
| `bClampHorizontalDelta` | `bool` | 是否钳制水平方向位移（方案AB）。默认关闭：水平位移是几何正确的，不应被截断。<br>	 仅在调试或特殊场景下打开，限制水平位移幅度。 |
| `SlopeAdapting_HorizontalDeltaLimit` | `float` | 仅当 bClampHorizontalDelta=true 时生效：水平位移钳制上限（cm）。 |
| `bEnableLionDanceLegAdapting` | `bool` | - |
| `bEnableFootAdapting` | `bool` | - |
| `FootAdapting_LHand` | `FBoneReference` | - |
| `FootAdapting_RHand` | `FBoneReference` | - |
| `FootAdapting_LFoot` | `FBoneReference` | - |
| `FootAdapting_RFoot` | `FBoneReference` | - |
| `FootAdapting_LimitRotation` | `FRotator` | - |
| `FootAdapting_RotationLerpSpeed` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_RandomPlayer.json -->

# FAnimNode_RandomPlayer

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bShuffleMode` | `bool` | When shuffle mode is active we will never loop a sequence beyond MaxLoopCount<br>	   without visiting each sequence in turn (no repeats). Enabling this will ignore<br>	   ChanceToPlay for each entry |
| `Entries` | `TArray < FRandomPlayerSequenceEntry >` | List of sequences to randomly step through |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_RectificationBone.json -->

# FAnimNode_RectificationBone

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoneToModify` | `FBoneReference` | - |
| `DestinRotation` | `FRotator` | - |
| `BeginOffsetRotation` | `FRotator` | - |
| `EndOffsetRotation` | `FRotator` | - |
| `BaseBoneCached` | `FCachedBoneParamInfo` | - |
| `BoneCachedOffsetList` | `TArray < FPairCachedBoneInfo >` | - |
| `AutoSortCacheList` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_RefPose.json -->

# FAnimNode_RefPose

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RefPoseType` | `TEnumAsByte < ERefPoseType >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_ResetBoneTransform.json -->

# FAnimNode_ResetBoneTransform

Simple controller that replaces or adds to the translationrotation of a single bone.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BonesToModify` | `TArray < FBoneReference >` | Name of bone to control. This is the main bone chain to modify from. |
| `ReferenceParentBone` | `FBoneReference` | - |
| `ReferenceRootBone` | `FBoneReference` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_RigidBody.json -->

# FAnimNode_RigidBody

Controller that simulates physics based on the physics asset of the skeletal mesh component

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OverridePhysicsAsset` | `UPhysicsAsset *` | Physics asset to use. If empty use the skeletal mesh's default physics asset |
| `LastUsePhysicsAsset` | `TWeakObjectPtr < UPhysicsAsset >` | - |
| `OverrideWorldGravity` | `FVector` | Override gravity |
| `ExternalForce` | `FVector` | Applies a uniform external force in world space. This allows for easily faking inertia of movement while still simulating in component space for example |
| `OverlapChannel` | `TEnumAsByte < ECollisionChannel >` | The channel we use to find static geometry to collide with |
| `bEnableWorldGeometry` | `bool` | - |
| `SimulationSpace` | `ESimulationSpace` | What space to simulate the bodies in. This affects how velocities are generated |
| `bOverrideWorldGravity` | `bool` | - |
| `CachedBoundsScale` | `float` | Scale of cached bounds (vs. actual bounds).<br>	  Increasing this may improve performance, but overlaps may not work as well.<br>	  (A value of 1.0 effectively disables cached bounds). |
| `bUseCompPhysicsAssetWhenNotSet` | `bool` | - |
| `bUseIntersectDetect` | `bool` | - |
| `bUseMultipleRigidBodyNodeInitDelay` | `bool` | - |
| `bComponentSpaceSimulation_DEPRECATED` | `bool` | - |
| `BoneShiftTolerenceChecker` | `FAnimNodeBoneShiftTolerenceChecker` | Bone Shift Tolerence Check Start |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_RigidBody_UE5.json -->

# FAnimNode_RigidBody_UE5

Controller that simulates physics based on the physics asset of the skeletal mesh component

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OverridePhysicsAsset` | `UPhysicsAsset *` | Physics asset to use. If empty use the skeletal mesh's default physics asset |
| `OverrideWorldGravity` | `FVector` | Override gravity |
| `ExternalForce` | `FVector` | Applies a uniform external force in world space. This allows for easily faking inertia of movement while still simulating in component space for example |
| `ComponentLinearAccScale` | `FVector` | When using non-world-space sim, this controls how much of the components world-space acceleration is passed on to the local-space simulation. |
| `ComponentLinearVelScale` | `FVector` | When using non-world-space sim, this applies a 'drag' to the bodies in the local space simulation, based on the components world-space velocity. |
| `ComponentAppliedLinearAccClamp` | `FVector` | When using non-world-space sim, this is an overall clamp on acceleration derived from ComponentLinearAccScale and ComponentLinearVelScale, to ensure it is not too large. |
| `SimSpaceSettings` | `FSimSpaceSettings` | Settings for the system which passes motion of the simulation's space<br>	  into the simulation. This allows the simulation to pass a<br>	  fraction of the world space motion onto the bodies which allows Bone-Space<br>	  and Component-Space simulations to react to world-space movement in a<br>	  controllable way.<br>	  This system is a superset of the functionality provided by ComponentLinearAccScale,<br>	  ComponentLinearVelScale, and ComponentAppliedLinearAccClamp. In general<br>	  you should not have both systems enabled.<br>	 <br>	UPROPERTY(EditAnywhere not support for without WITH_CHAOS, Category = Settings, meta = (PinHiddenByDefault)) |
| `CachedBoundsScale` | `float` | Scale of cached bounds (vs. actual bounds).<br>	  Increasing this may improve performance, but overlaps may not work as well.<br>	  (A value of 1.0 effectively disables cached bounds).<br>	 <br>	UPROPERTY(EditAnywhere, Category = Settings, meta = (ClampMin="1.0", ClampMax="2.0")) |
| `BaseBoneRef` | `FBoneReference` | Matters if SimulationSpace is BaseBone |
| `OverlapChannel` | `TEnumAsByte < ECollisionChannel >` | The channel we use to find static geometry to collide with <br>	UPROPERTY(EditAnywhere, Category = Settings, meta = (editcondition = "bEnableWorldGeometry")) |
| `SimulationSpace` | `ESimulationSpace_UE5` | What space to simulate the bodies in. This affects how velocities are generated |
| `bForceDisableCollisionBetweenConstraintBodies` | `bool` | Whether to allow collisions between two bodies joined by a constraint |
| `bEnableWorldGeometry` | `uint8` | - |
| `bOverrideWorldGravity` | `uint8` | UPROPERTY(EditAnywhere, Category = Settings, meta = (InlineEditConditionToggle)) |
| `bTransferBoneVelocities` | `uint8` | UPROPERTY(EditAnywhere, Category = Settings, meta=(PinHiddenByDefault)) |
| `bFreezeIncomingPoseOnStart` | `uint8` | UPROPERTY(EditAnywhere, Category = Settings Not Support Feature for Depends on Chaos) |
| `bClampLinearTranslationLimitToRefPose` | `uint8` | - |
| `WorldSpaceMinimumScale` | `float` | - |
| `EvaluationResetTime` | `float` | - |
| `bComponentSpaceSimulation_DEPRECATED` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_Root.json -->

# FAnimNode_Root

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Result` | `FPoseLink` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_RotateRootBone.json -->

# FAnimNode_RotateRootBone

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BasePose` | `FPoseLink` | - |
| `Pitch` | `float` | - |
| `Yaw` | `float` | - |
| `MeshToComponent` | `FRotator` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_RotationMultiplier.json -->

# FAnimNode_RotationMultiplier

Simple controller that multiplies scalar value to the translationrotationscale of a single bone.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TargetBone` | `FBoneReference` | Name of bone to control. This is the main bone chain to modify from. |
| `SourceBone` | `FBoneReference` | Source to get transform from |
| `Multiplier` | `float` | - |
| `RotationAxisToRefer` | `TEnumAsByte < EBoneAxis >` | - |
| `bIsAdditive` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_RotationOffsetBlendSpace.json -->

# FAnimNode_RotationOffsetBlendSpace

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BasePose` | `FPoseLink` | - |
| `LODThreshold` | `int32` | Max LOD that this node is allowed to run<br>	 For example if you have LODThreadhold to be 2, it will run until LOD 2 (based on 0 index)<br>	 when the component LOD becomes 3, it will stop updateevaluate<br>	 currently transition would be issue and that has to be re-visited |
| `bIsLODEnabled` | `bool` | - |
| `Alpha` | `float` | - |
| `AlphaScaleBias` | `FInputScaleBias` | - |
| `ActualAlpha` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_SaveCachedPose.json -->

# FAnimNode_SaveCachedPose

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Pose` | `FPoseLink` | - |
| `CachePoseName` | `FName` | Intentionally not exposed, set by AnimBlueprintCompiler |
| `GlobalWeight` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_ScaleChainLength.json -->

# FAnimNode_ScaleChainLength

Scale the length of a chain of bones.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InputPose` | `FPoseLink` | - |
| `DefaultChainLength` | `float` | Default chain length, as animated. |
| `ChainStartBone` | `FBoneReference` | - |
| `ChainEndBone` | `FBoneReference` | - |
| `ChainInitialLength` | `EScaleChainInitialLength` | - |
| `TargetLocation` | `FVector` | - |
| `Alpha` | `float` | - |
| `ActualAlpha` | `float` | - |
| `AlphaScaleBias` | `FInputScaleBias` | - |
| `bBoneIndicesCached` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_SequenceEvaluator.json -->

# FAnimNode_SequenceEvaluator

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Sequence` | `UAnimSequenceBase *` | - |
| `ExplicitTime` | `float` | - |
| `ExplicitTimeType` | `TEnumAsByte < ESequenceEvalTimeType :: Type >` | 输入时间类型： |
| `bShouldLoop` | `bool` | This only works if bTeleportToTargetTime is false OR this node is set to use SyncGroup |
| `bTeleportToExplicitTime` | `bool` | If true, teleport to explicit time, does NOT advance time (does not trigger notifies, does not extract Root Motion, etc.)<br>	Note: using a sync group forces advancing time regardless of what this option is set to. |
| `StartPosition` | `float` | - |
| `ReinitializationBehavior` | `TEnumAsByte < ESequenceEvalReinit :: Type >` | What to do when SequenceEvaluator is reinitialized |
| `bReinitialized` | `bool` | - |
| `CheckReTickFrameCounterSubValue` | `int32` | - |
| `bEnableTriggerNotify` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_SequencePlayer.json -->

# FAnimNode_SequencePlayer

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Sequence` | `UAnimSequenceBase *` | - |
| `bLoopAnimation` | `bool` | - |
| `bCheckNeedInitializeSupFirst` | `bool` | - |
| `PlayRate` | `float` | - |
| `StartPosition` | `float` | - |
| `ReversePlayRate` | `bool` | - |
| `bResetPlayTimeWhenReactivate` | `bool` | - |
| `bForceResetPlayTime` | `bool` | - |
| `CheckReactivateFrameCounterSubValue` | `int32` | - |
| `bShouldReinitPose` | `bool` | - |
| `ReInitPose` | `FBonesTransfromsWithFPP` | - |
| `bResetToAdditivePose` | `bool` | - |
| `EnableSequenceBlend` | `bool` | - |
| `SequenceBlendOutTime` | `float` | - |
| `SequenceBlendBySyncGroup` | `bool` | - |
| `SequenceBlendResetNewTimeAccumulator` | `bool` | - |
| `SequenceBlendOutWeightScale` | `float` | - |
| `bClearBlendOutPoseWhenSequenceReactive` | `bool` | - |
| `SequenceBlendOutWhenRelevant` | `bool` | - |
| `SequenceBlendOutTime_Counter` | `float` | - |
| `SequenceBlendOutTime_Alpha` | `float` | - |
| `SequenceBlendOutWeight` | `float` | - |
| `LastSequence` | `UAnimSequenceBase *` | - |
| `BlendOutPlayers_Cache` | `TArray < UAnimSequenceBase * >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_SkeletalControlBase.json -->

# FAnimNode_SkeletalControlBase

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Alpha` | `float` | - |
| `ComponentPose` | `FComponentSpacePoseLink` | - |
| `AlphaScaleBias` | `FInputScaleBias` | - |
| `LODThreshold` | `int32` | Max LOD that this node is allowed to run<br>	 For example if you have LODThreadhold to be 2, it will run until LOD 2 (based on 0 index)<br>	 when the component LOD becomes 3, it will stop updateevaluate<br>	 currently transition would be issue and that has to be re-visited |
| `bActiveNode` | `bool` | Engine Modify<br>	 Enable Node to be ignored at runtime but keep alpha value no change<br>	 false will ignore (do no or skip) evaluate, but no affect on update |
| `ActualAlpha` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_Slot.json -->

# FAnimNode_Slot

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Source` | `FPoseLink` | - |
| `SlotName` | `FName` | - |
| `GroupName` | `FName` | - |
| `bAlwaysUpdateSourcePose` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_SplineIK.json -->

# FAnimNode_SplineIK

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StartBone` | `FBoneReference` | Name of root bone from which the spline extends |
| `EndBone` | `FBoneReference` | Name of bone at the end of the spline chain. Bones after this will not be altered by the controller. |
| `BoneAxis` | `ESplineBoneAxis` | Axis of the controlled bone (ie the direction of the spline) to use as the direction for the curve. |
| `bAutoCalculateSpline` | `bool` | The number of points in the spline if we are specifying it directly |
| `PointCount` | `int32` | The number of points in the spline if we are not auto-calculating |
| `ControlPoints` | `TArray < FTransform >` | Transforms applied to spline points |
| `Roll` | `float` | Overall roll of the spline, applied on top of other rotations along the direction of the spline |
| `TwistStart` | `float` | The twist of the start bone. Twist is interpolated along the spline according to Twist Blend. |
| `TwistEnd` | `float` | The twist of the end bone. Twist is interpolated along the spline according to Twist Blend. |
| `TwistBlend` | `FAlphaBlend` | How to interpolate twist along the length of the spline |
| `Stretch` | `float` | The maximum stretch allowed when fitting bones to the spline. 0.0 means bones do not stretch their length,<br>	  1.0 means bones stretch to the length of the spline |
| `Offset` | `float` | The distance along the spline from the start from which bones are constrained |
| `BoneSpline` | `FSplineCurves` | Spline we maintain internally |
| `OriginalSplineLength` | `float` | Cached spline length from when the spline was originally applied to the skeleton |
| `CachedBoneReferences` | `TArray < FSplineIKCachedBoneData >` | Cached data for bones in the IK chain, from start to end |
| `CachedBoneLengths` | `TArray < float >` | Cached bone lengths. Same size as CachedBoneReferences |
| `CachedOffsetRotations` | `TArray < FQuat >` | Cached bone offset rotations. Same size as CachedBoneReferences |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_SpringBone.json -->

# FAnimNode_SpringBone

Simple controller that replaces or adds to the translationrotation of a single bone.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SpringBone` | `FBoneReference` | Name of bone to control. This is the main bone chain to modify from. |
| `bLimitDisplacement` | `bool` | Limit the amount that a bone can stretch from its ref-pose length. |
| `MaxDisplacement` | `float` | If bLimitDisplacement is true, this indicates how long a bone can stretch beyond its length in the ref-pose. |
| `SpringStiffness` | `float` | Stiffness of spring |
| `SpringDamping` | `float` | Damping of spring |
| `ErrorResetThresh` | `float` | If spring stretches more than this, reset it. Useful for catching teleports etc |
| `bNoZSpring_DEPRECATED` | `bool` | If true, Z position is always correct, no spring applied |
| `bTranslateX` | `bool` | If true take the spring calculation for translation in X |
| `bTranslateY` | `bool` | If true take the spring calculation for translation in Y |
| `bTranslateZ` | `bool` | If true take the spring calculation for translation in Z |
| `bRotateX` | `bool` | If true take the spring calculation for rotation in X |
| `bRotateY` | `bool` | If true take the spring calculation for rotation in Y |
| `bRotateZ` | `bool` | If true take the spring calculation for rotation in Z |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_StateMachine.json -->

# FAnimNode_StateMachine

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StateMachineIndexInClass` | `int32` | - |
| `MaxTransitionsPerFrame` | `int32` | - |
| `bSkipFirstUpdateTransition` | `bool` | - |
| `bReinitializeOnBecomingRelevant` | `bool` | - |
| `bAllowConduitEntryState` | `bool` | - |
| `bReinitializeOnTickRecoverOverTime` | `bool` | - |
| `NoTickOverTimeThreshold` | `float` | - |
| `CurrentState` | `int32` | - |
| `ElapsedTime` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_SubInput.json -->

# FAnimNode_SubInput

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Index` | `int32` | - |
| `bEnableForwardUpdateStreamTriggerNotify` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_SubInstance.json -->

# FAnimNode_SubInstance

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InPose` | `FPoseLink` | Input pose for the node, intentionally not accessible because if there's no input<br>	   Node in the target class we don't want to show this as a pin |
| `InPoses` | `TArray < FPoseLink >` | Each layer's blended pose |
| `SubInstanceSlotName` | `FName` | - |
| `InstanceClass` | `TSubclassOf < UAnimInstance >` | - |
| `bNeedCacheSubInstance` | `bool` | - |
| `MaxCacheSubInstanceCount` | `int32` | - |
| `bResetToAdditivePose` | `bool` | - |
| `InstanceToRun` | `UAnimInstance *` | This is the actual instance allocated at runtime that will run |
| `InstancePendingToRun` | `UAnimInstance *` | - |
| `bPendingCreateSubInstance` | `bool` | Flag set during Restore_AnyThread when a sub-instance needs to be created on game thread |
| `PendingSubInstanceClassPath` | `FString` | The class path for the pending sub-instance to create |
| `MultiInstancesToRunDatas` | `TArray < FMultiSubInstanceData >` | - |
| `BlendOutInstanceDatas` | `TArray < FSubInstanceBlendData >` | - |
| `InstanceProperties` | `TArray < UProperty * >` | List of properties on the calling instance to push from |
| `SubInstanceProperties` | `TArray < UProperty * >` | List of properties on the sub instance to push to, built from name list when initialised |
| `SourcePropertyNames` | `TArray < FName >` | List of source properties to use, 1-1 with Dest names below, built by the compiler |
| `DestPropertyNames` | `TArray < FName >` | List of destination properties to use, 1-1 with Source names above, built by the compiler |
| `PosInertialization` | `FAnimNode_SubAnimInertialization` | - |
| `bBlendSubAnim` | `bool` | - |
| `NewAnimBlendTime` | `float` | - |
| `bKeepUpdateOldSubInstanes` | `bool` | - |
| `bUpdateWhenNotRelevant` | `bool` | - |
| `NotRelevantUpdateConditions` | `TArray < UAnimInstanceUpdateCondition * >` | - |
| `bAlwaysUpdateInputNode` | `bool` | - |
| `bResetInertializationWhenReactive` | `bool` | - |
| `bUpdateAllInputNodeWhenNoInstanceRun` | `bool` | - |
| `bResetPendingBlendDurationWhenReactive` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_Trail.json -->

# FAnimNode_Trail

Trail Controller

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TrailBone` | `FBoneReference` | Reference to the active bone in the hierarchy to modify. |
| `ChainLength` | `int32` | Number of bones above the active one in the hierarchy to modify. ChainLength should be at least 2. |
| `ChainBoneAxis` | `TEnumAsByte < EAxis :: Type >` | Axis of the bones to point along trail. |
| `bInvertChainBoneAxis` | `bool` | Invert the direction specified in ChainBoneAxis. |
| `TrailRelaxation_DEPRECATED` | `float` | How quickly we 'relax' the bones to their animated positions. Deprecated. Replaced to TrailRelaxationCurve |
| `TrailRelaxationSpeed` | `FRuntimeFloatCurve` | How quickly we 'relax' the bones to their animated positions. Time 0 will map to top root joint, time 1 will map to the bottom joint. |
| `bLimitStretch` | `bool` | Limit the amount that a bone can stretch from its ref-pose length. |
| `StretchLimit` | `float` | If bLimitStretch is true, this indicates how long a bone can stretch beyond its length in the ref-pose. |
| `FakeVelocity` | `FVector` | 'Fake' velocity applied to bones. |
| `bActorSpaceFakeVel` | `bool` | Whether 'fake' velocity should be applied in actor or world space. |
| `BaseJoint` | `FBoneReference` | Base Joint to calculate velocity from. If none, it will use Component's World Transform. . |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_TransitionPoseEvaluator.json -->

# FAnimNode_TransitionPoseEvaluator

Animation data node for state machine transitions.
  Can be set to supply either the animation data from the transition source (From State) or the transition destination (To State).

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DataSource` | `TEnumAsByte < EEvaluatorDataSource :: Type >` | - |
| `EvaluatorMode` | `TEnumAsByte < EEvaluatorMode :: Mode >` | - |
| `FramesToCachePose` | `int32` | - |
| `CacheFramesRemaining` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_TransitionResult.json -->

# FAnimNode_TransitionResult

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bCanEnterTransition` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_TwistCorrectiveNode.json -->

# FAnimNode_TwistCorrectiveNode

This is the node that apply corrective morphtarget for twist 
  Good example is that if you twist your neck too far right or left, you're going to see odd stretch shape of neck, 
  This node can detect the angle and apply morphtarget curve 
  This isn't the twist control node for bone twist

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BaseFrame` | `FReferenceBoneFrame` | Base Frame of the reference for the twist node |
| `TwistFrame` | `FReferenceBoneFrame` | - |
| `TwistPlaneNormalAxis` | `FAxis` | Normal of the Plane that we'd like to calculate angle calculation from in BaseFrame. Please note we're looking for Normal Axis |
| `RangeMax` | `float` | - |
| `RemappedMin` | `float` | - |
| `RemappedMax` | `float` | - |
| `Curve` | `FAnimCurveParam` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_TwoBoneIK.json -->

# FAnimNode_TwoBoneIK

Simple 2 Bone IK Controller.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `IKBone` | `FBoneReference` | Name of bone to control. This is the main bone chain to modify from. |
| `bAllowStretching` | `uint32` | Should stretching be allowed, to be prevent over extension |
| `StartStretchRatio` | `float` | Limits to use if stretching is allowed. This value determines when to start stretch. For example, 0.9 means once it reaches 90% of the whole length of the limb, it will start apply. |
| `MaxStretchScale` | `float` | Limits to use if stretching is allowed. This value determins what is the max stretch scale. For example, 1.5 means it will stretch until 150 % of the whole length of the limb. |
| `StretchLimits_DEPRECATED` | `FVector2D` | Limits to use if stretching is allowed - old property DEPRECATED |
| `bTakeRotationFromEffectorSpace` | `uint32` | Set end bone to use End Effector rotation |
| `bMaintainEffectorRelRot` | `uint32` | Keep local rotation of end bone |
| `EffectorLocationSpace` | `TEnumAsByte < enum EBoneControlSpace >` | Reference frame of Effector Location. |
| `EffectorSpaceBoneName_DEPRECATED` | `FName` | If EffectorLocationSpace is a bone, this is the bone to use. |
| `EffectorLocation` | `FVector` | Effector Location. Target Location to reach. |
| `EffectorTarget` | `FBoneSocketTarget` | - |
| `JointTargetLocationSpace` | `TEnumAsByte < enum EBoneControlSpace >` | Reference frame of Joint Target Location. |
| `JointTargetLocation` | `FVector` | Joint Target Location. Location used to orient Joint bone. |
| `JointTargetSpaceBoneName_DEPRECATED` | `FName` | If JointTargetSpaceBoneName is a bone, this is the bone to use. |
| `JointTarget` | `FBoneSocketTarget` | - |
| `bAllowTwist` | `bool` | Whether or not to apply twist on the chain of joints. This clears the twist value along the TwistAxis |
| `TwistAxis` | `FAxis` | Specify which axis it's aligned. Used when removing twist |
| `bNoTwist_DEPRECATED` | `bool` | Whether or not to apply twist on the chain of joints. This clears the twist value along the TwistAxis |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_TwoWayBlend.json -->

# FAnimNode_TwoWayBlend

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `A` | `FPoseLink` | - |
| `B` | `FPoseLink` | - |
| `Alpha` | `float` | - |
| `AlphaScaleBias` | `FInputScaleBias` | - |
| `InternalBlendAlpha` | `float` | - |
| `bAIsRelevant` | `bool` | - |
| `bBIsRelevant` | `bool` | - |
| `bResetChildOnActivation` | `bool` | This reinitializes child pose when re-activated. For example, when active child changes |
| `AlwaysUpdateInputPose` | `bool` | - |
| `AlwaysEvaluateInputPose` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_UseCachedBoneTransform.json -->

# FAnimNode_UseCachedBoneTransform

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Source` | `FPoseLink` | - |
| `BoneToUseBeforeCache` | `FBoneReference` | - |
| `CacheFlagName` | `FName` | - |
| `bModifyBoneTransformInNode` | `bool` | - |
| `bUseTranslation` | `bool` | - |
| `bUseTranslationX` | `bool` | - |
| `bUseTranslationY` | `bool` | - |
| `bUseTranslationZ` | `bool` | - |
| `bUseRotation` | `bool` | - |
| `CachedUseBoneTransform` | `FTransform` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_UseCachedPose.json -->

# FAnimNode_UseCachedPose

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LinkToCachingNode` | `FPoseLink` | - |
| `CachePoseName` | `FName` | Intentionally not exposed, set by AnimBlueprintCompiler |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNodeBoneShiftTolerenceChecker.json -->

# FAnimNodeBoneShiftTolerenceChecker

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bShrinkIfOutofTolerence` | `bool` | - |
| `bIncludeRootKinamiticBone` | `bool` | - |
| `RootBone` | `FBoneReference` | - |
| `TolerencePolicy` | `EBoneShiftTolerencePolicy` | - |
| `MaxTolerenceBoneShiftDistance` | `float` | - |
| `MaxTolerenceBoneShiftScale` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNotifyStateBoneRetargetAdaptInfo.json -->

# FAnimNotifyStateBoneRetargetAdaptInfo

For Bone Retarget Feature Start

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoneRetargetObj` | `TWeakObjectPtr < UObject >` | - |
| `bBoneRetargetAdaptInitDone` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimParentNodeAssetOverride.json -->

# FAnimParentNodeAssetOverride

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NewAsset` | `UAnimationAsset *` | - |
| `ParentNodeGuid` | `FGuid` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimPhysBodyDefinition_UE5.json -->

# FAnimPhysBodyDefinition_UE5

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoundBone` | `FBoneReference` | - |
| `BoxExtents` | `FVector` | Extents of the box to use for simulation |
| `LocalJointOffset` | `FVector` | Vector relative to the body being simulated to attach the constraint to |
| `ConstraintSetup` | `FAnimPhysConstraintSetup_UE5` | Data describing the constraints we will apply to the body |
| `CollisionType` | `AnimPhysCollisionType` | Resolution method for planar limits |
| `SphereCollisionRadius` | `float` | Radius to use if CollisionType is set to CustomSphere |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimPhysConstraintSetup.json -->

# FAnimPhysConstraintSetup

Constraint setup struct, holds data required to build a physics constraint

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LinearXLimitType` | `AnimPhysLinearConstraintType` | Whether to limit the linear X axis |
| `LinearYLimitType` | `AnimPhysLinearConstraintType` | Whether to limit the linear Y axis |
| `LinearZLimitType` | `AnimPhysLinearConstraintType` | Whether to limit the linear Z axis |
| `LinearAxesMin` | `FVector` | Minimum linear movement per-axis (Set zero here and in the max limit to lock) |
| `LinearAxesMax` | `FVector` | Maximum linear movement per-axis (Set zero here and in the min limit to lock) |
| `AngularConstraintType` | `AnimPhysAngularConstraintType` | Method to use when constraining angular motion |
| `TwistAxis` | `AnimPhysTwistAxis` | Axis to consider for twist when constraining angular motion (forward axis) |
| `ConeAngle` | `float` | Angle to use when constraining using a cone |
| `AngularXAngle_DEPRECATED` | `float` | X-axis limit for angular motion when using the "Angular" constraint type (Set to 0 to lock, or 180 to remain free) |
| `AngularYAngle_DEPRECATED` | `float` | Y-axis limit for angular motion when using the "Angular" constraint type (Set to 0 to lock, or 180 to remain free) |
| `AngularZAngle_DEPRECATED` | `float` | Z-axis limit for angular motion when using the "Angular" constraint type (Set to 0 to lock, or 180 to remain free) |
| `AngularLimitsMin` | `FVector` | - |
| `AngularLimitsMax` | `FVector` | - |
| `AngularTargetAxis` | `AnimPhysTwistAxis` | Axis on body1 to match to the angular target direction. |
| `AngularTarget` | `FVector` | Target direction to face for body1 (in body0 local space) |
| `bLinearFullyLocked` | `bool` | The values below are calculated on initialisation and used when building the limits <br>	 If all axes are locked we can use 3 linear limits instead of the 6 needed for limited axes |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimPhysConstraintSetup_UE5.json -->

# FAnimPhysConstraintSetup_UE5

Constraint setup struct, holds data required to build a physics constraint

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LinearXLimitType` | `AnimPhysLinearConstraintType_UE5` | Whether to limit the linear X axis |
| `LinearYLimitType` | `AnimPhysLinearConstraintType_UE5` | Whether to limit the linear Y axis |
| `LinearZLimitType` | `AnimPhysLinearConstraintType_UE5` | Whether to limit the linear Z axis |
| `LinearAxesMin` | `FVector` | Minimum linear movement per-axis (Set zero here and in the max limit to lock) |
| `LinearAxesMax` | `FVector` | Maximum linear movement per-axis (Set zero here and in the min limit to lock) |
| `AngularConstraintType` | `AnimPhysAngularConstraintType_UE5` | Method to use when constraining angular motion |
| `TwistAxis` | `AnimPhysTwistAxis` | Axis to consider for twist when constraining angular motion (forward axis) |
| `AngularTargetAxis` | `AnimPhysTwistAxis` | The axis in the simulation pose to align to the Angular Target.<br>	  This is typically the axis pointing along the bone.<br>	  Note: This is affected by the Angular Spring Constant. |
| `ConeAngle` | `float` | Angle to use when constraining using a cone |
| `AngularLimitsMin` | `FVector` | - |
| `AngularLimitsMax` | `FVector` | - |
| `AngularTarget` | `FVector` | The axis to align the angular spring constraint to in the animation pose.<br>	  This typically points down the bone - so values of (1.0, 0.0, 0.0) are common,<br>	  but you can pick other values to align the spring to a different direction.<br>	  Note: This is affected by the Angular Spring Constant. |
| `AngularXAngle_DEPRECATED` | `float` | X-axis limit for angular motion when using the "Angular" constraint type (Set to 0 to lock, or 180 to remain free) |
| `AngularYAngle_DEPRECATED` | `float` | Y-axis limit for angular motion when using the "Angular" constraint type (Set to 0 to lock, or 180 to remain free) |
| `AngularZAngle_DEPRECATED` | `float` | Z-axis limit for angular motion when using the "Angular" constraint type (Set to 0 to lock, or 180 to remain free) |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimPhysPlanarLimit.json -->

# FAnimPhysPlanarLimit

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DrivingBone` | `FBoneReference` | When using a driving bone, the plane transform will be relative to the bone transform |
| `PlaneTransform` | `FTransform` | Transform of the plane, this is either in component-space if no DrivinBone is specified<br>	   or in bone-space if a driving bone is present. |
| `IsEnabled` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimPhysPlanarLimit_UE5.json -->

# FAnimPhysPlanarLimit_UE5

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DrivingBone` | `FBoneReference` | When using a driving bone, the plane transform will be relative to the bone transform |
| `PlaneTransform` | `FTransform` | Transform of the plane, this is either in component-space if no DrivinBone is specified<br>	   or in bone-space if a driving bone is present. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimPhysSphericalLimit.json -->

# FAnimPhysSphericalLimit

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DrivingBone` | `FBoneReference` | Bone to attach the sphere to |
| `SphereLocalOffset` | `FVector` | Local offset for the sphere, if no driving bone is set this is in node space, otherwise bone space |
| `LimitRadius` | `float` | Radius of the sphere |
| `LimitType` | `ESphericalLimitType` | Whether to lock bodies inside or outside of the sphere |
| `IsEnabled` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimPhysSphericalLimit_UE5.json -->

# FAnimPhysSphericalLimit_UE5

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DrivingBone` | `FBoneReference` | Bone to attach the sphere to |
| `SphereLocalOffset` | `FVector` | Local offset for the sphere, if no driving bone is set this is in node space, otherwise bone space |
| `LimitRadius` | `float` | Radius of the sphere |
| `LimitType` | `ESphericalLimitType_UE5` | Whether to lock bodies inside or outside of the sphere |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimSegment.json -->

# FAnimSegment

this is anim segment that defines what animation and how

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AnimReference` | `UAnimSequenceBase *` | Anim Reference to play - only allow AnimSequence or AnimComposite |
| `StartPos` | `float` | Start Pos within this AnimCompositeBase |
| `AnimStartTime` | `float` | Time to start playing AnimSequence at. |
| `AnimEndTime` | `float` | Time to end playing the AnimSequence at. |
| `AnimPlayRate` | `float` | Playback speed of this animation. If you'd like to reverse, set -1 |
| `LoopingCount` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimSequenceTrackContainer.json -->

# FAnimSequenceTrackContainer

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AnimationTracks` | `TArray < struct FRawAnimSequenceTrack >` | - |
| `TrackNames` | `TArray < FName >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimSetMeshLinkup.json -->

# FAnimSetMeshLinkup

This is a mapping table between each bone in a particular skeletal mesh and the tracks of this animation set.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoneToTrackTable` | `TArray < int32 >` | Mapping table. Size must be same as size of SkelMesh reference skeleton. <br>	  No index should be more than the number of tracks in this AnimSet.<br>	  -1 indicates no track for this bone - will use reference pose instead. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimSlotDesc.json -->

# FAnimSlotDesc

Used to indicate each slot name and how many channels they have.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SlotName` | `FName` | Name of the slot. |
| `NumChannels` | `int32` | Number of channels that are available in this slot. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimSlotGroup.json -->

# FAnimSlotGroup

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GroupName` | `FName` | - |
| `SlotNames` | `TArray < FName >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimSlotInfo.json -->

# FAnimSlotInfo

Struct used for passing information from Matinee to an Actor for blending animations during a sequence.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SlotName` | `FName` | Name of slot that we want to play the animtion in. |
| `ChannelWeights` | `TArray < float >` | Strength of each Channel within this Slot. Channel indexs are determined by track order in Matinee. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimTrack.json -->

# FAnimTrack

This is list of anim segments for this track 
  For now this is only one TArray, but in the future 
  we should define more transitionblending behaviors

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AnimSegments` | `TArray < FAnimSegment >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAnimUpdateRateParameters.json -->

# FAnimUpdateRateParameters

Container for Animation Update Rate parameters.
  They are shared for all components of an Actor, so they can be updated in sync.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UpdateRate` | `int32` | How often animation will be updatedticked. 1 = every frame, 2 = every 2 frames, etc. |
| `EvaluationRate` | `int32` | How often animation will be evaluated. 1 = every frame, 2 = every 2 frames, etc.<br>	   has to be a multiple of UpdateRate. |
| `bInterpolateSkippedFrames` | `uint32` | When skipping a frame, should it be interpolated or frozen? |
| `bShouldUseLodMap` | `uint32` | Whether or not to use the defined LODFrameskip map instead of separate distance factor thresholds |
| `bShouldUseMinLod` | `uint32` | If set, LODFrameskip map will be queried with mesh's MinLodModel instead of current LOD (PredictedLODLevel) |
| `bSkipUpdate` | `uint32` | (This frame) animation update should be skipped. |
| `bSkipEvaluation` | `uint32` | (This frame) animation evaluation should be skipped. |
| `TickedPoseOffestTime` | `float` | Track time we have lost via skipping |
| `AdditionalTime` | `float` | Total time of the last series of skipped updates |
| `BaseNonRenderedUpdateRate` | `int32` | Rate of animation evaluation when non rendered (off screen and dedicated servers).<br>	  a value of 4 means evaluated 1 frame, then 3 frames skipped |
| `BaseNonRenderedUpdateRateHigh` | `int32` | - |
| `MaxDistFromMainChar` | `float` | - |
| `BaseVisibleDistanceFactorThesholds` | `TArray < float >` | Array of MaxDistanceFactor to use for AnimUpdateRate when mesh is visible (rendered).<br>	  MaxDistanceFactor is size on screen, as used by LODs<br>	  Example:<br>	 		BaseVisibleDistanceFactorThesholds.Add(0.4f)<br>	 		BaseVisibleDistanceFactorThesholds.Add(0.2f)<br>	  means:<br>	 		0 frame skip, MaxDistanceFactor > 0.4f<br>	 		1 frame skip, MaxDistanceFactor > 0.2f<br>	 		2 frame skip, MaxDistanceFactor > 0.0f |
| `BaseVisibleDistanceFactorSkipNum` | `int32` | - |
| `LODToFrameSkipMap` | `TMap < int32 , int32 >` | Map of LOD levels to frame skip amounts. if bShouldUseLodMap is set these values will be used for<br>	  the frameskip amounts and the distance factor thresholds will be ignored. The flag and these values<br>	  should be configured using the customization callback when parameters are created for a component.<br>	 <br>	  Note that this is # of frames to skip, so if you have 20, that means every 21th frame, it will update, and evaluate. |
| `MinEvaluationRate` | `int32` | - |
| `LockAnimUpdateRate` | `int32` | - |
| `EnableUROInterpolation` | `bool` | - |
| `MaxEvalRateForInterpolation` | `int32` | Max Evaluation Rate allowed for interpolation to be enabled. Beyond, interpolation will be turned off. |
| `ShiftBucket` | `EUpdateRateShiftBucket` | The bucket to use when deciding which counter to use to calculate shift values |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FARFilter.json -->

# FARFilter

A struct to serve as a filter for Asset Registry queries. Each component element is processed as an 'OR' operation while all the components are processed together as an 'AND' operation.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PackageNames` | `TArray < FName >` | The filter component for package names |
| `PackagePaths` | `TArray < FName >` | The filter component for package paths |
| `ObjectPaths` | `TArray < FName >` | The filter component containing specific object paths |
| `FolderPaths` | `TArray < FName >` | The filter component containing specific object paths |
| `ClassNames` | `TArray < FName >` | The filter component for class names. Instances of the specified classes, but not subclasses (by default), will be included. Derived classes will be included only if bRecursiveClasses is true. |
| `RecursiveClassesExclusionSet` | `TSet < FName >` | Only if bRecursiveClasses is true, the results will exclude classes (and subclasses) in this list |
| `bRecursivePaths` | `bool` | If true, PackagePath components will be recursive |
| `bRecursiveClasses` | `bool` | If true, subclasses of ClassNames will also be included and RecursiveClassesExclusionSet will be excluded. |
| `bIncludeOnlyOnDiskAssets` | `bool` | If true, only on-disk assets will be returned. Be warned that this is rarely what you want and should only be used for performance reasons |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAssetBundleData.json -->

# FAssetBundleData

A struct with a list of asset bundle entries. If one of these is inside a UObject it will get automatically exported as the asset registry tag AssetBundleData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Bundles` | `TArray < FAssetBundleEntry >` | List of bundles defined |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAssetBundleEntry.json -->

# FAssetBundleEntry

A struct representing a single AssetBundle

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BundleScope` | `FPrimaryAssetId` | Asset this bundle is saved within. This is empty for global bundles, or in the saved bundle info |
| `BundleName` | `FName` | Specific name of this bundle, should be unique for a given scope |
| `BundleAssets` | `TArray < FSoftObjectPath >` | List of string assets contained in this bundle |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAssetData.json -->

# FAssetData

A struct to hold important information about an assets found by the Asset Registry
  This struct is transient and should never be serialized

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ObjectPath` | `FName` | The object path for the asset in the form PackageName.AssetName. Only top level objects in a package can have AssetData |
| `PackageName` | `FName` | The name of the package in which the asset is found, this is the full long package name such as GamePathPackage |
| `PackagePath` | `FName` | The path to the package in which the asset is found, this is GamePath with the Package stripped off |
| `AssetName` | `FName` | The name of the asset without the package |
| `AssetClass` | `FName` | The name of the asset's class |
| `AssetTags` | `TArray < FName >` | Custom Asset Type Tag |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAssetEditorOrbitCameraPosition.json -->

# FAssetEditorOrbitCameraPosition

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bIsSet` | `bool` | Whether or not this has been set to a valid value |
| `CamOrbitPoint` | `FVector` | The position to orbit the camera around |
| `CamOrbitZoom` | `FVector` | The distance of the camera from the orbit point |
| `CamOrbitRotation` | `FRotator` | The rotation to apply around the orbit point |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAssetManagerRedirect.json -->

# FAssetManagerRedirect

Simple structure for redirecting an old asset namepath to a new one

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Old` | `FString` | - |
| `New` | `FString` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAssetMapping.json -->

# FAssetMapping

This defines one asset mapping

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceAsset` | `UAnimationAsset *` | source asset |
| `TargetAsset` | `UAnimationAsset *` | source asset |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAtlasTexList.json -->

# FAtlasTexList

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Atlas` | `TArray < FAtlasTextures >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAtlasTextures.json -->

# FAtlasTextures

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Textures` | `TArray < FTextureInfo >` | - |
| `TextureSize` | `FVector2D` | - |
| `MinMipMapTextureIdx` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAtmospherePrecomputeParameters.json -->

# FAtmospherePrecomputeParameters

Structure storing Data for pre-computation

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DensityHeight` | `float` | Rayleigh scattering density height scale, ranges from [0...1] |
| `DecayHeight_DEPRECATED` | `float` | - |
| `MaxScatteringOrder` | `int32` | Maximum scattering order |
| `TransmittanceTexWidth` | `int32` | Transmittance Texture Width |
| `TransmittanceTexHeight` | `int32` | Transmittance Texture Height |
| `IrradianceTexWidth` | `int32` | Irradiance Texture Width |
| `IrradianceTexHeight` | `int32` | Irradiance Texture Height |
| `InscatterAltitudeSampleNum` | `int32` | Number of different altitudes at which to sample inscatter color (size of 3D texture Z dimension) |
| `InscatterMuNum` | `int32` | Inscatter Texture Height |
| `InscatterMuSNum` | `int32` | Inscatter Texture Width |
| `InscatterNuNum` | `int32` | Inscatter Texture Width |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAudioComponentParam.json -->

# FAudioComponentParam

Struct used for storing one per-instance named parameter for this AudioComponent.
 	Certain nodes in the SoundCue may reference parameters by name so they can be adjusted per-instance.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParamName` | `FName` | - |
| `FloatParam` | `float` | - |
| `BoolParam` | `bool` | - |
| `IntParam` | `int32` | - |
| `SoundWaveParam` | `USoundWave *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAudioEQEffect.json -->

# FAudioEQEffect

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FrequencyCenter0` | `float` | Center frequency in Hz for band 0 |
| `Gain0` | `float` | Boostcut of band 0 |
| `Bandwidth0` | `float` | Bandwidth of band 0. Region is center frequency +- Bandwidth 2 |
| `FrequencyCenter1` | `float` | Center frequency in Hz for band 1 |
| `Gain1` | `float` | Boostcut of band 1 |
| `Bandwidth1` | `float` | Bandwidth of band 1. Region is center frequency +- Bandwidth 2 |
| `FrequencyCenter2` | `float` | Center frequency in Hz for band 2 |
| `Gain2` | `float` | Boostcut of band 2 |
| `Bandwidth2` | `float` | Bandwidth of band 2. Region is center frequency +- Bandwidth 2 |
| `FrequencyCenter3` | `float` | Center frequency in Hz for band 3 |
| `Gain3` | `float` | Boostcut of band 3 |
| `Bandwidth3` | `float` | Bandwidth of band 3. Region is center frequency +- Bandwidth 2 |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAudioQualitySettings.json -->

# FAudioQualitySettings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DisplayName` | `FText` | - |
| `MaxChannels` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAutoCompleteCommand.json -->

# FAutoCompleteCommand

Structure for auto-complete commands and their descriptions.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Command` | `FString` | - |
| `Desc` | `FString` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAutoCompleteNode.json -->

# FAutoCompleteNode

Node for storing an auto-complete tree based on each char in the command.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `IndexChar` | `int32` | Char for node in the tree |
| `AutoCompleteListIndices` | `TArray < int32 >` | Indices into AutoCompleteList for commands that match to this level |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAutomationEvent.json -->

# FAutomationEvent

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Type` | `EAutomationEventType` | - |
| `Message` | `FString` | - |
| `Context` | `FString` | - |
| `Filename` | `FString` | - |
| `LineNumber` | `int32` | - |
| `Timestamp` | `FDateTime` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAxisBindingCluster.json -->

# FAxisBindingCluster

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AxisBindingInfos` | `TArray < FAxisBindingInfo >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FAxisBindingInfo.json -->

# FAxisBindingInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AxisName` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBakedAnimationState.json -->

# FBakedAnimationState

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StateName` | `FName` | - |
| `Transitions` | `TArray < FBakedStateExitTransition >` | - |
| `StateRootNodeIndex` | `int32` | - |
| `StartNotify` | `int32` | - |
| `EndNotify` | `int32` | - |
| `FullyBlendedNotify` | `int32` | - |
| `bIsAConduit` | `bool` | - |
| `EntryRuleNodeIndex` | `int32` | - |
| `PlayerNodeIndices` | `TArray < int32 >` | - |
| `bAlwaysResetOnEntry` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBakedAnimationStateMachine.json -->

# FBakedAnimationStateMachine

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MachineName` | `FName` | - |
| `InitialState` | `int32` | - |
| `States` | `TArray < FBakedAnimationState >` | - |
| `Transitions` | `TArray < FAnimationTransitionBetweenStates >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBakedStateExitTransition.json -->

# FBakedStateExitTransition

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CanTakeDelegateIndex` | `int32` | - |
| `CustomResultNodeIndex` | `int32` | - |
| `TransitionIndex` | `int32` | - |
| `bDesiredTransitionReturnValue` | `bool` | - |
| `bAutomaticRemainingTimeRule` | `bool` | - |
| `PoseEvaluatorLinks` | `TArray < int32 >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBaseAttenuationSettings.json -->

# FBaseAttenuationSettings

Base class for attenuation settings.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DistanceAlgorithm` | `EAttenuationDistanceModel` | The type of attenuation as a function of distance to use. |
| `CustomAttenuationCurve` | `FRuntimeFloatCurve` | The custom volume attenuation curve to use. |
| `AttenuationShape` | `TEnumAsByte < enum EAttenuationShape :: Type >` | The shape of the non-custom attenuation method. |
| `dBAttenuationAtMax` | `float` | The attenuation volume at maximum distance in decibels, used for natural attenuation method. |
| `AttenuationShapeExtents` | `FVector` | The dimensions to use for the attenuation shape. Interpretation of the values differ per shape. |
| `ConeOffset` | `float` | The distance back from the sound's origin to begin the cone when using the cone attenuation shape. |
| `FalloffDistance` | `float` | The distance over which volume attenuation occurs. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBasedMovementInfo.json -->

# FBasedMovementInfo

Struct to hold information about the "base" object the character is standing on.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MovementBaseActor` | `AActor *` | - |
| `BoneName` | `FName` | Bone name on component, for skeletal meshes. NAME_None if not a skeletal mesh or if bone is invalid. |
| `Location` | `FVector_NetQuantize100` | Location relative to MovementBase. Only valid if HasRelativeLocation() is true. |
| `Rotation` | `FRotator` | Rotation: relative to MovementBase if HasRelativeRotation() is true, absolute otherwise. |
| `bServerHasBaseComponent` | `bool` | Whether the server says that there is a base. On clients, the component may not have resolved yet. |
| `bRelativeRotation` | `bool` | Whether rotation is relative to the base or absolute. It can only be relative if location is also relative. |
| `bServerHasVelocity` | `bool` | Whether there is a velocity on the server. Used for forcing replication when velocity goes to zero. |
| `MovementBase` | `TWeakObjectPtr < UPrimitiveComponent >` | Component we are based on |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBasedPosition.json -->

# FBasedPosition

Struct for handling positions relative to a base actor, which is potentially moving

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Base` | `AActor *` | - |
| `Position` | `FVector` | - |
| `CachedBaseLocation` | `FVector` | - |
| `CachedBaseRotation` | `FRotator` | - |
| `CachedTransPosition` | `FVector` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBatchedLine.json -->

# FBatchedLine

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Start` | `FVector` | - |
| `End` | `FVector` | - |
| `Color` | `FLinearColor` | - |
| `Thickness` | `float` | - |
| `RemainingLifeTime` | `float` | - |
| `DepthPriority` | `uint8` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBatchedPoint.json -->

# FBatchedPoint

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Position` | `FVector` | - |
| `Color` | `FLinearColor` | - |
| `PointSize` | `float` | - |
| `RemainingLifeTime` | `float` | - |
| `DepthPriority` | `uint8` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBeamModifierOptions.json -->

# FBeamModifierOptions

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bModify` | `uint32` | If true, modify the value associated with this grouping. |
| `bScale` | `uint32` | If true, scale the associated value by the given value. |
| `bLock` | `uint32` | If true, lock the modifier to the life of the particle. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBeamTargetData.json -->

# FBeamTargetData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TargetName` | `FName` | Name of the target. |
| `TargetPercentage` | `float` | Percentage chance the target will be selected (100 = always). |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBehaviorTreeTemplateInfo.json -->

# FBehaviorTreeTemplateInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Asset` | `UBehaviorTree *` | behavior tree asset |
| `Template` | `UBTCompositeNode *` | initialized template |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBillboardData.json -->

# FBillboardData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Position` | `FVector` | - |
| `UVs` | `TArray < FVector2D >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBillBoardMaterialSpriteElement.json -->

# FBillBoardMaterialSpriteElement

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Material` | `UMaterialInterface *` | The material that the sprite is rendered with. |
| `DistanceToOpacityCurve` | `UCurveFloat *` | A curve that maps distance on the X axis to the sprite opacity on the Y axis. |
| `bSizeIsInScreenSpace` | `uint32` | Whether the size is defined in screen-space or world-space. |
| `BaseSizeX` | `float` | The base width of the sprite, multiplied with the DistanceToSizeCurve. |
| `BaseSizeY` | `float` | The base height of the sprite, multiplied with the DistanceToSizeCurve. |
| `DistanceToSizeCurve` | `UCurveFloat *` | A curve that maps distance on the X axis to the sprite size on the Y axis. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBlackboardEntry.json -->

# FBlackboardEntry

blackboard entry definition

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EntryName` | `FName` | - |
| `KeyType` | `UBlackboardKeyType *` | key type and additional properties |
| `bInstanceSynced` | `uint32` | if set to true then this field will be synchronized across all instances of this blackboard |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBlackListAssetData.json -->

# FBlackListAssetData

A struct to hold blacklist information about an assets.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StandardPath` | `FName` | - |
| `FullPath` | `FName` | - |
| `AssetTags` | `TArray < FName >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBLEEnumInfo.json -->

# FBLEEnumInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BLEValue` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBlendBoneByChannelEntry.json -->

# FBlendBoneByChannelEntry

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceBone` | `FBoneReference` | Bone to take Transform from |
| `TargetBone` | `FBoneReference` | Bone to apply Transform to |
| `bBlendTranslation` | `bool` | Copy Translation from Source to Target |
| `bBlendRotation` | `bool` | Copy Rotation from Source to Target |
| `bBlendScale` | `bool` | Copy Scale from Source to Target |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBlendParameter.json -->

# FBlendParameter

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DisplayName` | `FString` | - |
| `Min` | `float` | Min value for this parameter. |
| `Max` | `float` | Max value for this parameter. |
| `GridNum` | `int32` | The number of grid divisions for this parameter (axis). |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBlendProfileBoneEntry.json -->

# FBlendProfileBoneEntry

A single entry for a blend scale within a profile, mapping a bone to a blendscale

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoneReference` | `FBoneReference` | - |
| `BlendScale` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBlendSample.json -->

# FBlendSample

Sample data

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Animation` | `UAnimSequence *` | - |
| `SampleValue` | `FVector` | - |
| `RateScale` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBlendSampleData.json -->

# FBlendSampleData

Transform definition

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SampleDataIndex` | `int32` | - |
| `Animation` | `UAnimSequence *` | - |
| `TotalWeight` | `float` | - |
| `Time` | `float` | - |
| `PreviousTime` | `float` | - |
| `SamplePlayRate` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBlueprintComponentDelegateBinding.json -->

# FBlueprintComponentDelegateBinding

Entry for a delegate to assign after a blueprint has been instanced

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ComponentPropertyName` | `FName` | Name of component property that contains delegate we want to assign to. |
| `DelegatePropertyName` | `FName` | Name of property on the component that we want to assign to. |
| `FunctionNameToBind` | `FName` | Name of function that we want to bind to the delegate. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBlueprintEditorPromotionSettings.json -->

# FBlueprintEditorPromotionSettings

Holds settings for the blueprint editor build promotion tests

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FirstMeshPath` | `FFilePath` | The starting mesh for the blueprint |
| `SecondMeshPath` | `FFilePath` | The mesh to set on the blueprint after the delay |
| `DefaultParticleAsset` | `FFilePath` | Default particle asset to use for tests |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBlueprintInputActionDelegateBinding.json -->

# FBlueprintInputActionDelegateBinding

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InputActionName` | `FName` | - |
| `InputKeyEvent` | `TEnumAsByte < EInputEvent >` | - |
| `FunctionNameToBind` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBlueprintInputAxisDelegateBinding.json -->

# FBlueprintInputAxisDelegateBinding

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InputAxisName` | `FName` | - |
| `FunctionNameToBind` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBlueprintInputAxisKeyDelegateBinding.json -->

# FBlueprintInputAxisKeyDelegateBinding

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AxisKey` | `FKey` | - |
| `FunctionNameToBind` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBlueprintInputDelegateBinding.json -->

# FBlueprintInputDelegateBinding

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bConsumeInput` | `uint32` | - |
| `bExecuteWhenPaused` | `uint32` | - |
| `bOverrideParentBinding` | `uint32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBlueprintInputKeyDelegateBinding.json -->

# FBlueprintInputKeyDelegateBinding

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InputChord` | `FInputChord` | - |
| `InputKeyEvent` | `TEnumAsByte < EInputEvent >` | - |
| `FunctionNameToBind` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBlueprintInputTouchDelegateBinding.json -->

# FBlueprintInputTouchDelegateBinding

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InputKeyEvent` | `TEnumAsByte < EInputEvent >` | - |
| `FunctionNameToBind` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBlueprintWarningSettings.json -->

# FBlueprintWarningSettings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `WarningIdentifier` | `FName` | - |
| `WarningDescription` | `FText` | - |
| `WarningBehavior` | `EBlueprintWarningBehavior` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBlueprintWidgetAnimationDelegateBinding.json -->

# FBlueprintWidgetAnimationDelegateBinding

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Action` | `EWidgetAnimationEvent` | - |
| `AnimationToBind` | `FName` | - |
| `FunctionNameToBind` | `FName` | - |
| `UserTag` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBodyInstance.json -->

# FBodyInstance

Container for a physics representation of an object

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SleepFamily` | `ESleepFamily` | The set of values used in considering when put this body to sleep. |
| `DOFMode` | `TEnumAsByte < EDOFMode :: Type >` | Locks physical movement along specified axis. |
| `CollisionEnabled` | `TEnumAsByte < ECollisionEnabled :: Type >` | Type of collision enabled.<br>	  <br>	 	No Collision      : Will not create any representation in the physics engine. Cannot be used for spatial queries (raycasts, sweeps, overlaps) or simulation (rigid body, constraints). Best performance possible (especially for moving objects)<br>	 	Query Only        : Only used for spatial queries (raycasts, sweeps, and overlaps). Cannot be used for simulation (rigid body, constraints). Useful for character movement and things that do not need physical simulation. Performance gains by keeping data out of simulation tree.<br>	 	Physics Only      : Only used only for physics simulation (rigid body, constraints). Cannot be used for spatial queries (raycasts, sweeps, overlaps). Useful for jiggly bits on characters that do not need per bone detection. Performance gains by keeping data out of query tree<br>	 	Collision Enabled : Can be used for both spatial queries (raycasts, sweeps, overlaps) and simulation (rigid body, constraints). |
| `CollisionProfileName` | `FName` | Collision Profile Name |
| `CollisionResponses` | `FCollisionResponse` | Custom Channels for Responses |
| `bUseCCD` | `uint8` | If true Continuous Collision Detection (CCD) will be used for this component |
| `bNotifyRigidBodyCollision` | `uint8` | Should 'Hit' events fire when this object collides during physics simulation. |
| `bUseShapeCollisionOverride` | `uint8` | PhysicsAsset中有bCollisionPerShape功能，载具中经常用到。<br>	  在使用这个功能时，如果运行时调用了UpdatePhysicsShapeFilterData，shape的flag会被改写为组件中的配置，即bCollisionPerShape功能无效了。<br>	  这里增加一个开关，如果为true，在UpdatePhysicsShapeFilterData时也会去应用PA的bCollisionPerShape功能。	-lyonarzhang |
| `bSimulatePhysics` | `uint8` | If true, this body will use simulation. If false, will be 'fixed' (ie kinematic) and move where it is told. <br>	  For a Skeletal Mesh Component, simulating requires a physics asset setup and assigned on the SkeletalMesh asset.<br>	  For a Static Mesh Component, simulating requires simple collision to be setup on the StaticMesh asset. |
| `bOverrideMass` | `uint8` | If true, mass will not be automatically computed and you must set it directly |
| `bEnableGravity` | `uint8` | If object should have the force of gravity applied |
| `bAutoWeld` | `uint8` | If true and is attached to a parent, the two bodies will be joined into a single rigid body. Physical settings like collision profile and body settings are determined by the root |
| `bStartAwake` | `uint8` | If object should start awake, or if it should initially be sleeping |
| `bGenerateWakeEvents` | `uint8` | Should 'wakesleep' events fire when this object is woken up or put to sleep by the physics simulation. |
| `bUpdateMassWhenScaleChanges` | `uint8` | If true, it will update mass when scale changes |
| `bLockTranslation` | `uint8` | When a Locked Axis Mode is selected, will lock translation on the specified axis |
| `bLockRotation` | `uint8` | When a Locked Axis Mode is selected, will lock rotation to the specified axis |
| `bLockXTranslation` | `uint8` | Lock translation along the X-axis |
| `bLockYTranslation` | `uint8` | Lock translation along the Y-axis |
| `bLockZTranslation` | `uint8` | Lock translation along the Z-axis |
| `bLockXRotation` | `uint8` | Lock rotation about the X-axis |
| `bLockYRotation` | `uint8` | Lock rotation about the Y-axis |
| `bLockZRotation` | `uint8` | Lock rotation about the Z-axis |
| `bOverrideMaxAngularVelocity` | `uint8` | Override the default max angular velocity |
| `bUseAsyncScene` | `uint8` | If true, this body will be put into the asynchronous physics scene. If false, it will be put into the synchronous physics scene.<br>	 If the body is static, it will be placed into both scenes regardless of the value of bUseAsyncScene. |
| `bOverrideMaxDepenetrationVelocity` | `uint8` | Whether this body instance has its own custom MaxDepenetrationVelocity |
| `bOverrideWalkableSlopeOnInstance` | `uint8` | Whether this instance of the object has its own custom walkable slope override setting. |
| `MaxDepenetrationVelocity` | `float` | The maximum velocity used to depenetrate this object |
| `MassInKgOverride` | `float` | Mass of the body in KG. By default we compute this based on physical material and mass scale.<br>	@see bOverrideMass to set this directly |
| `LinearDamping` | `float` | 'Drag' force added to reduce linear movement |
| `AngularDamping` | `float` | 'Drag' force added to reduce angular movement |
| `CustomDOFPlaneNormal` | `FVector` | Locks physical movement along a custom plane for a given normal. |
| `COMNudge` | `FVector` | User specified offset for the center of mass of this object, from the calculated location |
| `bUseOverrideCOM` | `bool` | 为true时，锁定重心位置为OverrideCOM(Component space)，只对载具有效 |
| `OverrideCOM` | `FVector` | - |
| `MassScale` | `float` | Per-instance scaling of mass |
| `InertiaTensorScale` | `FVector` | Per-instance scaling of inertia (bigger number means  it'll be harder to rotate) |
| `bUsedPhysSimpleStaticMesh` | `uint8` | - |
| `ObjectType` | `TEnumAsByte < enum ECollisionChannel >` | Enum indicating what type of object this should be considered as when it moves |
| `WalkableSlopeOverride` | `FWalkableSlopeOverride` | Custom walkable slope override setting for this instance.<br>	 @see GetWalkableSlopeOverride(), SetWalkableSlopeOverride() |
| `PhysMaterialOverride` | `UPhysicalMaterial *` | Allows you to override the PhysicalMaterial to use for simple collision on this body. |
| `MaxAngularVelocity` | `float` | The maximum angular velocity for this instance |
| `CustomSleepThresholdMultiplier` | `float` | If the SleepFamily is set to custom, multiply the natural sleep threshold by this amount. A higher number will cause the body to sleep sooner. |
| `StabilizationThresholdMultiplier` | `float` | Stabilization factor for this body if Physics stabilization is enabled. A higher number will cause more aggressive stabilization at the risk of loss of momentum at low speeds. A value of 0 will disable stabilization for this body. |
| `PhysicsBlendWeight` | `float` | Influence of rigid body physics (blending) on the mesh's pose (0.0 == use only animation, 1.0 == use only physics) <br>	 Provide appropriate interface for doing this instead of allowing BlueprintReadWrite |
| `PositionSolverIterationCount` | `int32` | This physics body's solver iteration count for position. Increasing this will be more CPU intensive, but better stabilized. |
| `VelocitySolverIterationCount` | `int32` | This physics body's solver iteration count for velocity. Increasing this will be more CPU intensive, but better stabilized. |
| `ResponseToChannels_DEPRECATED` | `FCollisionResponseContainer` | Types of objects that this physics objects will collide with. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBoneListTransforms.json -->

# FBoneListTransforms

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoneNames` | `TArray < FName >` | Array of names |
| `Transforms` | `TArray < FTransform >` | Array of transforms |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBoneMirrorConfig.json -->

# FBoneMirrorConfig

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MirrorBoneSource` | `FName` | - |
| `MirrorType` | `EBoneMirrorType` | - |
| `Depth` | `int32` | - |
| `MirrorBoneTarget` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBoneMirrorConfig_AutoLR.json -->

# FBoneMirrorConfig_AutoLR

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MirrorBoneStart` | `FName` | - |
| `Depth` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBoneMirrorConfig_GivenName.json -->

# FBoneMirrorConfig_GivenName

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MirrorBoneSource` | `FName` | - |
| `MirrorBoneTarget` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBoneMirrorExport.json -->

# FBoneMirrorExport

Structure to exportimport bone mirroring information

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoneName` | `FName` | - |
| `SourceBoneName` | `FName` | - |
| `BoneFlipAxis` | `TEnumAsByte < EAxis :: Type >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBoneMirrorInfo.json -->

# FBoneMirrorInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceIndex` | `int32` | The bone to mirror. |
| `BoneFlipAxis` | `TEnumAsByte < EAxis :: Type >` | Axis the bone is mirrored across. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBoneMirrorMapData.json -->

# FBoneMirrorMapData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BonePairFirst` | `FName` | - |
| `BonePairSecond` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBoneNode.json -->

# FBoneNode

Each Bone node in BoneTree

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Name_DEPRECATED` | `FName` | Name of bone, this is the search criteria to match with mesh bone. This will be NAME_None if deleted. |
| `ParentIndex_DEPRECATED` | `int32` | Parent Index. -1 if not used. The root has 0 as its parent. Do not delete the element but set this to -1. If it is revived by other reason, fix up this link. |
| `TranslationRetargetingMode` | `TEnumAsByte < EBoneTranslationRetargetingMode :: Type >` | Retargeting Mode for Translation Component. |
| `PerBoneOverrideRetargetingModeConfig` | `TMap < FName , TEnumAsByte < EBoneTranslationRetargetingMode :: Type > >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBoneOffset.json -->

# FBoneOffset

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bTransition` | `bool` | - |
| `bRotation` | `bool` | - |
| `bScale` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBoneReductionSetting.json -->

# FBoneReductionSetting

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BonesToRemove` | `TArray < FName >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBoneSocketTarget.json -->

# FBoneSocketTarget

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bUseSocket` | `bool` | - |
| `BoneReference` | `FBoneReference` | - |
| `SocketReference` | `FSocketReference` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBonesTransfroms.json -->

# FBonesTransfroms

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Names` | `TArray < FName >` | Array of names |
| `Transforms` | `TArray < FTransform >` | Array of transforms |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBonesTransfromsWithFPP.json -->

# FBonesTransfromsWithFPP

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Names` | `TArray < FName >` | Array of names |
| `Transforms` | `TArray < FTransform >` | Array of transforms |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBoolTrackKey.json -->

# FBoolTrackKey

Information for one event in the track.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Time` | `float` | - |
| `Value` | `uint32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBoundActorProxy.json -->

# FBoundActorProxy

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoundActor` | `AActor *` | Specifies the actor to override the binding with |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBox.json -->

# FBox

A bounding box.
  The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\Box.h

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Min` | `FVector` | - |
| `Max` | `FVector` | - |
| `IsValid` | `uint8` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBox2D.json -->

# FBox2D

A rectangular 2D Box.
  The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\Box2D.h

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Min` | `FVector2D` | - |
| `Max` | `FVector2D` | - |
| `bIsValid` | `uint8` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBoxSphereBounds.json -->

# FBoxSphereBounds

A bounding box and bounding sphere with the same origin.
  The full C++ class is located here : Engine\Source\Runtime\Core\Public\Math\BoxSphereBounds.h

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Origin` | `FVector` | - |
| `BoxExtent` | `FVector` | - |
| `SphereRadius` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBPInterfaceDescription.json -->

# FBPInterfaceDescription

Struct containing information about what interfaces are implemented in this blueprint

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Interface` | `TSubclassOf < UInterface >` | Reference to the interface class we're adding to this blueprint |
| `Graphs` | `TArray < UEdGraph * >` | References to the graphs associated with the required functions for this interface |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBPVariableDescription.json -->

# FBPVariableDescription

Struct indicating a variable in the generated class

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VarName` | `FName` | Name of the variable |
| `VarGuid` | `FGuid` | A Guid that will remain constant even if the VarName changes |
| `VarType` | `FEdGraphPinType` | Type of the variable |
| `FriendlyName` | `FString` | Friendly name of the variable |
| `Category` | `FText` | Category this variable should be in |
| `PropertyFlags` | `uint64` | Property flags for this variable - Changed from int32 to uint64 |
| `RepNotifyFunc` | `FName` | - |
| `ReplicationCondition` | `TEnumAsByte < ELifetimeCondition >` | - |
| `MetaDataArray` | `TArray < struct FBPVariableMetaDataEntry >` | Metadata information for this variable |
| `DefaultValue` | `FString` | Optional new default value stored as string |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBPVariableMetaDataEntry.json -->

# FBPVariableMetaDataEntry

One metadata entry for a variable

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DataKey` | `FName` | Name of metadata key |
| `DataValue` | `FString` | Name of metadata value |
| `Flag` | `EVariableMetaDataFlag` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBranchFilter.json -->

# FBranchFilter

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoneName` | `FName` | Bone Name to filter |
| `BlendDepth` | `int32` | Blend Depth |
| `bIsIgnoreChildrenBones` | `bool` | 是否只针对改骨骼进行融合，不考虑其所有子节点。默认为false |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBranchingPoint.json -->

# FBranchingPoint

Remove FBranchingPoint when VER_UE4_MONTAGE_BRANCHING_POINT_REMOVAL is removed.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EventName` | `FName` | - |
| `DisplayTime_DEPRECATED` | `float` | - |
| `TriggerTimeOffset` | `float` | An offset from the DisplayTime to the actual time we will trigger the notify, as we cannot always trigger it exactly at the time the user wants |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBranchingPointMarker.json -->

# FBranchingPointMarker

AnimNotifies marked as BranchingPoints will create these markers on their BeginEnd times.
	They create stopping points when the Montage is being ticked to dispatch events.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NotifyIndex` | `int32` | - |
| `TriggerTime` | `float` | - |
| `NotifyEventType` | `TEnumAsByte < EAnimNotifyEventType :: Type >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBTCompositeChild.json -->

# FBTCompositeChild

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ChildComposite` | `UBTCompositeNode *` | child node |
| `ChildTask` | `UBTTaskNode *` | - |
| `Decorators` | `TArray < UBTDecorator * >` | execution decorators |
| `DecoratorOps` | `TArray < FBTDecoratorLogic >` | logic operations for decorators |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBTDecoratorLogic.json -->

# FBTDecoratorLogic

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Operation` | `TEnumAsByte < EBTDecoratorLogic :: Type >` | - |
| `Number` | `uint16` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBuilderPoly.json -->

# FBuilderPoly

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VertexIndices` | `TArray < int32 >` | - |
| `Direction` | `int32` | - |
| `ItemName` | `FName` | - |
| `PolyFlags` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBuildPromotionImportWorkflowSettings.json -->

# FBuildPromotionImportWorkflowSettings

Holds settings for the import workflow stage of the build promotion test

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Diffuse` | `FEditorImportWorkflowDefinition` | Import settings for the Diffuse texture |
| `Normal` | `FEditorImportWorkflowDefinition` | Import settings for the Normalmap texture |
| `StaticMesh` | `FEditorImportWorkflowDefinition` | Import settings for the static mesh |
| `ReimportStaticMesh` | `FEditorImportWorkflowDefinition` | Import settings for the static mesh to re-import |
| `BlendShapeMesh` | `FEditorImportWorkflowDefinition` | Import settings for the blend shape |
| `MorphMesh` | `FEditorImportWorkflowDefinition` | Import settings for the morph mesh |
| `SkeletalMesh` | `FEditorImportWorkflowDefinition` | Import settings for the skeletal mesh |
| `Animation` | `FEditorImportWorkflowDefinition` | Import settings for the animation asset.  (Will automatically use the skeleton of the skeletal mesh above) |
| `Sound` | `FEditorImportWorkflowDefinition` | Import settings for the sound |
| `SurroundSound` | `FEditorImportWorkflowDefinition` | Import settings for the surround sound (Select any of the channels.  It will auto import the rest) |
| `OtherAssetsToImport` | `TArray < FEditorImportWorkflowDefinition >` | Import settings for any other assets you may want to import |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBuildPromotionNewProjectSettings.json -->

# FBuildPromotionNewProjectSettings

Holds settings for the new project stage of the build promotion test

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NewProjectFolderOverride` | `FDirectoryPath` | The path for the new project |
| `NewProjectNameOverride` | `FString` | The name of the project |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBuildPromotionOpenAssetSettings.json -->

# FBuildPromotionOpenAssetSettings

Holds settings for the open assets stage of the build promotion test

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BlueprintAsset` | `FFilePath` | The blueprint asset to open |
| `MaterialAsset` | `FFilePath` | The material asset to open |
| `ParticleSystemAsset` | `FFilePath` | The particle system asset to open |
| `SkeletalMeshAsset` | `FFilePath` | The skeletal mesh asset to open |
| `StaticMeshAsset` | `FFilePath` | The static mesh asset to open |
| `TextureAsset` | `FFilePath` | The texture asset to open |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FBuildPromotionTestSettings.json -->

# FBuildPromotionTestSettings

Holds settings for the editor build promotion test

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefaultStaticMeshAsset` | `FFilePath` | Default static mesh asset to apply materials to |
| `ImportWorkflow` | `FBuildPromotionImportWorkflowSettings` | Import workflow settings |
| `OpenAssets` | `FBuildPromotionOpenAssetSettings` | Open assets settings |
| `NewProjectSettings` | `FBuildPromotionNewProjectSettings` | New project settings |
| `SourceControlMaterial` | `FFilePath` | Material to modify for the content browser step |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FButtonInputActionBinding.json -->

# FButtonInputActionBinding

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InputEvent` | `EButtonInputActionEvent` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FButtonInputActionBindings.json -->

# FButtonInputActionBindings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ActionMappings` | `TArray < FButtonInputActionBinding >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FButtonInputActionBindingsStruct.json -->

# FButtonInputActionBindingsStruct

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InputActionBindings` | `TMap < FButtonInputActionSelector , FButtonInputActionBindings >` | - |
| `InputAxisBindings` | `TMap < FButtonInputAxisSelector , FWidgetInputAxisBindings >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FButtonInputActionSelector.json -->

# FButtonInputActionSelector

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ActionName` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FButtonInputAxisSelector.json -->

# FButtonInputAxisSelector

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AxisName` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FButtonListenAction.json -->

# FButtonListenAction

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ActionName` | `FName` | - |
| `EventType` | `TEnumAsByte < EButtonListenActionEvent :: Type >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FButtonStyle.json -->

# FButtonStyle

Represents the appearance of an SButton

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Normal` | `FSlateBrush` | Button appearance when the button is not hovered or pressed |
| `Hovered` | `FSlateBrush` | Button appearance when hovered |
| `Pressed` | `FSlateBrush` | Button appearance when pressed |
| `Disabled` | `FSlateBrush` | Button appearance when disabled, by default this is set to an invalid resource when that is the case default disabled drawing is used. |
| `NormalPadding` | `FMargin` | Padding that accounts for the border in the button's background image.<br>	  When this is applied, the content of the button should appear flush<br>	  with the button's border. Use this padding when the button is not pressed. |
| `PressedPadding` | `FMargin` | Same as NormalPadding but used when the button is pressed. Allows for moving the content to match<br>	  any "movement" in the button's border image. |
| `PressedSlateSound` | `FSlateSound` | The sound the button should play when pressed |
| `HoveredSlateSound` | `FSlateSound` | The sound the button should play when initially hovered over |
| `PressedSound_DEPRECATED` | `FName` | - |
| `HoveredSound_DEPRECATED` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCacheCameraShakeData.json -->

# FCacheCameraShakeData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InsList` | `TArray < UCameraShake * >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCachedBoneParamInfo.json -->

# FCachedBoneParamInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CachedBoneName` | `FName` | - |
| `CachedBoneFlag` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCachedBoneTransformContainer.json -->

# FCachedBoneTransformContainer

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SaveFrameCounte` | `uint64` | - |
| `SaveIndex` | `int64` | - |
| `BoneTransform` | `FTransform` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCachedBoneTransformInfo.json -->

# FCachedBoneTransformInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoneTransformMap` | `TMap < FName , FCachedBoneTransformContainer >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCameraCacheEntry.json -->

# FCameraCacheEntry

Cached camera POV info, stored as optimization so we only
  need to do a full camera update once per tick.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TimeStamp` | `float` | World time this entry was created. |
| `POV` | `FMinimalViewInfo` | Camera POV to cache. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCameraCutInfo.json -->

# FCameraCutInfo

Helper struct for storing the camera world-position for each camera cut in the cinematic.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Location` | `FVector` | - |
| `TimeStamp` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCameraExposureSettings.json -->

# FCameraExposureSettings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Method` | `TEnumAsByte < enum EAutoExposureMethod >` | Luminance computation method |
| `LowPercent` | `float` | The eye adaptation will adapt to a value extracted from the luminance histogram of the scene color.<br>	  The value is defined as having x percent below this brightness. Higher values give bright spots on the screen more priority<br>	  but can lead to less stable results. Lower values give the medium and darker values more priority but might cause burn out of<br>	  bright spots.<br>	  >0, <100, good values are in the range 70 .. 80 |
| `HighPercent` | `float` | The eye adaptation will adapt to a value extracted from the luminance histogram of the scene color.<br>	  The value is defined as having x percent below this brightness. Higher values give bright spots on the screen more priority<br>	  but can lead to less stable results. Lower values give the medium and darker values more priority but might cause burn out of<br>	  bright spots.<br>	  >0, <100, good values are in the range 80 .. 95 |
| `MinBrightness` | `float` | A good value should be positive near 0. This is the minimum brightness the auto exposure can adapt to.<br>	  It should be tweaked in a dark lighting situation (too small: image appears too bright, too large: image appears too dark).<br>	  Note: Tweaking emissive materials and lights or tweaking auto exposure can look the same. Tweaking auto exposure has global<br>	  effect and defined the HDR range - you don't want to change that late in the project development.<br>	  Eye Adaptation is disabled if MinBrightness = MaxBrightness |
| `MaxBrightness` | `float` | A good value should be positive (2 is a good value). This is the maximum brightness the auto exposure can adapt to.<br>	  It should be tweaked in a bright lighting situation (too small: image appears too bright, too large: image appears too dark).<br>	  Note: Tweaking emissive materials and lights or tweaking auto exposure can look the same. Tweaking auto exposure has global<br>	  effect and defined the HDR range - you don't want to change that late in the project development.<br>	  Eye Adaptation is disabled if MinBrightness = MaxBrightness |
| `SpeedUp` | `float` | >0 |
| `SpeedDown` | `float` | >0 |
| `Bias` | `float` | Logarithmic adjustment for the exposure. Only used if a tonemapper is specified.<br>	  0: no adjustment, -1:2x darker, -2:4x darker, 1:2x brighter, 2:4x brighter, ... |
| `HistogramLogMin` | `float` | temporary exposed until we found good values, -8: 1256, -10: 11024 |
| `HistogramLogMax` | `float` | temporary exposed until we found good values 4: 16, 8: 256 |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCameraFilmbackSettings.json -->

# FCameraFilmbackSettings

#note, this struct has a details customization in CameraFilmbackSettingsCustomization.cpph

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SensorWidth` | `float` | Horizontal size of filmback or digital sensor, in mm. |
| `SensorHeight` | `float` | Vertical size of filmback or digital sensor, in mm. |
| `SensorAspectRatio` | `float` | Read-only. Computed from Sensor dimensions. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCameraFocusSettings.json -->

# FCameraFocusSettings

Settings to control camera focus

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FocusMethod` | `ECameraFocusMethod` | Which method to use to handle camera focus |
| `ManualFocusDistance` | `float` | Manually-controlled focus distance (manual focus mode only) |
| `TrackingFocusSettings` | `FCameraTrackingFocusSettings` | Settings to control tracking focus (tracking focus mode only) |
| `bDrawDebugFocusPlane` | `uint8` | True to draw a translucent plane at the current focus depth, for easy tweaking. |
| `DebugFocusPlaneColor` | `FColor` | For customizing the focus plane color, in case the default doesn't show up well in your scene. |
| `bSmoothFocusChanges` | `uint8` | True to use interpolation to smooth out changes in focus distance, false for focus distance changes to be instantaneous. |
| `FocusSmoothingInterpSpeed` | `float` | Controls interpolation speed when smoothing focus distance changes. Ignored if bSmoothFocusChanges is false. |
| `FocusOffset` | `float` | Additional focus depth offset, used for manually tweaking if your chosen focus method needs adjustment |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCameraLensSettings.json -->

# FCameraLensSettings

#note, this struct has a details customization in CameraLensSettingsCustomization.cpph

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MinFocalLength` | `float` | Minimum focal length for this lens |
| `MaxFocalLength` | `float` | Maximum focal length for this lens |
| `MinFStop` | `float` | Minimum aperture for this lens (e.g. 2.8 for an f2.8 lens) |
| `MaxFStop` | `float` | Minimum aperture for this lens (e.g. 2.8 for an f2.8 lens) |
| `MinimumFocusDistance` | `float` | Shortest distance this lens can focus on. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCameraLookatTrackingSettings.json -->

# FCameraLookatTrackingSettings

Settings to control the camera's lookat feature

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bEnableLookAtTracking` | `uint8` | True to enable lookat tracking, false otherwise. <br>	UPROPERTY(Interp, EditAnywhere, BlueprintReadWrite, Category = "LookAt") |
| `bDrawDebugLookAtTrackingPosition` | `uint8` | True to draw a debug representation of the lookat location |
| `LookAtTrackingInterpSpeed` | `float` | Controls degree of smoothing. 0.f for no smoothing, higher numbers for fastertighter tracking. |
| `ActorToTrack` | `AActor *` | If set, camera will track this actor's location |
| `RelativeOffset` | `FVector` | Offset from actor position to look at. Relative to actor if tracking an actor, relative to world otherwise. |
| `bAllowRoll` | `uint8` | True to allow user-defined roll, false otherwise. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCameraPreviewInfo.json -->

# FCameraPreviewInfo

Preview APawn class for this track

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PawnClass` | `TSubclassOf < APawn >` | - |
| `AnimSeq` | `UAnimSequence *` | - |
| `Location` | `FVector` | for now this is read-only. It has maintenance issue to be resolved if I enable this. |
| `Rotation` | `FRotator` | - |
| `PawnInst` | `APawn *` | APawn Inst - CameraAnimInst doesn't really exist in editor |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCameraTrackingFocusSettings.json -->

# FCameraTrackingFocusSettings

Settings to control tracking-focus mode.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ActorToTrack` | `AActor *` | Focus distance will be tied to this actor's location. |
| `RelativeOffset` | `FVector` | Offset from actor position to track. Relative to actor if tracking an actor, relative to world otherwise. |
| `bDrawDebugTrackingFocusPoint` | `uint8` | True to draw a debug representation of the tracked position. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCampConfigInfo.json -->

# FCampConfigInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CampID` | `int32` | - |
| `CampName` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCampReleation.json -->

# FCampReleation

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CampA_ID` | `int32` | - |
| `CampB_ID` | `int32` | - |
| `Releation` | `ECampRelation` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCanvasIcon.json -->

# FCanvasIcon

Holds texture information with UV coordinates as well.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Texture` | `UTexture *` | Source texture |
| `U` | `float` | UV coords |
| `V` | `float` | - |
| `UL` | `float` | - |
| `VL` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCanvasUVTri.json -->

# FCanvasUVTri

Simple 2d triangle with UVs

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `V0_Pos` | `FVector2D` | Position of first vertex |
| `V0_UV` | `FVector2D` | UV of first vertex |
| `V0_Color` | `FLinearColor` | Color of first vertex |
| `V1_Pos` | `FVector2D` | Position of second vertex |
| `V1_UV` | `FVector2D` | UV of second vertex |
| `V1_Color` | `FLinearColor` | Color of second vertex |
| `V2_Pos` | `FVector2D` | Position of third vertex |
| `V2_UV` | `FVector2D` | UV of third vertex |
| `V2_Color` | `FLinearColor` | Color of third vertex |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCaptureProtocolID.json -->

# FCaptureProtocolID

Structure used to uniquely identify a specific capture protocol

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Identifier` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCaptureResolution.json -->

# FCaptureResolution

Structure representing a capture resolution

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ResX` | `uint32` | - |
| `ResY` | `uint32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCDLODMeshNodeData.json -->

# FCDLODMeshNodeData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Material` | `UMaterialInterface *` | - |
| `MaterialInstance` | `UMaterialInstanceConstant *` | - |
| `MobileMaterialInterface` | `UMaterialInstance *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCheckBoxStyle.json -->

# FCheckBoxStyle

Represents the appearance of an SCheckBox

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CheckBoxType` | `TEnumAsByte < ESlateCheckBoxType :: Type >` | The visual type of the checkbox |
| `UncheckedImage` | `FSlateBrush` | CheckBox appearance when the CheckBox is unchecked (normal) |
| `UncheckedHoveredImage` | `FSlateBrush` | CheckBox appearance when the CheckBox is unchecked and hovered |
| `UncheckedPressedImage` | `FSlateBrush` | CheckBox appearance when the CheckBox is unchecked and hovered |
| `CheckedImage` | `FSlateBrush` | CheckBox appearance when the CheckBox is checked |
| `CheckedHoveredImage` | `FSlateBrush` | CheckBox appearance when checked and hovered |
| `CheckedPressedImage` | `FSlateBrush` | CheckBox appearance when checked and pressed |
| `UndeterminedImage` | `FSlateBrush` | CheckBox appearance when the CheckBox is undetermined |
| `UndeterminedHoveredImage` | `FSlateBrush` | CheckBox appearance when CheckBox is undetermined and hovered |
| `UndeterminedPressedImage` | `FSlateBrush` | CheckBox appearance when CheckBox is undetermined and pressed |
| `Padding` | `FMargin` | Padding |
| `ForegroundColor` | `FSlateColor` | The foreground color |
| `BorderBackgroundColor` | `FSlateColor` | BorderBackgroundColor refers to the actual color and opacity of the supplied border image on toggle buttons |
| `CheckedSlateSound` | `FSlateSound` | The sound the check box should play when checked |
| `UncheckedSlateSound` | `FSlateSound` | The sound the check box should play when unchecked |
| `HoveredSlateSound` | `FSlateSound` | The sound the check box should play when initially hovered over |
| `CheckedSound_DEPRECATED` | `FName` | - |
| `UncheckedSound_DEPRECATED` | `FName` | - |
| `HoveredSound_DEPRECATED` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FClassRedirect.json -->

# FClassRedirect

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ObjectName` | `FName` | - |
| `OldClassName` | `FName` | - |
| `NewClassName` | `FName` | - |
| `OldSubobjName` | `FName` | - |
| `NewSubobjName` | `FName` | - |
| `NewClassClass` | `FName` | - |
| `NewClassPackage` | `FName` | - |
| `InstanceOnly` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FClientReceiveData.json -->

# FClientReceiveData

Handles the many pieces of data passed into Client Receive

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LocalPC` | `APlayerController *` | - |
| `MessageType` | `FName` | - |
| `MessageIndex` | `int32` | - |
| `MessageString` | `FString` | - |
| `RelatedPlayerState_1` | `APlayerState *` | - |
| `RelatedPlayerState_2` | `APlayerState *` | - |
| `OptionalObject` | `UObject *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FClipmapFoliageHealthAndAbsorption.json -->

# FClipmapFoliageHealthAndAbsorption

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FoliageHealthMap` | `TMap < FClipmapGenOneOriChannel , float >` | - |
| `FoliageHealthAdd` | `FClipmapGenOneOriChannel` | - |
| `FoliageHealthSubtract` | `FClipmapGenOneOriChannel` | - |
| `bUseWaterDepthToGenerateAbsorption` | `bool` | - |
| `WaterAbsorption` | `FClipmapGenOneOriChannel` | - |
| `WaterDepth` | `FClipmapGenOneOriChannel` | - |
| `EdgeTransitionRange` | `float` | - |
| `BlurRadius` | `int32` | - |
| `ContrastStrength` | `float` | - |
| `BrightnessScale` | `float` | - |
| `ShallowBoost` | `float` | - |
| `DebugTexture` | `UTexture2D *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FClipmapGenOneOriChannel.json -->

# FClipmapGenOneOriChannel

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OriTexture` | `UTexture2D *` | - |
| `bUseForLandLayer` | `bool` | - |
| `LandLayerInfo` | `ULandscapeLayerInfoObject *` | - |
| `Channel` | `TEnumAsByte < EClipmapGenChannel >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FClipmapInfo.json -->

# FClipmapInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ChunkOffsetInFile` | `int32` | - |
| `FileSize` | `int32` | - |
| `ImageSize` | `int32` | - |
| `TotalTile` | `int32` | - |
| `MipLevel` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FClipmapInfos.json -->

# FClipmapInfos

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Infos` | `TArray < FClipmapInfo >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FClipmapLandscapeTint.json -->

# FClipmapLandscapeTint

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TintConfig` | `FClipmapGenOneOriChannel` | - |
| `IntensityConfig` | `FClipmapGenOneOriChannel` | - |
| `DepthCurve` | `UCurveLinearColor *` | - |
| `bHasBrushTint` | `bool` | - |
| `TintLayerName` | `FName` | - |
| `BrushPresetColors` | `TArray < FLinearColor >` | 笔刷预设色列表，美术在此配置可选的染色颜色，地形笔刷UI会提供下拉框选择 |
| `MaxWaterNum` | `int32` | - |
| `TintMaterialInstance` | `UMaterialInstanceConstant *` | 染色完成后自动设置LutNum的材质实例（可选，配置后每次生成染色会自动写入LutNum参数） |
| `TintLutNumParamName` | `FName` | 材质实例上的LutNum标量参数名 |
| `WaterTintLutNumParamName` | `FName` | - |
| `LandscapeTintLUT` | `UTexture2D *` | - |
| `CustomNodeCode` | `FString` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FClipmapSetting.json -->

# FClipmapSetting

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NumMip` | `int32` | - |
| `TotalMip` | `int32` | - |
| `PixelBytes` | `int32` | - |
| `DecompressPixelBytes` | `int32` | - |
| `BlockSizeX` | `int32` | - |
| `BlockSizeY` | `int32` | - |
| `PixelFormat` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FClipmapWetness.json -->

# FClipmapWetness

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `WetnessLayerName` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FClothCollisionData.json -->

# FClothCollisionData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Spheres` | `TArray < FClothCollisionPrim_Sphere >` | - |
| `SphereConnections` | `TArray < FClothCollisionPrim_SphereConnection >` | - |
| `Convexes` | `TArray < FClothCollisionPrim_Convex >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FClothCollisionPrim_Convex.json -->

# FClothCollisionPrim_Convex

Data for a single convex element
 	A convex is a collection of planes, in which the clothing will attempt to stay outside of the
 	shape created by the planes combined.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Planes` | `TArray < FPlane >` | - |
| `BoneIndex` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FClothCollisionPrim_Sphere.json -->

# FClothCollisionPrim_Sphere

Data for a single sphere primitive in the clothing simulation. This can either be a 
   sphere on its own, or part of a capsule referenced by the indices in FClothCollisionPrim_Capsule

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoneIndex` | `int32` | - |
| `Radius` | `float` | - |
| `LocalPosition` | `FVector` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FClothCollisionPrim_SphereConnection.json -->

# FClothCollisionPrim_SphereConnection

Data for a single connected sphere primitive. This should be configured after all spheres have
   been processed as they are really just indexing the existing spheres

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SphereIndices` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FClothConfig.json -->

# FClothConfig

Holds initial, asset level config for clothing actors.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `WindMethod` | `EClothingWindMethod` | - |
| `VerticalConstraintConfig` | `FClothConstraintSetup` | - |
| `HorizontalConstraintConfig` | `FClothConstraintSetup` | - |
| `BendConstraintConfig` | `FClothConstraintSetup` | - |
| `ShearConstraintConfig` | `FClothConstraintSetup` | - |
| `SelfCollisionRadius` | `float` | - |
| `SelfCollisionStiffness` | `float` | - |
| `SelfCollisionCullScale` | `float` | Scale to use for the radius of the culling checks for self collisions.<br>	  Any other self collision body within the radius of this check will be culled.<br>	  This helps performance with higher resolution meshes by reducing the number<br>	  of colliding bodies within the cloth. Reducing this will have a negative<br>	  effect on performance! |
| `Damping` | `FVector` | - |
| `Friction` | `float` | - |
| `WindDragCoefficient` | `float` | - |
| `WindLiftCoefficient` | `float` | - |
| `LinearDrag` | `FVector` | - |
| `AngularDrag` | `FVector` | - |
| `LinearInertiaScale` | `FVector` | - |
| `AngularInertiaScale` | `FVector` | - |
| `CentrifugalInertiaScale` | `FVector` | - |
| `SolverFrequency` | `float` | - |
| `StiffnessFrequency` | `float` | - |
| `GravityScale` | `float` | - |
| `TetherStiffness` | `float` | - |
| `TetherLimit` | `float` | - |
| `CollisionThickness` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FClothConstraintSetup.json -->

# FClothConstraintSetup

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Stiffness` | `float` | - |
| `StiffnessMultiplier` | `float` | - |
| `StretchLimit` | `float` | - |
| `CompressionLimit` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FClothingAssetData_Legacy.json -->

# FClothingAssetData_Legacy

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AssetName` | `FName` | - |
| `ApexFileName` | `FString` | - |
| `bClothPropertiesChanged` | `bool` | - |
| `PhysicsProperties` | `FClothPhysicsProperties_Legacy` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FClothLODData.json -->

# FClothLODData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PhysicalMeshData` | `FClothPhysicalMeshData` | - |
| `CollisionData` | `FClothCollisionData` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FClothParameterMask_PhysMesh.json -->

# FClothParameterMask_PhysMesh

A mask is simply some storage for a physical mesh parameter painted onto clothing.
  Used in the editor for users to paint onto and then target to a parameter, which
  is then later applied to a phys mesh

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaskName` | `FName` | Name of the mask, mainly for users to differentiate |
| `CurrentTarget` | `MaskTarget_PhysMesh` | The currently targeted parameter for the mask |
| `MaxValue` | `float` | The maximum value currently in the mask value array |
| `MinValue` | `float` | The maximum value currently in the mask value array |
| `Values` | `TArray < float >` | The actual values stored in the mask |
| `bEnabled` | `bool` | Whether this mask is enabled and able to effect final mesh values |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FClothPhysicalMeshData.json -->

# FClothPhysicalMeshData

Physical mesh data created during asset import or created from a skeletal mesh

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Vertices` | `TArray < FVector >` | - |
| `Normals` | `TArray < FVector >` | - |
| `Indices` | `TArray < uint32 >` | - |
| `MaxDistances` | `TArray < float >` | - |
| `BackstopDistances` | `TArray < float >` | - |
| `BackstopRadiuses` | `TArray < float >` | - |
| `InverseMasses` | `TArray < float >` | - |
| `BoneData` | `TArray < FClothVertBoneData >` | - |
| `MaxBoneWeights` | `int32` | - |
| `NumFixedVerts` | `int32` | - |
| `SelfCollisionIndices` | `TArray < uint32 >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FClothPhysicsProperties_Legacy.json -->

# FClothPhysicsProperties_Legacy

Legacy object for back-compat loading, no longer used by clothing system

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VerticalResistance` | `float` | - |
| `HorizontalResistance` | `float` | - |
| `BendResistance` | `float` | - |
| `ShearResistance` | `float` | - |
| `Friction` | `float` | - |
| `Damping` | `float` | - |
| `TetherStiffness` | `float` | - |
| `TetherLimit` | `float` | - |
| `Drag` | `float` | - |
| `StiffnessFrequency` | `float` | - |
| `GravityScale` | `float` | - |
| `MassScale` | `float` | - |
| `InertiaBlend` | `float` | - |
| `SelfCollisionThickness` | `float` | - |
| `SelfCollisionSquashScale` | `float` | - |
| `SelfCollisionStiffness` | `float` | - |
| `SolverFrequency` | `float` | - |
| `FiberCompression` | `float` | - |
| `FiberExpansion` | `float` | - |
| `FiberResistance` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FClothVertBoneData.json -->

# FClothVertBoneData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NumInfluences` | `int32` | - |
| `BoneIndices` | `uint16` | - |
| `BoneWeights` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FClusterNode.json -->

# FClusterNode

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoundMin` | `FVector` | - |
| `FirstChild` | `int32` | - |
| `BoundMax` | `FVector` | - |
| `LastChild` | `int32` | - |
| `FirstInstance` | `int32` | - |
| `LastInstance` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCollectionBoolParameter.json -->

# FCollectionBoolParameter

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefaultValue` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCollectionIntParameter.json -->

# FCollectionIntParameter

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefaultValue` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCollectionParameterBase.json -->

# FCollectionParameterBase

Base struct for collection parameters

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParameterName` | `FName` | The name of the parameter.  Changing this name will break any blueprints that reference the parameter. |
| `Id` | `FGuid` | Uniquely identifies the parameter, used for fixing up materials that reference this parameter when renaming. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCollectionReference.json -->

# FCollectionReference

Reference to an editor collection of assets. This allows an editor-only picker UI

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CollectionName` | `FName` | Name of the collection |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCollectionScalarParameter.json -->

# FCollectionScalarParameter

A scalar parameter

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefaultValue` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCollectionStructParameter.json -->

# FCollectionStructParameter

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MatchRules` | `FString` | - |
| `ScalarParameters` | `TArray < FCollectionScalarParameter >` | - |
| `VectorParameters` | `TArray < FCollectionVectorParameter >` | - |
| `BoolParameters` | `TArray < FCollectionBoolParameter >` | - |
| `IntParameters` | `TArray < FCollectionIntParameter >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCollectionVectorParameter.json -->

# FCollectionVectorParameter

A vector parameter

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefaultValue` | `FLinearColor` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCollisionImpactData.json -->

# FCollisionImpactData

Information about an overall collision, including contacts.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ContactInfos` | `TArray < FRigidBodyContactInfo >` | all the contact points in the collision |
| `TotalNormalImpulse` | `FVector` | the total impulse applied as the two objects push against each other |
| `TotalFrictionImpulse` | `FVector` | the total counterimpulse applied of the two objects sliding against each other |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCollisionProfileName.json -->

# FCollisionProfileName

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Name` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCollisionResponse.json -->

# FCollisionResponse

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ResponseToChannels` | `FCollisionResponseContainer` | Types of objects that this physics objects will collide with. |
| `ResponseArray` | `TArray < FResponseChannel >` | Custom Channels for Responses |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCollisionResponseContainer.json -->

# FCollisionResponseContainer

Container for indicating a set of collision channels that this object will collide with.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `WorldDynamic` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `WorldStatic` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `Pawn` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `Visibility` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `Camera` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `PhysicsBody` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `Vehicle` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `Destructible` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `EngineTraceChannel1` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `EngineTraceChannel2` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `EngineTraceChannel3` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `EngineTraceChannel4` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `EngineTraceChannel5` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `EngineTraceChannel6` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `GameTraceChannel1` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `GameTraceChannel2` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `GameTraceChannel3` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `GameTraceChannel4` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `GameTraceChannel5` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `GameTraceChannel6` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `GameTraceChannel7` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `GameTraceChannel8` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `GameTraceChannel9` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `GameTraceChannel10` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `GameTraceChannel11` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `GameTraceChannel12` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `GameTraceChannel13` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `GameTraceChannel14` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `GameTraceChannel15` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `GameTraceChannel16` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `GameTraceChannel17` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `GameTraceChannel18` | `TEnumAsByte < enum ECollisionResponse >` | - |
| `WorldStatic` | `uint8` | - |
| `WorldDynamic` | `uint8` | - |
| `Pawn` | `uint8` | - |
| `Visibility` | `uint8` | - |
| `Camera` | `uint8` | - |
| `PhysicsBody` | `uint8` | - |
| `Vehicle` | `uint8` | - |
| `Destructible` | `uint8` | - |
| `EngineTraceChannel1` | `uint8` | - |
| `EngineTraceChannel2` | `uint8` | - |
| `EngineTraceChannel3` | `uint8` | - |
| `EngineTraceChannel4` | `uint8` | - |
| `EngineTraceChannel5` | `uint8` | - |
| `EngineTraceChannel6` | `uint8` | - |
| `GameTraceChannel1` | `uint8` | - |
| `GameTraceChannel2` | `uint8` | - |
| `GameTraceChannel3` | `uint8` | - |
| `GameTraceChannel4` | `uint8` | - |
| `GameTraceChannel5` | `uint8` | - |
| `GameTraceChannel6` | `uint8` | - |
| `GameTraceChannel7` | `uint8` | - |
| `GameTraceChannel8` | `uint8` | - |
| `GameTraceChannel9` | `uint8` | - |
| `GameTraceChannel10` | `uint8` | - |
| `GameTraceChannel11` | `uint8` | - |
| `GameTraceChannel12` | `uint8` | - |
| `GameTraceChannel13` | `uint8` | - |
| `GameTraceChannel14` | `uint8` | - |
| `GameTraceChannel15` | `uint8` | - |
| `GameTraceChannel16` | `uint8` | - |
| `GameTraceChannel17` | `uint8` | - |
| `GameTraceChannel18` | `uint8` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCollisionResponseTemplate.json -->

# FCollisionResponseTemplate

Structure for collision response templates.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Name` | `FName` | - |
| `CollisionEnabled` | `TEnumAsByte < ECollisionEnabled :: Type >` | - |
| `ObjectTypeName` | `FName` | - |
| `CustomResponses` | `TArray < FResponseChannel >` | Types of objects that this physics objects will collide with. |
| `HelpMessage` | `FString` | Help message for collision profile |
| `bCanModify` | `bool` | Help message for collision profile |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FColor.json -->

# FColor

A Color (BGRA).
  The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\Color.h

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `B` | `uint8` | - |
| `G` | `uint8` | - |
| `R` | `uint8` | - |
| `A` | `uint8` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FColorGradePerRangeSettings.json -->

# FColorGradePerRangeSettings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Saturation` | `FVector4` | - |
| `Contrast` | `FVector4` | - |
| `Gamma` | `FVector4` | - |
| `Gain` | `FVector4` | - |
| `Offset` | `FVector4` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FColorGradingSettings.json -->

# FColorGradingSettings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Global` | `FColorGradePerRangeSettings` | - |
| `Shadows` | `FColorGradePerRangeSettings` | - |
| `Midtones` | `FColorGradePerRangeSettings` | - |
| `Highlights` | `FColorGradePerRangeSettings` | - |
| `ShadowsMax` | `float` | - |
| `HighlightsMin` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FColorMaterialInput.json -->

# FColorMaterialInput

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UseConstant` | `uint32` | - |
| `Constant` | `FColor` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FColorParameterNameAndCurves.json -->

# FColorParameterNameAndCurves

Structure representing an animated vector parameter and it's associated animation curve.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParameterName` | `FName` | The name of the vector parameter which is being animated. |
| `Index` | `int32` | - |
| `RedCurve` | `FRichCurve` | The curve which contains the animation data for the red component of the color parameter. |
| `GreenCurve` | `FRichCurve` | The curve which contains the animation data for the green component of the color parameter. |
| `BlueCurve` | `FRichCurve` | The curve which contains the animation data for the blue component of the color parameter. |
| `AlphaCurve` | `FRichCurve` | The curve which contains the animation data for the alpha component of the color parameter. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FComboBoxStyle.json -->

# FComboBoxStyle

Represents the appearance of an SComboBox

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ComboButtonStyle` | `FComboButtonStyle` | The style to use for our SComboButton |
| `PressedSlateSound` | `FSlateSound` | The sound the button should play when pressed |
| `SelectionChangeSlateSound` | `FSlateSound` | The Sound to play when the selection is changed |
| `PressedSound_DEPRECATED` | `FName` | - |
| `SelectionChangeSound_DEPRECATED` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FComboButtonStyle.json -->

# FComboButtonStyle

Represents the appearance of an SComboButton

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ButtonStyle` | `FButtonStyle` | The style to use for our SButton |
| `DownArrowImage` | `FSlateBrush` | Image to use for the down arrow |
| `MenuBorderBrush` | `FSlateBrush` | Brush to use to add a "menu border" around the drop-down content |
| `MenuBorderPadding` | `FMargin` | Padding to use to add a "menu border" around the drop-down content |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCompilerNativizationOptions.json -->

# FCompilerNativizationOptions

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PlatformName` | `FName` | - |
| `ServerOnlyPlatform` | `bool` | - |
| `ClientOnlyPlatform` | `bool` | - |
| `ExcludedModules` | `TArray < FName >` | - |
| `ExcludedAssets` | `TSet < FSoftObjectPath >` | - |
| `ExcludedFolderPaths` | `TArray < FString >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FComponentKey.json -->

# FComponentKey

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OwnerClass` | `UClass *` | - |
| `SCSVariableName` | `FName` | - |
| `AssociatedGuid` | `FGuid` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FComponentOverrideRecord.json -->

# FComponentOverrideRecord

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ComponentClass` | `UClass *` | - |
| `ComponentTemplate` | `UActorComponent *` | - |
| `ComponentKey` | `FComponentKey` | - |
| `CookedComponentInstancingData` | `FBlueprintCookedComponentInstancingData` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FComponentReference.json -->

# FComponentReference

Struct that allows for different ways to reference a component.
 	If just an Actor is specified, will return RootComponent of that Actor.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OtherActor` | `AActor *` | Pointer to a different Actor that owns the Component. |
| `ComponentProperty` | `FName` | Name of component property to use |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FComponentSpacePose.json -->

# FComponentSpacePose

A pose in component space (i.e. each transform is relative to the component's transform)

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Transforms` | `TArray < FTransform >` | - |
| `Names` | `TArray < FName >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCompositeFallbackFont.json -->

# FCompositeFallbackFont

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Typeface` | `FTypeface` | Typeface data for this sub-font |
| `ScalingFactor` | `float` | Amount to scale this sub-font so that it better matches the size of the default font |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCompositeFont.json -->

# FCompositeFont

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefaultTypeface` | `FTypeface` | The default typeface that will be used when not overridden by a sub-typeface |
| `SubTypefaces` | `TArray < FCompositeSubFont >` | Sub-typefaces to use for a specific set of characters |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCompositeSection.json -->

# FCompositeSection

Section data for each track. Reference of data will be stored in the child class for the way they want
  AnimComposite vs AnimMontage have different requirement for the actual data reference
  This only contains composite section information. (vertical sequences)

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SectionName` | `FName` | Section Name |
| `StartTime_DEPRECATED` | `float` | Start Time |
| `NextSectionName` | `FName` | Should this animation loop. |
| `MetaData` | `TArray < UAnimMetaData * >` | Meta data that can be saved with the asset<br>	 <br>	  You can query by GetMetaData function |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCompositeSubFont.json -->

# FCompositeSubFont

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CharacterRanges` | `TArray < FInt32Range >` | Array of character ranges for which this sub-font should be used |
| `Cultures` | `FString` | Optional semi-colon separated list of cultures that this sub-font should be used with (if specified, this sub-font will be favored by those cultures and ignored by others) |
| `EditorName` | `FName` | Name of this sub-font. Only used by the editor UI as a convenience to let you state the purpose of the font family. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCompositionGraphCapturePasses.json -->

# FCompositionGraphCapturePasses

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `TArray < FString >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCompressedTrack.json -->

# FCompressedTrack

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ByteStream` | `TArray < uint8 >` | - |
| `Times` | `TArray < float >` | - |
| `Mins` | `float` | - |
| `Ranges` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FConeConstraint.json -->

# FConeConstraint

Cone constraint

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Swing1LimitDegrees` | `float` | Angle of movement along the XY plane. This defines the first symmetric angle of the cone. |
| `Swing2LimitDegrees` | `float` | Angle of movement along the XZ plane. This defines the second symmetric angle of the cone. |
| `Swing1Motion` | `TEnumAsByte < enum EAngularConstraintMotion >` | Indicates whether the Swing1 limit is used. |
| `Swing2Motion` | `TEnumAsByte < enum EAngularConstraintMotion >` | Indicates whether the Swing2 limit is used. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FConfigOverriderSetting.json -->

# FConfigOverriderSetting

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Key` | `FString` | - |
| `Value` | `float` | - |
| `CacheValue` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FConstrainComponentPropName.json -->

# FConstrainComponentPropName

Struct used to specify the property name of the component to constrain

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ComponentName` | `FName` | Name of property |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FConstraint.json -->

# FConstraint

Constraint Set up

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TargetBone` | `FBoneReference` | Target Bone this is constraint to |
| `OffsetOption` | `EConstraintOffsetOption` | Maintain offset based on refpose or not.<br>	  <br>	  None - no offset<br>	  Offset_RefPose - offset is created based on reference pose<br>	  <br>	  In the future, we'd like to support custom offset, not just based on ref pose |
| `TransformType` | `ETransformConstraintType` | What transform type is constraint to - Translation, Rotation, Scale OR Parent. Parent overrides all component |
| `PerAxis` | `FFilterOptionPerAxis` | Per axis filter options - applied in their local space not in world space |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FConstraintBaseParams.json -->

# FConstraintBaseParams

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Stiffness` | `float` | Stiffness of the soft constraint. Only used when Soft Constraint is on. |
| `Damping` | `float` | Damping of the soft constraint. Only used when Soft Constraint is on. |
| `Restitution` | `float` | Controls the amount of bounce when the constraint is violated. A restitution value of 1 will bounce back with the same velocity the limit was hit. A value of 0 will stop dead. |
| `ContactDistance` | `float` | Determines how close to the limit we have to get before turning the joint on. Larger value will be more expensive, but will do a better job not violating constraints. A smaller value will be more efficient, but easier to violate. |
| `bSoftConstraint` | `uint8` | Whether we want to use a soft constraint (spring). |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FConstraintDrive.json -->

# FConstraintDrive

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Stiffness` | `float` | The spring strength of the drive. Force proportional to the position error. |
| `Damping` | `float` | The damping strength of the drive. Force proportional to the velocity error. |
| `MaxForce` | `float` | The force limit of the drive. |
| `bEnablePositionDrive` | `uint8` | EnablesDisables position drive (orientation if using angular drive) |
| `bEnableVelocityDrive` | `uint8` | EnablesDisables velocity drive (angular velocity if using angular drive) |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FConstraintInstance.json -->

# FConstraintInstance

Container for a physics representation of an object.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `JointName` | `FName` | Name of bone that this joint is associated with. |
| `ConstraintBone1` | `FName` | Name of first bone (body) that this constraint is connecting. <br>	 	This will be the 'child' bone in a PhysicsAsset. |
| `ConstraintBone2` | `FName` | Name of second bone (body) that this constraint is connecting. <br>	 	This will be the 'parent' bone in a PhysicsAset. |
| `Pos1` | `FVector` | Location of constraint in Body1 reference frame. |
| `PriAxis1` | `FVector` | Primary (twist) axis in Body1 reference frame. |
| `SecAxis1` | `FVector` | Seconday axis in Body1 reference frame. Orthogonal to PriAxis1. |
| `Pos2` | `FVector` | Location of constraint in Body2 reference frame. |
| `PriAxis2` | `FVector` | Primary (twist) axis in Body2 reference frame. |
| `SecAxis2` | `FVector` | Seconday axis in Body2 reference frame. Orthogonal to PriAxis2. |
| `AngularRotationOffset` | `FRotator` | Specifies the angular offset between the two frames of reference. By default limit goes from (-Angle, +Angle)<br>	 This allows you to bias the limit for swing1 swing2 and twist. |
| `bScaleLinearLimits` | `uint32` | If true, linear limits scale using the absolute min of the 3d scale of the owning component |
| `ProfileInstance` | `FConstraintProfileProperties` | - |
| `bDisableCollision_DEPRECATED` | `uint32` | - |
| `bEnableProjection_DEPRECATED` | `uint32` | - |
| `ProjectionLinearTolerance_DEPRECATED` | `float` | - |
| `ProjectionAngularTolerance_DEPRECATED` | `float` | - |
| `LinearXMotion_DEPRECATED` | `TEnumAsByte < enum ELinearConstraintMotion >` | - |
| `LinearYMotion_DEPRECATED` | `TEnumAsByte < enum ELinearConstraintMotion >` | - |
| `LinearZMotion_DEPRECATED` | `TEnumAsByte < enum ELinearConstraintMotion >` | - |
| `LinearLimitSize_DEPRECATED` | `float` | - |
| `bLinearLimitSoft_DEPRECATED` | `uint32` | - |
| `LinearLimitStiffness_DEPRECATED` | `float` | - |
| `LinearLimitDamping_DEPRECATED` | `float` | - |
| `bLinearBreakable_DEPRECATED` | `uint32` | - |
| `LinearBreakThreshold_DEPRECATED` | `float` | - |
| `AngularSwing1Motion_DEPRECATED` | `TEnumAsByte < enum EAngularConstraintMotion >` | - |
| `AngularTwistMotion_DEPRECATED` | `TEnumAsByte < enum EAngularConstraintMotion >` | - |
| `AngularSwing2Motion_DEPRECATED` | `TEnumAsByte < enum EAngularConstraintMotion >` | - |
| `bSwingLimitSoft_DEPRECATED` | `uint32` | - |
| `bTwistLimitSoft_DEPRECATED` | `uint32` | - |
| `Swing1LimitAngle_DEPRECATED` | `float` | - |
| `TwistLimitAngle_DEPRECATED` | `float` | - |
| `Swing2LimitAngle_DEPRECATED` | `float` | - |
| `SwingLimitStiffness_DEPRECATED` | `float` | - |
| `SwingLimitDamping_DEPRECATED` | `float` | - |
| `TwistLimitStiffness_DEPRECATED` | `float` | - |
| `TwistLimitDamping_DEPRECATED` | `float` | - |
| `bAngularBreakable_DEPRECATED` | `uint32` | - |
| `AngularBreakThreshold_DEPRECATED` | `float` | - |
| `bLinearXPositionDrive_DEPRECATED` | `uint32` | - |
| `bLinearXVelocityDrive_DEPRECATED` | `uint32` | - |
| `bLinearYPositionDrive_DEPRECATED` | `uint32` | - |
| `bLinearYVelocityDrive_DEPRECATED` | `uint32` | - |
| `bLinearZPositionDrive_DEPRECATED` | `uint32` | - |
| `bLinearZVelocityDrive_DEPRECATED` | `uint32` | - |
| `bLinearPositionDrive_DEPRECATED` | `uint32` | - |
| `bLinearVelocityDrive_DEPRECATED` | `uint32` | - |
| `LinearPositionTarget_DEPRECATED` | `FVector` | - |
| `LinearVelocityTarget_DEPRECATED` | `FVector` | - |
| `LinearDriveSpring_DEPRECATED` | `float` | - |
| `LinearDriveDamping_DEPRECATED` | `float` | - |
| `LinearDriveForceLimit_DEPRECATED` | `float` | - |
| `bSwingPositionDrive_DEPRECATED` | `uint32` | - |
| `bSwingVelocityDrive_DEPRECATED` | `uint32` | - |
| `bTwistPositionDrive_DEPRECATED` | `uint32` | - |
| `bTwistVelocityDrive_DEPRECATED` | `uint32` | - |
| `bAngularSlerpDrive_DEPRECATED` | `uint32` | - |
| `bAngularOrientationDrive_DEPRECATED` | `uint32` | - |
| `bEnableSwingDrive_DEPRECATED` | `uint32` | - |
| `bEnableTwistDrive_DEPRECATED` | `uint32` | - |
| `bAngularVelocityDrive_DEPRECATED` | `uint32` | - |
| `AngularPositionTarget_DEPRECATED` | `FQuat` | - |
| `AngularDriveMode_DEPRECATED` | `TEnumAsByte < EAngularDriveMode :: Type >` | - |
| `AngularOrientationTarget_DEPRECATED` | `FRotator` | - |
| `AngularVelocityTarget_DEPRECATED` | `FVector` | - |
| `AngularDriveSpring_DEPRECATED` | `float` | - |
| `AngularDriveDamping_DEPRECATED` | `float` | - |
| `AngularDriveForceLimit_DEPRECATED` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FConstraintProfileProperties.json -->

# FConstraintProfileProperties

Container for properties of a physics constraint that can be easily swapped at runtime. This is useful for switching different setups when going from ragdoll to standup for example

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ProjectionLinearTolerance` | `float` | Linear tolerance value in world units. If the distance error exceeds this tolerence limit, the body will be projected. |
| `ProjectionAngularTolerance` | `float` | Angular tolerance value in world units. If the distance error exceeds this tolerence limit, the body will be projected. |
| `LinearBreakThreshold` | `float` | Force needed to break the distance constraint. |
| `AngularBreakThreshold` | `float` | Torque needed to break the joint. |
| `LinearLimit` | `FLinearConstraint` | - |
| `ConeLimit` | `FConeConstraint` | - |
| `TwistLimit` | `FTwistConstraint` | - |
| `LinearDrive` | `FLinearDriveConstraint` | - |
| `AngularDrive` | `FAngularDriveConstraint` | - |
| `bDisableCollision` | `uint8` | - |
| `bParentDominates` | `uint8` | - |
| `bEnableProjection` | `uint8` | If distance error between bodies exceeds 0.1 units, or rotation error exceeds 10 degrees, body will be projected to fix this.<br>	 For example a chain spinning too fast will have its elements appear detached due to velocity, this will project all bodies so they still appear attached to each other. |
| `bAngularBreakable` | `uint8` | Whether it is possible to break the joint with angular force. |
| `bLinearBreakable` | `uint8` | Whether it is possible to break the joint with linear force. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FConvolutionBloomSettings.json -->

# FConvolutionBloomSettings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Texture` | `UTexture2D *` | Texture to replace default convolution bloom kernel |
| `Size` | `float` | Relative size of the convolution kernel image compared to the minor axis of the viewport |
| `CenterUV` | `FVector2D` | The UV location of the center of the kernel.  Should be very close to (.5,.5) |
| `PreFilterMin` | `float` | Boost intensity of select pixels  prior to computing bloom convolution (Min, Max, Multiplier).  Max < Min disables |
| `PreFilterMax` | `float` | Boost intensity of select pixels  prior to computing bloom convolution (Min, Max, Multiplier).  Max < Min disables |
| `PreFilterMult` | `float` | Boost intensity of select pixels  prior to computing bloom convolution (Min, Max, Multiplier).  Max < Min disables |
| `BufferScale` | `float` | Implicit buffer region as a fraction of the screen size to insure the bloom does not wrap across the screen.  Larger sizes have perf impact. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCrowdAvoidanceConfig.json -->

# FCrowdAvoidanceConfig

Check flags in CrowdDebugDrawing namespace (CrowdManager.cpp) for debugging options.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VelocityBias` | `float` | - |
| `DesiredVelocityWeight` | `float` | - |
| `CurrentVelocityWeight` | `float` | - |
| `SideBiasWeight` | `float` | - |
| `ImpactTimeWeight` | `float` | - |
| `ImpactTimeRange` | `float` | - |
| `CustomPatternIdx` | `uint8` | - |
| `AdaptiveDivisions` | `uint8` | - |
| `AdaptiveRings` | `uint8` | - |
| `AdaptiveDepth` | `uint8` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCrowdAvoidanceSamplingPattern.json -->

# FCrowdAvoidanceSamplingPattern

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Angles` | `TArray < float >` | - |
| `Radii` | `TArray < float >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCullDistanceSizePair.json -->

# FCullDistanceSizePair

Helper structure containing size and cull distance pair.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Size` | `float` | Size to associate with cull distance. |
| `CullDistance` | `float` | Cull distance associated with size. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCurveAtlasColorAdjustments.json -->

# FCurveAtlasColorAdjustments

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bChromaKeyTexture` | `uint32` | - |
| `AdjustBrightness` | `float` | - |
| `AdjustBrightnessCurve` | `float` | - |
| `AdjustVibrance` | `float` | - |
| `AdjustSaturation` | `float` | - |
| `AdjustRGBCurve` | `float` | - |
| `AdjustHue` | `float` | - |
| `AdjustMinAlpha` | `float` | - |
| `AdjustMaxAlpha` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCurveEdEntry.json -->

# FCurveEdEntry

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CurveObject` | `UObject *` | - |
| `CurveColor` | `FColor` | - |
| `CurveName` | `FString` | - |
| `bHideCurve` | `int32` | - |
| `bColorCurve` | `int32` | - |
| `bFloatingPointColorCurve` | `int32` | - |
| `bClamp` | `int32` | - |
| `ClampLow` | `float` | - |
| `ClampHigh` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCurveEdTab.json -->

# FCurveEdTab

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TabName` | `FString` | - |
| `Curves` | `TArray < struct FCurveEdEntry >` | - |
| `ViewStartInput` | `float` | - |
| `ViewEndInput` | `float` | - |
| `ViewStartOutput` | `float` | - |
| `ViewEndOutput` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCurveParams.json -->

# FCurveParams

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `curvefloat` | `UCurveFloat *` | - |
| `curveparam` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCurveTableRowHandle.json -->

# FCurveTableRowHandle

Handle to a particular row in a table.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CurveTable` | `UCurveTable *` | Pointer to table we want a row from |
| `RowName` | `FName` | Name of row in the table that we want |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCurveTrack.json -->

# FCurveTrack

Key frame curve data for one track
  CurveName: Morph Target Name
  CurveWeights: List of weights for each frame

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CurveName` | `FName` | - |
| `CurveWeights` | `TArray < float >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCustomChannelSetup.json -->

# FCustomChannelSetup

Structure for custom channel setup information.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Channel` | `TEnumAsByte < enum ECollisionChannel >` | Which channel you'd like to customize |
| `Name` | `FName` | Name of channel you'd like to show up |
| `DefaultResponse` | `TEnumAsByte < enum ECollisionResponse >` | Default Response for the channel |
| `bTraceType` | `bool` | Sets meta data TraceType="1" for the enum entry if true. Otherwise, this channel will be treated as object query channel, so you can query object types |
| `bStaticObject` | `bool` | Specifies if this is static object. Otherwise it will be dynamic object. This is used for query all objects vs all static objects vs all dynamic objects |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCustomHeightFog.json -->

# FCustomHeightFog

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Height` | `float` | - |
| `DensityCoefficient` | `float` | - |
| `CustomFogInscatteringColor` | `FLinearColor` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCustomInput.json -->

# FCustomInput

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InputName` | `FString` | - |
| `Input` | `FExpressionInput` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCustomizedToolMenu.json -->

# FCustomizedToolMenu

A menu customization is a specialization of menu profiles - that allows for advanced behavior such as modifying the order of sectionsentries
  A menu can only have one customization active at a time

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EntryOrder` | `TMap < FName , FCustomizedToolMenuNameArray >` | - |
| `SectionOrder` | `TArray < FName >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCustomizedToolMenuEntry.json -->

# FCustomizedToolMenuEntry

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Visibility` | `ECustomizedToolMenuVisibility` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCustomizedToolMenuNameArray.json -->

# FCustomizedToolMenuNameArray

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Names` | `TArray < FName >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCustomizedToolMenuSection.json -->

# FCustomizedToolMenuSection

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Visibility` | `ECustomizedToolMenuVisibility` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCustomMontageAnimInfo.json -->

# FCustomMontageAnimInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ApplyAvatarSlot` | `TArray < int32 >` | - |
| `bApplyToSubAnim` | `uint8` | - |
| `DisableBoneResolve` | `TArray < int32 >` | - |
| `bForceUseTPP` | `uint8` | - |
| `bAutoUseSwitch` | `uint8` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCustomOutput.json -->

# FCustomOutput

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OutputName` | `FString` | - |
| `OutputType` | `TEnumAsByte < enum ECustomMaterialOutputType >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCustomParameterValue.json -->

# FCustomParameterValue

项目自定义参数统一容器。
  一个值多街区须通过 Kind 分支。字段参考 FCustomParameterValue-重构方案.md 第 2.1 节。
 
  注意：
  - 该结构不进入 FMaterialInstanceResource，渲染线程完全无感
  - Atlas 的数值是 Index，写回 FScalarParameterValue::ParameterValue
  - Clipmap 的 Texture 值写回 FTextureParameterValue::ParameterValue（UClipmapTexture 继承 UTexture）

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Kind` | `ECustomParameterKind` | - |
| `ExpressionGUID` | `FGuid` | - |
| `bIsUsedAsAtlasPosition` | `bool` | - |
| `AtlasCurve` | `TSoftObjectPtr < UCurveLinearColor >` | - |
| `Atlas` | `TSoftObjectPtr < UCurveLinearColorAtlas >` | - |
| `bIsUsedAsClipmapTexture` | `bool` | - |
| `ClipmapTexture` | `UClipmapTexture *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCustomProfile.json -->

# FCustomProfile

Structure for custom profiles.
 
  if you'd like to just add custom channels, not changing anything else engine defined
  if you'd like to override all about profile, please use 
  +Profiles=(Name=NameOfProfileYouLikeToOverwrite,....)

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Name` | `FName` | - |
| `CustomResponses` | `TArray < FResponseChannel >` | Types of objects that this physics objects will collide with. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FCustomSkeletonName.json -->

# FCustomSkeletonName

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SkeletonNameMap` | `TMap < FName , FName >` | - |
| `SkeletonNotOffsetName` | `TMap < FName , FBoneOffset >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDamageEvent.json -->

# FDamageEvent

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DamageTypeClass` | `TSubclassOf < UDamageType >` | Optional DamageType for this event.  If nullptr, UDamageType will be assumed. |
| `DamageImpulseScale` | `float` | - |
| `DamageSourceObj` | `UObject *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDataDrivenPESkillAttributeItem.json -->

# FDataDrivenPESkillAttributeItem

属性修改项（DataDriven 版本，带 CustomizedSerialize）
  复制自 FPESkillAttributeItem，针对移动端简化：
  - GameAttribute: FGameAttributeContainer → FString（移动端无编辑器下拉选择器）
  - 移除 OptionalModifyItemNameID（移动端不需要）
  - ModifierValueWrapper: FGameMagnitudeWrapper → float（移动端仅使用常量值）
  用于 Mobile 序列化，不影响主干逻辑

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Method` | `FPESkillAttributeModifyMethod` | 修改方式 |
| `GameAttribute` | `FString` | 要修改的属性名 |
| `ModifierOp` | `EAttrOperator` | 属性修改操作类型（非永久修改） |
| `ModifierOp_DoChange` | `EAttrOperator_DoChange` | 属性修改操作类型（永久修改） |
| `ModifierValue` | `float` | 操作数值 |
| `bRepAttrModify` | `bool` | 是否同步客户端 |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDataDrivenPESkillCDWapper.json -->

# FDataDrivenPESkillCDWapper

技能CD信息（DataDriven 版本，带 CustomizedSerialize）
  用于 Mobile 序列化，不影响主干逻辑

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CDType` | `EPESkillCDType` | 技能CD类型 |
| `CDRecoveryTime` | `float` | CD能量充能时间 |
| `AllowRecoveryDuringActivation` | `bool` | 技能激活期间恢复CD能量 |
| `MaxLayer` | `int` | 最大充能次数 |
| `CDEnergyConsume` | `float` | 持续消耗型每秒扣除速率 |
| `AllowConsumeMinEnergy` | `float` | 能开始消耗能量的最小百分比 |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDataDrivenPESkillConsume.json -->

# FDataDrivenPESkillConsume

技能消耗（DataDriven 版本，带 CustomizedSerialize）
  用于 Mobile 序列化，不影响主干逻辑

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ConsumeAttrItems` | `TArray < FDataDrivenPESkillConsumeAttribute >` | 技能消耗数值Array |
| `ConsumeItems` | `TArray < FDataDrivenPESkillConsumeItem >` | 技能消耗物品Array |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDataDrivenPESkillConsumeAttribute.json -->

# FDataDrivenPESkillConsumeAttribute

技能属性消耗（DataDriven 版本，带 CustomizedSerialize）
  用于 Mobile 序列化，不影响主干逻辑

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GameAttribute` | `FString` | 要消耗的属性名 |
| `ConsumeValue` | `float` | 消耗的数值 |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDataDrivenPESkillConsumeItem.json -->

# FDataDrivenPESkillConsumeItem

消耗物品信息（DataDriven 版本，带 CustomizedSerialize）
  用于 Mobile 序列化，不影响主干逻辑

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ItemID` | `int32` | 消耗物品ID |
| `ItemNum` | `int32` | 消耗物品数量 |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDataTableCategoryHandle.json -->

# FDataTableCategoryHandle

Handle to a particular row in a table

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DataTable` | `UDataTable *` | Pointer to table we want a row from |
| `ColumnName` | `FName` | Name of column in the table that we want |
| `RowContents` | `FName` | Contents of rows in the table that we want |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDataTableRowHandle.json -->

# FDataTableRowHandle

Handle to a particular row in a table

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DataTable` | `UDataTable *` | Pointer to table we want a row from |
| `RowName` | `FName` | Name of row in the table that we want |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDebugDisplayProperty.json -->

# FDebugDisplayProperty

Debug property display functionality to interact with this, use "display", "displayall", "displayclear"
 
  @see UGameViewportClient
  @see FDebugDisplayProperty
  @see DrawStatsHUD

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Obj` | `UObject *` | the object whose property to display. If this is a class, all objects of that class are drawn. |
| `WithinClass` | `TSubclassOf < UObject >` | if Obj is a class and WithinClass is not nullptr, further limit the display to objects that have an Outer of WithinClass |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDebugFloatHistory.json -->

# FDebugFloatHistory

Structure for recording float values and displaying them as an Histogram through DrawDebugFloatHistory.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Samples` | `TArray < float >` | Samples |
| `MaxSamples` | `float` | Max Samples to record. |
| `MinValue` | `float` | Min value to record. |
| `MaxValue` | `float` | Max value to record. |
| `bAutoAdjustMinMax` | `bool` | Auto adjust MinMax as new values are recorded? |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDebugTextInfo.json -->

# FDebugTextInfo

Single entry of a debug text item to render. 
 
  @see AHud
  @see AddDebugText(), RemoveDebugText() and DrawDebugTextList()

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SrcActor` | `AActor *` | AActor related to text item |
| `SrcActorOffset` | `FVector` | Offset from SrcActor.Location to apply |
| `SrcActorDesiredOffset` | `FVector` | Desired offset to interpolate to |
| `DebugText` | `FString` | Text to display |
| `TimeRemaining` | `float` | Time remaining for the debug text, -1.f == infinite |
| `Duration` | `float` | Duration used to lerp desired offset |
| `TextColor` | `FColor` | Text color |
| `bAbsoluteLocation` | `uint32` | whether the offset should be treated as absolute world location of the string |
| `bKeepAttachedToActor` | `uint32` | If the actor moves does the text also move with it? |
| `bDrawShadow` | `uint32` | Whether to draw a shadow for the text |
| `OrigActorLocation` | `FVector` | When we first spawn store off the original actor location for use with bKeepAttachedToActor |
| `Font` | `UFont *` | The Font which to display this as.  Will Default to GetSmallFont() |
| `FontScale` | `float` | Scale to apply to font when rendering |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDecalBakingRequest.json -->

# FDecalBakingRequest

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Mesh` | `UObject *` | - |
| `DecalParams` | `TArray < FDecalParameter >` | - |
| `RenderTarget` | `UTextureRenderTarget2D *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDecalParameter.json -->

# FDecalParameter

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DecalTexture` | `UTexture2D *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDelayInitAnimTickParam.json -->

# FDelayInitAnimTickParam

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DeltaTime` | `float` | - |
| `bNeedsValidRootMotion` | `bool` | - |
| `bUpdateProx` | `bool` | - |
| `bForceUpdateProx` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDelegateArray.json -->

# FDelegateArray

Helper struct, since UnrealScript doesn't allow arrays of arrays, but
  arrays of structs of arrays are okay.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Delegates` | `TArray < FPlatformInterfaceDelegate >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDelegateRuntimeBinding.json -->

# FDelegateRuntimeBinding

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ObjectName` | `FString` | The widget that will be bound to the live data. |
| `PropertyName` | `FName` | The property on the widget that will have a binding placed on it. |
| `FunctionName` | `FName` | The function or property we're binding to on the source object. |
| `SourcePath` | `FDynamicPropertyPath` | - |
| `Kind` | `EBindingKind` | The kind of binding we're performing, are we binding to a property or a function. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDepthFieldGlowInfo.json -->

# FDepthFieldGlowInfo

info for glow when using depth field rendering

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bEnableGlow` | `uint32` | whether to turn on the outline glow (depth field fonts only) |
| `GlowColor` | `FLinearColor` | base color to use for the glow |
| `GlowOuterRadius` | `FVector2D` | if bEnableGlow, outline glow outer radius (0 to 1, 0.5 is edge of character silhouette)<br>	  glow influence will be 0 at GlowOuterRadius.X and 1 at GlowOuterRadius.Y |
| `GlowInnerRadius` | `FVector2D` | if bEnableGlow, outline glow inner radius (0 to 1, 0.5 is edge of character silhouette)<br>	  glow influence will be 1 at GlowInnerRadius.X and 0 at GlowInnerRadius.Y |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDialogueContext.json -->

# FDialogueContext

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Speaker` | `UDialogueVoice *` | The person speaking the dialogue. |
| `Targets` | `TArray < UDialogueVoice * >` | The people being spoken to. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDialogueContextMapping.json -->

# FDialogueContextMapping

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Context` | `FDialogueContext` | The context of the dialogue. |
| `SoundWave` | `USoundWave *` | The soundwave to play for this dialogue. |
| `LocalizationKeyFormat` | `FString` | - |
| `Proxy` | `UDialogueSoundWaveProxy *` | Cached object for playing the soundwave with subtitle information included. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDialogueWaveParameter.json -->

# FDialogueWaveParameter

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DialogueWave` | `UDialogueWave *` | The dialogue wave to play. |
| `Context` | `FDialogueContext` | The context to use for the dialogue wave. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDirectorTrackCut.json -->

# FDirectorTrackCut

A track type used for binding the view of a Player (attached to this tracks group) to the actor of a different group.
 
 
 Information for one cut in this track.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Time` | `float` | Time to perform the cut. |
| `TransitionTime` | `float` | Time taken to move view to new camera. |
| `TargetCamGroup` | `FName` | GroupName of UInterpGroup to cut viewpoint to. |
| `ShotNumber` | `int32` | Shot number for developer reference |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDirectoryPath.json -->

# FDirectoryPath

Structure for directory paths that are displayed in the UI.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Path` | `FString` | The path to the directory. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDistanceDatum.json -->

# FDistanceDatum

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FadeInDistanceStart` | `float` | The FadeInDistance at which to start hearing this sound.<br>	  If you want to hear the sound up close then setting this to 0 might be a good option. |
| `FadeInDistanceEnd` | `float` | The distance at which this sound has faded in completely. |
| `FadeOutDistanceStart` | `float` | The distance at which this sound starts fading out. |
| `FadeOutDistanceEnd` | `float` | The distance at which this sound is no longer audible. |
| `Volume` | `float` | The volume for which this Input should be played. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDistributionLookupTable.json -->

# FDistributionLookupTable

Lookup table for distributions.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Op` | `uint8` | - |
| `EntryCount` | `uint8` | - |
| `EntryStride` | `uint8` | - |
| `SubEntryStride` | `uint8` | - |
| `TimeScale` | `float` | - |
| `TimeBias` | `float` | - |
| `Values` | `TArray < float >` | - |
| `LockFlag` | `uint8` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDockTabStyle.json -->

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


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDPProfileMatch.json -->

# FDPProfileMatch

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Profile` | `FString` | - |
| `Match` | `TArray < FDPProfileMatchItem >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDPProfileMatchItem.json -->

# FDPProfileMatchItem

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceType` | `TEnumAsByte < EDPSourceType >` | - |
| `CompareType` | `TEnumAsByte < EDPCompareType >` | - |
| `MatchString` | `FString` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDrawToRenderTargetContext.json -->

# FDrawToRenderTargetContext

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RenderTarget` | `UTextureRenderTarget2D *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDropNoteInfo.json -->

# FDropNoteInfo

Info about one note dropped in the map during PIE.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Location` | `FVector` | Location to create Note actor in edited level. |
| `Rotation` | `FRotator` | Rotation to create Note actor in edited level. |
| `Comment` | `FString` | Text to assign to Note actor in edited level. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDynamicBatchSectionInfo.json -->

# FDynamicBatchSectionInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TransientMatInfo` | `TArray < FMaterialBatchInfo >` | - |
| `BatchMatList` | `TArray < UMaterialInterface * >` | - |
| `CacheAtlasMaterials` | `TMap < int32 , UMaterialInstanceDynamic * >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDynamicGenerateTargetNavigation.json -->

# FDynamicGenerateTargetNavigation

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TargetLocation` | `FVector` | - |
| `GenerateRadiusMin` | `float` | - |
| `GenerateRadiusMax` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDynamicPropertyPath.json -->

# FDynamicPropertyPath

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Segments` | `TArray < FPropertyPathSegment >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FDynamicTextureInstance.json -->

# FDynamicTextureInstance

Serialized ULevel information about dynamic texture instances

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Texture` | `UTexture2D *` | Texture that is used by a dynamic UPrimitiveComponent. |
| `bAttached` | `bool` | Whether the primitive that uses this texture is attached to the scene or not. |
| `OriginalRadius` | `float` | Original bounding sphere radius, at the time the TexelFactor was calculated originally. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FEdGraphPinReference.json -->

# FEdGraphPinReference

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OwningNode` | `TWeakObjectPtr < UEdGraphNode >` | The node that owns the pin referred to by this struct. Updated at Set and Save time. |
| `PinId` | `FGuid` | The pin's unique ID. Updated at Set and Save time. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FEdGraphPinType.json -->

# FEdGraphPinType

Struct used to define the type of information carried on this pin

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PinCategory` | `FString` | Category of pin type |
| `PinSubCategory` | `FString` | Sub-category of pin type |
| `PinSubCategoryObject` | `TWeakObjectPtr < UObject >` | Sub-category object |
| `PinSubCategoryMemberReference` | `FSimpleMemberReference` | Sub-category member reference |
| `PinValueType` | `FEdGraphTerminalType` | Data used to determine value types when bIsMap is true |
| `ContainerType` | `EPinContainerType` | - |
| `bIsArray_DEPRECATED` | `uint8` | DEPRECATED(4.17) Whether or not this pin represents an array of values |
| `bIsReference` | `uint8` | Whether or not this pin is a value passed by reference or not |
| `bIsConst` | `uint8` | Whether or not this pin is a immutable const value |
| `bIsWeakPointer` | `uint8` | Whether or not this is a weak reference |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FEdGraphSchemaAction.json -->

# FEdGraphSchemaAction

This structure represents a context dependent action, with sufficient information for the schema to perform it.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MenuDescription` | `FText` | The menu text that should be displayed for this node in the creation menu. |
| `TooltipDescription` | `FText` | The tooltip text that should be displayed for this node in the creation menu. |
| `Category` | `FText` | This is the UI centric category the action fits in (e.g., Functions, Variables). Use this instead of the NodeType.NodeCategory because multiple NodeCategories might visually belong together. |
| `Keywords` | `FText` | This is just an arbitrary dump of extra text that search will match on, in addition to the description and tooltip, e.g., Add might have the keyword Math. |
| `Grouping` | `int32` | This is a priority number for overriding alphabetical order in the action list (higher value  == higher in the list). |
| `SectionID` | `int32` | Section ID of the action list in which this action belongs. |
| `MenuDescriptionArray` | `TArray < FString >` | - |
| `FullSearchTitlesArray` | `TArray < FString >` | - |
| `FullSearchKeywordsArray` | `TArray < FString >` | - |
| `FullSearchCategoryArray` | `TArray < FString >` | - |
| `LocalizedMenuDescriptionArray` | `TArray < FString >` | - |
| `LocalizedFullSearchTitlesArray` | `TArray < FString >` | - |
| `LocalizedFullSearchKeywordsArray` | `TArray < FString >` | - |
| `LocalizedFullSearchCategoryArray` | `TArray < FString >` | - |
| `SearchText` | `FString` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FEdGraphSchemaAction_NewNode.json -->

# FEdGraphSchemaAction_NewNode

Action to add a node to the graph

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NodeTemplate` | `UEdGraphNode *` | Template of node we want to create |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FEdGraphTerminalType.json -->

# FEdGraphTerminalType

Struct used to define information for terminal types, e.g. types that can be contained
   by a container. Currently can represent strongweak references to a type (only UObjects), 
   a structure, or a primitive. Support for "Container of Containers" is done by wrapping 
   a structure, rather than implicitly defining names for containers.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TerminalCategory` | `FString` | Category |
| `TerminalSubCategory` | `FString` | Sub-category |
| `TerminalSubCategoryObject` | `TWeakObjectPtr < UObject >` | Sub-category object |
| `bTerminalIsConst` | `bool` | Whether or not this pin is a immutable const value |
| `bTerminalIsWeakPointer` | `bool` | Whether or not this is a weak reference |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FEditableTextBoxStyle.json -->

# FEditableTextBoxStyle

Represents the appearance of an SEditableTextBox

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BackgroundImageNormal` | `FSlateBrush` | Border background image when the box is not hovered or focused |
| `BackgroundImageHovered` | `FSlateBrush` | Border background image when the box is hovered |
| `BackgroundImageFocused` | `FSlateBrush` | Border background image when the box is focused |
| `BackgroundImageReadOnly` | `FSlateBrush` | Border background image when the box is read-only |
| `Padding` | `FMargin` | Padding |
| `Font` | `FSlateFontInfo` | Font family and size to be used when displaying this text. |
| `ForegroundColor` | `FSlateColor` | The foreground color of text. |
| `BackgroundColor` | `FSlateColor` | The background color applied to the active background image |
| `ReadOnlyForegroundColor` | `FSlateColor` | The read-only foreground color of text in read-only mode. |
| `HScrollBarPadding` | `FMargin` | Padding around the horizontal scrollbar |
| `VScrollBarPadding` | `FMargin` | Padding around the vertical scrollbar |
| `ScrollBarStyle` | `FScrollBarStyle` | Style used for the scrollbars |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FEditableTextStyle.json -->

# FEditableTextStyle

Represents the appearance of an SEditableText

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Font` | `FSlateFontInfo` | Font family and size to be used when displaying this text. |
| `ColorAndOpacity` | `FSlateColor` | The color and opacity of this text |
| `BackgroundImageSelected` | `FSlateBrush` | Background image for the selected text |
| `BackgroundImageComposing` | `FSlateBrush` | Background image for the selected text |
| `CaretImage` | `FSlateBrush` | Image brush used for the caret |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FEditedDocumentInfo.json -->

# FEditedDocumentInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EditedObject` | `UObject *` | - |
| `SavedViewOffset` | `FVector2D` | Saved view position |
| `SavedZoomAmount` | `float` | Saved zoom amount |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FEditorElement.json -->

# FEditorElement

Each elements in the grid

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Indices` | `int32` | - |
| `Weights` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FEditorImportExportTestDefinition.json -->

# FEditorImportExportTestDefinition

Holds settings for the asset import  export automation test

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ImportFilePath` | `FFilePath` | The file to import <br>	UPROPERTY(config, EditAnywhere, Category = Automation, meta = (FilePathFilter = "")) |
| `ExportFileExtension` | `FString` | The file extension to use when exporting |
| `bSkipExport` | `bool` | If true, the export step will be skipped |
| `FactorySettings` | `TArray < FImportFactorySettingValues >` | Settings for the import factory |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FEditorImportWorkflowDefinition.json -->

# FEditorImportWorkflowDefinition

Holds settings for the asset import workflow test

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ImportFilePath` | `FFilePath` | The file to import <br>	UPROPERTY(config, EditAnywhere, Category = Automation, meta = (FilePathFilter = "")) |
| `FactorySettings` | `TArray < FImportFactorySettingValues >` | Settings for the import factory |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FEditorMapPerformanceTestDefinition.json -->

# FEditorMapPerformanceTestDefinition

Holds settings for the asset import  export automation test

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PerformanceTestmap` | `FSoftObjectPath` | Map to be used for the Performance Capture |
| `TestTimer` | `int32` | How long is this test expected to run before stopping |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FElementID.json -->

# FElementID

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `IDValue` | `int32` | The actual mesh element index this ID represents.  Read-only. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FEmitterDynamicParameter.json -->

# FEmitterDynamicParameter

Helper structure for displaying the parameter.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParamName` | `FName` | The parameter name - from the material DynamicParameter expression. READ-ONLY |
| `bUseEmitterTime` | `uint32` | If true, use the EmitterTime to retrieve the value, otherwise use Particle RelativeTime. |
| `bSpawnTimeOnly` | `uint32` | If true, only set the value at spawn time of the particle, otherwise update each frame. |
| `ValueMethod` | `TEnumAsByte < enum EEmitterDynamicParameterValue >` | Where to get the parameter value from. |
| `bScaleVelocityByParamValue` | `uint32` | If true, scale the velocity value selected in ValueMethod by the evaluated ParamValue. |
| `ParamValue` | `FRawDistributionFloat` | The distriubtion for the parameter value. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FEmoteBoneAdaptConfig.json -->

# FEmoteBoneAdaptConfig

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EmoteBoneToAdapt` | `FBoneReference` | - |
| `EmoteBoneToAdaptOffset` | `FTransform` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FEngineShowFlagsSetting.json -->

# FEngineShowFlagsSetting

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ShowFlagName` | `FString` | - |
| `Enabled` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FEnvQueryInstanceCache.json -->

# FEnvQueryInstanceCache

cache of instances with sorted tests

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Template` | `UEnvQuery *` | query template, duplicated in manager's world |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FEnvQueryRequest.json -->

# FEnvQueryRequest

wrapper for easy query execution

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `QueryTemplate` | `UEnvQuery *` | query to run |
| `Owner` | `UObject *` | querier |
| `World` | `UWorld *` | world |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FEquipableSlotInfoV2.json -->

# FEquipableSlotInfoV2

可装备槽位信息
  描述一个物品可以装备到的目标位置

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParentItem` | `FItemDefineID` | 父物品DefineID<br>	  如果是装备到背包槽位上，则为无效物品（FItemDefineID()）<br>	  如果是作为配件装备到某个物品上，则为该物品的DefineID |
| `SlotName` | `FName` | 目标槽位名称 |
| `OccupiedItem` | `FItemDefineID` | 当前占据该槽位的物品（如果有）<br>	  无效则表示槽位为空 |
| `bIsOccupied` | `bool` | 该槽位是否已被占据 |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FEscRespondSetting.json -->

# FEscRespondSetting

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bIsRespondEsc` | `bool` | - |
| `HandlerFunctionName` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FEventPayload.json -->

# FEventPayload

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EventName` | `FName` | The name of the event to trigger |
| `Parameters` | `FMovieSceneEventParameters` | The event parameters |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FEventTrackKey.json -->

# FEventTrackKey

A track containing discrete events that are triggered as its played back. 
 	Events correspond to Outputs of the SeqAct_Interp in Kismet.
 	There is no PreviewUpdateTrack function for this type - events are not triggered in editor.
 
 Information for one event in the track.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Time` | `float` | - |
| `EventName` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FExpandableAreaStyle.json -->

# FExpandableAreaStyle

Represents the appearance of an SExpandableArea

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CollapsedImage` | `FSlateBrush` | Image to use when the area is collapsed |
| `ExpandedImage` | `FSlateBrush` | Image to use when the area is expanded |
| `RolloutAnimationSeconds` | `float` | How long the rollout animation lasts |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FExpectedQuality.json -->

# FExpectedQuality

hold all Quality setting that affect loading or other process

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CompareOp` | `EEQCompareOp` | - |
| `ExpectedRenderQuality` | `ERenderQualityEngine` | - |
| `ExpectedDeviceQuality` | `uint8` | - |
| `ExpectedMemory` | `uint8` | - |
| `bUseRenderQualityControl` | `uint8` | - |
| `bUseDeviceQualityControl` | `uint8` | - |
| `bUseMemoryControl` | `uint8` | - |
| `bRequireAllConditionMeet` | `uint8` | - |
| `PCExpectedRenderQuality` | `ERenderQualityEngine_PC` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FExposedValueCopyRecord.json -->

# FExposedValueCopyRecord

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceProperty_DEPRECATED` | `UProperty *` | - |
| `SourcePropertyName` | `FName` | - |
| `SourceSubPropertyName` | `FName` | - |
| `SourceArrayIndex` | `int32` | - |
| `DestProperty` | `UProperty *` | - |
| `DestArrayIndex` | `int32` | - |
| `Size` | `int32` | - |
| `bInstanceIsTarget` | `bool` | - |
| `bFastPathExtend` | `bool` | - |
| `PostCopyOperation` | `EPostCopyOperation` | - |
| `CopyType` | `ECopyType` | - |
| `CachedSourceProperty` | `UProperty *` | - |
| `SourceSubStructPropertyNameArray` | `TArray < FName >` | - |
| `CachedSourceStructSubPropertyArray` | `TArray < UProperty * >` | - |
| `CachedFastObj` | `UObject *` | - |
| `RootExposedNodeJsonStr` | `FString` | - |
| `RootExposedNodeStackData` | `TArray < uint8 >` | - |
| `bExposedOperationValid` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FExposedValueHandler.json -->

# FExposedValueHandler

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoundFunction` | `FName` | - |
| `CopyRecords` | `TArray < FExposedValueCopyRecord >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FExposureSettings.json -->

# FExposureSettings

Settings to allow designers to override the automatic expose

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LogOffset` | `int32` | - |
| `bFixed` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FExpressionInput.json -->

# FExpressionInput

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OutputIndex` | `int32` | Index into Expression's outputs array that this input is connected to. |
| `InputName` | `FString` | optional FName of the input.  <br>	  Note that this is the only member which is not derived from the output currently connected. |
| `Mask` | `int32` | - |
| `MaskR` | `int32` | - |
| `MaskG` | `int32` | - |
| `MaskB` | `int32` | - |
| `MaskA` | `int32` | - |
| `ExpressionName` | `FName` | Material expression name that this input is connected to, or None if not connected. Used only in cooked builds |
| `Expression` | `UMaterialExpression *` | UMaterial expression that this input is connected to, or NULL if not connected. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FExpressionOutput.json -->

# FExpressionOutput

Struct that represents an expression's output.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OutputName` | `FString` | - |
| `Mask` | `int32` | - |
| `MaskR` | `int32` | - |
| `MaskG` | `int32` | - |
| `MaskB` | `int32` | - |
| `MaskA` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FExternalToolDefinition.json -->

# FExternalToolDefinition

Structure for defining an external tool

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ToolName` | `FString` | The name of the tool  test. |
| `ExecutablePath` | `FFilePath` | The executable to run. <br>	UPROPERTY(config, EditAnywhere, Category=ExternalTools, meta=(FilePathFilter = "")) |
| `CommandLineOptions` | `FString` | The command line options to pass to the executable. |
| `WorkingDirectory` | `FDirectoryPath` | The working directory for the new process. |
| `ScriptExtension` | `FString` | If set, look for scripts with this extension. |
| `ScriptDirectory` | `FDirectoryPath` | If the ScriptExtension is set, look here for the script files. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FExtraPVSInfo.json -->

# FExtraPVSInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ExtraVisibleZone` | `TArray < FBox >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFarLandInfo.json -->

# FFarLandInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FarLandDiffuseTexture` | `UTexture2D *` | - |
| `FarLandNormalTexture` | `UTexture2D *` | - |
| `IndexX` | `int32` | - |
| `IndexY` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFastArraySerializerItem.json -->

# FFastArraySerializerItem

Base struct for items using Fast TArray Replication

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ReplicationID` | `int32` | Engine Modify End |
| `ReplicationKey` | `int32` | - |
| `MostRecentArrayReplicationKey` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFastRepRemoteContent.json -->

# FFastRepRemoteContent

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ContentBlockCount` | `uint16` | - |
| `ContentNumBytes` | `uint16` | - |
| `Content` | `TArray < uint8 >` | - |
| `ObjPtrs` | `TArray < UObject * >` | - |
| `DebugInfo` | `FString` | - |
| `DSFrameCounter` | `uint16` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFilePath.json -->

# FFilePath

Structure for file paths that are displayed in the UI.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FilePath` | `FString` | The path to the file. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFilmStockSettings.json -->

# FFilmStockSettings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Slope` | `float` | - |
| `Toe` | `float` | - |
| `Shoulder` | `float` | - |
| `BlackClip` | `float` | - |
| `WhiteClip` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFindFloorResult.json -->

# FFindFloorResult

Data about the floor for walking movement, used by CharacterMovementComponent.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bBlockingHit` | `uint32` | True if there was a blocking hit in the floor test that was NOT in initial penetration.<br>	 The HitResult can give more info about other circumstances. |
| `bWalkableFloor` | `uint32` | True if the hit found a valid walkable floor. |
| `bLineTrace` | `uint32` | True if the hit found a valid walkable floor using a line trace (rather than a sweep test, which happens when the sweep test fails to yield a walkable surface). |
| `FloorDist` | `float` | The distance to the floor, computed from the swept capsule trace. |
| `LineDist` | `float` | The distance to the floor, computed from the trace. Only valid if bLineTrace is true. |
| `HitResult` | `FHitResult` | Hit result of the test that found a floor. Includes more specific data about the point of impact and surface normal at that point. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFixedDPIValueEntry.json -->

# FFixedDPIValueEntry

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EntryValues` | `TMap < int32 , FFixedDPIValueMap >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFixedDPIValueMap.json -->

# FFixedDPIValueMap

通过分辨率XY查询固定缩放值

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ScaleValues` | `TMap < int32 , float >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFloatDistribution.json -->

# FFloatDistribution

Type-safe floating point distribution.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Table` | `FDistributionLookupTable` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFloatInterval.json -->

# FFloatInterval

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Min` | `float` | - |
| `Max` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFloatRange.json -->

# FFloatRange

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LowerBound` | `FFloatRangeBound` | - |
| `UpperBound` | `FFloatRangeBound` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFloatRangeBound.json -->

# FFloatRangeBound

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Type` | `TEnumAsByte < ERangeBoundTypes :: Type >` | - |
| `Value` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFloatRK4SpringInterpolator.json -->

# FFloatRK4SpringInterpolator

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StiffnessConstant` | `float` | - |
| `DampeningRatio` | `float` | 0 = Undamped, <1 = Underdamped, 1 = Critically damped, >1 = Over damped |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFoliageTypeLocation.json -->

# FFoliageTypeLocation

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FoliageTypeInfos` | `TMap < FName , FLevelBlockFoliageInfo >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFoliageTypeObject.json -->

# FFoliageTypeObject

A wrapper struct used to allow the use of either FoliageType assets or FoliageType blueprint classes

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FoliageTypeObject` | `UObject *` | The foliage type that will be spawned by the procedural foliage simulation |
| `TypeInstance` | `UFoliageType *` | The actual instance of the foliage type that is used for spawning |
| `bIsAsset` | `bool` | Whether this contains an asset object (as opposed to a BP class) |
| `Type_DEPRECATED` | `TSubclassOf < UFoliageType_InstancedStaticMesh >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFoliageVertexColorChannelMask.json -->

# FFoliageVertexColorChannelMask

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UseMask` | `uint32` | When checked, foliage will be masked from this mesh using this color channel |
| `MaskThreshold` | `float` | Specifies the threshold value above which the static mesh vertex color value must be, in order for foliage instances to be placed in a specific area |
| `InvertMask` | `uint32` | When unchecked, foliage instances will be placed only when the vertex color in the specified channel(s) is above the threshold amount.<br>	   When checked, the vertex color must be less than the threshold amount |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFontCharacter.json -->

# FFontCharacter

This struct is serialized using native serialization so any changes to it require a package version bump.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StartU` | `int32` | - |
| `StartV` | `int32` | - |
| `USize` | `int32` | - |
| `VSize` | `int32` | - |
| `TextureIndex` | `uint8` | - |
| `VerticalOffset` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFontData.json -->

# FFontData

Payload data describing an individual font in a typeface. Keep this lean as it's also used as a key!

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FontFilename` | `FString` | The filename of the font to use.<br>	  This variable is ignored if we have a font face asset, and is set to the .ufont file in a cooked build. |
| `Hinting` | `EFontHinting` | The hinting algorithm to use with the font.<br>	  This variable is ignored if we have a font face asset, and is synchronized with the font face asset on load in a cooked build. |
| `LoadingPolicy` | `EFontLoadingPolicy` | Enum controlling how this font should be loaded at runtime. See the enum for more explanations of the options.<br>	  This variable is ignored if we have a font face asset, and is synchronized with the font face asset on load in a cooked build. |
| `FontFaceAsset` | `UObject *` | Font data v3. This points to a font face asset. |
| `BulkDataPtr_DEPRECATED` | `UFontBulkData *` | Legacy font data v2. This used to be where font data was stored prior to font face assets. <br>	  This can be removed once we no longer support loading packages older than FEditorObjectVersion::AddedFontFaceAssets (as can UFontBulkData itself). |
| `FontData_DEPRECATED` | `TArray < uint8 >` | Legacy font data v1. This used to be where font data was stored prior to font bulk data.<br>	  This can be removed once we no longer support loading packages older than VER_UE4_SLATE_BULK_FONT_DATA. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFontImportOptionsData.json -->

# FFontImportOptionsData

Font import options

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FontName` | `FString` | Name of the typeface for the font to import |
| `Height` | `float` | Height of font (point size) |
| `bEnableAntialiasing` | `uint32` | Whether the font should be antialiased or not.  Usually you should leave this enabled. |
| `bEnableBold` | `uint32` | Whether the font should be generated in bold or not |
| `bEnableItalic` | `uint32` | Whether the font should be generated in italics or not |
| `bEnableUnderline` | `uint32` | Whether the font should be generated with an underline or not |
| `bAlphaOnly` | `uint32` | if true then forces PF_G8 and only maintains Alpha value and discards color |
| `CharacterSet` | `TEnumAsByte < enum EFontImportCharacterSet >` | Character set for this font |
| `Chars` | `FString` | Explicit list of characters to include in the font |
| `UnicodeRange` | `FString` | Range of Unicode character values to include in the font.  You can specify ranges using hyphens andor commas (e.g. '400-900') |
| `CharsFilePath` | `FString` | Path on disk to a folder where files that contain a list of characters to include in the font |
| `CharsFileWildcard` | `FString` | File mask wildcard that specifies which files within the CharsFilePath to scan for characters in include in the font |
| `bCreatePrintableOnly` | `uint32` | Skips generation of glyphs for any characters that are not considered 'printable' |
| `bIncludeASCIIRange` | `uint32` | When specifying a range of characters and this is enabled, forces ASCII characters (0 thru 255) to be included as well |
| `ForegroundColor` | `FLinearColor` | Color of the foreground font pixels.  Usually you should leave this white and instead use the UI Styles editor to change the color of the font on the fly |
| `bEnableDropShadow` | `uint32` | Enables a very simple, 1-pixel, black colored drop shadow for the generated font |
| `TexturePageWidth` | `int32` | Horizontal size of each texture page for this font in pixels |
| `TexturePageMaxHeight` | `int32` | The maximum vertical size of a texture page for this font in pixels.  The actual height of a texture page may be less than this if the font can fit within a smaller sized texture page. |
| `XPadding` | `int32` | Horizontal padding between each font character on the texture page in pixels |
| `YPadding` | `int32` | Vertical padding between each font character on the texture page in pixels |
| `ExtendBoxTop` | `int32` | How much to extend the top of the UV coordinate rectangle for each character in pixels |
| `ExtendBoxBottom` | `int32` | How much to extend the bottom of the UV coordinate rectangle for each character in pixels |
| `ExtendBoxRight` | `int32` | How much to extend the right of the UV coordinate rectangle for each character in pixels |
| `ExtendBoxLeft` | `int32` | How much to extend the left of the UV coordinate rectangle for each character in pixels |
| `bEnableLegacyMode` | `uint32` | Enables legacy font import mode.  This results in lower quality antialiasing and larger glyph bounds, but may be useful when debugging problems |
| `Kerning` | `int32` | The initial horizontal spacing adjustment between rendered characters.  This setting will be copied directly into the generated Font object's properties. |
| `bUseDistanceFieldAlpha` | `uint32` | If true then the alpha channel of the font textures will store a distance field instead of a color mask |
| `DistanceFieldScaleFactor` | `int32` | Scale factor determines how big to scale the font bitmap during import when generating distance field values <br>	 Note that higher values give better quality but importing will take much longer. |
| `DistanceFieldScanRadiusScale` | `float` | Shrinks or expands the scan radius used to determine the silhouette of the font edges. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFontOutlineSettings.json -->

# FFontOutlineSettings

Settings for applying an outline to a font

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OutlineSize` | `int32` | Size of the outline in slate units (at 1.0 font scale this unit is a pixel) |
| `OutlineMaterial` | `UObject *` | Optional material to apply to the outline |
| `OutlineColor` | `FLinearColor` | The color of the outline for any character in this font |
| `bSeparateFillAlpha` | `bool` | If checked, the outline will be completely translucent where the filled area will be.  This allows for a separate fill alpha value<br>	  The trade off when enabling this is slightly worse quality for completely opaque fills where the inner outline border meets the fill area |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFontParameterValue.json -->

# FFontParameterValue

Editable font parameter.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `FontValue` | `UFont *` | - |
| `FontPage` | `int32` | - |
| `ExpressionGUID` | `FGuid` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFontRenderInfo.json -->

# FFontRenderInfo

information used in font rendering

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bClipText` | `uint32` | whether to clip text |
| `bEnableShadow` | `uint32` | whether to turn on shadowing |
| `GlowInfo` | `FDepthFieldGlowInfo` | depth field glow parameters (only usable if font was imported with a depth field) |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FForceFeedbackChannelDetails.json -->

# FForceFeedbackChannelDetails

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bAffectsLeftLarge` | `uint32` | - |
| `bAffectsLeftSmall` | `uint32` | - |
| `bAffectsRightLarge` | `uint32` | - |
| `bAffectsRightSmall` | `uint32` | - |
| `Curve` | `FRuntimeFloatCurve` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FForeignControlPointData.json -->

# FForeignControlPointData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ModificationKey` | `FGuid` | - |
| `MeshComponent` | `UControlPointMeshComponent *` | - |
| `Identifier` | `TLazyObjectPtr < ULandscapeSplineControlPoint >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FForeignSplineSegmentData.json -->

# FForeignSplineSegmentData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ModificationKey` | `FGuid` | - |
| `MeshComponents` | `TArray < USplineMeshComponent * >` | - |
| `Identifier` | `TLazyObjectPtr < ULandscapeSplineSegment >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FForeignWorldSplineData.json -->

# FForeignWorldSplineData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ForeignControlPointDataMap_DEPRECATED` | `TMap < TLazyObjectPtr < ULandscapeSplineControlPoint > , FForeignControlPointData >` | - |
| `ForeignControlPointData` | `TArray < FForeignControlPointData >` | - |
| `ForeignSplineSegmentDataMap_DEPRECATED` | `TMap < TLazyObjectPtr < ULandscapeSplineSegment > , FForeignSplineSegmentData >` | - |
| `ForeignSplineSegmentData` | `TArray < FForeignSplineSegmentData >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFormatArgumentData.json -->

# FFormatArgumentData

Used to pass argumentvalue pairs into FText::Format.
  The full C++ struct is located here: Engine\Source\Runtime\Core\Public\Internationalization\Text.h

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ArgumentName` | `FString` | - |
| `ArgumentValueType` | `TEnumAsByte < EFormatArgumentType :: Type >` | - |
| `ArgumentValue` | `FText` | - |
| `ArgumentValueInt` | `int32` | - |
| `ArgumentValueFloat` | `float` | - |
| `ArgumentValueGender` | `ETextGender` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFOscillator.json -->

# FFOscillator

Defines oscillation of a single number.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Amplitude` | `float` | Amplitude of the sinusoidal oscillation. |
| `Frequency` | `float` | Frequency of the sinusoidal oscillation. |
| `InitialOffset` | `TEnumAsByte < enum EInitialOscillatorOffset >` | Defines how to begin (either at zero, or at a randomized value. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFppTppShadowChangeRecord.json -->

# FFppTppShadowChangeRecord

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PrimitiveKey` | `TWeakObjectPtr < UPrimitiveComponent >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFractureEffect.json -->

# FFractureEffect

Struct used to hold effects for destructible damage events

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParticleSystem` | `UParticleSystem *` | Particle system effect to play at fracture location. |
| `Sound` | `USoundBase *` | Sound cue to play at fracture location. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFullyLoadedPackagesInfo.json -->

# FFullyLoadedPackagesInfo

Struct to help hold information about packages needing to be fully-loaded for DLC, etc.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FullyLoadType` | `TEnumAsByte < enum EFullyLoadPackageType >` | When to load these packages |
| `Tag` | `FString` | When this map or gametype is loaded, the packages in the following array will be loaded and added to root, then removed from root when map is unloaded |
| `PackagesToLoad` | `TArray < FName >` | The list of packages that will be fully loaded when the above Map is loaded |
| `LoadedObjects` | `TArray < UObject * >` | List of objects that were loaded, for faster cleanup |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFunctionBoneModifyData.json -->

# FFunctionBoneModifyData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoneName` | `FName` | - |
| `CSTransform` | `FTransform` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFunctionExpressionInput.json -->

# FFunctionExpressionInput

Struct that stores information about a function input which is needed to maintain connections and implement the function call.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ExpressionInput` | `UMaterialExpressionFunctionInput *` | Reference to the FunctionInput in the material function.  <br>	  This is a reference to a private object so it can't be saved, and must be generated by UpdateFromFunctionResource or SetMaterialFunction. |
| `ExpressionInputId` | `FGuid` | Id of the FunctionInput, used to link ExpressionInput. |
| `Input` | `FExpressionInput` | Actual input struct which stores information about how this input is connected in the material. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FFunctionExpressionOutput.json -->

# FFunctionExpressionOutput

Struct that stores information about a function output which is needed to maintain connections and implement the function call.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ExpressionOutput` | `UMaterialExpressionFunctionOutput *` | Reference to the FunctionOutput in the material function.  <br>	  This is a reference to a private object so it can't be saved, and must be generated by UpdateFromFunctionResource or SetMaterialFunction. |
| `ExpressionOutputId` | `FGuid` | Id of the FunctionOutput, used to link ExpressionOutput. |
| `Output` | `FExpressionOutput` | Actual output struct which stores information about how this output is connected in the material. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGameMagnitudeWrapper.json -->

# FGameMagnitudeWrapper

数值Wrapper

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CalculatorType` | `EPESkillValueCalculatorType` | 数值计算方式 |
| `Value` | `float` | 数值 |
| `GameAttribute` | `FGameAttributeContainer` | 要使用的属性名<br>	 <br>	UPROPERTY(EditAnywhere, BlueprintReadWrite, meta = (DisplayName = "数值=AX+B")) |
| `ValueA` | `FFloatGetter` | 公式参数A |
| `ValueB` | `FFloatGetter` | 公式参数B |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGameModeName.json -->

# FGameModeName

Helper structure, used to associate GameModes with shortcut names.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Name` | `FString` | Abbreviationprefix that can be used as an alias for the class name |
| `GameMode` | `FSoftClassPath` | GameMode class to load |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGameModePawnPool.json -->

# FGameModePawnPool

简单的pawn对象池 add by czcheng 2025.10.15

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PawnPool` | `TMap < APlayerController * , APawn * >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGameNameRedirect.json -->

# FGameNameRedirect

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OldGameName` | `FName` | - |
| `NewGameName` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGameplayTag.json -->

# FGameplayTag

A single gameplay tag, which represents a hierarchical name of the form x.y that is registered in the GameplayTagsManager 
 
  一个GameplayTag，由项目设置GameplayTags中注册的"x.y.z"格式的分层名称

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TagName` | `FName` | This Tags Name <br>	 UGC<br>	  GameplayTag的"x.y.z"格式的分层名称 |
| `bUseSlowReplication` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGameplayTagCategoryRemap.json -->

# FGameplayTagCategoryRemap

Category remapping. This allows base engine tag category meta data to remap to multiple project-specific categories.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BaseCategory` | `FString` | - |
| `RemapCategories` | `TArray < FString >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGameplayTagContainer.json -->

# FGameplayTagContainer

A Tag Container holds a collection of FGameplayTags, tags are included explicitly by adding them, and implicitly from adding child tags 
 
  一个容纳GameplayTag的集合，GameplayTag能够通过显式添加或者添加子标签隐式地包含进来

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GameplayTags` | `TArray < FGameplayTag >` | Array of gameplay tags <br>	 UGC<br>	  包含GameplayTag的数组 |
| `ParentTags` | `TArray < FGameplayTag >` | Array of expanded parent tags, in addition to GameplayTags. Used to accelerate parent searches. May contain duplicates in some cases <br>	 UGC<br>	  除 GameplayTags 之外的父级GameplayTag的数组，用于加速父级搜索。 可能包含重复项。 |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGameplayTagQuery.json -->

# FGameplayTagQuery

Queries are internally represented as a byte stream that is memory-efficient and can be evaluated quickly at runtime.
  Note: these have an extensive details and graph pin customization for editing, so there is no need to expose the internals to Blueprints.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TokenStreamVersion` | `int32` | Versioning for future token stream protocol changes. See EGameplayTagQueryStreamVersion. |
| `TagDictionary` | `TArray < FGameplayTag >` | List of tags referenced by this entire query. Token stream stored indices into this list. |
| `QueryTokenStream` | `TArray < uint8 >` | Stream representation of the actual hierarchical query |
| `UserDescription` | `FString` | User-provided string describing the query |
| `AutoDescription` | `FString` | Auto-generated string describing the query |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGameplayTagRedirect.json -->

# FGameplayTagRedirect

A single redirect from a deleted tag to the new tag that should replace it

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OldTagName` | `FName` | - |
| `NewTagName` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGameplayTagSource.json -->

# FGameplayTagSource

Struct defining where gameplay tags are loadedsaved from. Mostly for the editor

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceName` | `FName` | Name of this source |
| `SourceType` | `EGameplayTagSourceType` | Type of this source |
| `SourceTagList` | `UGameplayTagsList *` | If this is bound to an ini object for saving, this is the one |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGameplayTagTableRow.json -->

# FGameplayTagTableRow

Simple struct for a table row in the gameplay tag table and element in the ini list

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Tag` | `FName` | Tag specified in the table |
| `DevComment` | `FString` | Developer comment clarifying the usage of a particular tag, not user facing |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGaussianSumBloomSettings.json -->

# FGaussianSumBloomSettings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Intensity` | `float` | Multiplier for all bloom contributions >=0: off, 1(default), >1 brighter |
| `Threshold` | `float` | minimum brightness the bloom starts having effect<br>	  -1:all pixels affect bloom equally (physically correct, faster as a threshold pass is omitted), 0:all pixels affect bloom brights more, 1(default), >1 brighter |
| `SizeScale` | `float` | Scale for all bloom sizes |
| `Filter1Size` | `float` | Diameter size for the Bloom1 in percent of the screen width<br>	  (is done in 12 resolution, larger values cost more performance, good for high frequency details)<br>	  >=0: can be clamped because of shader limitations |
| `Filter2Size` | `float` | Diameter size for Bloom2 in percent of the screen width<br>	  (is done in 14 resolution, larger values cost more performance)<br>	  >=0: can be clamped because of shader limitations |
| `Filter3Size` | `float` | Diameter size for Bloom3 in percent of the screen width<br>	  (is done in 18 resolution, larger values cost more performance)<br>	  >=0: can be clamped because of shader limitations |
| `Filter4Size` | `float` | Diameter size for Bloom4 in percent of the screen width<br>	  (is done in 116 resolution, larger values cost more performance, best for wide contributions)<br>	  >=0: can be clamped because of shader limitations |
| `Filter5Size` | `float` | Diameter size for Bloom5 in percent of the screen width<br>	  (is done in 132 resolution, larger values cost more performance, best for wide contributions)<br>	  >=0: can be clamped because of shader limitations |
| `Filter6Size` | `float` | Diameter size for Bloom6 in percent of the screen width<br>	  (is done in 164 resolution, larger values cost more performance, best for wide contributions)<br>	  >=0: can be clamped because of shader limitations |
| `Filter1Tint` | `FLinearColor` | Bloom1 tint color |
| `Filter2Tint` | `FLinearColor` | Bloom2 tint color |
| `Filter3Tint` | `FLinearColor` | Bloom3 tint color |
| `Filter4Tint` | `FLinearColor` | Bloom4 tint color |
| `Filter5Tint` | `FLinearColor` | Bloom5 tint color |
| `Filter6Tint` | `FLinearColor` | Bloom6 tint color |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGenericStruct.json -->

# FGenericStruct

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Data` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGenericTeamId.json -->

# FGenericTeamId

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TeamID` | `uint8` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGeomSelection.json -->

# FGeomSelection

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Type` | `int32` | - |
| `Index` | `int32` | - |
| `SelectionIndex` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGerstnerWaterWaveGeneratorSimple.json -->

# FGerstnerWaterWaveGeneratorSimple

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NumWaves` | `int32` | - |
| `Seed` | `int32` | - |
| `Randomness` | `float` | - |
| `MinWavelength` | `float` | - |
| `MaxWavelength` | `float` | - |
| `WavelengthFalloff` | `float` | - |
| `MinAmplitude` | `float` | - |
| `MaxAmplitude` | `float` | - |
| `AmplitudeFalloff` | `float` | - |
| `DirectionAngularSpreadDeg` | `float` | UPROPERTY(EditAnywhere, BlueprintReadWrite, meta = (DisplayName = "Dominant Wind Angle", Category = "Directions", UIMin = -180, ClampMin = -180, UIMax = 180, ClampMax = 180, Units = deg))<br>		float GerstnerAngleDeg = 0.0f; |
| `SmallWaveSteepness` | `float` | - |
| `LargeWaveSteepness` | `float` | - |
| `SteepnessFalloff` | `float` | - |
| `WaveSpeed` | `float` | - |
| `Gerstnersamplesize` | `float` | - |
| `GerstnerParallelness` | `float` | - |
| `GerstnerWaves` | `TArray < FGerstnerWave >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGerstnerWave.json -->

# FGerstnerWave

Raw wave parameters for one gerstner wave

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `WaveLength` | `float` | - |
| `Amplitude` | `float` | - |
| `Steepness` | `float` | - |
| `GerstnerAngle` | `float` | - |
| `WaveVector` | `FVector2D` | - |
| `WaveSpeed` | `float` | - |
| `WKA` | `float` | - |
| `Q` | `float` | - |
| `PhaseOffset` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGPUSpriteEmitterInfo.json -->

# FGPUSpriteEmitterInfo

The data needed by the runtime to simulate sprites.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RequiredModule` | `UParticleModuleRequired *` | The required module. Needed for now, but should be divorced from the runtime. |
| `SpawnModule` | `UParticleModuleSpawn *` | The spawn module. Needed for now, but should be divorced from the runtime. |
| `SpawnPerUnitModule` | `UParticleModuleSpawnPerUnit *` | The spawn-per-unit module. |
| `SpawnModules` | `TArray < UParticleModule * >` | List of spawn modules that must be evaluated at runtime. |
| `LocalVectorField` | `FGPUSpriteLocalVectorFieldInfo` | Local vector field info. |
| `VectorFieldScale` | `FFloatDistribution` | Per-particle vector field scale. |
| `DragCoefficient` | `FFloatDistribution` | Per-particle drag coefficient. |
| `PointAttractorStrength` | `FFloatDistribution` | Point attractor strength over time. |
| `Resilience` | `FFloatDistribution` | Damping factor applied to particle collisions. |
| `ConstantAcceleration` | `FVector` | Constant acceleration to apply to particles. |
| `PointAttractorPosition` | `FVector` | Point attractor position. |
| `PointAttractorRadiusSq` | `float` | Point attractor radius, squared. |
| `OrbitOffsetBase` | `FVector` | Amount by which to offset particles when they are spawned. |
| `OrbitOffsetRange` | `FVector` | - |
| `InvMaxSize` | `FVector2D` | One over the maximum size of a sprite particle. |
| `InvRotationRateScale` | `float` | The inverse scale to apply to rotation rate. |
| `MaxLifetime` | `float` | The maximum lifetime of particles in this emitter. |
| `MaxParticleCount` | `int32` | The maximum number of particles expected for this emitter. |
| `ScreenAlignment` | `TEnumAsByte < EParticleScreenAlignment >` | The method for aligning the particle based on the camera. |
| `LockAxisFlag` | `TEnumAsByte < EParticleAxisLock >` | The method for locking the particles to a particular axis. |
| `bEnableCollision` | `uint32` | If true, collisions are enabled for this emitter. |
| `CollisionMode` | `TEnumAsByte < EParticleCollisionMode :: Type >` | - |
| `bRemoveHMDRoll` | `uint32` | If true, removes the HMD view roll (e.g. in VR) |
| `MinFacingCameraBlendDistance` | `float` | The distance at which PSA_FacingCameraDistanceBlend	is fully PSA_Square |
| `MaxFacingCameraBlendDistance` | `float` | The distance at which PSA_FacingCameraDistanceBlend	is fully PSA_FacingCameraPosition |
| `DynamicColor` | `FRawDistributionVector` | Dynamic color scale from the ColorOverLife module. |
| `DynamicAlpha` | `FRawDistributionFloat` | Dynamic alpha scale from the ColorOverLife module. |
| `DynamicColorScale` | `FRawDistributionVector` | Dynamic color scale from the ColorScaleOverLife module. |
| `DynamicAlphaScale` | `FRawDistributionFloat` | Dynamic alpha scale from the ColorScaleOverLife module. |
| `DynamicColorHDR` | `FRawDistributionVector` | Dynamic color scale from the ColorOverLife module. |
| `DynamicAlphaHDR` | `FRawDistributionFloat` | Dynamic alpha scale from the ColorOverLife module. |
| `DynamicColorScaleHDR` | `FRawDistributionVector` | Dynamic color scale from the ColorScaleOverLife module. |
| `DynamicAlphaScaleHDR` | `FRawDistributionFloat` | Dynamic alpha scale from the ColorScaleOverLife module. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGPUSpriteLocalVectorFieldInfo.json -->

# FGPUSpriteLocalVectorFieldInfo

Data needed for local vector fields.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Field` | `UVectorField *` | Local vector field to apply to this emitter. |
| `Transform` | `FTransform` | Local vector field transform. |
| `MinInitialRotation` | `FRotator` | Minimum initial rotation. |
| `MaxInitialRotation` | `FRotator` | Maximum initial rotation. |
| `RotationRate` | `FRotator` | Local vector field rotation rate. |
| `Intensity` | `float` | Local vector field intensity. |
| `Tightness` | `float` | Local vector field tightness. |
| `bIgnoreComponentTransform` | `uint32` | Ignore Components Transform |
| `bTileX` | `uint32` | Tile vector field in x axis? |
| `bTileY` | `uint32` | Tile vector field in y axis? |
| `bTileZ` | `uint32` | Tile vector field in z axis? |
| `bUseFixDT` | `uint32` | Use fix delta time in the simulation? |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGPUSpriteResourceData.json -->

# FGPUSpriteResourceData

The source data for runtime resources.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `QuantizedColorSamples` | `TArray < FColor >` | Quantized color samples. |
| `QuantizedMiscSamples` | `TArray < FColor >` | Quantized samples for misc curve attributes to be evaluated at runtime. |
| `QuantizedSimulationAttrSamples` | `TArray < FColor >` | Quantized samples for simulation attributes. |
| `ColorScale` | `FVector4` | Scale and bias to be applied to the color of sprites. |
| `ColorBias` | `FVector4` | - |
| `QuantizedColorSamplesHDR` | `TArray < FColor >` | - |
| `ColorScaleHDR` | `FVector4` | - |
| `ColorBiasHDR` | `FVector4` | - |
| `MiscScale` | `FVector4` | Scale and bias to be applied to the misc curve. |
| `MiscBias` | `FVector4` | - |
| `SimulationAttrCurveScale` | `FVector4` | Scale and bias to be applied to the simulation attribute curves. |
| `SimulationAttrCurveBias` | `FVector4` | - |
| `SubImageSize` | `FVector4` | Size of subimages. X:SubImageCountH Y:SubImageCountV Z:1SubImageCountH W:1SubImageCountV |
| `SizeBySpeed` | `FVector4` | SizeBySpeed parameters. XY=SpeedScale ZW=MaxSpeedScale. |
| `ConstantAcceleration` | `FVector` | Constant acceleration to apply to particles. |
| `OrbitOffsetBase` | `FVector` | Offset at which to orbit. |
| `OrbitOffsetRange` | `FVector` | - |
| `OrbitFrequencyBase` | `FVector` | Frequency at which the particle orbits around each axis. |
| `OrbitFrequencyRange` | `FVector` | - |
| `OrbitPhaseBase` | `FVector` | Phase offset of orbit around each axis. |
| `OrbitPhaseRange` | `FVector` | - |
| `GlobalVectorFieldScale` | `float` | Scale to apply to global vector fields. |
| `GlobalVectorFieldTightness` | `float` | Tightness override value for the global vector fields. |
| `PerParticleVectorFieldScale` | `float` | Scale to apply to per-particle vector field scale. |
| `PerParticleVectorFieldBias` | `float` | Bias to apply to per-particle vector field scale. |
| `DragCoefficientScale` | `float` | Scale to apply to per-particle drag coefficient. |
| `DragCoefficientBias` | `float` | Bias to apply to per-particle drag coefficient. |
| `ResilienceScale` | `float` | Scale to apply to per-particle damping factor. |
| `ResilienceBias` | `float` | Bias to apply to per-particle damping factor. |
| `CollisionRadiusScale` | `float` | Scale to apply to per-particle size for collision. |
| `CollisionRadiusBias` | `float` | Bias to apply to per-particle size for collision. |
| `CollisionTimeBias` | `float` | Bias applied to relative time upon collision. |
| `CollisionRandomSpread` | `float` | Control on reflection's random distribution spread. |
| `CollisionRandomDistribution` | `float` | Control on reflection's random distribution when colliding. (1=uniform distribution) |
| `OneMinusFriction` | `float` | One minus the coefficient of friction applied to particles upon collision. |
| `RotationRateScale` | `float` | Scale to apply to per-particle rotation rate. |
| `CameraMotionBlurAmount` | `float` | How much to stretch sprites based on camera motion blur. |
| `ScreenAlignment` | `TEnumAsByte < enum EParticleScreenAlignment >` | Screen alignment for particles. |
| `LockAxisFlag` | `TEnumAsByte < enum EParticleAxisLock >` | The method for locking the particles to a particular axis. |
| `PivotOffset` | `FVector2D` | Pivot offset in UV space for placing the verts of each particle. |
| `bRemoveHMDRoll` | `uint32` | If true, removes the HMD view roll (e.g. in VR) |
| `MinFacingCameraBlendDistance` | `float` | The distance at which PSA_FacingCameraDistanceBlend	is fully PSA_Square |
| `MaxFacingCameraBlendDistance` | `float` | The distance at which PSA_FacingCameraDistanceBlend	is fully PSA_FacingCameraPosition |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGraphReference.json -->

# FGraphReference

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MacroGraph` | `UEdGraph *` | - |
| `GraphBlueprint` | `UBlueprint *` | - |
| `GraphGuid` | `FGuid` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGrassInput.json -->

# FGrassInput

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Name` | `FName` | - |
| `GrassType` | `ULandscapeGrassType *` | - |
| `Input` | `FExpressionInput` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGrassVariety.json -->

# FGrassVariety

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GrassMesh` | `UStaticMesh *` | - |
| `GrassDensity` | `float` | Instances per 10 square meters. |
| `bUseGrid` | `bool` | If true, use a jittered grid sequence for placement, otherwise use a halton sequence. |
| `PlacementJitter` | `float` | - |
| `StartCullDistance` | `int32` | The distance where instances will begin to fade out if using a PerInstanceFadeAmount material node. 0 disables. |
| `EndCullDistance` | `int32` | The distance where instances will have completely faded out when using a PerInstanceFadeAmount material node. 0 disables. <br>	  When the entire cluster is beyond this distance, the cluster is completely culled and not rendered at all. |
| `MinLOD` | `int32` | Specifies the smallest LOD that will be used for this component.<br>	  If -1 (default), the MinLOD of the static mesh asset will be used instead. |
| `Scaling` | `EGrassScaling` | Specifies grass instance scaling type |
| `ScaleX` | `FFloatInterval` | Specifies the range of scale, from minimum to maximum, to apply to a grass instance's X Scale property |
| `ScaleY` | `FFloatInterval` | Specifies the range of scale, from minimum to maximum, to apply to a grass instance's Y Scale property |
| `ScaleZ` | `FFloatInterval` | Specifies the range of scale, from minimum to maximum, to apply to a grass instance's Z Scale property |
| `RandomRotation` | `bool` | Whether the grass instances should be placed at random rotation (true) or all at the same rotation (false) |
| `AlignToSurface` | `bool` | Whether the grass instances should be tilted to the normal of the landscape (true), or always vertical (false) |
| `bUseLandscapeLightmap` | `bool` | Whether to use the landscape's lightmap when rendering the grass. |
| `bUseVolumeProbeGI` | `bool` | - |
| `LightingChannels` | `FLightingChannels` | Lighting channels that the grass will be assigned. Lights with matching channels will affect the grass.<br>	  These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing. |
| `bReceivesDecals` | `bool` | Whether the grass instances should receive decals. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGridBlendSample.json -->

# FGridBlendSample

result of how much weight of the grid element

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GridElement` | `FEditorElement` | - |
| `BlendWeight` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGridVisibilityCameraInfo.json -->

# FGridVisibilityCameraInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CameraDirections` | `TArray < FVector >` | - |
| `CameraLocation` | `FVector` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGroupedSkeletalOptimizationSettings.json -->

# FGroupedSkeletalOptimizationSettings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bAutoComputeLODDistance` | `bool` | Whether to compute LOD switch distance or not |
| `LevelOfDetailType` | `ESkeletalMeshLODType` | The type to use when optimizing the skeletal mesh LOD |
| `ReductionSettings` | `FSkeletalMeshOptimizationSettings` | - |
| `ProxySettings` | `FMeshProxySettings` | - |
| `bForceLODRebuild` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGroupedStaticMeshOptimizationSettings.json -->

# FGroupedStaticMeshOptimizationSettings

---------------------------------------------------------------------------
---------------------------------------------------------------------------

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LevelOfDetailType` | `EStaticMeshLODType` | The type to use when optimizing the skeletal mesh LOD |
| `ReductionSettings` | `FMeshReductionSettings` | - |
| `ProxySettings` | `FMeshProxySettings` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGroupedTagEntry.json -->

# FGroupedTagEntry

Grouped Tag Entry - Stores tags for a single category group

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GroupName` | `FName` | Group name (e.g. "StreamingType", "LODLevel") |
| `Tags` | `TArray < FName >` | Tags in this group |
| `bOverrideStaticMeshTags` | `bool` | Component-local flag: this group overrides the same StaticMesh tag group, even when Tags is empty. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FGuid.json -->

# FGuid

A globally unique identifier.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `A` | `int32` | - |
| `B` | `int32` | - |
| `C` | `int32` | - |
| `D` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FHapticFeedbackDetails_Curve.json -->

# FHapticFeedbackDetails_Curve

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Combine` | `FRuntimeFloatCurveHaptic` | The frequency to vibrate the haptic device at.  Frequency ranges vary by device! <br>		 The amplitude to vibrate the haptic device at.  Amplitudes are normalized over the range [0.0, 1.0], with 1.0 being the max setting of the device |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FHardwareCursorReference.json -->

# FHardwareCursorReference

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CursorPath` | `FName` | Specify the partial game content path to the hardware cursor.  For example,<br>	    DO:   SlateDefaultPointer<br>	    DONT: SlateDefaultPointer.cur<br>	 <br>	  NOTE: Having a 'Slate' directory in your game content folder will always be cooked, if<br>	        you're trying to decide where to locate these cursor files.<br>	  <br>	  The hardware cursor system will search for platform specific formats first if you want to <br>	  take advantage of those capabilities.<br>	 <br>	  Windows:<br>	    .ani -> .cur -> .png<br>	 <br>	  Mac:<br>	    .tiff -> .png<br>	 <br>	  Linux:<br>	    .png<br>	 <br>	  Multi-Resolution Png Fallback<br>	   Because there's not a universal multi-resolution format for cursors there's a pattern we look for<br>	   on all platforms where pngs are all that is found instead of curanitiff.<br>	 <br>	     Pointer.png<br>	     Pointer@1.25x.png<br>	     Pointer@1.5x.png<br>	     Pointer@1.75x.png<br>	     Pointer@2x.png<br>	     ...etc |
| `HotSpot` | `FVector2D` | HotSpot needs to be in normalized (0..1) coordinates since it may apply to different resolution images.<br>	  NOTE: This HotSpot is only used on formats that do not provide their own hotspot, e.g. Tiff, PNG. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FHeaderRowStyle.json -->

# FHeaderRowStyle

Represents the appearance of an SHeaderRow

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ColumnStyle` | `FTableColumnHeaderStyle` | Style of the normal header row columns |
| `LastColumnStyle` | `FTableColumnHeaderStyle` | Style of the last header row column |
| `ColumnSplitterStyle` | `FSplitterStyle` | Style of the splitter used between the columns |
| `BackgroundBrush` | `FSlateBrush` | Brush used to draw the header row background |
| `ForegroundColor` | `FSlateColor` | Color used to draw the header row foreground |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FHierarchicalSimplification.json -->

# FHierarchicalSimplification

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TransitionScreenSize` | `float` | The screen radius an mesh object should reach before swapping to the LOD actor, once one of parent displays, it won't draw any of children. |
| `OverrideDrawDistance` | `float` | - |
| `bUseOverrideDrawDistance` | `bool` | - |
| `bAllowSpecificExclusion` | `uint8` | - |
| `bSimplifyMesh` | `bool` | If this is true, it will simplify mesh but it is slower.<br>	 If false, it will just merge actors but not simplify using the lower LOD if exists.<br>	 For example if you build LOD 1, it will use LOD 1 of the mesh to merge actors if exists.<br>	 If you merge material, it will reduce drawcalls. |
| `ProxySetting` | `FMeshProxySettings` | Simplification Setting if bSimplifyMesh is true |
| `MergeSetting` | `FMeshMergingSettings` | Merge Mesh Setting if bSimplifyMesh is false |
| `DesiredBoundRadius` | `float` | Desired Bounding Radius for clustering - this is not guaranteed but used to calculate filling factor for auto clustering |
| `DesiredFillingPercentage` | `float` | Desired Filling Percentage for clustering - this is not guaranteed but used to calculate filling factor  for auto clustering |
| `DesiredGridSize` | `float` | - |
| `DesiredGridOffset` | `float` | - |
| `DesiredGridVolume` | `TArray < FVector4 >` | - |
| `GridIgnoreStaticMeshs` | `TArray < FString >` | - |
| `HLODGroups` | `TArray < FHLODGroup >` | - |
| `MinNumberOfActorsToBuild` | `int32` | Min number of actors to build LODActor |
| `bOnlyGenerateClustersForVolumes` | `bool` | Min number of actors to build LODActor |
| `bReusePreviousLevelClusters` | `bool` | Will reuse the clusters generated for the previous (lower) HLOD level |
| `ProxyMeshLOD1SwitchDistance` | `float` | Distance (in cm) at which ProxyMesh switches from LOD0 to LOD1. Overrides legacy triangle-count-based ScreenSize calculation. |
| `bOverrideProxyMeshLOD1SwitchDistance` | `bool` | - |
| `ProxyMeshCullingDistance` | `float` | Distance (in cm) at which ProxyMesh is culled (not rendered). Overrides legacy CVar-based culling distance. |
| `bOverrideProxyMeshCullingDistance` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FHitResult.json -->

# FHitResult

Structure containing information about one hit of a trace, such as point of impact and surface normal at that point.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Time` | `float` | 'Time' of impact along trace direction (ranging from 0.0 to 1.0) if there is a hit, indicating time between TraceStart and TraceEnd.<br>	  For swept movement (but not queries) this may be pulled back slightly from the actual time of impact, to prevent precision problems with adjacent geometry. |
| `bBlockingHit` | `uint32` | Indicates if this hit was a result of blocking collision. If false, there was no hit or it was an overlaptouch instead. |
| `bStartPenetrating` | `uint32` | Whether the trace started in penetration, i.e. with an initial blocking overlap.<br>	  In the case of penetration, if PenetrationDepth > 0.f, then it will represent the distance along the Normal vector that will result in<br>	  minimal contact between the swept shape and the object that was hit. In this case, ImpactNormal will be the normal opposed to movement at that location<br>	  (ie, Normal may not equal ImpactNormal). ImpactPoint will be the same as Location, since there is no single impact point to report. |
| `Distance` | `float` | The distance from the TraceStart to the Location in world space. This value is 0 if there was an initial overlap (trace started inside another colliding object). |
| `Location` | `FVector_NetQuantize` | The location in world space where the moving shape would end up against the impacted object, if there is a hit. Equal to the point of impact for line tests.<br>	  Example: for a sphere trace test, this is the point where the center of the sphere would be located when it touched the other object.<br>	  For swept movement (but not queries) this may not equal the final location of the shape since hits are pulled back slightly to prevent precision issues from overlapping another surface. |
| `ImpactPoint` | `FVector_NetQuantize` | Location in world space of the actual contact of the trace shape (box, sphere, ray, etc) with the impacted object.<br>	  Example: for a sphere trace test, this is the point where the surface of the sphere touches the other object.<br>	  @note: In the case of initial overlap (bStartPenetrating=true), ImpactPoint will be the same as Location because there is no meaningful single impact point to report. |
| `Normal` | `FVector_NetQuantizeNormal` | Normal of the hit in world space, for the object that was swept. Equal to ImpactNormal for line tests.<br>	  This is computed for capsules and spheres, otherwise it will be the same as ImpactNormal.<br>	  Example: for a sphere trace test, this is a normalized vector pointing in towards the center of the sphere at the point of impact. |
| `ImpactNormal` | `FVector_NetQuantizeNormal` | Normal of the hit in world space, for the object that was hit by the sweep, if any.<br>	  For example if a box hits a flat plane, this is a normalized vector pointing out from the plane.<br>	  In the case of impact with a corner or edge of a surface, usually the "most opposing" normal (opposed to the query direction) is chosen. |
| `TraceStart` | `FVector_NetQuantize` | Start location of the trace.<br>	  For example if a sphere is swept against the world, this is the starting location of the center of the sphere. |
| `TraceEnd` | `FVector_NetQuantize` | End location of the trace; this is NOT where the impact occurred (if any), but the furthest point in the attempted sweep.<br>	  For example if a sphere is swept against the world, this would be the center of the sphere if there was no blocking hit. |
| `PenetrationDepth` | `float` | If this test started in penetration (bStartPenetrating is true) and a depenetration vector can be computed,<br>	   this value is the distance along Normal that will result in moving out of penetration.<br>	   If the distance cannot be computed, this distance will be zero. |
| `Item` | `int32` | Extra data about item that was hit (hit primitive specific). |
| `PhysMaterial` | `TWeakObjectPtr < UPhysicalMaterial >` | Physical material that was hit.<br>	  @note Must set bReturnPhysicalMaterial on the swept PrimitiveComponent or in the query params for this to be returned. |
| `Actor` | `TWeakObjectPtr < AActor >` | Actor hit by the trace. |
| `Component` | `TWeakObjectPtr < UPrimitiveComponent >` | PrimitiveComponent hit by the trace. |
| `BoneName` | `FName` | Name of bone we hit (for skeletal meshes). |
| `FaceIndex` | `int32` | Face index we hit (for complex hits with triangle meshes). |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FHLODClusterRef.json -->

# FHLODClusterRef

记录一个 LODActor 拥有的 HISM ClusterTree 节点引用。
 
  方案：按 Grid 坐标分配"整 Node"。
    - 分组单元 = 一整个 ClusterTree Node（Node 中心落 Grid）。Node 要么完整归属某个 LODActor，
      要么完全不归属，绝不拆分到 instance 粒度。
    - OwnedClusterNodeIndices 是唯一主键：烘焙端按 Node 取 [FirstInstance,LastInstance]
      (Sorted) -> SortedInstances[] 映射 Logical -> 拷贝；运行时用同一 NodeIndex 下 Mask。
      两端针对同一批物理实例，不会穿帮。
    - ClusterBounds 仅用于 LODActor 位置包围盒。
 
  前提（打破任一条必须重新评估方案）：
    - 重组关卡不允许人为修改（实例与 ClusterTree 稳定）；
    - 使用普通 HISM（bIsFoliage=false，默认 bEnableDensityScaling=false，不会触发密度剔除重建）；
    - 一次重组对应一次 HLOD 构建。

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `HISMActor` | `TSoftObjectPtr < AActor >` | - |
| `OwnedClusterNodeIndices` | `TArray < int32 >` | - |
| `ClusterBounds` | `FBox` | - |
| `InstanceCount` | `int32` | - |
| `PerInstanceTriangleCount` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FHLODGroup.json -->

# FHLODGroup

LODDrawDistanceScale 等参数。
   - bClusterBasedMode 不在 Group 内独立配置，全局服从 r.LevelReorgHLOD.ClusterBasedMode。

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bEnabled` | `bool` | - |
| `GroupName` | `FName` | - |
| `StaticMeshes` | `TArray < TSoftObjectPtr < UStaticMesh > >` | 参与该 Group 的 StaticMesh 集合（编辑用资产引用，运行期取 ToSoftObjectPath().ToString() 做精确字符串匹配） |
| `ProxyBaseMaterial` | `TSoftObjectPtr < UMaterialInterface >` | ProxyMesh 烘焙用 BaseMaterial |
| `OverrideDrawDistance` | `float` | DrawDistance value to use when the inline toggle is checked. Takes precedence over LODSetup.bUseOverrideDrawDistance and skips LODDrawDistanceScale. |
| `bUseOverrideDrawDistance` | `bool` | - |
| `LODDrawDistanceScale` | `float` | - |
| `DesiredGridSize` | `float` | - |
| `DesiredGridOffset` | `float` | - |
| `MaxBoundForHLOD` | `float` | - |
| `MinSubActorsForHLOD` | `int32` | - |
| `ClusterBoundsMinRadius` | `float` | - |
| `ClusterTreeLevel` | `int32` | - |
| `ClusterMinInstances` | `int32` | - |
| `MinClustersPerLODActor` | `int32` | - |
| `MaxClustersPerLODActor` | `int32` | - |
| `LOD0ReduceFactor` | `float` | LOD0 percentage-based reduction factor (OriginalTriangles  this value). Corresponds to global r.HLOD.ProxyMeshLOD0ReduceFactor |
| `PerVolumeTriangles` | `float` | Volume-based: triangles allowed per cubic-meter of Bounds. Corresponds to global r.HLOD.ProxyMeshPerVolumeTraingles |
| `LODReduceFactor` | `float` | LOD1~N successive reduction factor. Corresponds to global r.HLOD.ProxyMeshReduceFactor |
| `LODMinTriangles` | `int32` | Minimum triangle threshold (no further LOD generated below this). Corresponds to global r.HLOD.ProxyMeshLODMinTriangles |
| `LODMaxCount` | `int32` | Maximum LOD level count. Corresponds to global r.HLOD.ProxyMeshLODMax |
| `ProxyMeshLOD1SwitchDistance` | `float` | Distance (in cm) at which ProxyMesh switches from LOD0 to LOD1. Overrides legacy triangle-count-based ScreenSize calculation. |
| `bOverrideProxyMeshLOD1SwitchDistance` | `bool` | - |
| `ProxyMeshCullingDistance` | `float` | Distance (in cm) at which ProxyMesh is culled (not rendered). Overrides legacy CVar-based culling distance. |
| `bOverrideProxyMeshCullingDistance` | `bool` | - |
| `bEmissiveMap` | `bool` | Whether to bake Emissive channel into ProxyMesh material for this Group. |
| `EmissiveTextureSize` | `FIntPoint` | Override Emissive texture size (only used when bEmissiveMap=true) |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FHLODProxyMesh.json -->

# FHLODProxyMesh

A mesh proxy entry

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LODActor` | `TLazyObjectPtr < ALODActor >` | The ALODActor that we were generated from |
| `StaticMesh` | `UStaticMesh *` | The mesh used to display this proxy |
| `Key` | `FName` | The key generated from an ALODActor. If this differs from that generated from the ALODActor, then the mesh needs regenerating. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FHLODStreamTicker.json -->

# FHLODStreamTicker

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Actors` | `TArray < AActor * >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FHyperlinkStyle.json -->

# FHyperlinkStyle

Represents the appearance of an SHyperlink

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UnderlineStyle` | `FButtonStyle` | Underline style |
| `TextStyle` | `FTextBlockStyle` | Text style |
| `Padding` | `FMargin` | Padding |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FIdeaBakingPrimitiveSettings.json -->

# FIdeaBakingPrimitiveSettings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `IdeaMaterialDiffuse` | `float` | When baking, use this diffuse calculate reflection fro sun related lighting, not use really material's diffuse texture |
| `LightmapBoost` | `float` | Scales the lightmap result of idea baking. |
| `DiscardPixelFrontfaceFactor` | `float` | When ray intersected surface frontface counter lower DiscardPixelFrontfaceFactor  NumRays, the pixel will be discard. Larger value will help decrease black edge artifact.<br>	 But if scene has two side surface(like flags), will cause another artifact, pixels behind back side of flags maybe discarded wrong. |
| `SunIntensity` | `float` | By luciuszhang:<br>	 Control the sun intensity from the sky, unit is cdm^2, default value is 1.0. |
| `LocalLightsAffectMaxDistance` | `float` | By luciuszhang:<br>	 Control the sun indirect intensity from the sky, unit is cdm^2, default value is 1.0. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FIdeaBakingWorldInfoSettings.json -->

# FIdeaBakingWorldInfoSettings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BakingLayout` | `EIdeaBakingLayout` | By luciuszhang: Baking layout mode |
| `NumCoarseSamples` | `int32` | Number of first pass light samples. |
| `NumSamples` | `int32` | Number of second pass light samples for two pass mode and samples for brute force mode. |
| `NumLightingBounces` | `int32` | Number of light bounces to simulate for point  spot  directional lights, starting from the light source.<br>	 0 is direct lighting only, 1 is one bounce, etc.<br>	 Bounce 1 takes the most time to calculate and contributes the most to visual quality, followed by bounce 2.<br>	 Successive bounces don't really affect build times, but have a much lower visual impact, unless the material diffuse colors are close to 1. |
| `LightmapBoost` | `float` | Scales the lightmap result of idea baking. |
| `SunHardness` | `float` | Control Sun direction falloff, bigger SunHardness, three direction will be more separated |
| `BakingMode` | `EIdeaBakingMode` | Baking path tracing mode, just for debug |
| `bUseParallelBaking` | `uint32` | If true, parallel baking will be enabled. |
| `bUseConservativeRasterization` | `uint32` | If true, Conservative Rasterization (emulated by multi-tap) will be enabled. |
| `bUseLocalOcclusion` | `uint32` | If true, local ambient occlusion (A0) will be enabled. |
| `LocalOcclusionRadius` | `float` | Local ambient occlusion(A0) tracing radius. |
| `LocalOcclusionFallOff` | `float` | Local ambient occlusion(A0) transition speed. |
| `LocalOcclusionDistribution` | `float` | Local ambient occlusion(A0) sampling distribution. |
| `LocalOcclusionFadeRatio` | `float` | Local ambient occlusion(A0) fade start ratio. |
| `LocalOcclusionRes` | `int32` | Local ambient occlusion(A0) resolution multiple. |
| `LocalOcclusionMultiple` | `int32` | Local ambient occlusion(A0) sampling multiple. |
| `LocalOcclusionPower` | `float` | Local ambient occlusion(A0) strength, larger value, darker AO. |
| `LocalOcclusionDenoising` | `int32` | Local ambient occlusion(A0) denoising filter count. |
| `LocalOcclusionDilation` | `int32` | Local ambient occlusion(A0) dilation filter count. |
| `NumDenoisingIterators` | `int32` | If true, denoise filter will be enabled. |
| `NumDilationIterators` | `int32` | If true, dilation filter will be enabled. |
| `DirectLightDenoising` | `int32` | Denoising filter iteration number for direct lighting. |
| `RayTraceMaxDistance` | `float` | By luciuszhang: Path tracing distance threshold in centimeters. |
| `RayTraceBias` | `float` | By luciuszhang: Path tracing ray bias in centimeters. |
| `RetraceDistance` | `float` | By luciuszhang: Retrace distance threshold in centimeters. |
| `SmallestTexelRadius` | `float` | By luciuszhang:<br>	 Smallest texel radius allowed, useful for clamping edge cases where some texels have a radius of 0.<br>	 This should be smaller than the smallest valid texel radius in the scene. |
| `AreaLightSampleCount` | `uint32` | Path tracing distance threshold in centimeters. |
| `bWithPortalDirectLighting` | `uint32` | If true, calculate portal light direct lighting. |
| `bWithGrayDiffuse` | `uint32` | If true, use gray diffuse material for sun indirect lighting. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FIdeaGrassFieldData.json -->

# FIdeaGrassFieldData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ForceTextureRT` | `UTextureRenderTarget2D *` | - |
| `TramplerPositionList` | `TArray < FVector >` | - |
| `TramplerDirectionList` | `TArray < FRotator >` | - |
| `TramplerCutoff` | `TArray < float >` | - |
| `TrampleTexture` | `UTexture *` | - |
| `TrampleScale` | `float` | - |
| `SkillTexture` | `UTexture *` | - |
| `CleanTextureScale` | `TArray < float >` | - |
| `GrassSpringness` | `float` | - |
| `GrassFieldRect` | `FVector4` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FImportanceTexture.json -->

# FImportanceTexture

Texture processed for importance sampling
 Holds marginal PDF of the rows, as well as the PDF of each row

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Size` | `FIntPoint` | - |
| `NumMips` | `int` | - |
| `MarginalCDF` | `TArray < float >` | - |
| `ConditionalCDF` | `TArray < float >` | - |
| `TextureData` | `TArray < FColor >` | - |
| `Texture` | `TWeakObjectPtr < UTexture2D >` | - |
| `Weighting` | `TEnumAsByte < EImportanceWeight :: Type >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FImportFactorySettingValues.json -->

# FImportFactorySettingValues

Holds UProperty names and values to customize factory settings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SettingName` | `FString` | The name of the UProperty to change |
| `Value` | `FString` | The value to apply to the UProperty |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FIndexedCurve.json -->

# FIndexedCurve

A curve base class which enables key handles to index lookups.
 
  @todo sequencer: Some heavy refactoring can be done here. Much more stuff can go in this base class.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `KeyHandlesToIndices` | `FKeyHandleMap` | Map of which key handles go to which indices. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInlineEditableTextBlockStyle.json -->

# FInlineEditableTextBlockStyle

Represents the appearance of an SInlineEditableTextBlock

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EditableTextBoxStyle` | `FEditableTextBoxStyle` | The style of the editable text box, which dictates the font, color, and shadow options. |
| `TextStyle` | `FTextBlockStyle` | The style of the text block, which dictates the font, color, and shadow options. Style overrides all other properties! |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInlineTextImageStyle.json -->

# FInlineTextImageStyle

Represents the appearance of an inline image used by rich text

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Image` | `FSlateBrush` | Image to use when the slider thumb is in its normal state |
| `Baseline` | `int16` | The offset from the bottom of the image height to the baseline. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInputActionKeyMapping.json -->

# FInputActionKeyMapping

Defines a mapping between an action and key

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ActionName` | `FName` | Friendly name of action, e.g "jump" |
| `Key` | `FKey` | Key to bind it to. |
| `bShift` | `uint8` | true if one of the Shift keys must be down when the KeyEvent is received to be acknowledged |
| `bCtrl` | `uint8` | true if one of the Ctrl keys must be down when the KeyEvent is received to be acknowledged |
| `bAlt` | `uint8` | true if one of the Alt keys must be down when the KeyEvent is received to be acknowledged |
| `bCmd` | `uint8` | true if one of the Cmd keys must be down when the KeyEvent is received to be acknowledged |
| `KeySeq` | `uint8` | key sequence number: 0 for Primary key, 1 for Backup key |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInputAxisConfigEntry.json -->

# FInputAxisConfigEntry

Configurable properties for control axes.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AxisKeyName` | `FName` | Axis Key these properties apply to |
| `AxisProperties` | `FInputAxisProperties` | Properties for the Axis Key |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInputAxisKeyMapping.json -->

# FInputAxisKeyMapping

Defines a mapping between an axis and key

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AxisName` | `FName` | Friendly name of axis, e.g "MoveForward" |
| `Key` | `FKey` | Key to bind it to. |
| `Scale` | `float` | Multiplier to use for the mapping when accumulating the axis value |
| `KeySeq` | `uint8` | key sequence number: 0 for Primary key, 1 for Backup key |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInputAxisProperties.json -->

# FInputAxisProperties

Configurable properties for control axes, used to transform raw input into game ready values.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DeadZone` | `float` | What the dead zone of the axis is.  For control axes such as analog sticks. |
| `Sensitivity` | `float` | Scaling factor to multiply raw value by. |
| `Exponent` | `float` | For applying curves to [0..1] axes, e.g. analog sticks |
| `bInvert` | `uint8` | Inverts reported values for this axis |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInputBindingInfo.json -->

# FInputBindingInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FunctionName` | `FName` | - |
| `bConsumeInput` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInputBlendPose.json -->

# FInputBlendPose

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BranchFilters` | `TArray < FBranchFilter >` | Bone Name to filter |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInputChord.json -->

# FInputChord

An Input Chord is a key and the modifier keys that are to be held with it.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bShift` | `uint32` | Whether the shift key is part of the chord. |
| `Key` | `FKey` | The Key is the core of the chord. |
| `bCtrl` | `uint32` | Whether the control key is part of the chord. |
| `bAlt` | `uint32` | Whether the alt key is part of the chord. |
| `bCmd` | `uint32` | Whether the command key is part of the chord. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInputScaleBias.json -->

# FInputScaleBias

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Scale` | `float` | - |
| `Bias` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInputTouchCacheData.json -->

# FInputTouchCacheData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ITCDHandle` | `int32` | - |
| `ITCDType` | `int32` | - |
| `ITCDTouchLocation` | `FVector2D` | - |
| `ITCDTouchpadIndex` | `int32` | - |
| `ITCDforce` | `float` | - |
| `ITCDTimeStamp` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInstancedStaticMeshInstanceData.json -->

# FInstancedStaticMeshInstanceData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Transform` | `FMatrix` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInstancedWidget3DInstanceData.json -->

# FInstancedWidget3DInstanceData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Transform` | `FMatrix` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInstanceRecoverData.json -->

# FInstanceRecoverData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InstanceRenderDataMap` | `TMap < int32 , FInstancedStaticMeshInstanceDataWithLightmap >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInstanceRun.json -->

# FInstanceRun

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BeginIdx` | `int32` | - |
| `Num` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInstanceVisibilityData.json -->

# FInstanceVisibilityData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PVSHandlerID` | `int32` | - |
| `InsVisibilityID` | `int32` | - |
| `bAllowOverride` | `bool` | - |
| `OverrideTo` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInt32Interval.json -->

# FInt32Interval

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Min` | `int32` | - |
| `Max` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInt32Range.json -->

# FInt32Range

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LowerBound` | `FInt32RangeBound` | - |
| `UpperBound` | `FInt32RangeBound` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInt32RangeBound.json -->

# FInt32RangeBound

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Type` | `TEnumAsByte < ERangeBoundTypes :: Type >` | - |
| `Value` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FIntegralCurve.json -->

# FIntegralCurve

An integral curve, which holds the key time and the key value

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Keys` | `TArray < FIntegralKey >` | The keys, ordered by time |
| `DefaultValue` | `int32` | Default value |
| `bUseDefaultValueBeforeFirstKey` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FIntegralKey.json -->

# FIntegralKey

An integral key, which holds the key time and the key value

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Time` | `float` | The keyed time |
| `Value` | `int32` | The keyed integral value |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInteriorSettings.json -->

# FInteriorSettings

Struct encapsulating settings for interior areas.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bIsWorldSettings` | `uint32` | - |
| `ExteriorVolume` | `float` | - |
| `ExteriorTime` | `float` | - |
| `ExteriorLPF` | `float` | - |
| `ExteriorLPFTime` | `float` | - |
| `InteriorVolume` | `float` | - |
| `InteriorTime` | `float` | - |
| `InteriorLPF` | `float` | - |
| `InteriorLPFTime` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInterpControlPoint.json -->

# FInterpControlPoint

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PositionControlPoint` | `FVector` | - |
| `bPositionIsRelative` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInterpCurveFloat.json -->

# FInterpCurveFloat

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Points` | `TArray < FInterpCurvePointFloat >` | - |
| `bIsLooped` | `bool` | - |
| `LoopKeyOffset` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInterpCurveLinearColor.json -->

# FInterpCurveLinearColor

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Points` | `TArray < FInterpCurvePointLinearColor >` | - |
| `bIsLooped` | `bool` | - |
| `LoopKeyOffset` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInterpCurvePointFloat.json -->

# FInterpCurvePointFloat

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InVal` | `float` | - |
| `OutVal` | `float` | - |
| `ArriveTangent` | `float` | - |
| `LeaveTangent` | `float` | - |
| `InterpMode` | `TEnumAsByte < enum EInterpCurveMode >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInterpCurvePointLinearColor.json -->

# FInterpCurvePointLinearColor

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InVal` | `float` | - |
| `OutVal` | `FLinearColor` | - |
| `ArriveTangent` | `FLinearColor` | - |
| `LeaveTangent` | `FLinearColor` | - |
| `InterpMode` | `TEnumAsByte < enum EInterpCurveMode >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInterpCurvePointQuat.json -->

# FInterpCurvePointQuat

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InVal` | `float` | - |
| `OutVal` | `FQuat` | - |
| `ArriveTangent` | `FQuat` | - |
| `LeaveTangent` | `FQuat` | - |
| `InterpMode` | `TEnumAsByte < enum EInterpCurveMode >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInterpCurvePointTwoVectors.json -->

# FInterpCurvePointTwoVectors

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InVal` | `float` | - |
| `OutVal` | `FTwoVectors` | - |
| `ArriveTangent` | `FTwoVectors` | - |
| `LeaveTangent` | `FTwoVectors` | - |
| `InterpMode` | `TEnumAsByte < enum EInterpCurveMode >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInterpCurvePointVector.json -->

# FInterpCurvePointVector

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InVal` | `float` | - |
| `OutVal` | `FVector` | - |
| `ArriveTangent` | `FVector` | - |
| `LeaveTangent` | `FVector` | - |
| `InterpMode` | `TEnumAsByte < enum EInterpCurveMode >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInterpCurvePointVector2D.json -->

# FInterpCurvePointVector2D

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InVal` | `float` | - |
| `OutVal` | `FVector2D` | - |
| `ArriveTangent` | `FVector2D` | - |
| `LeaveTangent` | `FVector2D` | - |
| `InterpMode` | `TEnumAsByte < enum EInterpCurveMode >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInterpCurveQuat.json -->

# FInterpCurveQuat

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Points` | `TArray < FInterpCurvePointQuat >` | - |
| `bIsLooped` | `bool` | - |
| `LoopKeyOffset` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInterpCurveTwoVectors.json -->

# FInterpCurveTwoVectors

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Points` | `TArray < FInterpCurvePointTwoVectors >` | - |
| `bIsLooped` | `bool` | - |
| `LoopKeyOffset` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInterpCurveVector.json -->

# FInterpCurveVector

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Points` | `TArray < FInterpCurvePointVector >` | - |
| `bIsLooped` | `bool` | - |
| `LoopKeyOffset` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInterpCurveVector2D.json -->

# FInterpCurveVector2D

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Points` | `TArray < FInterpCurvePointVector2D >` | - |
| `bIsLooped` | `bool` | - |
| `LoopKeyOffset` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInterpEdSelKey.json -->

# FInterpEdSelKey

A group, associated with a particular  AActor  or set of Actors, which contains a set of InterpTracks for interpolating 
  properties of the  AActor  over time.
  The Outer of an UInterpGroup is an InterpData.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Group` | `UInterpGroup *` | - |
| `Track` | `UInterpTrack *` | - |
| `KeyIndex` | `int32` | - |
| `UnsnappedPosition` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInterpGroupActorInfo.json -->

# FInterpGroupActorInfo

A group and all the actors controlled by the group

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ObjectName` | `FName` | - |
| `Actors` | `TArray < AActor * >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInterpLookupPoint.json -->

# FInterpLookupPoint

Array of group names to retrieve position and rotation data from instead of using the data stored in the keyframe.
  A value of NAME_None means to use the PosTrack and EulerTrack data for the keyframe.
  There needs to be the same amount of elements in this array as there are keyframes.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GroupName` | `FName` | - |
| `Time` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInterpLookupTrack.json -->

# FInterpLookupTrack

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Points` | `TArray < struct FInterpLookupPoint >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FInterpolationParameter.json -->

# FInterpolationParameter

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InterpolationTime` | `float` | Interpolation Time for input, when it gets input, it will use this time to interpolate to target, used for smoother interpolation. |
| `InterpolationType` | `TEnumAsByte < EFilterInterpolationType >` | Type of interpolation used for filtering the input value to decide how to get to target. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FIntMargin.json -->

# FIntMargin

Describes the space around a 2D area on an integer grid.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Left` | `int32` | Holds the margin to the left. |
| `Top` | `int32` | Holds the margin to the top. |
| `Right` | `int32` | Holds the margin to the right. |
| `Bottom` | `int32` | Holds the margin to the bottom. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FIntPoint.json -->

# FIntPoint

Screen coordinates.
  The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\IntPoint.h

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `X` | `int32` | - |
| `Y` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FIntVector.json -->

# FIntVector

An integer vector in 3D space.
  The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\IntVector.h

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `X` | `int32` | - |
| `Y` | `int32` | - |
| `Z` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FItemDefineID.json -->

# FItemDefineID

物品DefineID

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Type` | `int32` | 物品类型 |
| `TypeSpecificID` | `int32` | 物品ID |
| `bValidItem` | `bool` | 是否有效道具 |
| `bValidInstance` | `bool` | 是否实体道具（已放入背包生成InstanceID） |
| `InstanceID` | `uint64` | 实例ID |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FItemOperationInfoV2.json -->

# FItemOperationInfoV2

V2背包操作事件信息

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefineID` | `FItemDefineID` | 触发操作的物品 DefineID |
| `ItemOperationType` | `EItemOperationTypeV2` | 触发的操作类型<br>	  <br>	  (SwapEquip 类型的操作将触发2次事件，分别对应两个物品) |
| `CommonReason` | `uint8` | 触发操作时物品携带的通用 Reason |
| `Count` | `int32` | 被操作的物品数量<br>	  添加、丢弃、移除时表示对应的数量<br>	  其它操作 Count 数量为 1 |
| `TargetDefineID` | `FItemDefineID` | Attach: 附加的物品 DefineID<br>	  Detach: 解除附加的物品 DefineID<br>	  SwapEquip: 与此物品交换的物品 DefineID<br>	  <br>	  其它操作类型此变量无意义 |
| `TargetSlot` | `FName` | Equip: 装备的目标槽位<br>	  UnEquip: 从哪个槽位卸下<br>	  Attach: 附加物品的槽位<br>	  Detach: 解除附加物品的槽位<br>	  SwapEquip: 交换装备后物品的新槽位<br>	  <br>	  其它操作类型此变量无意义 |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FJsonHaptic.json -->

# FJsonHaptic

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `JsonValue` | `FString` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FJsonObjectWrapper.json -->

# FJsonObjectWrapper

UStruct that holds a JsonObject, can be used by structs passed to JsonObjectConverter to pass through JsonObjects directly

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `JsonString` | `FString` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FKAggregateGeom.json -->

# FKAggregateGeom

Container for an aggregate of collision shapes

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SphereElems` | `TArray < FKSphereElem >` | - |
| `BoxElems` | `TArray < FKBoxElem >` | - |
| `SphylElems` | `TArray < FKSphylElem >` | - |
| `ConvexElems` | `TArray < FKConvexElem >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FKBoxElem.json -->

# FKBoxElem

Box shape used for collision

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TM_DEPRECATED` | `FMatrix` | - |
| `Orientation_DEPRECATED` | `FQuat` | - |
| `Center` | `FVector` | Position of the box's origin |
| `Rotation` | `FRotator` | Rotation of the box |
| `X` | `float` | Extent of the box along the y-axis |
| `Y` | `float` | Extent of the box along the y-axis |
| `Z` | `float` | Extent of the box along the z-axis |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FKConvexElem.json -->

# FKConvexElem

One convex hull, used for simplified collision.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VertexData` | `TArray < FVector >` | Array of indices that make up the convex hull. |
| `ElemBox` | `FBox` | Bounding box of this convex hull. |
| `Transform` | `FTransform` | Transform of this element |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FKeyBind.json -->

# FKeyBind

Struct containing mappings for legacy method of binding keys to exec commands.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Key` | `FKey` | The key to be bound to the command |
| `Command` | `FString` | The command to execute when the key is pressedreleased |
| `Control` | `uint8` | Whether the control key needs to be held when the key event occurs |
| `Shift` | `uint8` | Whether the shift key needs to be held when the key event occurs |
| `Alt` | `uint8` | Whether the alt key needs to be held when the key event occurs |
| `Cmd` | `uint8` | Whether the command key needs to be held when the key event occurs |
| `bIgnoreCtrl` | `uint8` | Whether the control key must not be held when the key event occurs |
| `bIgnoreShift` | `uint8` | Whether the shift key must not be held when the key event occurs |
| `bIgnoreAlt` | `uint8` | Whether the alt key must not be held when the key event occurs |
| `bIgnoreCmd` | `uint8` | Whether the command key must not be held when the key event occurs |
| `bDisabled` | `uint8` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FKSphereElem.json -->

# FKSphereElem

Sphere shape used for collision

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TM_DEPRECATED` | `FMatrix` | - |
| `Center` | `FVector` | Position of the sphere's origin |
| `Radius` | `float` | Radius of the sphere |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FKSphylElem.json -->

# FKSphylElem

Capsule shape used for collision. Z axis is capsule axis.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TM_DEPRECATED` | `FMatrix` | - |
| `Orientation_DEPRECATED` | `FQuat` | - |
| `Center` | `FVector` | Position of the capsule's origin |
| `Rotation` | `FRotator` | Rotation of the capsule |
| `Radius` | `float` | Radius of the capsule |
| `Length` | `float` | This is of line-segment ie. add Radius to both ends to find total length. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLandscapeColorMask.json -->

# FLandscapeColorMask

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ColorMaskName` | `FString` | - |
| `ColorMaskLayerList` | `TArray < FLandscapeColorMaskLayer >` | - |
| `LayerIndexUsed` | `TArray < bool >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLandscapeColorMaskLayer.json -->

# FLandscapeColorMaskLayer

Structure storing Color Mask Layer names

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ColorMaskName` | `FString` | - |
| `LayerName` | `FString` | - |
| `bVisibility` | `bool` | - |
| `LayerIndex` | `int` | - |
| `bLockStatus` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLandscapeCustomWeightAllocation.json -->

# FLandscapeCustomWeightAllocation

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ChannelName` | `FName` | - |
| `ToolTips` | `FString` | - |
| `ChannelThumbnail` | `UTexture2D *` | - |
| `bIsColorChannel` | `bool` | - |
| `ChannelIndex` | `int32` | - |
| `ChannelCount` | `int32` | - |
| `TextureIndex` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLandscapeEditorLayerSettings.json -->

# FLandscapeEditorLayerSettings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LayerInfoObj` | `ULandscapeLayerInfoObject *` | - |
| `ReimportLayerFilePath` | `FString` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLandscapeEditToolRenderData.json -->

# FLandscapeEditToolRenderData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ToolMaterial` | `UMaterialInterface *` | - |
| `GizmoMaterial` | `UMaterialInterface *` | - |
| `SelectedType` | `int32` | - |
| `DebugChannelR` | `int32` | - |
| `DebugChannelG` | `int32` | - |
| `DebugChannelB` | `int32` | - |
| `DebugChannelA` | `int32` | - |
| `DataTexture` | `UTexture2D *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLandscapeImportLayerInfo.json -->

# FLandscapeImportLayerInfo

Structure storing Layer Data for import

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LayerName` | `FName` | - |
| `LayerInfo` | `ULandscapeLayerInfoObject *` | - |
| `SourceFilePath` | `FString` | - |
| `LayerData` | `TArray < uint8 >` | - |
| `BiomesInfo` | `ULandscapeBiomesInfoObject *` | - |
| `SplatmapIndex` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLandscapeInfoLayerSettings.json -->

# FLandscapeInfoLayerSettings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LayerInfoObj` | `ULandscapeLayerInfoObject *` | - |
| `LayerInfoObj_ForPC` | `ULandscapeLayerInfoObject *` | - |
| `LayerName` | `FName` | - |
| `BiomesInfoObj` | `ULandscapeBiomesInfoObject *` | - |
| `ThumbnailMIC` | `UMaterialInstanceConstant *` | - |
| `Owner` | `ALandscapeProxy *` | - |
| `DebugColorChannel` | `int32` | - |
| `bValid` | `uint32` | - |
| `bUseForPC` | `uint32` | - |
| `bUseForOrigin` | `uint32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLandscapeLayerStruct.json -->

# FLandscapeLayerStruct

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LayerInfoObj` | `ULandscapeLayerInfoObject *` | - |
| `ThumbnailMIC` | `ULandscapeMaterialInstanceConstant *` | - |
| `Owner` | `ALandscapeProxy *` | - |
| `DebugColorChannel` | `int32` | - |
| `bSelected` | `uint32` | - |
| `SourceFilePath` | `FString` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLandscapeSplineConnection.json -->

# FLandscapeSplineConnection

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Segment` | `ULandscapeSplineSegment *` | - |
| `End` | `uint32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLandscapeSplineInterpPoint.json -->

# FLandscapeSplineInterpPoint

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Center` | `FVector` | Center Point |
| `Left` | `FVector` | Left Point |
| `Right` | `FVector` | Right Point |
| `FalloffLeft` | `FVector` | Left Falloff Point |
| `FalloffRight` | `FVector` | Right FalloffPoint |
| `StartEndFalloff` | `float` | StartEnd Falloff fraction |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLandscapeSplineMeshEntry.json -->

# FLandscapeSplineMeshEntry

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Mesh` | `UStaticMesh *` | Mesh to use on the spline |
| `MaterialOverrides` | `TArray < UMaterialInterface * >` | Overrides mesh's materials |
| `bCenterH` | `uint32` | Whether to automatically center the mesh horizontally on the spline |
| `CenterAdjust` | `FVector2D` | Tweak to center the mesh correctly on the spline |
| `bScaleToWidth` | `uint32` | Whether to scale the mesh to fit the width of the spline |
| `Scale` | `FVector` | Scale of the spline mesh, (Z=Forwards) |
| `Orientation_DEPRECATED` | `TEnumAsByte < LandscapeSplineMeshOrientation >` | Orientation of the spline mesh, X=Up or Y=Up |
| `ForwardAxis` | `TEnumAsByte < ESplineMeshAxis :: Type >` | Chooses the forward axis for the spline mesh orientation |
| `UpAxis` | `TEnumAsByte < ESplineMeshAxis :: Type >` | Chooses the up axis for the spline mesh orientation |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLandscapeSplineSegmentConnection.json -->

# FLandscapeSplineSegmentConnection

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ControlPoint` | `ULandscapeSplineControlPoint *` | - |
| `TangentLen` | `float` | - |
| `SocketName` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLandscapeWeightmapUsage.json -->

# FLandscapeWeightmapUsage

Structure storing channel usage for weightmap textures

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ChannelUsage` | `ULandscapeComponent *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLatentActionInfo.json -->

# FLatentActionInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Linkage` | `int32` | The resume point within the function to execute |
| `UUID` | `int32` | the UUID for this action |
| `ExecutionFunction` | `FName` | The function to execute. |
| `CallbackTarget` | `UObject *` | Object to execute the function on. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLaunchOnTestSettings.json -->

# FLaunchOnTestSettings

Holds settings for the editor Launch On With Map Iterations test.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LaunchOnTestmap` | `FFilePath` | Map to be used for the Launch On test |
| `DeviceID` | `FString` | Device to be used |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLayerActorStats.json -->

# FLayerActorStats

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Type` | `UClass *` | A Type of Actor currently associated with the Layer |
| `Total` | `int32` | The total number of Actors of Type assigned to the Layer |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLayerBlendInput.json -->

# FLayerBlendInput

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LayerName` | `FName` | - |
| `BlendType` | `TEnumAsByte < ELandscapeLayerBlendType >` | - |
| `LayerInput` | `FExpressionInput` | - |
| `HeightInput` | `FExpressionInput` | - |
| `PreviewWeight` | `float` | - |
| `ConstLayerInput` | `FVector` | only used if LayerInput is not hooked up |
| `ConstHeightInput` | `float` | only used if HeightInput is not hooked up |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLensBloomSettings.json -->

# FLensBloomSettings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GaussianSum` | `FGaussianSumBloomSettings` | Bloom gaussian sum method specific settings. |
| `Convolution` | `FConvolutionBloomSettings` | Bloom convolution method specific settings. |
| `Method` | `TEnumAsByte < enum EBloomMethod >` | Bloom algorithm |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLensImperfectionSettings.json -->

# FLensImperfectionSettings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DirtMask` | `UTexture *` | Texture that defines the dirt on the camera lens where the light of very bright objects is scattered. |
| `DirtMaskIntensity` | `float` | BloomDirtMask intensity |
| `DirtMaskTint` | `FLinearColor` | BloomDirtMask tint color |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLensSettings.json -->

# FLensSettings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Bloom` | `FLensBloomSettings` | - |
| `Imperfections` | `FLensImperfectionSettings` | - |
| `ChromaticAberration` | `float` | in percent, Scene chromatic aberration  color fringe (camera imperfection) to simulate an artifact that happens in real-world lens, mostly visible in the image corners. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLevelBlockFoliageDstLocation.json -->

# FLevelBlockFoliageDstLocation

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FoliageDstLocations` | `TMap < int32 , FVector >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLevelBlockFoliageInfo.json -->

# FLevelBlockFoliageInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FoliageLocations` | `TArray < FVector >` | - |
| `LandscapeHeight` | `TArray < float >` | - |
| `Indices` | `TArray < int32 >` | - |
| `DstLocationHeightDiffs` | `TMap < int32 , float >` | - |
| `DstLocations` | `TMap < int32 , FVector >` | - |
| `CulledInstanceIndices` | `TArray < int32 >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLevelCollection.json -->

# FLevelCollection

Contains a group of levels of a particular ELevelCollectionType within a UWorld
  and the context required to properly tickupdate those levels. This object is move-only.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GameState` | `AGameStateBase *` | The GameState associated with this collection. This may be different than the UWorld's GameState<br>	  since the source collection and the duplicated collection will have their own instances. |
| `NetDriver` | `UNetDriver *` | The network driver associated with this collection.<br>	  The source collection and the duplicated collection will have their own instances. |
| `DemoNetDriver` | `UDemoNetDriver *` | The demo network driver associated with this collection.<br>	  The source collection and the duplicated collection will have their own instances. |
| `MDNetDriverServer` | `UNetDriver *` | The md network driver associated with this collection.<br>	  The source collection and the duplicated collection will have their own instances. |
| `MDNetDriverClient` | `UNetDriver *` | - |
| `PersistentLevel` | `ULevel *` | The persistent level associated with this collection.<br>	  The source collection and the duplicated collection will have their own instances. |
| `Levels` | `TSet < ULevel * >` | All the levels in this collection. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLevelIndexVisibilityInfo.json -->

# FLevelIndexVisibilityInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Visible` | `bool` | - |
| `MappingIndex` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLevelNameAndTime.json -->

# FLevelNameAndTime

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LevelName` | `FString` | - |
| `LevelChangeTimeInMS` | `uint32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLevelSequenceBindingReference.json -->

# FLevelSequenceBindingReference

An external reference to an level sequence object, resolvable through an arbitrary context.
  
  Bindings consist of an optional package name, and the path to the object within that package.
  Where package name is empty, the reference is a relative path from a specific outer (the context).
  Currently, the package name should only ever be empty for component references, which must remain relative bindings to work correctly with spawnables and reinstanced actors.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PackageName_DEPRECATED` | `FString` | Replaced by ExternalObjectPath |
| `ExternalObjectPath` | `FSoftObjectPath` | Path to a specific actorcomponent inside an external package |
| `ObjectPath` | `FString` | Object path relative to a passed in context object, this is used if ExternalObjectPath is invalid |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLevelSequenceBindingReferenceArray.json -->

# FLevelSequenceBindingReferenceArray

An array of binding references

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `References` | `TArray < FLevelSequenceBindingReference >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLevelSequenceBindingReferences.json -->

# FLevelSequenceBindingReferences

Structure that stores a one to many mapping from object binding ID, to object references that pertain to that ID.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BindingIdToReferences` | `TMap < FGuid , FLevelSequenceBindingReferenceArray >` | The map from object binding ID to an array of references that pertain to that ID |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLevelSequenceObject.json -->

# FLevelSequenceObject

Structure for animated Actor objects.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ObjectOrOwner` | `TLazyObjectPtr < UObject >` | The object or the owner of the object being possessed. |
| `ComponentName` | `FString` | Optional name of an ActorComponent. |
| `CachedComponent` | `TWeakObjectPtr < UObject >` | Cached pointer to the Actor component (only if ComponentName is set). |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLevelSequencePlayerSnapshot.json -->

# FLevelSequencePlayerSnapshot

Frame snapshot information for a level sequence

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MasterName` | `FText` | - |
| `MasterTime` | `float` | - |
| `CurrentShotName` | `FText` | - |
| `CurrentShotLocalTime` | `float` | - |
| `CameraComponent` | `UCameraComponent *` | - |
| `Settings` | `FLevelSequenceSnapshotSettings` | - |
| `ShotID` | `FMovieSceneSequenceID` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLevelSequenceSnapshotSettings.json -->

# FLevelSequenceSnapshotSettings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ZeroPadAmount` | `uint8` | Zero pad frames |
| `FrameRate` | `float` | Playback framerate |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLevelSimplificationDetails.json -->

# FLevelSimplificationDetails

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bCreatePackagePerAsset` | `bool` | Whether to create separate packages for each generated asset. All in map package otherwise |
| `DetailsPercentage` | `float` | Percentage of details for static mesh proxy |
| `StaticMeshMaterialSettings` | `FMaterialProxySettings` | Landscape material simplification |
| `bOverrideLandscapeExportLOD` | `bool` | - |
| `LandscapeExportLOD` | `int32` | Landscape LOD to use for static mesh generation, when not specified 'Max LODLevel' from landscape actor will be used |
| `LandscapeMaterialSettings` | `FMaterialProxySettings` | Landscape material simplification |
| `bBakeFoliageToLandscape` | `bool` | Whether to bake foliage into landscape static mesh texture |
| `bBakeGrassToLandscape` | `bool` | Whether to bake grass into landscape static mesh texture |
| `bGenerateMeshNormalMap_DEPRECATED` | `bool` | - |
| `bGenerateMeshMetallicMap_DEPRECATED` | `bool` | - |
| `bGenerateMeshRoughnessMap_DEPRECATED` | `bool` | - |
| `bGenerateMeshSpecularMap_DEPRECATED` | `bool` | - |
| `bGenerateLandscapeNormalMap_DEPRECATED` | `bool` | - |
| `bGenerateLandscapeMetallicMap_DEPRECATED` | `bool` | - |
| `bGenerateLandscapeRoughnessMap_DEPRECATED` | `bool` | - |
| `bGenerateLandscapeSpecularMap_DEPRECATED` | `bool` | - |
| `bUseLandscapeCulling` | `bool` | Whether or not to use available landscape geometry to cull away invisible triangles |
| `LandscapeCullingPrecision` | `TEnumAsByte < ELandscapeCullingPrecision :: Type >` | Level of detail of the landscape that should be used for the culling |
| `bUseScreenSize` | `bool` | - |
| `ScreenSize` | `uint32` | - |
| `bUseTargetTriangleNumber` | `bool` | - |
| `TargetTriangleNumber` | `uint32` | - |
| `LODSelectionType` | `EMeshLODSelectionType` | - |
| `SpecificLOD` | `int32` | - |
| `UnresolvedGeometryColor` | `FColor` | Base color assigned to LOD geometry that can't be associated with the source geometry: e.g. doors and windows that have been closed by the Merge Distance |
| `bReuseMeshLightmapUVs` | `bool` | Whether to attempt to re-use the source mesh's lightmap UVs when baking the material or always generate a new set. |
| `bUseHardAngleThreshold` | `bool` | Enable the use of hard angle based vertex splitting |
| `HardAngleThreshold` | `float` | Angle at which a hard edge is introduced between faces |
| `NormalCalculationMethod` | `TEnumAsByte < EProxyNormalComputationMethod :: Type >` | Controls the method used to calculate the normal for the simplified geometry |
| `ExpectedQualityLimit` | `FExpectedQuality` | Render quality control for certain devicesplatforms, if limit > actual, primitive won't be rendered. |
| `bLodGenerateSubLevel` | `bool` | - |
| `DefaultCullScreenSize` | `float` | - |
| `bIncludeHISMMesh` | `bool` | - |
| `bHalfVoxelSize` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLevelStreamingStatus.json -->

# FLevelStreamingStatus

level streaming updates that should be applied immediately after committing the map change

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PackageName` | `FName` | - |
| `bShouldBeLoaded` | `uint32` | - |
| `bShouldBeVisible` | `uint32` | - |
| `LODIndex` | `uint32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLevelViewportInfo.json -->

# FLevelViewportInfo

Saved editor viewport state information

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CamPosition` | `FVector` | Where the camera is positioned within the viewport. |
| `CamRotation` | `FRotator` | The camera's position within the viewport. |
| `CamOrthoZoom` | `float` | The zoom value  for orthographic mode. |
| `CamUpdated` | `bool` | Whether camera settings have been systematically changed since the last level viewport update. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLevelVisibilityInfo.json -->

# FLevelVisibilityInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Visible` | `bool` | - |
| `PackageName` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLightingChannels.json -->

# FLightingChannels

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bChannel1` | `uint8` | - |
| `bChannel0` | `uint8` | Default channel for all primitives and lights. |
| `bChannel2` | `uint8` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLightmassDebugOptions.json -->

# FLightmassDebugOptions

Debug options for Lightmass

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bStatsEnabled` | `uint32` | If true, all participating Lightmass agents will report back detailed stats to the log. |
| `bDebugMode` | `uint32` | If false, UnrealLightmass.exe is launched automatically (default)<br>	 	If true, it must be launched manually (e.g. through a debugger) with the -debug command line parameter. |
| `bGatherBSPSurfacesAcrossComponents` | `uint32` | If true, BSP surfaces split across model components are joined into 1 mapping |
| `CoplanarTolerance` | `float` | The tolerance level used when gathering BSP surfaces. |
| `bUseImmediateImport` | `uint32` | If true, Lightmass will import mappings immediately as they complete.<br>	 	It will not process them, however. |
| `bImmediateProcessMappings` | `uint32` | If true, Lightmass will process appropriate mappings as they are imported.<br>	 	NOTE: Requires ImmediateMode be enabled to actually work. |
| `bSortMappings` | `uint32` | If true, Lightmass will sort mappings by texel cost. |
| `bDumpBinaryFiles` | `uint32` | If true, the generate coefficients will be dumped to binary files. |
| `bDebugMaterials` | `uint32` | If true, Lightmass will write out BMPs for each generated material property sample to \ScreenShots\Materials. |
| `bPadMappings` | `uint32` | If true, Lightmass will pad the calculated mappings to reduceeliminate seams. |
| `bDebugPaddings` | `uint32` | If true, will fill padding of mappings with a color rather than the sampled edges.<br>	 	Means nothing if bPadMappings is not enabled... |
| `bOnlyCalcDebugTexelMappings` | `uint32` | If true, only the mapping containing a debug texel will be calculated, all others<br>	  will be set to white |
| `bUseRandomColors` | `uint32` | If true, color lightmaps a random color |
| `bColorBordersGreen` | `uint32` | If true, a green border will be placed around the edges of mappings |
| `bColorByExecutionTime` | `uint32` | If true, Lightmass will overwrite lightmap data with a shade of red relating to<br>	  how long it took to calculate the mapping (Red = Time  ExecutionTimeDivisor) |
| `ExecutionTimeDivisor` | `float` | The amount of time that will be count as full red when bColorByExecutionTime is enabled |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLightmassDirectionalLightSettings.json -->

# FLightmassDirectionalLightSettings

Directional light settings for Lightmass

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LightSourceAngle` | `float` | Angle that the directional light's emissive surface extends relative to a receiver, affects penumbra sizes. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLightmassLightSettings.json -->

# FLightmassLightSettings

Per-light settings for Lightmass

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `IndirectLightingSaturation` | `float` | 0 will be completely desaturated, 1 will be unchanged |
| `ShadowExponent` | `float` | Controls the falloff of shadow penumbras |
| `bUseAreaShadowsForStationaryLight` | `bool` | Whether to use area shadows for stationary light precomputed shadowmaps.<br>	  Area shadows get softer the further they are from shadow casters, but require higher lightmap resolution to get the same quality where the shadow is sharp. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLightmassMaterialInterfaceSettings.json -->

# FLightmassMaterialInterfaceSettings

UMaterial interface settings for Lightmass

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bCastShadowAsMasked` | `uint32` | If true, forces translucency to cast static shadows as if the material were masked. |
| `EmissiveBoost` | `float` | Scales the emissive contribution of this material to static lighting. |
| `DiffuseBoost` | `float` | Scales the diffuse contribution of this material to static lighting. |
| `ExportResolutionScale` | `float` | Scales the resolution that this material's attributes were exported at.<br>	  This is useful for increasing material resolution when details are needed. |
| `bOverrideCastShadowAsMasked` | `uint32` | Boolean override flags - only used in MaterialInstance cases. <br>	 If true, override the bCastShadowAsMasked setting of the parent material. |
| `bOverrideEmissiveBoost` | `uint32` | If true, override the emissive boost setting of the parent material. |
| `bOverrideDiffuseBoost` | `uint32` | If true, override the diffuse boost setting of the parent material. |
| `bOverrideExportResolutionScale` | `uint32` | If true, override the export resolution scale setting of the parent material. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLightmassPrecomputedVisibilitySettings.json -->

# FLightmassPrecomputedVisibilitySettings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BigBuildingSize` | `float` | Too big to split into small box |
| `bQucikPVS` | `bool` | Set sample num to a small number |
| `bOnlyExternalPVS` | `bool` | Only External PVS, to reduce memory |
| `SampleNumMultiplier` | `float` | Multiplier for the number of samples rays. |
| `bUseAccurateSamplingEndPoint` | `bool` | - |
| `CellPlacementStrategy` | `ECellPlacementStrategy` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLightmassPrimitiveSettings.json -->

# FLightmassPrimitiveSettings

Per-object settings for Lightmass

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bUseTwoSidedLighting` | `uint32` | If true, this object will be lit as if it receives light from both sides of its polygons. |
| `bShadowIndirectOnly` | `uint32` | If true, this object will only shadow indirect lighting. |
| `EmissiveLightExplicitInfluenceRadius` | `float` | Direct lighting influence radius.<br>	  The default is 0, which means the influence radius should be automatically generated based on the emissive light brightness.<br>	  Values greater than 0 override the automatic method. |
| `bUseVertexNormalForHemisphereGather` | `uint32` | Typically the triangle normal is used for hemisphere gathering which prevents incorrect self-shadowing from artist-tweaked vertex normals.<br>	  However in the case of foliage whose vertex normal has been setup to match the underlying terrain, gathering in the direction of the vertex normal is desired. |
| `EmissiveLightFalloffExponent` | `float` | Direct lighting falloff exponent for mesh area lights created from emissive areas on this primitive. |
| `bUseEmissiveForStaticLighting` | `uint32` | If true, allow using the emissive for static lighting. |
| `EmissiveBoost` | `float` | Scales the emissive contribution of all materials applied to this object. |
| `DiffuseBoost` | `float` | Scales the diffuse contribution of all materials applied to this object. |
| `FullyOccludedSamplesFraction` | `float` | Fraction of samples taken that must be occluded in order to reach full occlusion. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLightmassWorldInfoSettings.json -->

# FLightmassWorldInfoSettings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StaticLightingLevelScale` | `float` | Warning: Setting this to less than 1 will greatly increase build times!<br>	  Scale of the level relative to real world scale (1 Unreal Unit = 1 cm).<br>	  All scale-dependent Lightmass setting defaults have been tweaked to work well with real world scale,<br>	  Any levels with a different scale should use this scale to compensate.<br>	  For large levels it can drastically reduce build times to set this to 2 or 4. |
| `NumIndirectLightingBounces` | `int32` | Number of light bounces to simulate for point  spot  directional lights, starting from the light source.<br>	  0 is direct lighting only, 1 is one bounce, etc.<br>	  Bounce 1 takes the most time to calculate and contributes the most to visual quality, followed by bounce 2.<br>	  Successive bounces don't really affect build times, but have a much lower visual impact, unless the material diffuse colors are close to 1. |
| `NumSkyLightingBounces` | `int32` | Number of skylight and emissive bounces to simulate.<br>	  Lightmass uses a non-distributable radiosity method for skylight bounces whose cost is proportional to the number of bounces. |
| `IndirectLightingQuality` | `float` | Warning: Setting this higher than 1 will greatly increase build times!<br>	  Can be used to increase the GI solver sample counts in order to get higher quality for levels that need it.<br>	  It can be useful to reduce IndirectLightingSmoothness somewhat (~.75) when increasing quality to get defined indirect shadows.<br>	  Note that this can't affect compression artifacts, UV seams or other texture based artifacts. |
| `IndirectLightingSmoothness` | `float` | Smoothness factor to apply to indirect lighting.  This is useful in some lighting conditions when Lightmass cannot resolve accurate indirect lighting.<br>	  1 is default smoothness tweaked for a variety of lighting situations.<br>	  Higher values like 3 smooth out the indirect lighting more, but at the cost of indirect shadows losing detail. |
| `EnvironmentColor` | `FColor` | Represents a constant color light surrounding the upper hemisphere of the level, like a sky.<br>	  This light source currently does not get bounced as indirect lighting and causes reflection capture brightness to be incorrect.  Prefer using a Static Skylight instead. |
| `EnvironmentIntensity` | `float` | Scales EnvironmentColor to allow independent color and brightness controls. |
| `EmissiveBoost` | `float` | Scales the emissive contribution of all materials in the scene.  Currently disabled and should be removed with mesh area lights. |
| `DiffuseBoost` | `float` | Scales the diffuse contribution of all materials in the scene. |
| `VolumeLightingMethod` | `TEnumAsByte < enum EVolumeLightingMethod >` | Technique to use for providing precomputed lighting at all positions inside the Lightmass Importance Volume |
| `VolumetricLightmapDetailCellSize` | `float` | Size of an Volumetric Lightmap voxel at the highest density (used around geometry), in world space units.<br>	  This setting has a large impact on build times and memory, use with caution.<br>	  Halving the DetailCellSize can increase memory by up to a factor of 8x. |
| `VolumetricLightmapMaximumBrickMemoryMb` | `float` | Maximum amount of memory to spend on Volumetric Lightmap Brick data.  High density bricks will be discarded until this limit is met, with bricks furthest from geometry discarded first. |
| `VolumeLightSamplePlacementScale` | `float` | Scales the distances at which volume lighting samples are placed.  Volume lighting samples are computed by Lightmass and are used for GI on movable components.<br>	  Using larger scales results in less sample memory usage and reduces Indirect Lighting Cache update times, but less accurate transitions between lighting areas. |
| `bUseVolumeLightmapStreaming` | `uint32` | - |
| `bUseAmbientOcclusion` | `uint32` | If true, AmbientOcclusion will be enabled. |
| `bGenerateAmbientOcclusionMaterialMask` | `uint32` | Whether to generate textures storing the AO computed by Lightmass.<br>	  These can be accessed through the PrecomputedAOMask material node,<br>	  Which is useful for blending between material layers on environment assets.<br>	  Be sure to set DirectIlluminationOcclusionFraction and IndirectIlluminationOcclusionFraction to 0 if you only want the PrecomputedAOMask! |
| `DirectIlluminationOcclusionFraction` | `float` | How much of the AO to apply to direct lighting. |
| `IndirectIlluminationOcclusionFraction` | `float` | How much of the AO to apply to indirect lighting. |
| `OcclusionExponent` | `float` | Higher exponents increase contrast. |
| `FullyOccludedSamplesFraction` | `float` | Fraction of samples taken that must be occluded in order to reach full occlusion. |
| `MaxOcclusionDistance` | `float` | Maximum distance for an object to cause occlusion on another object. |
| `bVisualizeMaterialDiffuse` | `uint32` | If true, override normal direct and indirect lighting with just the exported diffuse term. |
| `bVisualizeAmbientOcclusion` | `uint32` | If true, override normal direct and indirect lighting with just the AO term. |
| `bCompressLightmaps` | `uint32` | Whether to compress lightmap textures.  Disabling lightmap texture compression will reduce artifacts but increase memory and disk size by 4x.<br>	  Use caution when disabling this. |
| `bUseSimpleLightmap` | `uint32` | Whether to use simple lightmap on the mobile platform. |
| `LightmapResolutionScale` | `float` | - |
| `VolumeProbeGIBakingMethod` | `TEnumAsByte < enum EBakingVolumeProbeGIMethod >` | - |
| `bCompressLowQualityVolumeProbeGI` | `uint32` | - |
| `bUseSkyVisibility` | `uint32` | - |
| `bUseIndoorSkyVisibility` | `uint32` | - |
| `MaxSkyOcclusionDistance` | `float` | Maximum distance for sky occlusion trace. 0 = no limit (default). Only affects VolumeProbeGI baking. |
| `LandscapeLightmapResolutionScale` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLinearColor.json -->

# FLinearColor

A linear color.
  The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\Color.h

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `R` | `float` | - |
| `G` | `float` | - |
| `B` | `float` | - |
| `A` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLinearConstraint.json -->

# FLinearConstraint

Distance constraint

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Limit` | `float` | The distance allowed between between the two joint reference frames. Distance applies on all axes enabled (one axis means line, two axes implies circle, three axes implies sphere) |
| `XMotion` | `TEnumAsByte < enum ELinearConstraintMotion >` | Indicates the linear constraint applied along the X-axis. Free implies no constraint at all. Locked implies no movement along X is allowed. Limited implies the distance in the joint along all active axes must be less than the Distance provided. |
| `YMotion` | `TEnumAsByte < enum ELinearConstraintMotion >` | Indicates the linear constraint applied along the Y-axis. Free implies no constraint at all. Locked implies no movement along Y is allowed. Limited implies the distance in the joint along all active axes must be less than the Distance provided. |
| `ZMotion` | `TEnumAsByte < enum ELinearConstraintMotion >` | Indicates the linear constraint applied along theZX-axis. Free implies no constraint at all. Locked implies no movement along Z is allowed. Limited implies the distance in the joint along all active axes must be less than the Distance provided. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLinearDriveConstraint.json -->

# FLinearDriveConstraint

Linear Drive

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PositionTarget` | `FVector` | Target position the linear drive. |
| `VelocityTarget` | `FVector` | Target velocity the linear drive. |
| `XDrive` | `FConstraintDrive` | - |
| `YDrive` | `FConstraintDrive` | - |
| `ZDrive` | `FConstraintDrive` | - |
| `bEnablePositionDrive` | `uint8` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLocalizedSubtitle.json -->

# FLocalizedSubtitle

A subtitle localized to a specific language.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bMature` | `uint32` | true if this sound is considered to contain mature content. |
| `LanguageExt` | `FString` | The 3-letter language for this subtitle |
| `Subtitles` | `TArray < FSubtitleCue >` | Subtitle cues.  If empty, use SoundNodeWave's SpokenText as the subtitle.  Will often be empty,<br>	  as the contents of the subtitle is commonly identical to what is spoken. |
| `bManualWordWrap` | `uint32` | true if the subtitles have been split manually. |
| `bSingleLine` | `uint32` | true if the subtitles should be displayed one line at a time. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLocalSpacePose.json -->

# FLocalSpacePose

A pose in local space (i.e. each transform is relative to its parent)

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Transforms` | `TArray < FTransform >` | - |
| `Names` | `TArray < FName >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLocationBoneSocketInfo.json -->

# FLocationBoneSocketInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoneSocketName` | `FName` | The name of the bonesocket on the skeletal mesh |
| `Offset` | `FVector` | The offset from the bonesocket to use |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLODSoloTrack.json -->

# FLODSoloTrack

Temporary array for tracking 'solo' emitter mode.
 	Entry will be true if emitter was enabled

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SoloEnableSetting` | `TArray < uint8 >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FLODStealConfig.json -->

# FLODStealConfig

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StealerTileShortName` | `FString` | - |
| `TargetTileShortName` | `FString` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMainUILayoutData.json -->

# FMainUILayoutData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `WidgetVisibility` | `ESlateVisibility` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FManagementRule.json -->

# FManagementRule

ManagementRule逻辑规则的运行时版本

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bEnable` | `bool` | - |
| `SetResult` | `EAssetSetManagerResult` | - |
| `CheckTargetDirectories` | `FManagementRuleFStringArrayCheck` | - |
| `CheckTargetAssets` | `FManagementRuleFNameArrayCheck` | - |
| `CheckTargetAssetClassTypes` | `FManagementRuleFNameArrayCheck` | - |
| `CheckTargetAssetTags` | `FManagementRuleFNameArrayCheck` | - |
| `CheckSourcePackages` | `FManagementRuleFNameArrayCheck` | - |
| `CheckSourcePackageClassTypes` | `FManagementRuleFNameArrayCheck` | - |
| `bOnlySoftReferences` | `bool` | - |
| `CheckOrMask` | `uint8` | 控制7个检查条件之间的或与非逻辑，每一位对应一个检查条件（见EManagementRuleCheckOrMask）。<br>	  置1的位参与\|\|组合（OrGroup），置0的位参与&&组合（AndGroup）。<br>	  最终结果 = AndGroup全部为true && (OrGroup为空 \|\| OrGroup至少一个为true)。<br>	  默认值0x00，即全部&&，保持原有行为。 |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FManagementRuleBase.json -->

# FManagementRuleBase

Base structure for management rule checks

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bEnable` | `bool` | - |
| `bFlip` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FManagementRuleFNameArrayCheck.json -->

# FManagementRuleFNameArrayCheck

Structure to encapsulate a set of assetsdirectories with a flip flag

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Names` | `TSet < FName >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FManagementRuleFNameCheck.json -->

# FManagementRuleFNameCheck

ini配置使用, Structure to encapsulate a package name with a flip flag

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bEnable` | `bool` | - |
| `Name` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FManagementRuleFStringArrayCheck.json -->

# FManagementRuleFStringArrayCheck

Structure to encapsulate a set of directories with a flip flag

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Names` | `TArray < FManagementRuleFStringEntry >` | 每一行可独立指定字符串匹配方式 |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FManagementRuleFStringCheck.json -->

# FManagementRuleFStringCheck

ini配置使用，Structure to encapsulate a directory with a flip flag

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bEnable` | `bool` | - |
| `Name` | `FString` | - |
| `CompareRule` | `EStringCompareRule` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FManagementRuleFStringEntry.json -->

# FManagementRuleFStringEntry

运行时单条目录条目：每个条目自带独立的字符串匹配规则

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Name` | `FString` | - |
| `CompareRule` | `EStringCompareRule` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FManagementRuleSwitch.json -->

# FManagementRuleSwitch

ini配置使用，规则开关

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bEnable` | `bool` | - |
| `bFlip` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMargin.json -->

# FMargin

Describes the space around a Widget.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Left` | `float` | Holds the margin to the left. |
| `Top` | `float` | Holds the margin to the top. |
| `Right` | `float` | Holds the margin to the right. |
| `Bottom` | `float` | Holds the margin to the bottom. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMarkerSyncAnimPosition.json -->

# FMarkerSyncAnimPosition

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PreviousMarkerName` | `FName` | The marker we have passed |
| `NextMarkerName` | `FName` | The marker we are heading towards |
| `PositionBetweenMarkers` | `float` | Value between 0 and 1 representing where we are:<br>	0.5 we are half way between the two |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMaterialAttributesInput.json -->

# FMaterialAttributesInput

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PropertyConnectedBitmask` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMaterialBatchInfo.json -->

# FMaterialBatchInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AtlasTextures` | `TMap < ETextureType , UDynamicAtlasTexture2D * >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMaterialEditorPromotionSettings.json -->

# FMaterialEditorPromotionSettings

Holds settings for the material editor build promotion tests

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefaultMaterialAsset` | `FFilePath` | Default material asset to apply to static meshes |
| `DefaultDiffuseTexture` | `FFilePath` | Default material asset to apply to static meshes |
| `DefaultNormalTexture` | `FFilePath` | Default material asset to apply to static meshes |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMaterialFunctionInfo.json -->

# FMaterialFunctionInfo

Stores information about a function that this material references, used to know when the material needs to be recompiled.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StateId` | `FGuid` | Id that the function had when this material was last compiled. |
| `Function` | `UMaterialFunction *` | The function which this material has a dependency on. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMaterialIdLayerAllocInfo.json -->

# FMaterialIdLayerAllocInfo

Store all layers allocation of all biomes of this landscape

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaterialId` | `int32` | MaterialId of this layerInfo |
| `BiomesInfoOwner` | `ULandscapeBiomesInfoObject *` | Owner of this layer info object |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMaterialIdUserSettings.json -->

# FMaterialIdUserSettings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BiomesInfoObjectList` | `TArray < ULandscapeBiomesInfoObject * >` | List of BiomesInfoObject used by this Landscape Actor |
| `CustomWeightAllocations` | `TArray < FLandscapeCustomWeightAllocation >` | - |
| `bEditMatIDProperty` | `bool` | - |
| `bUseOneShaderMap` | `bool` | - |
| `HoleIndex` | `uint8` | - |
| `NoiseTexture` | `UTexture2D *` | Noise Texture applied when sample splatmap |
| `LandscapeCorner` | `FVector2D` | - |
| `NoiseMultiplier` | `float` | Larger the value is, larger the UVOffset will applied when sample splatmap |
| `NoiseTiling` | `FVector2D` | - |
| `NoiseLerpPercentFromEdge` | `float` | Starting percentage of lerp from Edge to center of the component, to avoid shifted UV go over the component. |
| `DiffuseArrayInfo` | `FTextureArrayInfo` | Diffuse texture array used as base color to render the landscape |
| `NormalArrayInfo` | `FTextureArrayInfo` | Normalmap texture array used as base color to render the landscape |
| `LayerInfoToAllocInfoMap` | `TMap < ULandscapeLayerInfoObject * , FMaterialIdLayerAllocInfo >` | Valid LayerInfoObject to MaterialIdAllocInfo map. |
| `MaterialIdLayerCount` | `int32` | MaterialId Layer Count, fixed with 2, align SJZ |
| `CustomWeightPaintingColor` | `FLinearColor` | - |
| `DummyLayerInfoRemap` | `TMap < FName , ULandscapeLayerInfoObject * >` | - |
| `CustomWeightConfig` | `UCustomWeightConfig *` | - |
| `FallbackLayerConfig` | `UMatIDFallbackConfig *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMaterialInput.json -->

# FMaterialInput

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OutputIndex` | `int32` | Index into Expression's outputs array that this input is connected to. |
| `InputName` | `FString` | Optional name of the input.<br>	  Note that this is the only member which is not derived from the output currently connected. |
| `Mask` | `int32` | - |
| `MaskR` | `int32` | - |
| `MaskG` | `int32` | - |
| `MaskB` | `int32` | - |
| `MaskA` | `int32` | - |
| `ExpressionName` | `FName` | Material expression name that this input is connected to, or None if not connected. Used only in cooked builds |
| `Expression` | `UMaterialExpression *` | Material expression that this input is connected to, or NULL if not connected. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMaterialInstanceBasePropertyOverrides.json -->

# FMaterialInstanceBasePropertyOverrides

Properties from the base material that can be overridden in material instances.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bOverride_OpacityMaskClipValue` | `bool` | Enables override of the opacity mask clip value. |
| `bOverride_BlendMode` | `bool` | Enables override of the blend mode. |
| `bOverride_ShadingModel` | `bool` | Enables override of the shading model. |
| `bOverride_DitheredLODTransition` | `bool` | Enables override of the dithered LOD transition property. |
| `bOverride_ForceOpaqueLevelPointIndirectLighting` | `bool` | - |
| `bOverride_CastDynamicShadowAsMasked` | `bool` | Enables override of whether to shadow using masked opacity on translucent materials. |
| `bOverride_TwoSided` | `bool` | Enables override of the two sided property. |
| `bOverride_UsedWithTranslucentGI` | `bool` | [SurfelGI - brainfkli ADD]<br>	  Indicates that the material and its instances can be affected by GI in translucent blend mode. |
| `bOverride_ShadingRate` | `bool` | Enables override of the shading rate. |
| `OpacityMaskClipValue` | `float` | If BlendMode is BLEND_Masked, the surface is not rendered where OpacityMask < OpacityMaskClipValue. |
| `BlendMode` | `TEnumAsByte < EBlendMode >` | The blend mode |
| `ShadingModel` | `TEnumAsByte < EMaterialShadingModel >` | The shading model |
| `TwoSided` | `uint32` | Indicates that the material should be rendered without backface culling and the normal should be flipped for backfaces. |
| `DitheredLODTransition` | `uint32` | Whether the material should support a dithered LOD transition when used with the foliage system. |
| `ForceOpaqueLevelPointIndirectLighting` | `uint32` | - |
| `bCastDynamicShadowAsMasked` | `uint32` | Whether the material should cast shadows as masked even though it has a translucent blend mode. |
| `bUsedWithTranslucentGI` | `uint32` | [SurfelGI - brainfkli ADD]<br>	  Indicates that the material and its instances can be affected by GI in translucent blend mode. |
| `ShadingRate` | `TEnumAsByte < EMaterialShadingRate >` | The shading rate |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMaterialParameterCollectionInfo.json -->

# FMaterialParameterCollectionInfo

Stores information about a parameter collection that this material references, used to know when the material needs to be recompiled.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StateId` | `FGuid` | Id that the collection had when this material was last compiled. |
| `ParameterCollection` | `UMaterialParameterCollection *` | The collection which this material has a dependency on. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMaterialParameterInfo.json -->

# FMaterialParameterInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Name` | `FName` | - |
| `bCanCollectedForCustomData` | `bool` | - |
| `CustomDataIndex` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMaterialProxySettings.json -->

# FMaterialProxySettings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TextureSize` | `FIntPoint` | - |
| `TextureSizingType` | `TEnumAsByte < ETextureSizingType >` | - |
| `GutterSpace` | `float` | - |
| `SamplingQuality` | `EMaterialProxySmaplingQuality` | Texture Sampling Quality for our parameterizer |
| `UVStrech` | `EUVStrech` | The max amount of uv stretch allowed |
| `bSplitProxyMaterialBasedOnType` | `bool` | Enabling this settings would split split non-opaques and opaque types |
| `bUseTangentSpace` | `bool` | - |
| `bNormalMap` | `bool` | - |
| `bMetallicMap` | `bool` | - |
| `MetallicConstant` | `float` | - |
| `bRoughnessMap` | `bool` | - |
| `RoughnessConstant` | `float` | - |
| `bSpecularMap` | `bool` | - |
| `SpecularConstant` | `float` | - |
| `bEmissiveMap` | `bool` | - |
| `bOpacityMap` | `bool` | - |
| `OpacityConstant` | `float` | - |
| `AOConstant_DEPRECATED` | `float` | - |
| `bOpacityMaskMap` | `bool` | - |
| `OpacityMaskConstant` | `float` | - |
| `bAmbientOcclusionMap` | `bool` | - |
| `AmbientOcclusionConstant` | `float` | - |
| `DiffuseTextureSize` | `FIntPoint` | - |
| `NormalTextureSize` | `FIntPoint` | - |
| `MetallicTextureSize` | `FIntPoint` | - |
| `RoughnessTextureSize` | `FIntPoint` | - |
| `SpecularTextureSize` | `FIntPoint` | - |
| `EmissiveTextureSize` | `FIntPoint` | - |
| `OpacityTextureSize` | `FIntPoint` | - |
| `OpacityMaskTextureSize` | `FIntPoint` | - |
| `AmbientOcclusionTextureSize` | `FIntPoint` | - |
| `MaterialMergeType` | `TEnumAsByte < EMaterialMergeType >` | - |
| `BlendMode` | `TEnumAsByte < EBlendMode >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMaterialQualityOverrides.json -->

# FMaterialQualityOverrides

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bEnableOverride` | `bool` | - |
| `bForceFullyRough` | `bool` | - |
| `bForceNonMetal` | `bool` | - |
| `bForceDisableLMDirectionality` | `bool` | - |
| `bForceLQReflections` | `bool` | - |
| `bHighDeviceSkipForceFullyRough` | `bool` | 仅在 ENABLE_DEVICE_LEVEL_SHADER_VARIANT 开启时生效 |
| `bHighDeviceSkipForceNonMetal` | `bool` | 仅在 ENABLE_DEVICE_LEVEL_SHADER_VARIANT 开启时生效 |
| `MobileCSMQuality` | `EMobileCSMQuality` | - |
| `MobilePointLightShadowQuality` | `EMobileCSMQuality` | - |
| `MobilePhotonShadowQuality` | `EMobileCSMQuality` | #if WITH_PHOTON_SHADOW |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMaterialRemapIndex.json -->

# FMaterialRemapIndex

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ImportVersionKey` | `uint32` | - |
| `MaterialRemap` | `TArray < int32 >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMaterialSpriteElement.json -->

# FMaterialSpriteElement

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Material` | `UMaterialInterface *` | The material that the sprite is rendered with. |
| `DistanceToOpacityCurve` | `UCurveFloat *` | A curve that maps distance on the X axis to the sprite opacity on the Y axis. |
| `bSizeIsInScreenSpace` | `uint32` | Whether the size is defined in screen-space or world-space. |
| `BaseSizeX` | `float` | The base width of the sprite, multiplied with the DistanceToSizeCurve. |
| `BaseSizeY` | `float` | The base height of the sprite, multiplied with the DistanceToSizeCurve. |
| `DistanceToSizeCurve` | `UCurveFloat *` | A curve that maps distance on the X axis to the sprite size on the Y axis. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMaterialTextureInfo.json -->

# FMaterialTextureInfo

This struct holds data about how a texture is sampled within a material.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SamplingScale` | `float` | The scale used when sampling the texture |
| `UVChannelIndex` | `int32` | The coordinate index used when sampling the texture |
| `TextureName` | `FName` | The texture name. Used for debugging and also to for quick matching of the entries. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMatIDFallbackArray.json -->

# FMatIDFallbackArray

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `IDs` | `TArray < uint8 >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMatrix.json -->

# FMatrix

A 4x4 matrix.
  The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\Matrix.h

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `XPlane` | `FPlane` | - |
| `YPlane` | `FPlane` | - |
| `ZPlane` | `FPlane` | - |
| `WPlane` | `FPlane` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMemberReference.json -->

# FMemberReference

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MemberParent` | `UObject *` | Most often the Class that this member is defined in. Could be a UPackage <br>	  if it is a native delegate signature function (declared globally). Should <br>	  be NULL if bSelfContext is true. |
| `MemberScope` | `FString` | - |
| `MemberName` | `FName` | Name of variable |
| `MemberGuid` | `FGuid` | The Guid of the variable |
| `bSelfContext` | `bool` | Whether or not this should be a "self" context |
| `bWasDeprecated` | `bool` | Whether or not this property has been deprecated |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMergedAtlasList.json -->

# FMergedAtlasList

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AtlasList` | `TMap < ETextureType , FAtlasTexList >` | - |
| `ReferenceAtlasType` | `ETextureType` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMeshBuildSettings.json -->

# FMeshBuildSettings

Settings applied when building a mesh.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bUseMikkTSpace` | `bool` | If true, degenerate triangles will be removed. |
| `bRecomputeNormals` | `bool` | If true, normals in the raw mesh are ignored and recomputed. |
| `bRecomputeTangents` | `bool` | If true, tangents in the raw mesh are ignored and recomputed. |
| `bRemoveDegenerates` | `bool` | If true, degenerate triangles will be removed. |
| `bBuildAdjacencyBuffer` | `bool` | Required for PNT tessellation but can be slow. Recommend disabling for larger meshes. |
| `bBuildReversedIndexBuffer` | `bool` | Required to optimize mesh in mirrored transform. Double index buffer size. |
| `bIgnoreTriangleOrderOptimization` | `bool` | - |
| `bUseHighPrecisionTangentBasis` | `bool` | If true, Tangents will be stored at 16 bit vs 8 bit precision. |
| `bUseFullPrecisionUVs` | `bool` | If true, UVs will be stored at full floating point precision. |
| `bGenerateLightmapUVs` | `bool` | - |
| `MinLightmapResolution` | `int32` | - |
| `SrcLightmapIndex` | `int32` | - |
| `DstLightmapIndex` | `int32` | - |
| `BuildScale_DEPRECATED` | `float` | - |
| `BuildScale3D` | `FVector` | The local scale applied when building the mesh |
| `DistanceFieldResolutionScale` | `float` | Scale to apply to the mesh when allocating the distance field volume texture.<br>	  The default scale is 1, which is assuming that the mesh will be placed unscaled in the world. |
| `bGenerateDistanceFieldAsIfTwoSided` | `bool` | Whether to generate the distance field treating every triangle hit as a front face.<br>	  When enabled prevents the distance field from being discarded due to the mesh being open, but also lowers Distance Field AO quality. |
| `DistanceFieldBias_DEPRECATED` | `float` | - |
| `DistanceFieldReplacementMesh` | `UStaticMesh *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMeshInstancingSettings.json -->

# FMeshInstancingSettings

Mesh instance-replacement settings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ActorClassToUse` | `TSubclassOf < AActor >` | The actor class to attach new instance static mesh components to |
| `InstanceReplacementThreshold` | `int32` | The number of static mesh instances needed before a mesh is replaced with an instanced version |
| `MeshReplacementMethod` | `EMeshInstancingReplacementMethod` | How to replace the original actors when instancing |
| `bSkipMeshesWithVertexColors` | `bool` | Whether to skip the conversion to an instanced static mesh for meshes with vertex colors.<br>	  Instanced static meshes do not support vertex colors per-instance, so conversion will lose<br>	  this data. |
| `bUseHLODVolumes` | `bool` | Whether split up instanced static mesh components based on their intersection with HLOD volumes |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMeshLODBiasCondition.json -->

# FMeshLODBiasCondition

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MeshLODBiasConfig` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMeshMergingSettings.json -->

# FMeshMergingSettings

Mesh merging settings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TargetLightMapResolution` | `int32` | Target lightmap resolution |
| `bGenerateLightMapUV` | `bool` | Whether to generate lightmap UVs for a merged mesh |
| `bComputedLightMapResolution` | `bool` | Whether or not the lightmap resolution should be computed by summing the lightmap resolutions for the input Mesh Components |
| `bImportVertexColors_DEPRECATED` | `bool` | Whether we should import vertex colors into merged mesh |
| `bPivotPointAtZero` | `bool` | Whether merged mesh should have pivot at world origin, or at first merged component otherwise |
| `bMergePhysicsData` | `bool` | Whether to merge physics data (collision primitives) |
| `bAssignLODGroup` | `bool` | - |
| `LODGroupIndex` | `int32` | - |
| `bMergeMaterials` | `bool` | Whether to merge source materials into one flat material, ONLY available when merging a single LOD level, see LODSelectionType |
| `MaterialSettings` | `FMaterialProxySettings` | Material simplification |
| `bBakeVertexDataToMesh` | `bool` | Whether or not vertex data such as vertex colours should be baked into the resulting mesh |
| `bUseVertexDataForBakingMaterial` | `bool` | Whether or not vertex data such as vertex colours should be used when baking out materials |
| `bUseTextureBinning` | `bool` | - |
| `bReuseMeshLightmapUVs` | `bool` | Whether to attempt to re-use the source mesh's lightmap UVs when baking the material or always generate a new set. |
| `bMergeEquivalentMaterials` | `bool` | Whether to attempt to merge materials that are deemed equivalent. This can cause artifacts in the merged mesh if world positionactor position etc. is used to determine output color. |
| `OutputUVs` | `EUVOutput` | Whether to output the specified UV channels into the merged mesh (only if the source meshes contain valid UVs for the specified channel) |
| `GutterSize` | `int32` | Whether to output the specified UV channels into the merged mesh (only if the source meshes contain valid UVs for the specified channel) <br>	 The gutter (in texels) to add to each sub-chart for our baked-out material for the top mip level |
| `bCalculateCorrectLODModel_DEPRECATED` | `bool` | - |
| `LODSelectionType` | `EMeshLODSelectionType` | - |
| `ExportSpecificLOD_DEPRECATED` | `int32` | - |
| `SpecificLOD` | `int32` | - |
| `bUseLandscapeCulling` | `bool` | Whether or not to use available landscape geometry to cull away invisible triangles |
| `bIncludeImposters` | `bool` | - |
| `bAllowDistanceField` | `bool` | Whether to allow distance field to be computed for this mesh. Disable this to save memory if the merged mesh will only be rendered in the distance. |
| `FilteredMinBoundsRadius` | `float` | - |
| `bDisableBorderSmear` | `bool` | - |
| `BorderSmearReplaceColor` | `FLinearColor` | - |
| `CustomOutputSize` | `FIntPoint` | - |
| `bExportNormalMap_DEPRECATED` | `bool` | Whether to export normal maps for material merging |
| `bExportMetallicMap_DEPRECATED` | `bool` | Whether to export metallic maps for material merging |
| `bExportRoughnessMap_DEPRECATED` | `bool` | Whether to export roughness maps for material merging |
| `bExportSpecularMap_DEPRECATED` | `bool` | Whether to export specular maps for material merging |
| `MergedMaterialAtlasResolution_DEPRECATED` | `int32` | Merged material texture atlas resolution |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMeshPerLODBiasArray.json -->

# FMeshPerLODBiasArray

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LODBiasArray` | `TArray < EMeshPerLODBiasType >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMeshProxySettings.json -->

# FMeshProxySettings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ScreenSize` | `int32` | Screen size of the resulting proxy mesh in pixels |
| `MaterialSettings` | `FMaterialProxySettings` | Material simplification |
| `TextureWidth_DEPRECATED` | `int32` | - |
| `TextureHeight_DEPRECATED` | `int32` | - |
| `bExportNormalMap_DEPRECATED` | `bool` | - |
| `bExportMetallicMap_DEPRECATED` | `bool` | - |
| `bExportRoughnessMap_DEPRECATED` | `bool` | - |
| `bExportSpecularMap_DEPRECATED` | `bool` | - |
| `bCalculateCorrectLODModel` | `bool` | Determines whether or not the correct LOD models should be calculated given the source meshes and transition size |
| `MergeDistance` | `float` | Distance at which meshes should be merged together, this can close gaps like doors and windows in distant geometry |
| `HardAngleThreshold` | `float` | Angle at which a hard edge is introduced between faces |
| `LightMapResolution` | `int32` | Lightmap resolution |
| `bComputeLightMapResolution` | `bool` | If ticked will compute the lightmap resolution by summing the dimensions for each mesh included for merging |
| `bRecalculateNormals` | `bool` | Whether Simplygon should recalculate normals, otherwise the normals channel will be sampled from the original mesh |
| `bBakeVertexData_DEPRECATED` | `bool` | - |
| `bUseLandscapeCulling` | `bool` | Whether or not to use available landscape geometry to cull away invisible triangles |
| `LandscapeCullingPrecision` | `TEnumAsByte < ELandscapeCullingPrecision :: Type >` | Level of detail of the landscape that should be used for the culling |
| `bAssignLODGroup` | `bool` | Choose whether you want to apply LODs to the generated mesh or not. |
| `LODGroupIndex` | `int32` | - |
| `bAggregateMeshes` | `bool` | - |
| `AggregatorMode` | `EChartAggregationMode` | - |
| `bUseCustomHemisphere` | `bool` | - |
| `bUseTargetTriangleNumber` | `bool` | - |
| `TargetTriangleNumber` | `int32` | - |
| `LODSelectionType` | `EMeshLODSelectionType` | - |
| `SpecificLOD` | `int32` | - |
| `bIncludeHISMMesh` | `bool` | - |
| `bHalfVoxelSize` | `bool` | - |
| `ExpectedQualityLimit` | `FExpectedQuality` | Render quality control for certain devicesplatforms, if limit > actual, primitive won't be rendered. |
| `bOverrideVoxelSize` | `uint8` | If true, Spatial Sampling Distance will not be automatically computed based on geometry and you must set it directly |
| `VoxelSize` | `float` | Override when converting multiple meshes for proxy LOD merging. Warning, large geometry with small sampling has very high memory costs |
| `UnresolvedGeometryColor` | `FColor` | Base color assigned to LOD geometry that can't be associated with the source geometry: e.g. doors and windows that have been closed by the Merge Distance |
| `bOverrideTransferDistance` | `bool` | Enable an override for material transfer distance |
| `MaxRayCastDist` | `float` | Override search distance used when discovering texture values for simplified geometry. Useful when non-zero Merge Distance setting generates new geometry in concave corners. |
| `bUseHardAngleThreshold` | `bool` | Enable the use of hard angle based vertex splitting |
| `NormalCalculationMethod` | `TEnumAsByte < EProxyNormalComputationMethod :: Type >` | Controls the method used to calculate the normal for the simplified geometry |
| `bAllowAdjacency` | `bool` | Whether to allow adjacency buffers for tessellation in the merged mesh |
| `bAllowDistanceField` | `bool` | Whether to allow distance field to be computed for this mesh. Disable this to save memory if the merged mesh will only be rendered in the distance. |
| `bReuseMeshLightmapUVs` | `bool` | Whether to attempt to re-use the source mesh's lightmap UVs when baking the material or always generate a new set. |
| `bCreateCollision` | `bool` | Whether to generate collision for the merged mesh |
| `bAllowVertexColors` | `bool` | Whether to allow vertex colors saved in the merged mesh |
| `bGenerateLightmapUVs` | `bool` | Whether to generate lightmap uvs for the merged mesh |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMeshReductionSettings.json -->

# FMeshReductionSettings

Settings used to reduce a mesh.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BaseLODModel` | `int32` | Source Index. The index into source models from which to generate the LOD from |
| `MetricToUse` | `EOptimizationMetric` | Optimize the mesh based on the following metric option |
| `PercentTriangles` | `float` | Percentage of triangles to keep. 1.0 = no reduction, 0.0 = no triangles. |
| `ScreenSize` | `float` | - |
| `MaxDeviation` | `float` | The maximum distance in object space by which the reduced mesh may deviate from the original mesh. |
| `PixelError` | `float` | The amount of error in pixels allowed for this LOD. |
| `WeldingThreshold` | `float` | Threshold in object space at which vertices are welded together. |
| `SilhouetteImportance` | `TEnumAsByte < EMeshFeatureImportance :: Type >` | Higher values minimize change to border edges. |
| `TextureImportance` | `TEnumAsByte < EMeshFeatureImportance :: Type >` | Higher values reduce texture stretching. |
| `ShadingImportance` | `TEnumAsByte < EMeshFeatureImportance :: Type >` | Higher values try to preserve normals better. |
| `VertexColorImportance` | `TEnumAsByte < EMeshFeatureImportance :: Type >` | Higher values minimize change to vertex color data. |
| `bRecalculateNormals` | `bool` | - |
| `HardAngleThreshold` | `float` | Angle at which a hard edge is introduced between faces. |
| `bActive_DEPRECATED` | `bool` | - |
| `bGenerateUniqueLightmapUVs` | `bool` | - |
| `bKeepSymmetry` | `bool` | - |
| `bVisibilityAided` | `bool` | - |
| `bCullOccluded` | `bool` | - |
| `VisibilityAggressiveness` | `TEnumAsByte < EMeshFeatureImportance :: Type >` | Higher values generates fewer samples |
| `bUseVertexWeights` | `bool` | Vertex colors are converted to weights. The weights are used<br>	- Red: Vertices will be less important |
| `bSimplifyMaterials` | `bool` | The following will create a material proxy |
| `MaterialLODSettings_DEPRECATED` | `FSimplygonMaterialLODSettings` | - |
| `MaterialProxySettings` | `FMaterialProxySettings` | Material Proxy for LODs |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMeshSectionInfo.json -->

# FMeshSectionInfo

Per-section settings.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaterialIndex` | `int32` | Index in to the Materials array on UStaticMesh. |
| `bEnableCollision` | `bool` | If true, collision is enabled for this section. |
| `bCastShadow` | `bool` | If true, this section will cast shadows. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMeshSectionInfoMap.json -->

# FMeshSectionInfoMap

Map containing per-section settings for each section of each LOD.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Map` | `TMap < uint32 , FMeshSectionInfo >` | Maps an LOD+Section to the material it should render with. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMeshShiftParam.json -->

# FMeshShiftParam

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bOverride_MeshShiftAnchorRefBone` | `bool` | - |
| `MeshShiftAnchorRefBone` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMeshSocketSelector.json -->

# FMeshSocketSelector

在Mesh上的位置

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Socket` | `FName` | Mesh上的Socket名字 |
| `Offset` | `FTransform` | 相对于Socket的偏移 |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMeshTriangle.json -->

# FMeshTriangle

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VertexInstanceID0` | `FVertexInstanceID` | First vertex instance that makes up this triangle.  Indices must be ordered counter-clockwise. |
| `VertexInstanceID1` | `FVertexInstanceID` | Second vertex instance that makes up this triangle.  Indices must be ordered counter-clockwise. |
| `VertexInstanceID2` | `FVertexInstanceID` | Third vertex instance that makes up this triangle.  Indices must be ordered counter-clockwise. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMinimalViewInfo.json -->

# FMinimalViewInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Location` | `FVector` | Location |
| `LocationLocalSpace` | `FVector` | Location In Local Space |
| `Rotation` | `FRotator` | Rotation |
| `ViewTag` | `FName` | - |
| `FOV` | `float` | The field of view (in degrees) in perspective mode (ignored in Orthographic mode) |
| `bUseFirstPersonParameters` | `uint32` | - |
| `FirstPersonFOV` | `float` | The horizontal field of view (in degrees) used for primitives tagged as "IsFirstPerson". |
| `FirstPersonScale` | `float` | The scale to apply to primitives tagged as "IsFirstPerson". This is used to scale down primitives towards the camera such that they are small enough not to intersect with the scene. |
| `FirstPersonScaleParameters` | `FVector` | - |
| `OrthoWidth` | `float` | The desired width (in world units) of the orthographic view (ignored in Perspective mode) |
| `OrthoNearClipPlane` | `float` | The near plane distance of the orthographic view (in world units) |
| `OrthoFarClipPlane` | `float` | The far plane distance of the orthographic view (in world units) |
| `AspectRatio` | `float` | - |
| `bConstrainAspectRatio` | `uint32` | - |
| `bUseFieldOfViewForLOD` | `uint32` | - |
| `ProjectionMode` | `TEnumAsByte < ECameraProjectionMode :: Type >` | - |
| `PostProcessBlendWeight` | `float` | Indicates if PostProcessSettings should be applied. |
| `PostProcessSettings` | `FPostProcessSettings` | Post-process settings to use if PostProcessBlendWeight is non-zero. |
| `OffCenterProjectionOffset` | `FVector2D` | Off-axis  off-center projection offset as proportion of screen dimensions |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FModulatorContinuousParams.json -->

# FModulatorContinuousParams

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParameterName` | `FName` | The name of the sound instance parameter that specifies the current value. |
| `Default` | `float` | The default value to be used if the parameter is not found. |
| `MinInput` | `float` | The minimum input value. Values will be clamped to the [MinInput, MaxInput] range. |
| `MaxInput` | `float` | The maximum input value. Values will be clamped to the [MinInput, MaxInput] range. |
| `MinOutput` | `float` | The minimum output value. The input value will be scaled from the range [MinInput, MaxInput] to [MinOut, MaxOutput] |
| `MaxOutput` | `float` | The maximum output value. The input value will be scaled from the range [MinInput, MaxInput] to [MinOut, MaxOutput] |
| `ParamMode` | `TEnumAsByte < enum ModulationParamMode >` | The mode with which to treat the input value |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMontageSectionsPlayInfo.json -->

# FMontageSectionsPlayInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LoopCount` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMoveAdditiveLayeringData.json -->

# FMoveAdditiveLayeringData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PerBoneBlendWeights` | `TArray < FPerBoneBlendWeight >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovementProperties.json -->

# FMovementProperties

Movement capabilities, determining available movement options for Pawns and used by AI for reachability tests.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bCanCrouch` | `uint32` | If true, this Pawn is capable of crouching. |
| `bCanJump` | `uint32` | If true, this Pawn is capable of jumping. |
| `bCanWalk` | `uint32` | If true, this Pawn is capable of walking or moving on the ground. |
| `bCanSwim` | `uint32` | If true, this Pawn is capable of swimming or moving through fluid volumes. |
| `bCanFly` | `uint32` | If true, this Pawn is capable of flying. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieScene3DLocationKeyStruct.json -->

# FMovieScene3DLocationKeyStruct

Proxy structure for translation keys in 3D transform sections.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Location` | `FVector` | The key's translation value. |
| `Time` | `float` | The key's time. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieScene3DRotationKeyStruct.json -->

# FMovieScene3DRotationKeyStruct

Proxy structure for translation keys in 3D transform sections.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Rotation` | `FRotator` | The key's rotation value. |
| `Time` | `float` | The key's time. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieScene3DScaleKeyStruct.json -->

# FMovieScene3DScaleKeyStruct

Proxy structure for translation keys in 3D transform sections.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Scale` | `FVector` | The key's scale value. |
| `Time` | `float` | The key's time. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieScene3DTransformKeyStruct.json -->

# FMovieScene3DTransformKeyStruct

Proxy structure for 3D transform section key data.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Location` | `FVector` | The key's translation value. |
| `Rotation` | `FRotator` | The key's rotation value. |
| `Scale` | `FVector` | The key's scale value. |
| `Time` | `float` | The key's time. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieScene3DTransformTemplateData.json -->

# FMovieScene3DTransformTemplateData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TranslationCurve` | `FRichCurve` | - |
| `RotationCurve` | `FRichCurve` | - |
| `ScaleCurve` | `FRichCurve` | - |
| `ManualWeight` | `FRichCurve` | - |
| `BlendType` | `EMovieSceneBlendType` | - |
| `Mask` | `FMovieSceneTransformMask` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneBinding.json -->

# FMovieSceneBinding

A set of tracks bound to runtime objects

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ObjectGuid` | `FGuid` | Object binding guid for runtime objects |
| `BindingName` | `FString` | Display name |
| `EditableDisplayName` | `FString` | EditTable Display name |
| `Tracks` | `TArray < UMovieSceneTrack * >` | All tracks in this binding |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneBindingOverrideData.json -->

# FMovieSceneBindingOverrideData

Movie scene binding override data

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ObjectBindingId` | `FMovieSceneObjectBindingID` | Specifies the object binding to override. |
| `Object` | `TWeakObjectPtr < UObject >` | Specifies the object to override the binding with. |
| `bOverridesDefault` | `bool` | Specifies whether the default assignment should remain bound (false) or if this should completely override the default binding (false). |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneCameraAnimSectionData.json -->

# FMovieSceneCameraAnimSectionData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CameraAnim` | `UCameraAnim *` | The camera anim to play |
| `PlayRate` | `float` | How fast to play back the animation. |
| `PlayScale` | `float` | Scalar to control intensity of the animation. |
| `BlendInTime` | `float` | - |
| `BlendOutTime` | `float` | - |
| `bLooping` | `bool` | - |
| `bRandomStartTime` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneCameraShakeSectionData.json -->

# FMovieSceneCameraShakeSectionData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ShakeClass` | `TSubclassOf < UCameraShake >` | Class of the camera shake to play |
| `PlayScale` | `float` | Scalar that affects shake intensity |
| `PlaySpace` | `TEnumAsByte < ECameraAnimPlaySpace :: Type >` | - |
| `UserDefinedPlaySpace` | `FRotator` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneCaptureSettings.json -->

# FMovieSceneCaptureSettings

Common movie-scene capture settings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OutputDirectory` | `FDirectoryPath` | The directory to output the captured file(s) in |
| `GameModeOverride` | `TSubclassOf < AGameModeBase >` | Optional game mode to override the map's default game mode with.  This can be useful if the game's normal mode displays UI elements or loading screens that you don't want captured. |
| `OutputFormat` | `FString` | - |
| `bOverwriteExisting` | `bool` | Whether to overwrite existing files or not |
| `bUseRelativeFrameNumbers` | `bool` | True if frame numbers in the output files should be relative to zero, rather than the actual frame numbers in the originating animation content |
| `HandleFrames` | `int32` | Number of frame handles to include for each shot |
| `ZeroPadFrameNumbers` | `uint8` | How much to zero-pad frame numbers on filenames |
| `FrameRate` | `int32` | The frame rate at which to capture |
| `BitRate` | `int32` | The bit rate at which to capture |
| `MovieLiveUrl` | `FString` | - |
| `bFixedTimeStep` | `bool` | - |
| `Resolution` | `FCaptureResolution` | The resolution at which to capture |
| `bEnableTextureStreaming` | `bool` | Whether to texture streaming should be enabled while capturing.  Turning off texture streaming may cause much more memory to be used, but also reduces the chance of blurry textures in your captured video. |
| `bCinematicEngineScalability` | `bool` | Whether to enable cinematic engine scalability settings |
| `bCinematicMode` | `bool` | Whether to enable cinematic mode whilst capturing |
| `bAllowMovement` | `bool` | Whether to allow player movement whilst capturing |
| `bAllowTurning` | `bool` | Whether to allow player rotation whilst capturing |
| `bShowPlayer` | `bool` | Whether to show the local player whilst capturing |
| `bShowHUD` | `bool` | Whether to show the in-game HUD whilst capturing |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneColorKeyStruct.json -->

# FMovieSceneColorKeyStruct

Proxy structure for color section key data.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Color` | `FLinearColor` | The key's color value. |
| `Time` | `float` | The key's time. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneComponentMaterialSectionTemplate.json -->

# FMovieSceneComponentMaterialSectionTemplate

Evaluation template for primitive component materials

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaterialIndex` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneComponentTransformSectionTemplate.json -->

# FMovieSceneComponentTransformSectionTemplate

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TemplateData` | `FMovieScene3DTransformTemplateData` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEasingSettings.json -->

# FMovieSceneEasingSettings

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AutoEaseInTime` | `float` | Automatically applied ease in time |
| `AutoEaseOutTime` | `float` | Automatically applied ease out time |
| `EaseIn` | `TScriptInterface < IMovieSceneEasingFunction >` | - |
| `bManualEaseIn` | `bool` | Whether to manually override this section's ease in time |
| `ManualEaseInTime` | `float` | Manually override this section's ease in time |
| `EaseOut` | `TScriptInterface < IMovieSceneEasingFunction >` | - |
| `bManualEaseOut` | `bool` | Whether to manually override this section's ease out time |
| `ManualEaseOutTime` | `float` | Manually override this section's ease-out time |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEditorData.json -->

# FMovieSceneEditorData

Editor only data that needs to be saved between sessions for editing but has no runtime purpose

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ExpansionStates` | `TMap < FString , FMovieSceneExpansionState >` | Map of node path -> expansion state. |
| `WorkingRange` | `FFloatRange` | User-defined working range in which the entire sequence should reside. |
| `ViewRange` | `FFloatRange` | The last view-range that the user was observing |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEvalTemplate.json -->

# FMovieSceneEvalTemplate

Structure used for movie scene evaluation templates contained within a track. Typically these are defined as one per-section.
  Serialized into a FMovieSceneEvaluationTemplate contained within the sequence itself (for fast initialization at runtime).
  Templates are executed in a 3-phase algorithm:
 		1) Initialize: (opt-in) Called at the start of the frame. Able to access mutable state from the playback context. Used to initialize any persistent state required for the evaluation pass.
 		2) Evaluate: Potentially called on a thread. Should (where possible) perform all costly evaluation logic, accumulating into execution tokens which will be executed at a later time on the game thread.
 		3) Execute: Called on all previously submitted execution tokens to apply the evaluated state to the movie scene player

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CompletionMode` | `EMovieSceneCompletionMode` | Enumeration value signifying whether we should restore any animated state stored by this entity when this eval tempalte is no longer evaluated |
| `SourceSection` | `UMovieSceneSection *` | The section from which this template originates |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEvaluationField.json -->

# FMovieSceneEvaluationField

Memory layout optimized primarily for speed of searching the applicable ranges

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Ranges` | `TArray < FFloatRange >` | Ranges stored separately for fast (cache efficient) lookup. Each index has a corresponding entry in FMovieSceneEvaluationField::Groups. |
| `Groups` | `TArray < FMovieSceneEvaluationGroup >` | Groups that store segment pointers for each of the above ranges. Each index has a corresponding entry in FMovieSceneEvaluationField::Ranges. |
| `MetaData` | `TArray < FMovieSceneEvaluationMetaData >` | Meta data that maps to entries in the 'Ranges' array. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEvaluationFieldSegmentPtr.json -->

# FMovieSceneEvaluationFieldSegmentPtr

A pointer to a particular segment of a track held within an evaluation template

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SegmentIndex` | `int32` | The index of the segment within the track (see FMovieSceneEvaluationTrack::Segments) |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEvaluationFieldTrackPtr.json -->

# FMovieSceneEvaluationFieldTrackPtr

A pointer to a track held within an evaluation template

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SequenceID` | `FMovieSceneSequenceID` | The sequence ID that identifies to which sequence the track belongs |
| `TrackIdentifier` | `FMovieSceneTrackIdentifier` | The Identifier of the track inside the track map (see FMovieSceneEvaluationTemplate::Tracks) |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEvaluationGroup.json -->

# FMovieSceneEvaluationGroup

Holds segment pointers for all segments that are active for a given range of the sequence

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LUTIndices` | `TArray < FMovieSceneEvaluationGroupLUTIndex >` | Array of indices that define all the flush groups in the range. |
| `SegmentPtrLUT` | `TArray < FMovieSceneEvaluationFieldSegmentPtr >` | A grouping of evaluation pointers that occur in this range of the sequence |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEvaluationGroupLUTIndex.json -->

# FMovieSceneEvaluationGroupLUTIndex

Lookup table index for a group of evaluation templates

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LUTOffset` | `int32` | The offset within FMovieSceneEvaluationGroup::SegmentPtrLUT that this index starts |
| `NumInitPtrs` | `int32` | The number of initialization pointers are stored after &FMovieSceneEvaluationGroup::SegmentPtrLUT[0] + LUTOffset. |
| `NumEvalPtrs` | `int32` | The number of evaluation pointers are stored after &FMovieSceneEvaluationGroup::SegmentPtrLUT[0] + LUTOffset + NumInitPtrs. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEvaluationKey.json -->

# FMovieSceneEvaluationKey

Keyable struct that represents a particular entity within an evaluation template (either a sectiontemplate or a track)

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SequenceID` | `FMovieSceneSequenceID` | ID of the sequence that the entity is contained within |
| `TrackIdentifier` | `FMovieSceneTrackIdentifier` | ID of the track this key relates to |
| `SectionIdentifier` | `uint32` | ID of the section this key relates to (or -1 where this key relates to a track) |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEvaluationMetaData.json -->

# FMovieSceneEvaluationMetaData

Informational meta-data that applies to a given time range

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ActiveSequences` | `TArray < FMovieSceneSequenceID >` | Array of sequences that are active in this time range. |
| `ActiveEntities` | `TArray < FMovieSceneOrderedEvaluationKey >` | Array of entities (tracks andor sections) that are active in this time range. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEvaluationTemplate.json -->

# FMovieSceneEvaluationTemplate

Template that is used for efficient runtime evaluation of a movie scene sequence. Potentially serialized into the asset.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Tracks` | `TMap < uint32 , FMovieSceneEvaluationTrack >` | Map of evaluation tracks from identifier to track |
| `EvaluationField` | `FMovieSceneEvaluationField` | Evaluation field for efficient runtime evaluation |
| `Hierarchy` | `FMovieSceneSequenceHierarchy` | Map of all sequences found in this template (recursively) |
| `TemplateLedger` | `FMovieSceneTemplateGenerationLedger` | - |
| `bHasLegacyTrackInstances` | `uint32` | When set, this template contains legacy track instances that require the initialization of a legacy sequence instance |
| `bKeepStaleTracks` | `uint32` | Primarily used in editor to keep stale tracks around during template regeneration to ensure we can call OnEndEvaluation on them. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEvaluationTrack.json -->

# FMovieSceneEvaluationTrack

Evaluation track that is stored within an evaluation template for a sequence.
  Contains user-defined evaluation templates, and an optional track implementation

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ObjectBindingID` | `FGuid` | ID of the possessable or spawnable within the UMovieScene this track belongs to, if any. Zero guid where this relates to a master track. |
| `EvaluationPriority` | `uint16` | Evaluation priority. Highest is evaluated first |
| `EvaluationMethod` | `EEvaluationMethod` | Evaluation method - static or swept |
| `EvaluationRunSide` | `int32` | - |
| `MinRunnableTCQuality` | `int32` | - |
| `RunTagArray` | `TArray < FString >` | - |
| `Segments` | `TArray < FMovieSceneSegment >` | Array of segmented ranges contained within the track. |
| `ChildTemplates` | `TArray < FMovieSceneEvalTemplatePtr >` | Domain-specific evaluation templates (normally 1 per section) |
| `TrackTemplate` | `FMovieSceneTrackImplementationPtr` | Domain-specific track implementation override. |
| `EvaluationGroup` | `FName` | Flush group that determines whether this track belongs to a group of tracks |
| `bEvaluateInPreroll` | `uint32` | Whether this track is evaluated in preroll |
| `bEvaluateInPostroll` | `uint32` | Whether this track is evaluated in postroll |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEvent.json -->

# FMovieSceneEvent

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Ptrs` | `FMovieSceneEventPtrs` | The function that should be called to invoke this event.<br>	 Functions must have either no parameters, or a single, pass-by-value objectinterface parameter, with no return parameter. |
| `PayloadVariables` | `TMap < FName , FMovieSceneEventPayloadVariable >` | Array of payload variables to be added to the generated function |
| `CompiledFunctionName` | `FName` | - |
| `BoundObjectPinName` | `FName` | - |
| `WeakEndpoint` | `TWeakObjectPtr < UObject >` | Serialized weak pointer to the function entry (UK2Node_FunctionEntry) or custom event node (UK2Node_CustomEvent) within the blueprint graph for this event. Stored as an editor-only UObject so UHT can parse it when building for non-editor. |
| `GraphGuid_DEPRECATED` | `FGuid` | (deprecated) The UEdGraph::GraphGuid property that relates the graph within which our endpoint lives. |
| `NodeGuid_DEPRECATED` | `FGuid` | (deprecated) When valid, relates to the The UEdGraphNode::NodeGuid for a custom event node that defines our event endpoint. When invalid, we must be bound to a UBlueprint::FunctionGraphs graph. |
| `FunctionEntry_DEPRECATED` | `TWeakObjectPtr < UObject >` | Deprecated weak pointer to the function entry to call - no longer serialized but cached on load. Predates GraphGuid and NodeGuid |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEventPayloadVariable.json -->

# FMovieSceneEventPayloadVariable

Value definition for any type-agnostic variable (exported as text)

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FString` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEventPtrs.json -->

# FMovieSceneEventPtrs

Compiled reflection pointers for the event function and parameters

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Function` | `UFunction *` | - |
| `BoundObjectProperty` | `UProperty *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEventSectionData.json -->

# FMovieSceneEventSectionData

A curve of events

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `KeyTimes` | `TArray < float >` | Sorted array of key times |
| `KeyValues` | `TArray < FEventPayload >` | Array of values that correspond to each key time |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEventWrapper.json -->

# FMovieSceneEventWrapper

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SceneEvent` | `FMovieSceneEvent` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneExpansionState.json -->

# FMovieSceneExpansionState

@todo: remove this type when support for intrinsics on TMap values is added?

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bExpanded` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneLegacyTrackInstanceTemplate.json -->

# FMovieSceneLegacyTrackInstanceTemplate

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Track` | `UMovieSceneTrack *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneObjectBindingID.json -->

# FMovieSceneObjectBindingID

Persistent identifier to a specific object binding within a sequence hierarchy.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SequenceID` | `int32` | Sequence ID stored as an int32 so that it can be used in the blueprint VM |
| `Space` | `EMovieSceneObjectBindingSpace` | The binding's resolution space |
| `Guid` | `FGuid` | Identifier for the object binding within the sequence |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneOrderedEvaluationKey.json -->

# FMovieSceneOrderedEvaluationKey

Struct that stores the key for an evaluated entity, and the index at which it was (or is to be) evaluated

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Key` | `FMovieSceneEvaluationKey` | - |
| `EvaluationIndex` | `uint32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneParameterSectionTemplate.json -->

# FMovieSceneParameterSectionTemplate

Template that performs evaluation of parameter sections

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Scalars` | `TArray < FScalarParameterNameAndCurve >` | The scalar parameter names and their associated curves. |
| `Vectors` | `TArray < FVectorParameterNameAndCurves >` | The vector parameter names and their associated curves. |
| `Colors` | `TArray < FColorParameterNameAndCurves >` | The color parameter names and their associated curves. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieScenePossessable.json -->

# FMovieScenePossessable

MovieScenePossessable is a "typed slot" used to allow the MovieScene to control an already-existing object

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Guid` | `FGuid` | Unique identifier of the possessable object. |
| `Name` | `FString` | Name label for this slot |
| `PossessedObjectClass` | `UClass *` | Type of the object we'll be possessing |
| `ParentGuid` | `FGuid` | GUID relating to this possessable's parent, if applicable. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneRootEvaluationTemplateInstance.json -->

# FMovieSceneRootEvaluationTemplateInstance

Root evaluation template instance used to play back any sequence

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DirectorInstances` | `TMap < FMovieSceneSequenceID , UObject * >` | Map of director instances by sequence ID. Kept alive by this map assuming this struct is reference collected |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneSectionEvalOptions.json -->

# FMovieSceneSectionEvalOptions

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bCanEditCompletionMode` | `bool` | - |
| `CompletionMode` | `EMovieSceneCompletionMode` | When set to "RestoreState", this section will restore any animation back to its previous state |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneSectionParameters.json -->

# FMovieSceneSectionParameters

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StartOffset` | `float` | Number of seconds to skip at the beginning of the sub-sequence. |
| `TimeScale` | `float` | Playback time scaling factor. |
| `HierarchicalBias` | `int32` | Hierachical bias. Higher bias will take precedence. |
| `PrerollTime_DEPRECATED` | `float` | - |
| `PostrollTime_DEPRECATED` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneSequenceCachedSignature.json -->

# FMovieSceneSequenceCachedSignature

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Sequence` | `TWeakObjectPtr < UMovieSceneSequence >` | - |
| `CachedSignature` | `FGuid` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneSequenceHierarchy.json -->

# FMovieSceneSequenceHierarchy

Structure that stores hierarchical information pertaining to all sequences contained within a master sequence

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SubSequences` | `TMap < uint32 , FMovieSceneSubSequenceData >` | Map of all (recursive) sub sequences found in this template, keyed on sequence ID |
| `Hierarchy` | `TMap < uint32 , FMovieSceneSequenceHierarchyNode >` | Structural information describing the structure of the sequence |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneSequenceHierarchyNode.json -->

# FMovieSceneSequenceHierarchyNode

Simple structure specifying parent and child sequence IDs for any given sequences

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParentID` | `FMovieSceneSequenceID` | Movie scene sequence ID of this node's parent sequence |
| `Children` | `TArray < FMovieSceneSequenceID >` | Array of child sequences contained within this sequence |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneSequenceID.json -->

# FMovieSceneSequenceID

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `uint32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneSequencePlaybackSettings.json -->

# FMovieSceneSequencePlaybackSettings

Settings for the level sequence player actor.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LoopCount` | `int32` | Number of times to loop playback. -1 for infinite, else the number of times to loop before stopping |
| `PlayRate` | `float` | The rate at which to playback the animation |
| `bRandomStartTime` | `bool` | Start playback at a random time |
| `StartTime` | `float` | Start playback at the specified time |
| `bRestoreState` | `bool` | Flag used to specify whether actor states should be restored on stop |
| `bDisableMovementInput` | `bool` | Disable Input from player during play |
| `bDisableLookAtInput` | `bool` | Disable LookAt Input from player during play |
| `bHidePlayer` | `bool` | Hide Player Pawn during play |
| `bHideHud` | `bool` | Hide HUD during play |
| `bEnableHDR` | `bool` | EnableHDR When Play Sequence |
| `BindingOverrides` | `TScriptInterface < IMovieSceneBindingOverridesInterface >` | Interface that defines overridden bindings for this sequence |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneSequenceTransform.json -->

# FMovieSceneSequenceTransform

Movie scene sequence transform class that transforms from one time-space to another.
 
  @note The transform can be thought of as the top row of a 2x2 matrix, where the bottom row is the identity:
  			| TimeScale	Offset	|
 			| 0			1		|
 
  As such, traditional matrix mathematics can be applied to transform between different sequence's time-spaces.
  Transforms apply offset first, then time scale.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TimeScale` | `float` | The sequence's time scale (or play rate) |
| `Offset` | `float` | Scalar time offset applied before the scale |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneSkeletalAnimation_MultipleDeviceGrade.json -->

# FMovieSceneSkeletalAnimation_MultipleDeviceGrade

For MovieSceneSkeletalAnimation MultipleDeviceGrade Feature Start

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DeviceGrade_Min` | `int32` | - |
| `DeviceGrade_Max` | `int32` | - |
| `Animation` | `UAnimSequenceBase *` | The animation this section plays |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneSkeletalAnimationParams.json -->

# FMovieSceneSkeletalAnimationParams

For MovieSceneSkeletalAnimation MultipleDeviceGrade Feature End

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Animation` | `UAnimSequenceBase *` | The animation this section plays |
| `MultipleDeviceGradeAnimList` | `TArray < FMovieSceneSkeletalAnimation_MultipleDeviceGrade >` | - |
| `StartOffset` | `float` | The offset into the beginning of the animation clip |
| `EndOffset` | `float` | The offset into the end of the animation clip |
| `PlayRate` | `float` | The playback rate of the animation clip |
| `bReverse` | `uint32` | Reverse the playback of the animation clip |
| `SlotName` | `FName` | The slot name to use for the animation |
| `Weight` | `FRichCurve` | The weight curve for this animation section |
| `BlendOutTime` | `float` | BlendOutTimeWhenStop |
| `bClearPose` | `uint32` | clear the cached pose |
| `bForceUseTPP` | `uint32` | if use TPP when player is in Newfpp |
| `bSetSequenceEvalReinitStartPosition` | `uint32` | SetSequenceEvalReinit  to StartPosition |
| `bApplySubAnim` | `uint32` | Apply Anim To SubAnim |
| `ApplyAvatarSlot` | `TArray < int32 >` | Apply Anim To Avatar |
| `DisableBoneResolve` | `TArray < int32 >` | Apply Anim To SubAnim |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneSkeletalAnimationSectionTemplate.json -->

# FMovieSceneSkeletalAnimationSectionTemplate

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Params` | `FMovieSceneSkeletalAnimationSectionTemplateParameters` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneSkeletalAnimationSectionTemplateParameters.json -->

# FMovieSceneSkeletalAnimationSectionTemplateParameters

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SectionStartTime` | `float` | - |
| `SectionEndTime` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneSpawnable.json -->

# FMovieSceneSpawnable

MovieSceneSpawnable describes an object that can be spawned for this MovieScene

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Guid` | `FGuid` | Unique identifier of the spawnable object. |
| `Name` | `FString` | Name label |
| `ObjectTemplate` | `UObject *` | - |
| `ChildPossessables` | `TArray < FGuid >` | Set of GUIDs to possessable object bindings that are bound to an object inside this spawnable |
| `Ownership` | `ESpawnOwnership` | Property indicating where ownership responsibility for this object lies |
| `GeneratedClass_DEPRECATED` | `UClass *` | Deprecated generated class |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneSpawnSectionTemplate.json -->

# FMovieSceneSpawnSectionTemplate

Spawn track eval template that evaluates a curve

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Curve` | `FIntegralCurve` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneSubSequenceData.json -->

# FMovieSceneSubSequenceData

Sub sequence data that is stored within an evaluation template as a backreference to the originating sequence, and section

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Sequence` | `UMovieSceneSequence *` | The sequence that the sub section references |
| `SequenceKeyObject` | `UObject *` | The key object that the sub section uses. Usually either the sequence or the section. |
| `RootToSequenceTransform` | `FMovieSceneSequenceTransform` | Transform that transforms a given time from the sequences outer space, to its authored space. |
| `SourceSequenceSignature` | `FGuid` | Cached signature of the evaluation template |
| `DeterministicSequenceID` | `FMovieSceneSequenceID` | This sequence's deterministic sequence ID. Used in editor to reduce the risk of collisions on recompilation |
| `PreRollRange` | `FFloatRange` | The sequence preroll range considering the start offset |
| `PostRollRange` | `FFloatRange` | The sequence postroll range considering the start offset |
| `HierarchicalBias` | `int32` | The accumulated hierarchical bias of this sequence. Higher bias will take precedence |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneSubtitleParams.json -->

# FMovieSceneSubtitleParams

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SubTitleText` | `FText` | BlendOutTimeWhenStop |
| `Tags` | `TArray < FMovieSceneSubtitleTagsKeyValue >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneSubtitleTagsKeyValue.json -->

# FMovieSceneSubtitleTagsKeyValue

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Key` | `ESubtitleKeyType` | BlendOutTimeWhenStop |
| `Animation` | `ESubtitleKeyAnimationType` | - |
| `Anchor` | `ESubtitleKeyAnchorType` | - |
| `RichText` | `ESubtitleRichTextType` | - |
| `CustomUI` | `FSoftObjectPath` | - |
| `BackGround` | `UTexture2D *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneTemplateGenerationLedger.json -->

# FMovieSceneTemplateGenerationLedger

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LastTrackIdentifier` | `FMovieSceneTrackIdentifier` | - |
| `TrackReferenceCounts` | `TMap < FMovieSceneTrackIdentifier , int32 >` | Map of track identifiers to number of references within th template (generally 1, maybe >1 for shared tracks) |
| `TrackSignatureToTrackIdentifier` | `TMap < FGuid , FMovieSceneTrackIdentifiers >` | Map of track signature to array of track identifiers that it created |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneTrackCompilationParams.json -->

# FMovieSceneTrackCompilationParams

Movie scene compilation parameters. Serialized items contribute to a compiled template's cached hash

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bForEditorPreview` | `bool` | Whether we're generating for an editor preview, or for efficient runtime evaluation |
| `bDuringBlueprintCompile` | `bool` | Whether we're generating during a blueprint compile. As such, UObject types may not have been fully loaded. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneTrackEvalOptions.json -->

# FMovieSceneTrackEvalOptions

Generic evaluation options for any track

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bCanEvaluateNearestSection` | `uint32` | true when the value of bEvalNearestSection is to be considered for the track |
| `bEvalNearestSection` | `uint32` | When evaluating empty space on a track, will evaluate the last position of the previous section (if possible), or the first position of the next section, in that order of preference. |
| `bEvaluateInPreroll` | `uint32` | Evaluate this track as part of its parent sub-section's pre-roll, if applicable |
| `bEvaluateInPostroll` | `uint32` | Evaluate this track as part of its parent sub-section's post-roll, if applicable |
| `bEvaluateNearestSection_DEPRECATED` | `uint32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneTrackIdentifier.json -->

# FMovieSceneTrackIdentifier

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `uint32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneTrackIdentifiers.json -->

# FMovieSceneTrackIdentifiers

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Data` | `TArray < FMovieSceneTrackIdentifier >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneTrackLabels.json -->

# FMovieSceneTrackLabels

Structure for labels that can be assigned to movie scene tracks.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Strings` | `TArray < FString >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneTransformMask.json -->

# FMovieSceneTransformMask

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Mask` | `uint32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneVector2DKeyStruct.json -->

# FMovieSceneVector2DKeyStruct

Proxy structure for 2D vector section key data.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Vector` | `FVector2D` | They key's vector value. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneVector4KeyStruct.json -->

# FMovieSceneVector4KeyStruct

Proxy structure for vector4 section key data.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Vector` | `FVector4` | They key's vector value. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneVectorKeyStruct.json -->

# FMovieSceneVectorKeyStruct

Proxy structure for vector section key data.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Vector` | `FVector` | They key's vector value. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneVectorKeyStructBase.json -->

# FMovieSceneVectorKeyStructBase

Base Proxy structure for vector section key data.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Time` | `float` | The key's time. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMTDResult.json -->

# FMTDResult

Structure containing information about minimum translation direction (MTD)

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Direction` | `FVector` | Normalized direction of the minimum translation required to fix penetration. |
| `Distance` | `float` | Distance required to move along the MTD vector (Direction). |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMultiSubInstanceData.json -->

# FMultiSubInstanceData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InstanceClass_Multi` | `TSubclassOf < UAnimInstance >` | - |
| `InstanceToRun_Multi` | `UAnimInstance *` | - |
| `RunPriority` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FMyLandscapeConfigurationParams.json -->

# FMyLandscapeConfigurationParams

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SaveAssetNameBSM` | `FString` | - |
| `SaveAssetPathBSM` | `FString` | - |
| `ImproveLODToBuild` | `bool` | - |
| `SaveExtendDataBSM` | `bool` | - |
| `IniLODLevelBSM` | `uint8` | - |
| `MinLODLevelBSM` | `uint8` | - |
| `FarFactorBSM` | `float` | - |
| `EnableCullingUnderHeightBSM` | `bool` | - |
| `CullingUnderHeightBSM` | `float` | - |
| `SkirtDeepZBSM` | `int32` | - |
| `SkirtAngleBSM` | `int32` | - |
| `BorderUVOffsetBSM` | `float` | - |
| `ComponentSizeQuadsReducedBSM` | `int32` | - |
| `HighQualityMesh` | `TSoftObjectPtr < UStaticMesh >` | - |
| `HighQualityMeshDestroyHight` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNameCurve.json -->

# FNameCurve

Implements a curve of FNames.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Keys` | `TArray < FNameCurveKey >` | Sorted array of keys |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNameCurveKey.json -->

# FNameCurveKey

One key in a curve of FNames.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Time` | `float` | Time at this key |
| `Value` | `FName` | Value at this key |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNamedColor.json -->

# FNamedColor

A named color

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FColor` | - |
| `Name` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNamedCurveValue.json -->

# FNamedCurveValue

Namevalue pair for retrieving curve values

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Name` | `FName` | The name of the curve |
| `Value` | `float` | The value of the curve |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNamedEmitterMaterial.json -->

# FNamedEmitterMaterial

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Name` | `FName` | - |
| `Material` | `UMaterialInterface *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNamedFilmbackPreset.json -->

# FNamedFilmbackPreset

A named bundle of filmback settings used to implement filmback presets

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Name` | `FString` | Name for the preset. |
| `FilmbackSettings` | `FCameraFilmbackSettings` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNamedFloat.json -->

# FNamedFloat

A named float

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `float` | - |
| `Name` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNamedLensPreset.json -->

# FNamedLensPreset

A named bundle of lens settings used to implement lens presets.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Name` | `FString` | Name for the preset. |
| `LensSettings` | `FCameraLensSettings` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNamedNetDriver.json -->

# FNamedNetDriver

Active and named net drivers instantiated from an FNetDriverDefinition
  The net driver will remain instantiated on this struct until it is destroyed

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NetDriver` | `UNetDriver *` | Instantiation of named net driver |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNamedSlotBinding.json -->

# FNamedSlotBinding

The state passed into OnPaint that we can expose as a single painting structure to blueprints to
 allow script code to override OnPaint behavior.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Name` | `FName` | - |
| `Content` | `UWidget *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNamedTransform.json -->

# FNamedTransform

A named transform

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FTransform` | - |
| `Name` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNamedVector.json -->

# FNamedVector

A named float

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FVector` | - |
| `Name` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNameMapping.json -->

# FNameMapping

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NodeName` | `FName` | - |
| `BoneName` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNavAgentProperties.json -->

# FNavAgentProperties

Properties of representation of an 'agent' (or Pawn) used by AI navigationpathfinding.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AgentRadius` | `float` | Radius of the capsule used for navigationpathfinding. |
| `AgentHeight` | `float` | Total height of the capsule used for navigationpathfinding. |
| `AgentStepHeight` | `float` | Step height to use, or -1 for default value from navdata's config. |
| `NavWalkingSearchHeightScale` | `float` | Scale factor to apply to height of bounds when searching for navmesh to project to when nav walking |
| `PreferredNavData` | `TSubclassOf < ANavigationData >` | Type of navigation data used by agent, null means "any" |
| `AgentType` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNavAgentSelector.json -->

# FNavAgentSelector

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bSupportsAgent0` | `uint32` | - |
| `bSupportsAgent1` | `uint32` | - |
| `bSupportsAgent2` | `uint32` | - |
| `bSupportsAgent3` | `uint32` | - |
| `bSupportsAgent4` | `uint32` | - |
| `bSupportsAgent5` | `uint32` | - |
| `bSupportsAgent6` | `uint32` | - |
| `bSupportsAgent7` | `uint32` | - |
| `bSupportsAgent8` | `uint32` | - |
| `bSupportsAgent9` | `uint32` | - |
| `bSupportsAgent10` | `uint32` | - |
| `bSupportsAgent11` | `uint32` | - |
| `bSupportsAgent12` | `uint32` | - |
| `bSupportsAgent13` | `uint32` | - |
| `bSupportsAgent14` | `uint32` | - |
| `bSupportsAgent15` | `uint32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNavAvoidanceMask.json -->

# FNavAvoidanceMask

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bGroup0` | `uint32` | - |
| `bGroup1` | `uint32` | - |
| `bGroup2` | `uint32` | - |
| `bGroup3` | `uint32` | - |
| `bGroup4` | `uint32` | - |
| `bGroup5` | `uint32` | - |
| `bGroup6` | `uint32` | - |
| `bGroup7` | `uint32` | - |
| `bGroup8` | `uint32` | - |
| `bGroup9` | `uint32` | - |
| `bGroup10` | `uint32` | - |
| `bGroup11` | `uint32` | - |
| `bGroup12` | `uint32` | - |
| `bGroup13` | `uint32` | - |
| `bGroup14` | `uint32` | - |
| `bGroup15` | `uint32` | - |
| `bGroup16` | `uint32` | - |
| `bGroup17` | `uint32` | - |
| `bGroup18` | `uint32` | - |
| `bGroup19` | `uint32` | - |
| `bGroup20` | `uint32` | - |
| `bGroup21` | `uint32` | - |
| `bGroup22` | `uint32` | - |
| `bGroup23` | `uint32` | - |
| `bGroup24` | `uint32` | - |
| `bGroup25` | `uint32` | - |
| `bGroup26` | `uint32` | - |
| `bGroup27` | `uint32` | - |
| `bGroup28` | `uint32` | - |
| `bGroup29` | `uint32` | - |
| `bGroup30` | `uint32` | - |
| `bGroup31` | `uint32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNavCollisionBox.json -->

# FNavCollisionBox

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Offset` | `FVector` | - |
| `Extent` | `FVector` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNavCollisionCylinder.json -->

# FNavCollisionCylinder

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Offset` | `FVector` | - |
| `Radius` | `float` | - |
| `Height` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNavDataConfig.json -->

# FNavDataConfig

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Name` | `FName` | - |
| `Color` | `FColor` | - |
| `DefaultQueryExtent` | `FVector` | - |
| `NavigationDataClass` | `TSubclassOf < ANavigationData >` | - |
| `NavigationDataClassName` | `FSoftClassPath` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNavGraphNode.json -->

# FNavGraphNode

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Owner` | `UObject *` | Who's this node referring to? This will most commonly point to an actor or a component |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNavigationFilterArea.json -->

# FNavigationFilterArea

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AreaClass` | `TSubclassOf < UNavArea >` | navigation area class |
| `TravelCostOverride` | `float` | override for travel cost |
| `EnteringCostOverride` | `float` | override for entering cost |
| `bIsExcluded` | `uint32` | mark as excluded |
| `bOverrideTravelCost` | `uint32` | - |
| `bOverrideEnteringCost` | `uint32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNavigationFilterFlags.json -->

# FNavigationFilterFlags

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bNavFlag0` | `uint32` | - |
| `bNavFlag1` | `uint32` | - |
| `bNavFlag2` | `uint32` | - |
| `bNavFlag3` | `uint32` | - |
| `bNavFlag4` | `uint32` | - |
| `bNavFlag5` | `uint32` | - |
| `bNavFlag6` | `uint32` | - |
| `bNavFlag7` | `uint32` | - |
| `bNavFlag8` | `uint32` | - |
| `bNavFlag9` | `uint32` | - |
| `bNavFlag10` | `uint32` | - |
| `bNavFlag11` | `uint32` | - |
| `bNavFlag12` | `uint32` | - |
| `bNavFlag13` | `uint32` | - |
| `bNavFlag14` | `uint32` | - |
| `bNavFlag15` | `uint32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNavigationLink.json -->

# FNavigationLink

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Left` | `FVector` | - |
| `Right` | `FVector` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNavigationLinkBase.json -->

# FNavigationLinkBase

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LeftProjectHeight` | `float` | if greater than 0 nav system will attempt to project navlink's start point on geometry below |
| `MaxFallDownLength` | `float` | if greater than 0 nav system will attempt to project navlink's end point on geometry below |
| `Direction` | `TEnumAsByte < ENavLinkDirection :: Type >` | - |
| `SnapRadius` | `float` | - |
| `SnapHeight` | `float` | - |
| `SupportedAgents` | `FNavAgentSelector` | restrict area only to specified agents |
| `bSupportsAgent0` | `uint32` | - |
| `bSupportsAgent1` | `uint32` | - |
| `bSupportsAgent2` | `uint32` | - |
| `bSupportsAgent3` | `uint32` | - |
| `bSupportsAgent4` | `uint32` | - |
| `bSupportsAgent5` | `uint32` | - |
| `bSupportsAgent6` | `uint32` | - |
| `bSupportsAgent7` | `uint32` | - |
| `bSupportsAgent8` | `uint32` | - |
| `bSupportsAgent9` | `uint32` | - |
| `bSupportsAgent10` | `uint32` | - |
| `bSupportsAgent11` | `uint32` | - |
| `bSupportsAgent12` | `uint32` | - |
| `bSupportsAgent13` | `uint32` | - |
| `bSupportsAgent14` | `uint32` | - |
| `bSupportsAgent15` | `uint32` | - |
| `bUseSnapHeight` | `uint32` | - |
| `bSnapToCheapestArea` | `uint32` | If set, link will try to snap to cheapest area in given radius |
| `bCustomFlag0` | `uint32` | custom flag, check DescribeCustomFlags for details |
| `bCustomFlag1` | `uint32` | custom flag, check DescribeCustomFlags for details |
| `bCustomFlag2` | `uint32` | custom flag, check DescribeCustomFlags for details |
| `bCustomFlag3` | `uint32` | custom flag, check DescribeCustomFlags for details |
| `bCustomFlag4` | `uint32` | custom flag, check DescribeCustomFlags for details |
| `bCustomFlag5` | `uint32` | custom flag, check DescribeCustomFlags for details |
| `bCustomFlag6` | `uint32` | custom flag, check DescribeCustomFlags for details |
| `bCustomFlag7` | `uint32` | custom flag, check DescribeCustomFlags for details |
| `AreaClass` | `TSubclassOf < UNavArea >` | Area type of this link (empty = default) |
| `Description` | `FString` | this is an editor-only property to put descriptions in navlinks setup, to be able to identify it easier |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNavigationSegmentLink.json -->

# FNavigationSegmentLink

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LeftStart` | `FVector` | - |
| `LeftEnd` | `FVector` | - |
| `RightStart` | `FVector` | - |
| `RightEnd` | `FVector` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNetDriverDefinition.json -->

# FNetDriverDefinition

Container for describing various types of netdrivers available to the engine
  The engine will try to construct a netdriver of a given type and, failing that,
  the fallback version.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefName` | `FName` | Unique name of this net driver definition |
| `DriverClassName` | `FName` | Class name of primary net driver |
| `DriverClassNameFallback` | `FName` | Class name of the fallback net driver if the main net driver class fails to initialize |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNetViewer.json -->

# FNetViewer

stores information on a viewer that actors need to be checked against for relevancy

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Connection` | `UNetConnection *` | - |
| `InViewer` | `AActor *` | The "controlling net object" associated with this view (typically player controller) |
| `ViewTarget` | `AActor *` | The actor that is being directly viewed, usually a pawn.  Could also be the net actor of consequence |
| `ViewLocation` | `FVector` | Where the viewer is looking from |
| `ViewDir` | `FVector` | Direction the viewer is looking |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNewFPPPoseOffset.json -->

# FNewFPPPoseOffset

Simple controller to copy a bone's transform to another one.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Map` | `TMap < FName , FTransform >` | Array of names |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FNode.json -->

# FNode

Rig Controller for bone transform

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Name` | `FName` | Name of the original node. We don't allow to change this. This is used for identity. |
| `ParentName` | `FName` | We save Parent Node but if the parent node is removed, it will reset to root |
| `Transform` | `FTransform` | Absolute transform of the node. Hoping to use this data in the future to render |
| `DisplayName` | `FString` | This is Display Name where it will be used to display in Retarget Manager. This name has to be unique. |
| `bAdvanced` | `bool` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FObjectPoolConfig.json -->

# FObjectPoolConfig

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ObjectClassName` | `FName` | - |
| `ObjectClassFullPath` | `FString` | - |
| `MaxObjectNum` | `int32` | - |
| `MinObjectNum` | `int32` | - |
| `CleanupTimeout` | `int32` | - |
| `AllocateObjectGapTimeOverride` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FOptionalMovieSceneBlendType.json -->

# FOptionalMovieSceneBlendType

Optional blend type structure

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BlendType` | `EMovieSceneBlendType` | The actual blend type |
| `bIsValid` | `bool` | Boolean indicating whether BlendType is valid |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FOrbitOptions.json -->

# FOrbitOptions

Container struct for holding options on the data updating for the module.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bProcessDuringSpawn` | `uint32` | Whether to process the data during spawning. |
| `bProcessDuringUpdate` | `uint32` | Whether to process the data during updating. |
| `bUseEmitterTime` | `uint32` | Whether to use emitter time during data retrieval. |
| `bUseParticleIDInsteadOfTime` | `uint32` | Whether to use particle ID instead of time (emitter time or particle time). |
| `ParticleIDLoop` | `uint32` | If >0, the distribution input will be ParticleID % ParticleIDLoop |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FOrientedBox.json -->

# FOrientedBox

Structure for arbitrarily oriented boxes (i.e. not necessarily axis-aligned).
  The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\OrientedBox.h

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Center` | `FVector` | - |
| `AxisX` | `FVector` | - |
| `AxisY` | `FVector` | - |
| `AxisZ` | `FVector` | - |
| `ExtentX` | `float` | - |
| `ExtentY` | `float` | - |
| `ExtentZ` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FOverlapResult.json -->

# FOverlapResult

Structure containing information about one hit of an overlap test

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Actor` | `TWeakObjectPtr < AActor >` | Actor that the check hit. |
| `Component` | `TWeakObjectPtr < UPrimitiveComponent >` | PrimitiveComponent that the check hit. |
| `bBlockingHit` | `uint32` | Indicates if this hit was requesting a block - if false, was requesting a touch instead |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FOverlayItem.json -->

# FOverlayItem

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StartTime` | `FTimespan` | When the overlay should be displayed |
| `EndTime` | `FTimespan` | When the overlay should be cleared |
| `Text` | `FString` | Text that appears onscreen when the overlay is shown |
| `Position` | `FVector2D` | The position of the text on screen (Between 0.0 and 1.0) |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FOverrideBoneTranslationRetargetingModeConfig.json -->

# FOverrideBoneTranslationRetargetingModeConfig

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RetargetingModeConfig` | `TMap < TEnumAsByte < EBoneTranslationRetargetingMode :: Type > , TEnumAsByte < EBoneTranslationRetargetingMode :: Type > >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FOverridePhyxMaterial.json -->

# FOverridePhyxMaterial

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OriginalPhysxMaterial` | `TArray < UPhysicalMaterial * >` | - |
| `OverridePhysxMaterial` | `TArray < UPhysicalMaterial * >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPackedNormal.json -->

# FPackedNormal

A packed normal.
  The full C++ class is located here: Engine\Source\Runtime\RenderCore\Public\PackedNormal.h

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `X` | `uint8` | - |
| `Y` | `uint8` | - |
| `Z` | `uint8` | - |
| `W` | `uint8` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPackedRGB10A2N.json -->

# FPackedRGB10A2N

A packed basis vector.
 The full C++ class is located here: Engine\Source\Runtime\RenderCore\Public\PackedNormal.h

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Packed` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPackedRGBA16N.json -->

# FPackedRGBA16N

A packed vector.
 The full C++ class is located here: Engine\Source\Runtime\RenderCore\Public\PackedNormal.h

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `XY` | `int32` | - |
| `ZW` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPacketSimulationSettings.json -->

# FPacketSimulationSettings

Holds the packet simulation settings in one place

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PktLoss` | `int32` | When set, will cause calls to FlushNet to drop packets.<br>	  Value is treated as % of packets dropped (i.e. 0 = None, 100 = All).<br>	  No general pattern  ordering is guaranteed.<br>	  Clamped between 0 and 100.<br>	 <br>	  Works with all other settings. |
| `PktOrder` | `int32` | When set, will cause calls to FlushNet to change ordering of packets at random.<br>	  Value is treated as a bool (i.e. 0 = False, anything else = True).<br>	  This works by randomly selecting packets to be delayed until a subsequent call to FlushNet.<br>	 <br>	  Takes precedence over PktDup and PktLag. |
| `PktDup` | `int32` | When set, will cause calls to FlushNet to duplicate packets.<br>	  Value is treated as % of packets duplicated (i.e. 0 = None, 100 = All).<br>	  No general pattern  ordering is guaranteed.<br>	  Clamped between 0 and 100.<br>	 <br>	  Cannot be used with PktOrder or PktLag. |
| `PktLag` | `int32` | When set, will cause calls to FlushNet to delay packets.<br>	  Value is treated as millisecond lag.<br>	 <br>	  Cannot be used with PktOrder. |
| `PktLagVariance` | `int32` | When set, will cause PktLag to use variable lag instead of constant.<br>	  Value is treated as millisecond lag range (e.g. -GivenVariance <= 0 <= GivenVariance).<br>	  Clamped between 0 and 100.<br>	 <br>	  Can only be used when PktLag is enabled. |
| `PktIncomingLoss` | `int32` | The ratio of incoming packets that will be dropped<br>	  to simulate packet loss |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPaintedVertex.json -->

# FPaintedVertex

Cached vertex information at the time the mesh was painted.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Position` | `FVector` | - |
| `Normal` | `FPackedNormal` | - |
| `Color` | `FColor` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPairCachedBoneInfo.json -->

# FPairCachedBoneInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ResetRoll` | `bool` | - |
| `PreBoneCached` | `FCachedBoneParamInfo` | - |
| `PostBoneCached` | `FCachedBoneParamInfo` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPaperFlipbookKeyFrame.json -->

# FPaperFlipbookKeyFrame

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Sprite` | `UPaperSprite *` | - |
| `FrameRun` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPaperSpriteAtlasSlot.json -->

# FPaperSpriteAtlasSlot

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SpriteRef` | `TSoftObjectPtr < UPaperSprite >` | - |
| `AtlasIndex` | `int32` | - |
| `X` | `int32` | - |
| `Y` | `int32` | - |
| `Width` | `int32` | - |
| `Height` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPaperSpriteSocket.json -->

# FPaperSpriteSocket

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LocalTransform` | `FTransform` | - |
| `SocketName` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPaperTerrainMaterialRule.json -->

# FPaperTerrainMaterialRule

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StartCap` | `UPaperSprite *` | - |
| `Body` | `TArray < UPaperSprite * >` | - |
| `EndCap` | `UPaperSprite *` | - |
| `MinimumAngle` | `float` | - |
| `MaximumAngle` | `float` | - |
| `bEnableCollision` | `bool` | - |
| `CollisionOffset` | `float` | - |
| `DrawOrder` | `int32` | - |
| `Description` | `FText` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPaperTileInfo.json -->

# FPaperTileInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TileSet` | `UPaperTileSet *` | - |
| `PackedTileIndex` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPaperTileMetadata.json -->

# FPaperTileMetadata

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UserDataName` | `FName` | - |
| `CollisionData` | `FSpriteGeometryCollection` | - |
| `TerrainMembership` | `uint8` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPaperTileSetTerrain.json -->

# FPaperTileSetTerrain

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TerrainName` | `FString` | - |
| `CenterTileIndex` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FParallelWorldInfo.json -->

# FParallelWorldInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GameModeURL` | `FURL` | - |
| `AdditionalLevel` | `FString` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FParallelWorldPlayerInfo.json -->

# FParallelWorldPlayerInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `WorldParallelismID` | `uint32` | - |
| `PlayerName` | `FString` | - |
| `PlayerController` | `APlayerController *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FParameterGroupData.json -->

# FParameterGroupData

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GroupName` | `FString` | - |
| `GroupSortPriority` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FParticleBurst.json -->

# FParticleBurst

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Count` | `int32` | The number of particles to burst |
| `CountLow` | `int32` | If >= 0, use as a range [CountLow..Count] |
| `Time` | `float` | The time at which to burst them (0..1: emitter lifetime) |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FParticleCurvePair.json -->

# FParticleCurvePair

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CurveName` | `FString` | - |
| `CurveObject` | `UObject *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FParticleEditorPromotionSettings.json -->

# FParticleEditorPromotionSettings

Holds settings for the particle editor build promotion tests

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefaultParticleAsset` | `FFilePath` | Default particle asset to use for tests |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FParticleEvent_GenerateInfo.json -->

# FParticleEvent_GenerateInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Type` | `TEnumAsByte < EParticleEventType >` | The type of event. |
| `Frequency` | `int32` | How often to trigger the event (<= 1 means EVERY time). |
| `ParticleFrequency` | `int32` | Only fire the first time (collision only). |
| `FirstTimeOnly` | `uint32` | Only fire the first time (collision only). |
| `LastTimeOnly` | `uint32` | Only fire the last time (collision only). |
| `UseReflectedImpactVector` | `uint32` | Use the impact FVector not the hit normal (collision only). |
| `bUseOrbitOffset` | `uint32` | Use the orbit offset when computing the position at which the event occurred. |
| `CustomName` | `FName` | Should the event tag with a custom name? Leave blank for the default. |
| `ParticleModuleEventsToSendToGame` | `TArray < UParticleModuleEventSendToGame * >` | The events we want to fire off when this event has been generated |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FParticleRandomSeedInfo.json -->

# FParticleRandomSeedInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParameterName` | `FName` | The name to expose to the placed instances for setting this seed |
| `bGetSeedFromInstance` | `uint32` | If true, the module will attempt to get the seed from the owner<br>	 	instance. If that fails, it will fall back to getting it from<br>	 	the RandomSeeds array. |
| `bInstanceSeedIsIndex` | `uint32` | If true, the seed value retrieved from the instance will be an<br>	 	index into the array of seeds. |
| `bResetSeedOnEmitterLooping` | `uint32` | If true, then reset the seed upon the emitter looping.<br>	 	For looping environmental effects this should likely be set to false to avoid<br>	 	a repeating pattern. |
| `bRandomlySelectSeedArray` | `uint32` | If true, then randomly select a seed entry from the RandomSeeds array |
| `RandomSeeds` | `TArray < int32 >` | The random seed values to utilize for the module. <br>	 	More than 1 means the instance will randomly select one. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FParticleReplayTrackKey.json -->

# FParticleReplayTrackKey

This track implements support for creating and playing back captured particle system data
 
 Data for a single key in this track

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Time` | `float` | Position along timeline |
| `Duration` | `float` | Time length this clip should be capturedplayed for |
| `ClipIDNumber` | `int32` | Replay clip ID number that identifies the clip we should capture to or playback from |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FParticleSysParam.json -->

# FParticleSysParam

Struct used for a particular named instance parameter for this ParticleSystemComponent.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Name` | `FName` | The name of the parameter |
| `ParamType` | `TEnumAsByte < enum EParticleSysParamType >` | The type of parameters<br>	 	PSPT_None       - There is no data type<br>	 	PSPT_Scalar     - Use the scalar value<br>	 	PSPT_ScalarRand - Select a scalar value in the range [Scalar_Low..Scalar)<br>	 	PSPT_Vector     - Use the vector value<br>	 	PSPT_VectorRand - Select a vector value in the range [Vector_Low..Vector)<br>	 	PSPT_Color      - Use the color value<br>	 	PSPT_Actor      - Use the actor value<br>	 	PSPT_Material   - Use the material value |
| `Scalar` | `float` | - |
| `Scalar_Low` | `float` | - |
| `Vector` | `FVector` | - |
| `Vector_Low` | `FVector` | - |
| `Color` | `FColor` | - |
| `Actor` | `AActor *` | - |
| `Material` | `UMaterialInterface *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPassiveSoundMixModifier.json -->

# FPassiveSoundMixModifier

Structure containing information on a SoundMix to activate passively.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SoundMix` | `USoundMix *` | The SoundMix to activate |
| `MinVolumeThreshold` | `float` | Minimum volume level required to activate SoundMix. Below this value the SoundMix will not be active. |
| `MaxVolumeThreshold` | `float` | Maximum volume level required to activate SoundMix. Above this value the SoundMix will not be active. |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPawnActionEvent.json -->

# FPawnActionEvent

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Action` | `UPawnAction *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPawnActionStack.json -->

# FPawnActionStack

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TopAction` | `UPawnAction *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPEBuffInfo.json -->

# FPEBuffInfo

包含了Buff的所有配置信息

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UIInfo` | `FPEBuffUIInfo` | Buff的UI信息 |
| `ApplyTagGroup` | `FGameplayTagGroups` | Tag的配置组，包含该Buff与各个Tag的互斥关系 |
| `MergeConditionType` | `EPEBuffMergeConditionType` | 配置另一个Buff能够与当前Buff合并的判断条件，可以通过CanMerge_BP扩展这个条件，CanMerge_BP与当前条件是“与”的关系 |
| `MergeTypeMask` | `uint32` | 配置另一个Buff合并到当前后的行为，可通过OnMerge_BP扩展这些行为 |
| `MaxStackNum` | `int32` | 最大堆叠次数 |
| `DurationStrategy` | `EPEBuffDurationType` | 堆叠持续时长计算方式 |
| `BuffEffects` | `TArray < UPEBuffEffectBase * >` | 触发效果 |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPEBuffUIInfo.json -->

# FPEBuffUIInfo

Buff的UI信息

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BuffName` | `FName` | Buff的名字 |
| `OverwriteBuffName` | `FName` | 覆盖的Buff名字，该字段不为空时UI优先显示覆盖的Buff名字 |
| `BuffDetail` | `FString` | Buff的描述 |
| `OverwriteBuffDetail` | `FString` | 覆盖的Buff描述，该字段不为空时UI优先显示覆盖的Buff描述 |
| `BuffIcon` | `FSoftObjectPath` | Buff的图标 |
| `OverwriteBuffIcon` | `FSoftObjectPath` | 覆盖的Buff图标，该字段不为空时UI优先显示覆盖的Buff图标 |
| `bShowUI` | `bool` | Buff是否显示表示当前状态的图标在UI上 |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPerBoneInterpolation.json -->

# FPerBoneInterpolation

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoneReference` | `FBoneReference` | - |
| `InterpolationSpeedPerSec` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPerConOwningObjectInfo.json -->

# FPerConOwningObjectInfo

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Actor` | `AActor *` | - |
| `Channel` | `UActorChannel *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPESkillAttributeItem.json -->

# FPESkillAttributeItem

属性修改信息数组

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Method` | `FPESkillAttributeModifyMethod` | 修改方式 |
| `GameAttribute` | `FGameAttributeContainer` | 要修改的属性名 |
| `ModifierOp` | `EAttrOperator` | 属性修改操作类型 |
| `ModifierOp_DoChange` | `EAttrOperator_DoChange` | 属性修改操作类型 |
| `ModifierValueWrapper` | `FGameMagnitudeWrapper` | 操作数值 |
| `bModifyForever` | `bool` | 是否为永久修改（属性修改结束时不还原属性） deprecated from GC033 ！！！ |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPESkillCDWapper.json -->

# FPESkillCDWapper

技能CD信息

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CDType` | `EPESkillCDType` | 技能CD类型 |
| `CDRecoveryTime` | `float` | CD能量充能时间 |
| `AllowRecoveryDuringActivation` | `bool` | 技能激活期间恢复CD能量 |
| `MaxLayer` | `int` | 最大充能次数 |
| `CDEnergyConsume` | `float` | 持续消耗型每秒扣除速率，如果不选energy，就是直接扣完一层的所有能量 |
| `AllowConsumeMinEnergy` | `float` | 能开始消耗能量的最小百分比 |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPESkillConsume.json -->

# FPESkillConsume

技能消耗

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ConsumeAttrItems` | `TArray < FPESkillConsumeAttribute >` | 技能消耗数值Array |
| `ConsumeItems` | `TArray < FPESkillConsumeItem >` | 技能消耗物品Array |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPESkillConsumeAttribute.json -->

# FPESkillConsumeAttribute

技能属性消耗

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GameAttribute` | `FGameAttributeContainer` | 要消耗的属性名 |
| `ConsumeValue` | `float` | 消耗的数值 |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPESkillConsumeItem.json -->

# FPESkillConsumeItem

消耗物品信息

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ItemID` | `int32` | 消耗物品ID |
| `ItemNum` | `int32` | 消耗物品数量 |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPESkillTargetData.json -->

# FPESkillTargetData

条件触发时的数据

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TargetActors` | `TArray < AActor * >` | 范围Action中的Actor列表 |
| `HitResult` | `FHitResult` | 碰撞结果 |
| `Origin` | `FVector` | 发射起点 |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPESkillUIInfo.json -->

# FPESkillUIInfo

技能UI信息

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SkillName` | `FName` | 技能名字 |
| `OverwriteSkillName` | `FName` | 覆盖的技能名字，该字段不为空时UI优先显示覆盖的技能名字 |
| `SkillDetail` | `FString` | 技能描述 |
| `OverwriteSkillDetail` | `FString` | 覆盖的技能描述，该字段不为空时UI优先显示覆盖的技能描述 |
| `SkillIcon` | `FSoftObjectPath` | 技能图标 |
| `OverwriteSkillIcon` | `FSoftObjectPath` | 覆盖的技能图标，该字段不为空时UI优先显示覆盖的技能图标 |
| `bUseSkillUISlot` | `bool` | 是否使用技能预设UI槽位，勾了这个选项的话，则会走createui的逻辑注册到技能槽位上，否则走技能UI绑定技能槽位获取技能的逻辑 |
| `PESkillUIAsset` | `FSoftClassPath` | 默认技能UI |
| `SkillUISlot` | `FGameplayTag` | 预设技能UI插槽 |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPhysicalAnimationData.json -->

# FPhysicalAnimationData

Stores info on the type of motor that will be used for a given bone

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BodyName` | `FName` | The body we will be driving. We specifically hide this from users since they provide the body name and bodies below in the component API. |
| `bIsLocalSimulation` | `uint8` | Whether the drive targets are in world space or local |
| `OrientationStrength` | `float` | The strength used to correct orientation error |
| `AngularVelocityStrength` | `float` | The strength used to correct angular velocity error |
| `PositionStrength` | `float` | The strength used to correct linear position error. Only used for non-local simulation |
| `VelocityStrength` | `float` | The strength used to correct linear velocity error. Only used for non-local simulation |
| `MaxLinearForce` | `float` | The max force used to correct linear errors |
| `MaxAngularForce` | `float` | The max force used to correct angular errors |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPhysicalAnimationProfile.json -->

# FPhysicalAnimationProfile

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ProfileName` | `FName` | Profile name used to identify set of physical animation parameters |
| `PhysicalAnimationData` | `FPhysicalAnimationData` | Physical animation parameters used to drive animation |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPhysicalSurfaceName.json -->

# FPhysicalSurfaceName

Structure that represents the name of physical surfaces.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Type` | `TEnumAsByte < enum EPhysicalSurface >` | - |
| `Name` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPhysicsConstraintProfileHandle.json -->

# FPhysicsConstraintProfileHandle

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ProfileProperties` | `FConstraintProfileProperties` | - |
| `ProfileName` | `FName` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPlane.json -->

# FPlane

A plane definition in 3D space.
  The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\Plane.h

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `W` | `float` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPlatformInterfaceData.json -->

# FPlatformInterfaceData

Struct that encompasses the most common types of data. This is the data payload
  of PlatformInterfaceDelegateResult.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DataName` | `FName` | An optional tag for this data |
| `Type` | `TEnumAsByte < enum EPlatformInterfaceDataType >` | Specifies which value is valid for this structure |
| `IntValue` | `int32` | Various typed result values |
| `FloatValue` | `float` | - |
| `StringValue` | `FString` | - |
| `ObjectValue` | `UObject *` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPlatformInterfaceDelegateResult.json -->

# FPlatformInterfaceDelegateResult

Generic structure for returning most any kind of data from C++ to delegate functions

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bSuccessful` | `bool` | This is always usable, no matter the type |
| `Data` | `FPlatformInterfaceData` | The result actual data |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPlayerMuteList.json -->

# FPlayerMuteList

Container responsible for managing the mute state of a player controller
  at the gameplay level (VoiceInterface handles actual muting)

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bHasVoiceHandshakeCompleted` | `bool` | Has server and client handshake completed |
| `VoiceChannelIdx` | `int32` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPluginRedirect.json -->

# FPluginRedirect

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OldPluginName` | `FString` | - |
| `NewPluginName` | `FString` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPointDamageEvent.json -->

# FPointDamageEvent

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Damage` | `float` | - |
| `ShotDirection` | `FVector_NetQuantizeNormal` | Direction the shot came from. Should be normalized. |
| `HitInfo` | `FHitResult` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPoseData.json -->

# FPoseData

Pose data 
  
  This is one pose data structure
  This will let us blend poses quickly easily
  All poses within this asset should contain same number of tracks, 
  so that we can blend quickly

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LocalSpacePose` | `TArray < FTransform >` | - |
| `LocalSpacePoseMask` | `TArray < bool >` | - |
| `CurveData` | `TArray < float >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPoseDataContainer.json -->

# FPoseDataContainer

Pose data container
 
 Contains animation and curve for all poses

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PoseNames` | `TArray < FSmartName >` | - |
| `Poses` | `TArray < FPoseData >` | - |
| `Tracks` | `TArray < FName >` | - |
| `TrackMap` | `TMap < FName , int32 >` | - |
| `Curves` | `TArray < FAnimCurveBase >` | - |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPoseDriverTarget.json -->

# FPoseDriverTarget

Information about each target in the PoseDriver

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoneTransforms` | `TArray < FPoseDriverTransform >` | Translation of this target |
| `TargetRotation` | `FRotator` | Rotation of this target |
| `TargetScale` | `float` | Scale applied to this target's function - a larger value will activate this target sooner |
| `bApplyCustomCurve` | `bool` | If we should apply a custom curve mapping to how this target activates |
| `CustomCurve` | `FRichCurve` | Custom curve mapping to apply if bApplyCustomCurve is true |
| `DrivenName` | `FName` | Name of item to drive - depends on DriveOutput setting.  <br>	 	If DriveOutput is DrivePoses, this should be the name of a pose in the assigned PoseAsset<br>	 	If DriveOutput is DriveCurves, this is the name of the curve (morph target, material param etc) to drive |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPoseDriverTransform.json -->

# FPoseDriverTransform

Translation and rotation for a particular bone at a particular target

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TargetTranslation` | `FVector` | Translation of this target |
| `TargetRotation` | `FRotator` | Rotation of this target |


---

<!-- Source: https://developer.gp.qq.com/api/cppstruct/detail/FPoseLinkBase.json -->

# FPoseLinkBase

A pose link to another node

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LinkID` | `int32` | Serialized link ID, used to build the non-serialized pointer map. |
| `SourceLinkID` | `int32` | The source link ID, used for debug visualization. |

