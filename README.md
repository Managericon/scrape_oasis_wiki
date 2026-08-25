# Tencent Oasis Wiki crawler

面向腾讯绿洲启元教程 Wiki `catalog/20418` 与 API Wiki 的 Markdown
知识库和 OpenAI Vector Store 同步工作流。

## 工作流

1. Playwright 启动 Chromium 并等待 Vue/Element UI 目录树渲染。
2. 递归展开 `.el-tree`，从叶子节点的 `data-key` 获取全部文章 ID 与分类路径。
3. 依次访问 `#/catalog/{id}`，只提取 `.github-markdown-body` 正文。
4. 使用 `html2text` 转换 Markdown；代码块保留语言围栏，图片转换为绝对链接或下载到本地。
5. 分文档保存、生成合并文档，并按内容哈希增量同步到 OpenAI Vector Store。
6. 从 API Wiki 官方静态 JSON 索引完整发现类、枚举、结构体和全局函数，分类生成 Markdown 与语义索引分片。

## 本地运行

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium

python scripts/crawl_wiki.py --output-dir knowledge --force --prune-output
python scripts/crawl_api_wiki.py --output-dir knowledge/api --force --prune-output
```

测试少量文档：

```powershell
python scripts/crawl_wiki.py --output-dir knowledge --limit 3 --force
```

按文章 ID 定点抓取：

```powershell
python scripts/crawl_wiki.py --output-dir knowledge --article-id 20351 --force
```

下载图片并改写为本地相对路径：

```powershell
python scripts/crawl_wiki.py --output-dir knowledge --download-images --force
```

生成内容：

- `knowledge/catalog.json`：完整目录、文章 ID、URL 和分类路径。
- `knowledge/articles/**/*.md`：分类保存的 Markdown 正文。
- `knowledge/all_articles.md`：全部文档合并文件。
- `knowledge/manifest.json`：抓取状态、代码块、图片数量与 SHA-256。

## Vector Store

配置 `OPENAI_API_KEY` 后执行：

```powershell
python scripts/vector_store.py --state knowledge/vector_store.json sync `
  --directory knowledge/articles --directory knowledge/api/chunks --prune

python scripts/vector_store.py --state knowledge/vector_store.json search `
  "UGCGameSystem 如何使用"
```

首次同步会创建 Vector Store；后续只上传内容哈希发生变化的 Markdown，并把非敏感的
`vector_store_id` 与文件映射保存到 `knowledge/vector_store.json`。API Key 不会写入文件。

OpenAI 官方接口参考：[Vector Stores](https://developers.openai.com/api/reference/resources/vector_stores)。

## GitHub Actions

`.github/workflows/crawl-and-index.yml` 每周运行，也支持手动触发。要启用知识库上传，
在仓库 `Settings > Secrets and variables > Actions` 中添加 `OPENAI_API_KEY` secret。
没有该 secret 时，爬取和 Markdown 提交仍会正常执行，只跳过 Vector Store 同步。

## Agent skill

`skills/oasis-wiki-knowledge` 可作为 Codex skill 安装。它优先搜索本地 Markdown，
本地语料不存在时使用 Vector Store 语义检索，并返回原始 Wiki 来源链接。

```powershell
Copy-Item -Recurse .\skills\oasis-wiki-knowledge "$env:USERPROFILE\.codex\skills\"
```

