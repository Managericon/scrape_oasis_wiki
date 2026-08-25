---
id: "api:cppstruct:FAIStimulus"
title: "FAIStimulus"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAIStimulus.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

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
