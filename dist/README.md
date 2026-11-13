# 技能包获取

仓库不直接存放二进制 zip（便于审查文本 diff），提供三种等价方式生成可直接上传 WorkBuddy 的 `chengshi-huoke-skill-public.zip`。任选其一。

## 方式 1：从 base64 还原（无需 clone，最省事）

不下载整个仓库，直接取技能包：

```bash
curl -L -o skill.b64 https://raw.githubusercontent.com/duwei56789/chengshi-huoke-mijue/main/dist/chengshi-huoke-skill-public.zip.b64
python -c "import base64; open('chengshi-huoke-skill.zip','wb').write(base64.b64decode(open('skill.b64').read()))"
```

已 clone 仓库的话，在仓库根目录执行：

```bash
python -c "import base64; from pathlib import Path; p=Path('dist/chengshi-huoke-skill-public.zip.b64'); Path('dist/chengshi-huoke-skill-public.zip').write_bytes(base64.b64decode(p.read_text()))"
```

## 方式 2：本地构建脚本（推荐维护者使用）

```bash
python scripts/build_zip.py
```

脚本从 `SKILL.md` 与 `references/*.md` 重新打包，并同步刷新 `.b64` 文件。仅需 Python 3 标准库。

## 方式 3：git archive

在仓库根目录执行（若技能包位于子目录，请改用方式 1 或 2，路径会不同）：

```bash
git archive --format=zip --prefix=baishu-chengshi-mijue/ \
  -o dist/chengshi-huoke-skill-public.zip HEAD SKILL.md references/
```

## 结构校验

```bash
python -c "import zipfile; print('\n'.join(zipfile.ZipFile('dist/chengshi-huoke-skill-public.zip').namelist()))"
```

期望输出（第一层必须是技能文件夹，不能多套一层）：

```
baishu-chengshi-mijue/SKILL.md
baishu-chengshi-mijue/references/book_index.md
baishu-chengshi-mijue/references/行业案例库.md
```

## 说明

- 文件夹名 `baishu-chengshi-mijue` 必须与 `SKILL.md` 里的 `name` 一致，否则平台解析失败。
- 公开版不含变现落地总纲（定价与私域 SOP），详见仓库根目录 README 第六节。
- `dist/*.zip` 已被 `.gitignore` 忽略，`.b64` 文件纳入版本控制，因此发版时需同时刷新两者。
