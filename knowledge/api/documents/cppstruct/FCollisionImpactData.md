---
id: "api:cppstruct:FCollisionImpactData"
title: "FCollisionImpactData"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FCollisionImpactData.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FCollisionImpactData

Information about an overall collision, including contacts.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ContactInfos` | `TArray < FRigidBodyContactInfo >` | all the contact points in the collision |
| `TotalNormalImpulse` | `FVector` | the total impulse applied as the two objects push against each other |
| `TotalFrictionImpulse` | `FVector` | the total counterimpulse applied of the two objects sliding against each other |
