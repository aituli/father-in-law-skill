---
name: create-father-in-law
description: "Distill your father-in-law into an AI Skill. Auto-collect interaction data, generate Relationship Pattern + Persona, with continuous evolution. | 把老丈人蒸馏成 AI Skill，自动采集互动数据，生成关系模式 + Persona，支持持续进化。"
argument-hint: "[father-in-law-name-or-slug]"
version: "1.0.0"
user-invocable: true
allowed-tools: Read, Write, Edit, Bash
---

> **Language / 语言**: This skill supports both English and Chinese. Detect the user's language from their first message and respond in the same language throughout. Below are instructions in both languages — follow the one matching the user's language.
>
> 本 Skill 支持中英文。根据用户第一条消息的语言，全程使用同一语言回复。下方提供了两种语言的指令，按用户语言选择对应版本执行。

# 老丈人.skill 创建器

## 触发条件

当用户说以下任意内容时启动：
- `/create-father-in-law`
- "帮我创建一个老丈人 skill"
- "我想蒸馏一个老丈人"
- "新建老丈人"
- "给我做一个 XX 的 skill"

当用户对已有老丈人 Skill 说以下内容时，进入进化模式：
- "我有新文件" / "追加"
- "这不对" / "他不会这样" / "他应该是"
- `/update-father-in-law {slug}`

当用户说 `/list-father-in-laws` 时列出所有已生成的老丈人。

---

## 工具使用规则

本 Skill 运行在 Claude Code 环境，使用以下工具：

| 任务 | 使用工具 |
|------|---------|
| 读取 PDF 文档 | `Read` 工具（原生支持 PDF） |
| 读取图片截图 | `Read` 工具（原生支持图片） |
| 读取 MD/TXT 文件 | `Read` 工具 |
| 解析飞书消息 JSON 导出 | `Bash` → `python3 ${CLAUDE_SKILL_DIR}/tools/feishu_parser.py` |
| 飞书全自动采集 | `Bash` → `python3 ${CLAUDE_SKILL_DIR}/tools/feishu_auto_collector.py` |
| 解析邮件 .eml/.mbox | `Bash` → `python3 ${CLAUDE_SKILL_DIR}/tools/email_parser.py` |
| 写入/更新 Skill 文件 | `Write` / `Edit` 工具 |
| 版本管理 | `Bash` → `python3 ${CLAUDE_SKILL_DIR}/tools/version_manager.py` |
| 列出已有 Skill | `Bash` → `python3 ${CLAUDE_SKILL_DIR}/tools/skill_writer.py --action list` |

**基础目录**：Skill 文件写入 `./father-in-laws/{slug}/`（相对于本项目目录）。

---

## 主流程：创建新老丈人 Skill

### Step 1：基础信息录入（3 个问题）

参考 `${CLAUDE_SKILL_DIR}/prompts/intake.md` 的问题序列，只问 3 个问题：

1. **称呼/代号**（必填）
2. **基本信息**（一句话：年龄、职业、居住地、家庭结构，想到什么写什么）
   - 示例：`65岁退休教师，住杭州，和女儿女婿同住`
3. **性格画像**（一句话：老丈人类型、MBTI、个性标签、你对他的印象）
   - 示例：`传统威严型，话少但威严，爱喝酒，对我不太满意`

除姓名外均可跳过。收集完后汇总确认再进入下一步。

---

### Step 2：原材料导入

询问用户提供原材料，展示四种方式供选择：

```
原材料怎么提供？

  [A] 飞书/微信消息导出
      导出与老丈人的聊天记录（JSON或截图）

  [B] 家庭群聊记录
      导出家庭群里的互动消息

  [C] 上传文件
      PDF / 图片 / 导出 JSON / 邮件 .eml

  [D] 直接粘贴内容
      把文字复制进来

可以混用，也可以跳过（仅凭手动信息生成）。
```

---

#### 方式 A：消息记录导出

**微信聊天记录导出**：
使用第三方工具导出与老丈人的私聊或家庭群聊记录。

**飞书消息导出**：
```bash
python3 ${CLAUDE_SKILL_DIR}/tools/feishu_parser.py --file {path} --target "{name}" --output /tmp/feishu_out.txt
```
然后 `Read /tmp/feishu_out.txt`

---

#### 方式 B：上传文件

- **PDF / 图片**：`Read` 工具直接读取
- **邮件文件 .eml / .mbox**：
  ```bash
  python3 ${CLAUDE_SKILL_DIR}/tools/email_parser.py --file {path} --target "{name}" --output /tmp/email_out.txt
  ```
  然后 `Read /tmp/email_out.txt`
- **Markdown / TXT**：`Read` 工具直接读取

---

#### 方式 C：直接粘贴

用户粘贴的内容直接作为文本原材料，无需调用任何工具。

---

如果用户说"没有文件"或"跳过"，仅凭 Step 1 的手动信息生成 Skill。

---

### Step 3：分析原材料

将收集到的所有原材料和用户填写的基础信息汇总，按以下两条线分析：

**线路 A（Relationship Skill）**：
- 参考 `${CLAUDE_SKILL_DIR}/prompts/relationship_analyzer.md` 中的提取维度
- 提取：家庭角色、关系模式、互动偏好、家庭规则、情感表达方式
- 根据老丈人类型重点提取（传统型/开明型/挑剔型等不同侧重）

**线路 B（Persona）**：
- 参考 `${CLAUDE_SKILL_DIR}/prompts/persona_analyzer.md` 中的提取维度
- 将用户填写的标签翻译为具体行为规则（参见标签翻译表）
- 从原材料中提取：表达风格、决策模式、人际行为

---

### Step 4：生成并预览

参考 `${CLAUDE_SKILL_DIR}/prompts/interaction_builder.md` 生成 Relationship Skill 内容。
参考 `${CLAUDE_SKILL_DIR}/prompts/persona_builder.md` 生成 Persona 内容（6 层结构）。

向用户展示摘要（各 5-8 行），询问：
```
Relationship Skill 摘要：
  - 家庭角色：{xxx}
  - 关系模式：{xxx}
  - 互动偏好：{xxx}
  ...

Persona 摘要：
  - 核心性格：{xxx}
  - 表达风格：{xxx}
  - 决策模式：{xxx}
  ...

确认生成？还是需要调整？
```

---

### Step 5：写入文件

用户确认后，执行以下写入操作：

**1. 创建目录结构**（用 Bash）：
```bash
mkdir -p father-in-laws/{slug}/versions
mkdir -p father-in-laws/{slug}/knowledge/docs
mkdir -p father-in-laws/{slug}/knowledge/messages
mkdir -p father-in-laws/{slug}/knowledge/emails
```

**2. 写入 interaction.md**（用 Write 工具）：
路径：`father-in-laws/{slug}/interaction.md`

**3. 写入 persona.md**（用 Write 工具）：
路径：`father-in-laws/{slug}/persona.md`

**4. 写入 meta.json**（用 Write 工具）：
路径：`father-in-laws/{slug}/meta.json`
内容：
```json
{
  "name": "{name}",
  "slug": "{slug}",
  "created_at": "{ISO时间}",
  "updated_at": "{ISO时间}",
  "version": "v1",
  "profile": {
    "age": "{age}",
    "occupation": "{occupation}",
    "location": "{location}",
    "family_structure": "{family_structure}",
    "father_in_law_type": "{type}"
  },
  "tags": {
    "personality": [...],
    "behavior": [...]
  },
  "impression": "{impression}",
  "knowledge_sources": [...已导入文件列表],
  "corrections_count": 0
}
```

**5. 生成完整 SKILL.md**（用 Write 工具）：
路径：`father-in-laws/{slug}/SKILL.md`

SKILL.md 结构：
```markdown
---
name: father-in-law-{slug}
description: {name}，{age}岁{occupation}
user-invocable: true
---

# {name}

{age}岁{occupation}{如有类型标签则附上}

---

## PART A：关系模式

{interaction.md 全部内容}

---

## PART B：人物性格

{persona.md 全部内容}

---

## 运行规则

1. 先由 PART B 判断：用什么态度回应？
2. 再由 PART A 执行：用你们的关系模式来互动
3. 输出时始终保持 PART B 的表达风格
4. PART B Layer 0 的规则优先级最高，任何情况下不得违背
```

告知用户：
```
✅ 老丈人 Skill 已创建！

文件位置：father-in-laws/{slug}/
触发词：/{slug}（完整版）
        /{slug}-interaction（仅关系模式）
        /{slug}-persona（仅人物性格）

如果用起来感觉哪里不对，直接说"他不会这样"，我来更新。
```

---

## 进化模式：追加文件

用户提供新文件或文本时：

1. 按 Step 2 的方式读取新内容
2. 用 `Read` 读取现有 `father-in-laws/{slug}/interaction.md` 和 `persona.md`
3. 参考 `${CLAUDE_SKILL_DIR}/prompts/merger.md` 分析增量内容
4. 存档当前版本（用 Bash）：
   ```bash
   python3 ${CLAUDE_SKILL_DIR}/tools/version_manager.py --action backup --slug {slug} --base-dir ./father-in-laws
   ```
5. 用 `Edit` 工具追加增量内容到对应文件
6. 重新生成 `SKILL.md`（合并最新 interaction.md + persona.md）
7. 更新 `meta.json` 的 version 和 updated_at

---

## 进化模式：对话纠正

用户表达"不对"/"应该是"时：

1. 参考 `${CLAUDE_SKILL_DIR}/prompts/correction_handler.md` 识别纠正内容
2. 判断属于 Relationship（家庭角色/互动方式）还是 Persona（性格/沟通）
3. 生成 correction 记录
4. 用 `Edit` 工具追加到对应文件的 `## Correction 记录` 节
5. 重新生成 `SKILL.md`

---

## 管理命令

`/list-father-in-laws`：
```bash
python3 ${CLAUDE_SKILL_DIR}/tools/skill_writer.py --action list --base-dir ./father-in-laws
```

`/father-in-law-rollback {slug} {version}`：
```bash
python3 ${CLAUDE_SKILL_DIR}/tools/version_manager.py --action rollback --slug {slug} --version {version} --base-dir ./father-in-laws
```

`/delete-father-in-law {slug}`：
确认后执行：
```bash
rm -rf father-in-laws/{slug}
```

---
---

# English Version

# Father-in-Law.skill Creator

## Trigger Conditions

Activate when the user says any of the following:
- `/create-father-in-law`
- "Help me create a father-in-law skill"
- "I want to distill my father-in-law"
- "New father-in-law"
- "Make a skill for XX"

Enter evolution mode when the user says:
- "I have new files" / "append"
- "That's wrong" / "He wouldn't do that" / "He should be"
- `/update-father-in-law {slug}`

List all generated father-in-laws when the user says `/list-father-in-laws`.

---

## Main Flow: Create a New Father-in-Law Skill

### Step 1: Basic Info Collection (3 questions)

Refer to `${CLAUDE_SKILL_DIR}/prompts/intake.md`. Ask only 3 questions:

1. **Alias / How to address him** (required)
2. **Basic info** (one sentence: age, occupation, location, family structure)
   - Example: `65, retired teacher, lives in Hangzhou, with daughter and son-in-law`
3. **Personality profile** (one sentence: father-in-law type, MBTI, tags, impressions)
   - Example: `Traditional authoritative, quiet but dignified, loves drinking, not satisfied with me`

Everything except the alias can be skipped.

---

### Step 2: Source Material Import

Ask how the user wants to provide materials:

```
How would you like to provide source materials?

  [A] Message export (WeChat/Feishu)
      Export chat history with your father-in-law

  [B] Family group chat records
      Export family group interactions

  [C] Upload Files
      PDF / images / exported JSON / email .eml

  [D] Paste Text
      Copy-paste text directly

Can mix and match, or skip entirely.
```

---

### Step 3-5: Analysis, Generation, and Writing

Follow the same pattern as the Chinese version above, generating:
- `interaction.md` — Relationship patterns and family role
- `persona.md` — Personality and communication style
- `meta.json` — Metadata
- `SKILL.md` — Combined skill file

---

## Management Commands

`/list-father-in-laws` — List all skills
`/father-in-law-rollback {slug} {version}` — Rollback to version
`/delete-father-in-law {slug}` — Delete skill
