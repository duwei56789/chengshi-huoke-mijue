# 成事获客秘诀

> 把 104 本跨文明经典读薄成一套「遇事该用哪条底层逻辑、今天先做哪一件小事」的行动清单。

WorkBuddy 技能（Skill）· v1.0.1 · 纯提示词实现，零运行时依赖。

> **获取方式**：本技能包按独立仓库 `chengshi-huoke-mijue` 组织。若你拿到的是托管在其他仓库子目录下的副本，先 `cd` 进入该子目录，再执行下文命令即可，内容完全一致。

---

## 一、技能用途

面向个体工商户、小微创业者和普通人，处理经营与自我管理中的具体卡点：客流下滑、竞争内卷、合伙识人、价值定价、拖延内耗、留不住钱、决策纠结。

技能不替你读书，也不给鸡汤。它做三件事：**定位卡点 → 调一条元规则 → 给一个今天就能完成的最小动作**。

### 底层框架

| 层 | 内容 | 作用 |
|---|---|---|
| 七条定律 | 认知透镜律、人性五力律、价值交换律、系统复利律、时间杠杆律、信任资本律、势能集中律 | 判断「这件事的根本规律是什么」 |
| 六步回路 | 0 定锚 → 1 修内 → 2 识人 → 3 做值 → 4 建系 → 5 借势 → 6 守信 | 定位「现在卡在哪一步」 |
| 场景速查表 | 10 类高频困境 → 对应定律 + 元规则 + 今日小事 | 快速给出可执行的下一步 |

### 固定输出格式

每次调用输出四段，不空谈：

1. **一句话诊断**（你卡在哪）
2. **一条元规则**（标注对应第几条定律）
3. **今天能做的一件事**（单动作、当天可完成）
4. **可选原书推荐**（从 104 本书单中溯源）

### 边界

- 不虚构营业额、增长率、客户数等「已验证案例」数据，不承诺收益。
- 权谋类内容（厚黑、罗织、鬼谷子）仅用于识坑自保，不用于算计他人。
- 涉及医疗、法律、具体投资标的时，明确声明「本技能是心法，不是专业建议」。
- 不是聊天陪伴或知识问答工具，它只在遇到具体实务卡点时有用。

---

## 二、目录结构

```
chengshi-huoke-mijue/
├── SKILL.md                  # 技能定义（YAML frontmatter + 执行指令）
├── references/
│   ├── book_index.md         # 104 本经典分类索引（作者 + 一句话内核）
│   └── 行业案例库.md         # 四类行业的诊断模板与红线
├── examples/                 # 三则完整的调用示例
│   ├── 01-客流下滑.md
│   ├── 02-合伙识人.md
│   └── 03-拖延内耗.md
├── scripts/
│   └── build_zip.py          # 一键生成可上传的技能包
├── dist/
│   ├── README.md             # 获取技能包的三种方式
│   └── chengshi-huoke-skill-public.zip.b64   # 技能包（base64 文本形式）
├── CHANGELOG.md
├── LICENSE                   # MIT
└── .gitignore
```

技术 ID 沿用 `baishu-chengshi-mijue`（历史资产标识），市场展示名为「成事获客秘诀」。两者不同是有意为之：技术 ID 必须与技能目录名一致，且已注册资产不宜随意更换。

---

## 三、安装方法

### 方式 A：上传技能包（推荐，最省事）

1. 取得 `dist/chengshi-huoke-skill-public.zip`，获取方式见 [dist/README.md](dist/README.md)（可直接从 `.b64` 还原，或运行 `python scripts/build_zip.py` 生成）。
2. 打开 WorkBuddy 左侧 **「专家·技能·连接器」** → **「技能」** 页签。
3. 点 **「添加技能」** → **「上传技能」**，选择该 zip，导入后系统自动完成配置。
4. 新建任务，在输入框敲 `/`，选中「成事获客秘诀」即可提问。

zip 解压后的第一层必须是技能文件夹（`baishu-chengshi-mijue/`），`dist/` 里提供的包已符合此结构。

### 方式 B：从源码放置到技能目录

```bash
git clone https://github.com/duwei56789/chengshi-huoke-mijue.git
cd chengshi-huoke-mijue

# Windows（Git Bash / PowerShell 均可，注意目标目录名须与技术 ID 一致）
mkdir -p "$USERPROFILE/.workbuddy/skills/baishu-chengshi-mijue/references"
cp SKILL.md "$USERPROFILE/.workbuddy/skills/baishu-chengshi-mijue/"
cp references/*.md "$USERPROFILE/.workbuddy/skills/baishu-chengshi-mijue/references/"

# macOS / Linux
mkdir -p ~/.workbuddy/skills/baishu-chengshi-mijue/references
cp SKILL.md ~/.workbuddy/skills/baishu-chengshi-mijue/
cp references/*.md ~/.workbuddy/skills/baishu-chengshi-mijue/references/
```

然后**新开一个任务**（技能列表在会话启动时加载），在「已安装」中确认开关为启用。

### 方式 C：技能市场

若该技能已在 WorkBuddy 开放平台上架，在「技能市场」搜索「成事获客秘诀」，点卡片右上角 `+` 安装即可。

### 安装验证

| 检查项 | 预期结果 |
|---|---|
| 「专家·技能·连接器」→「技能」→「已安装」 | 出现「成事获客秘诀」，开关为开启 |
| 新任务输入框敲 `/` | 列表里能选到该技能 |
| 发送「我开包子店，最近客流掉了一半」 | 返回四段式输出，且包含一件今天可做的小事 |

若列表仍显示旧名或未出现：确认目录名与 `name` 一致、技能未处于关闭状态，然后重启客户端让列表重新扫描。

---

## 四、使用示例

```
我开包子店，最近客流掉了一半，用成事获客秘诀帮我看看
```

技能会先识别身份（个体工商户）与卡点（客户太少），定位到「5 借势」，再输出：

> **一句话诊断**：客流掉一半不是产品坏了，是获客动作散在多个渠道、没有一处形成势能。
>
> **一条元规则**（定律 7 · 势能集中律）：不平均用力，先把有限资源集中到能当第一的那一个渠道。
>
> **今天能做的一件事**：只选 1 个渠道（如门店周边社群），连续测 7 天，每天记录进店人数，不做其他渠道动作。
>
> **可选原书**：《定位》《流量池》

更多完整示例：

- [01-客流下滑.md](examples/01-客流下滑.md) —— 借势 · 获客五环
- [02-合伙识人.md](examples/02-合伙识人.md) —— 识人 · 人性五力律
- [03-拖延内耗.md](examples/03-拖延内耗.md) —— 修内 · 时间杠杆律

技能也支持自动触发：直接描述困境（不写技能名），WorkBuddy 会按 `description` 里的触发词匹配调用。

---

## 五、依赖与配置要求

| 项 | 要求 |
|---|---|
| 运行环境 | WorkBuddy 客户端，或任何兼容 `SKILL.md` 开放格式的 Agent |
| 运行时依赖 | **无**：无脚本、无 npm/pip 包、无外部 API、无网络请求 |
| 凭证 / API Key | **不需要**，无任何第三方凭据或授权步骤 |
| 权限范围 | 仅按需读取技能目录内的 `references/*.md`；不写文件、不执行系统命令、不联网 |
| 文件编码 | UTF-8（无 BOM）；`SKILL.md` 的 YAML frontmatter 必须保留 |
| 构建步骤 | 无需构建；仅在需要重新打包时运行 `python scripts/build_zip.py` |
| 打包工具 | Python 3 标准库（`zipfile`），或 `git archive`；不需要第三方依赖 |
| 体积 | 约 50 KB（含书单索引） |
| 客户端配置 | 技能开关需为「启用」；关闭后仅影响新会话，已加载的会话仍可调用 |

`SKILL.md` 的必填 frontmatter 字段：`name`、`display_name`、`display_name_en`、`description`、`description_zh`、`description_en`、`version`、`author`。字段大小写敏感，YAML 用两个空格缩进，冒号后需有一个空格。

---

## 六、公开版说明

本仓库为**公开分发版**，与作者本机完整版有一处差异：

- 未包含 `references/全链路落地项目.md`（内含付费产品定价、私域 SOP 与变现闭环设计）。
- 公开版 `SKILL.md` 第七节已移除该文件的引用，并加了说明行，避免出现失效引用。
- 影响范围：仅「怎么用这套方法做项目 / 引流 / 变现」这一专项场景没有落地模板。七条定律、六步回路、场景速查表、行业诊断模板与 104 本书单**全部保留**。

---

## 七、维护与发布

### 提交信息规范

采用 [Conventional Commits](https://www.conventionalcommits.org/)：`<type>(<scope>): <subject>`，正文用列表说明改动。

```
feat(skill): 新增 XX 场景的元规则
docs(readme): 补充 Windows 安装命令
fix(skill): 修正第七节失效引用
chore(release): 发布 v1.0.2
```

`type` 取 `feat / fix / docs / chore / refactor / test`；破坏性变更在正文写明 `BREAKING CHANGE:`。

### 发版步骤

1. 修改 `SKILL.md`（或 `references/`），同步更新 `SKILL.md` 的 `version`、`CHANGELOG.md`、README 顶部版本号。
2. 重新生成技能包：`python scripts/build_zip.py`，并刷新 `dist/*.b64`（见 dist/README.md）。
3. 本地提交：
   ```bash
   git add .
   git commit -m "feat(skill): 新增 XX 场景的元规则"
   git tag v1.0.2
   git push origin main --tags
   ```
4. 在 GitHub Releases 基于该 tag 新建 Release，把 `dist/*.zip` 作为附件上传，Release Notes 摘自 CHANGELOG。
5. 若同步开放平台，需在「更新版本」入口上传新包，版本号必须高于平台当前版本。

---

## 八、常见问题

**Q：技能装在「已安装」里但对话不触发？**
检查开关是否启用、是否在新会话中使用；关闭的技能不会出现在对话查询结果里。

**Q：显示的是英文 ID 而不是中文名？**
部分内部清单按技术 ID `baishu-chengshi-mijue` 列出，客户端「已安装」页按 `display_name` 显示中文，属正常现象。

**Q：中文乱码？**
确认文件保存为 UTF-8 无 BOM，且未被编辑器转换编码。

**Q：能用于其他 Agent 吗？**
可以。`SKILL.md` 是开放格式，把 `SKILL.md` 与 `references/` 一起放到对应 Agent 的技能目录即可，无需修改内容。

---

## 九、许可证与声明

- 代码与文档采用 [MIT License](LICENSE)。
- 104 本经典著作的书名、作者及思想归各自权利人所有；本仓库仅做方法论整理与索引，不摘录原文，不替代原书。
- 本技能提供的是心法与行动建议，不构成投资、法律、医疗或经营收益承诺；请结合自身实际情况判断。
