---
id: "20469"
title: "热重载 HotReload Lua 使用说明"
source: "https://developer.gp.qq.com/wikieditor/#/catalog/20469"
category: "绿洲编辑器基础内容/脚本编写"
---

# 热重载 HotReload Lua 使用说明

创建于 2026-09-14 05:50

## 功能简介

能力边界速览

维度 | 是否支持 | 说明
---|---|---
函数逻辑替换 | ✅ | 新版本函数在下次调用时生效
变量状态保留 | ✅ | 模块内的变量值保持不变，不会被重置
upvalue 状态嫁接 | ✅ | 闭包捕获的外部局部变量状态会被保留
蓝图绑定同步更新 | ✅ | LuaBind 模块对应的蓝图 UFunction 自动重绑定
自定义热更回调 | ✅ | 模块可实现 `OnHotReload()` 执行初始化逻辑
新变量初始化 | ❌ | 新增变量的初始化表达式不会执行，需手动处理
协程/定时器引用更新 | ❌ | 已注册的 timer/协程仍引用旧函数，需手动处理
运行时编辑（免 PIE 改文件） | ❌ | 需在 PIE 运行中改文件后触发热更

  * 适用场景：调参、改逻辑、定位 bug 时的快速迭代
  * 不适用场景：新增模块、修改模块结构、需要重置运行时状态的场景（建议重启 PIE）

## 快速上手

典型迭代流程三步走：

  1. 启动 PIE 调试：编辑器中点击调试，等待 DebugGame 窗口显示 “Project Succeeded” 且 PIE 客户端启动完成
  2. 修改 Lua 文件：在 Script/ 目录下编辑目标 .lua 文件并保存（例如 Script/Game/MySystem.lua）
  3. 触发热更并验证：点击 DebugGame 窗口底部的 “热重载Lua文件” 按钮，等待日志提示成功后，在 PIE 中触发对应逻辑验证效果

> 热更生效后，PIE 客户端与 DS 的日志（ShadowTrackerExtra/Saved/Logs/项目名称/）中可见 lua hotreload 相关记录，可用于确认热更是否真正触达目标端

## 触发方式

HotReload Lua 通过 DebugGame 窗口的 “HotReload Lua” 按钮触发热更，按钮位于 PIE 调试窗口底部。

![image.png](https://cgugc-video-test-1258633575.cos.ap-shanghai.myqcloud.com/wiki_picture/nbKeB%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_17876434823517.png)

**触发流程**

点击按钮后，系统自动完成以下操作：

  1. 扫描工程 Script/ 目录下所有 .lua 文件；
  2. 自动检测自上次热更以来有改动的文件；
  3. 将改动文件下发到 DS 与所有客户端，触发函数级热更；
  4. 在窗口日志区显示当前热更的模块名与最终重载数量。

优势：无需手动指定模块名，自动增量检测，DS 与客户端同步下发；按钮路径直接下发文件内容到目标端，可靠性高

## OnHotReload 回调

若模块需要在热更完成后执行初始化逻辑（例如重新订阅事件、刷新缓存、重置临时状态），可在模块中实现 `OnHotReload` 回调：

```
local M = {}

function M.OnHotReload(self)
    -- self 即模块表本身
    -- 热更完成后自动调用，可在此处：
    --   - 重新订阅事件
    --   - 刷新缓存
    --   - 初始化新增变量
    --   - 重启定时器/协程
end

function M.SomeFunc()
    -- 业务逻辑
end

return M
```

热更完成时，系统会自动以 M:OnHotReload() 形式调用该回调。建议凡是有运行时状态的模块都实现此回调，确保热更后状态一致。

## 重要注意事项

**硬性限制**

以下限制由热更机制本质决定，无法绕过，需在开发中主动规避：

  1. 模块名必须以 Script 开头

按钮路径自动转换的模块名形如 Script.X.Y；否则会被拒绝并提示 Can Only Reload File under Script Folder。

  2. 新变量不会初始化

热更对变量只保留旧值或新增空值，新变量的初始化表达式（如 local counter = 10）不会执行。如需初始化新变量，请在 OnHotReload 中手动处理。

  3. 协程与定时器仍引用旧函数

如果旧函数已注册了 timer 或协程引用了旧 closure，热更后这些引用仍指向旧函数，新逻辑不会被调用。必须在 OnHotReload 中手动重启定时器或重新注册协程。

  4. 每次重新 PIE 需等待连接重建

每次重新 PIE 会清空客户端连接列表，必须等 PIE 客户端 BeginPlay 重新注册后才能热更。若过早触发热更会提示 “Connection not established”。

  5. DS 不能直接读本地文件

DS 收到的热更消息必须携带文件内容（由客户端中转读取并附加）。这一过程对开发者透明，但意味着 DS 热更依赖至少一个客户端已连接。

**热更友好的代码模式**

为降低热更失败风险，建议遵循以下代码模式：

推荐 | 不推荐 | 原因
---|---|---
状态存入模块表字段 `M.counter` | 顶层 `local counter` 计数器 | 模块表字段在热更时可被显式保留/初始化
纯函数逻辑，状态外置 | 闭包捕获大量外部状态 | upvalue 嫁接仅对同名 `upvalue` 生效，复杂闭包易出错
定时器回调引用模块表函数 | 定时器回调直接捕获 `local` 函数 | 前者热更后通过 `OnHotReload` 重启即可生效；后者引用旧 `closure`
修改现有函数体 | 新增/删除函数或改命名 | 热更依赖函数名匹配，结构变更易导致引用错乱
热更前保存全部文件 | 部分文件未保存即热更 | 多文件协同修改时，未保存文件不参与热更，可能导致模块间不一致

## 常见问题排查

现象 | 排查方向
---|---
点击按钮提示 “Connection not established” | 确认 PIE 客户端是否启动完成；连接列表可能被重新 PIE 清空后未重新注册，稍等片刻再试
热更提示 “LUA_CONSOLE_HOTRELOAD Require Failed” | 检查 Lua 文件语法是否正确（luaL_dostring 返回非 0 即报此错）
提示 “NewModule is Not a Table” | 模块返回值不是 table，例如直接 `return 1` 或文件末尾忘了 `return M`
函数已更新但变量没变化 | 这是设计行为：变量值被保留。如需重置请在 OnHotReload 中手动初始化
函数已更新但行为没变化 | 检查是否有定时器/协程引用了旧 closure；需在 OnHotReload 中重启
DS 收不到热更消息 | 确认是否有客户端已连接（DS 热更依赖客户端中转）；检查消息是否超长分块未重组完整
蓝图事件绑定的 Lua 函数热更后没生效 | 确认模块走的是 LuaBind 路径，非 LuaBind 模块的蓝图绑定不会自动更新
热更后部分模块生效、部分不生效 | 多文件协同修改时，确认所有改动文件均已保存；未保存文件不参与热更
