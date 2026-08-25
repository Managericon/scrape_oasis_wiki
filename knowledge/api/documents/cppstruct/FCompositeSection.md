---
id: "api:cppstruct:FCompositeSection"
title: "FCompositeSection"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FCompositeSection.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

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
