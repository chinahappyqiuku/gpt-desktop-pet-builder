# GPT Desktop Pet Builder · GPT 桌宠生成器

> **English**
> A production-minded, privacy-safe GPT Skill for turning a completed desktop-pet brief into reviewable character assets, animation plans, runtime integration, and a release-ready package.
>
> **中文**
> 一个面向 GPT 的生产级隐私安全 Skill：把填写完成的桌宠设定表，转化为可验收的人物素材、动作方案、运行时集成和可发布项目包。

## Overview / 项目简介

**English**

GPT Desktop Pet Builder turns an idea into a repeatable, approval-gated production workflow. It keeps visual generation, transparent RGBA cleanup, animation continuity, runtime behavior, QA, and packaging in one documented process.

**中文**

本项目把“想做一个桌宠”整理成可复用、分阶段验收的生产流程，覆盖视觉生成、透明 RGBA 素材修复、动作连续性、运行时行为、质量检查和最终打包。

## Workflow / 工作流

- **Brief → Default pose → Action draft → Final frames** / 设定表 → 默认动作 → 动作初稿 → 完整动作帧
- **RGBA asset QA**：透明背景、边缘、浅色袜子/鞋面、尺寸和帧顺序检查。
- **Continuity rules**：牵手、拖动、鼠标悬停、时间表和动作循环的一致性约束。
- **Runtime contract**：把动作、触发方式、时间段和资源命名整理成可实现的契约。
- **Release checklist**：发布前检查缺失肢体、场景道具、透明度、隐私内容和目录结构。

## Privacy and portrait rights / 隐私与肖像权

**English**

This public Skill contains only general methods and anonymous templates. It does **not** include the images, facial assets, generated frames, names, chat history, local paths, or API keys from any private desktop-pet project. If real people are used as references, keep the source photos and completed briefs in a private local directory and confirm that you have permission to use their likeness.

**中文**

本公开 Skill 只保留通用方法和匿名模板，**不包含任何私有桌宠项目的图片、脸部素材、生成帧、姓名、对话记录、个人路径或 API Key**。如果使用真实人物照片作为参考，请将照片和填写完成的表格保存在本地私有目录，并确认拥有肖像使用许可。不要把真人素材提交到公开 GitHub 仓库。

## Usage / 使用方式

Install this skill into your GPT/Codex Skills directory, then invoke:

~~~text
$gpt-desktop-pet-builder
~~~

Provide a completed project-brief-template.md, or ask GPT to create the brief first. The workflow pauses after the default pose and action-draft stages so you can review before more frames are produced.

安装到 GPT/Codex 的 Skills 目录后，使用上面的命令。提供一份填写好的 project-brief-template.md，或让 GPT 先创建表格；默认动作和动作初稿阶段会暂停等待验收。

## Validation / 本地验证

~~~powershell
python scripts/check_skill_privacy.py .
python scripts/validate_pet_assets.py path\\to\\cutouts\\manifest.json --actions-root path\\to\\actions
~~~

Before publishing, run the privacy check and manually confirm that the Skill directory contains no private images, completed briefs, caches, executables, or local machine paths.

发布前先通过隐私检查，并人工确认 Skill 目录中没有私有图片、已填写表格、缓存、可执行文件或本地路径。
