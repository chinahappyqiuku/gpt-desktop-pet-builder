# GPT Desktop Pet Builder

这是一个 GPT 专属 Skill，用于把一份填写好的桌宠设定表转化为可验收的桌宠素材、动作配置和项目包。

它包含：

- 分阶段生成流程：默认动作 → 动作初稿 → 完整动作帧；
- 透明抠图、白色袜子/鞋面等浅色素材修复规则；
- 牵手、拖动、鼠标悬停、时间表和动作循环的连续性要求；
- 透明度、尺寸、帧顺序、缺失肢体、场景道具和发布内容检查；
- 空白填写表格、运行时契约、QA 清单和通用验证脚本。

## 重要隐私说明

本 Skill **不包含任何前两个桌宠的图片、脸部素材、生成帧、姓名、对话记录、个人路径或 API Key**。它只保留通用方法和匿名模板。

如果使用真实人物照片作为参考，请将照片保存在本地私有目录，并确认拥有肖像使用许可。不要把照片、生成出的真人脸部素材或填写完成的表格提交到公开 GitHub 仓库。

## 使用方式

安装到 GPT/Codex 的 Skills 目录后，使用：

```text
$gpt-desktop-pet-builder
```

然后提供一份填写好的 `project-brief-template.md`，或告诉 GPT 使用模板创建表格。Skill 会在默认动作和动作初稿阶段停下来等待验收。

## 本地验证

```powershell
python scripts/check_skill_privacy.py .
python scripts/validate_pet_assets.py path\to\cutouts\manifest.json --actions-root path\to\actions
```

发布前必须先通过隐私检查，并人工确认 Skill 目录中没有私有图片、表格、可执行文件、缓存或本地路径。
