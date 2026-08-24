---
id: "196"
title: "自定义自己的BuffAction"
source: "https://developer.gp.qq.com/wikieditor/#/catalog/196"
category: "进阶内容/GamePlay系统/技能系统/Buff编辑器1.0"
---

# 自定义自己的BuffAction

最后修改于 2025-06-19 03:33

### 使用Lua脚本Action

  * 在BuffActions中添加新的Action,类型选择Lua脚本Action
  * 在LuaFile中填入路径

![企业微信截图_16867095152247.png](https://cgugc-video-test-1258633575.cos.ap-shanghai.myqcloud.com/wiki_picture/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_16867095152247.png)

  * 对应的脚本路径

![企业微信截图_16867095284718.png](https://cgugc-video-test-1258633575.cos.ap-shanghai.myqcloud.com/wiki_picture/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_16867095284718.png)

  * 脚本对应实现如下

```
local myBuffAction = {};

function myBuffAction:LuaDoAction()
    print("myBuffAction:LuaDoAction")
    return true
end

function myBuffAction:LuaUndoAction()
    print("myBuffAction:LuaUndoAction")
    return true
end

function myBuffAction:LuaResetAction()
    print("myBuffAction:LuaResetAction")
    return true
end

function myBuffAction:LuaUpdateAction(DeltaSeconds)
    print("myBuffAction:LuaUpdateAction:"..DeltaSeconds)
    return true
end

return myBuffAction;
```
