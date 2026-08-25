---
id: "api:cppstruct:FAnimPhysPlanarLimit"
title: "FAnimPhysPlanarLimit"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimPhysPlanarLimit.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimPhysPlanarLimit

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DrivingBone` | `FBoneReference` | When using a driving bone, the plane transform will be relative to the bone transform |
| `PlaneTransform` | `FTransform` | Transform of the plane, this is either in component-space if no DrivinBone is specified<br>	   or in bone-space if a driving bone is present. |
| `IsEnabled` | `bool` | - |
