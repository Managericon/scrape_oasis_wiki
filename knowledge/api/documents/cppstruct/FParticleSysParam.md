---
id: "api:cppstruct:FParticleSysParam"
title: "FParticleSysParam"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FParticleSysParam.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

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
