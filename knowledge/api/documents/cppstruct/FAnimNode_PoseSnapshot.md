---
id: "api:cppstruct:FAnimNode_PoseSnapshot"
title: "FAnimNode_PoseSnapshot"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_PoseSnapshot.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimNode_PoseSnapshot

Provide a snapshot pose, either from the internal named pose cache or via a supplied snapshot

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Mode` | `ESnapshotSourceMode` | How to access the snapshot |
| `SnapshotName` | `FName` | The name of the snapshot previously stored with SavePoseSnapshot |
| `Snapshot` | `FPoseSnapshot` | Snapshot to use. This should be populated at first by calling SnapshotPose |
