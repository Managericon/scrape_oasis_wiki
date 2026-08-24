---
id: "195"
title: "Buff简介"
source: "https://developer.gp.qq.com/wikieditor/#/catalog/195"
category: "进阶内容/GamePlay系统/技能系统/Buff编辑器1.0"
---

# Buff简介

# Buff系统

最后修改于 2025-06-19 03:33

## Buff简介

* * *

### Buff的主要特点

  * 有持续时间，有完整的生命周期
  * 可以叠加层数
  * 单个Buff功能相对单一
  * Buff功能基本只影响Buff宿主本身

### Buff的基本框架

整个项目中，可以包含多个BuffList，BuffList仅用方便Buff的分类管理，不参与逻辑
通常情况下同一个玩法下的Buff，或者归属同一个功能管理的Buff都放在一个BuffList下，方便后续管理

每个Buff可以添加多个BuffAction，单个BuffAction的功能单一，通常用于实现一个简单的功能
例如播放特效，或者播放一个角色动画
单个Buff的最终效果由所属的所有BuffAction组合而成，而BuffAction的生命周期也由Buff管理
![企业微信截图_16867094188854.png](https://cgugc-video-test-1258633575.cos.ap-shanghai.myqcloud.com/wiki_picture/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_16867094188854.png)

## 新建/删除Buff

* * *

### 添加一个Buff

  * 继承UGCBuffList新建蓝图，命名为MyBuffList
  * 新建的BuffList需要将其放到Asset\Blueprint\UGCBuffs目录下才能被识别生效，若是没有该目录需要自己新建一个
  * 打开MyBuffList，在BuffList中新增一项，在Name中输入需要新建的Buff名，回车保存，对应的Buff蓝图会由编辑器自动新建
![企业微信截图_16867094317361.png](https://cgugc-video-test-1258633575.cos.ap-shanghai.myqcloud.com/wiki_picture/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_16867094317361.png)
![企业微信截图_16867094488625.png](https://cgugc-video-test-1258633575.cos.ap-shanghai.myqcloud.com/wiki_picture/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_16867094488625.png)

### 删除一个Buff

- 先从BuffList中删除Buff数据后再手动删除Buff蓝图，否则会引起引用错误

![企业微信截图_1686709463911.png](https://cgugc-video-test-1258633575.cos.ap-shanghai.myqcloud.com/wiki_picture/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_1686709463911.png)

  * 删除BuffList中数据后，再找到对应目录，删除Buff蓝图

![企业微信截图_16867094753692.png](https://cgugc-video-test-1258633575.cos.ap-shanghai.myqcloud.com/wiki_picture/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_16867094753692.png)

## Lua中使用Buff

* * *

### `PlayerPawn`上的3个常用函数，添加，删除，查找

```
--判断是否拥有此Buff
HasBuff:fun(BuffName:FName):bool

--移除Buff，可指定只移除层数
RemoveBuff:fun(BuffName:FName,RemoveLayerOnly:bool,BuffApplierActor:AActor):bool

--添加Buff，可指定来源以及添加层数
AddBuff:fun(BuffName:FName,BuffCauser:AController,LayerCount:int32,BuffApplierActor:AActor,CauserActor:AActor):int32
```

  * 以我们上面新建的MyBuff为例，最简单的添加方式如下

示例：给角色添加Buff

```
	PlayerPawn:AddBuff("MyBuff", nil, 1, nil, nil)
```

## Buff设置介绍

  * 其中，标红为最常用字段

字段名称 | 解释
---|---
BuffName | Buff名称
Icon | Buff图标
Layerable | Buff是否可以叠加层数
LyaerMax | Buff可叠加的最大层数
ValidityTime |  Buff持续时间
ValidityTimeAccumulable | Buff持续时间是否可以累加
MaxValidityTime |  Buff最大持续时间
BuffConditions | 角色状态条件，如果角色不满足状态，Buff失效
NeedSimulateToClient | 是否需要同步到客户端，默认全体广播
SimulateAddBuffRole | 客户端模拟加Buff的规则
MutexBuffs | Buff互斥，例如Buff_1的互斥中填了Buff_2，那有Buff_1时，无法添加Buff_2
BuffActions |  Buff功能
EventBuffAction | 特定事件下触发的Buff功能
IsAlwaysExists | 是否永久存在
  * `NeedSimulateToClient`的说明

选项 | 说明
---|---
AddBuffRole_None | 无客户端模拟加载
AddBuffRole_All | 所有客户都安模拟加载
AddBuffRole_Self | 自己模拟加载
AddBuffRole_Causer | 施放者模拟加载
AddBuffRole_Firend | Buff目标以及其队友模拟加载，即Buff目标敌人看不到
AddBuffRole_Enermy | Buff目标的敌人模拟加载，即Buff目标及其队友看不到
