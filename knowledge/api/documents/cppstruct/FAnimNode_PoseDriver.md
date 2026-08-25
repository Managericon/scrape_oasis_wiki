---
id: "api:cppstruct:FAnimNode_PoseDriver"
title: "FAnimNode_PoseDriver"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_PoseDriver.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

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
