# 中文字词成语学习库 · Chinese Vocab & Idiom Library

一个面向中文学习者（中文作为外语 / 第二语言）的 **WorkBuddy 技能（Skill）**：当用户想认识一个汉字、弄懂一个词语、或理解一条成语时，给出结构清晰、准确易懂、带有画面感的讲解，并能生成「字卡 / 词卡 / 成语卡」。

> 本技能仅用于**中文学习辅助**，不用于品牌内容生产（品牌向内容请用 `hanyuwu-chinese` 技能）。

## 它能做什么

- **汉字字卡**：拼音（带声调）、部首、笔画、结构、造字法（象形 / 指事 / 会意 / 形声）、本义→义项、例词、字源小故事 / 记忆口诀。
- **词语词卡**：拼音、词性、释义、常用搭配、中英文对照例句、近义·反义 / 易混辨析。
- **成语卡**：拼音（每字标调）、字面义、引申义、出处·典故、中英文例句、近义·反义、易错点。
- 自带**起步库**（references/），命中即复用；库中没有的按统一字段规范现写，并标注「通行说法，建议核对权威出处」。

## 目录结构

```
chinese-vocab-idiom-library/
├── SKILL.md                    # 技能主文件（元数据 + 使用规范）
├── README.md                   # 本文件
├── references/
│   ├── characters.md           # 汉字起步库（象形/指事/会意/形声示例）
│   ├── words.md                # 词语起步库
│   ├── idioms.md               # 成语起步库（含出处典故与易错点）
│   └── output-templates.md     # 字卡/词卡/成语卡 输出模板
└── scripts/
    └── search.py               # 库检索工具（按汉字/拼音/关键字）
```

## 作为 WorkBuddy 技能使用

将本仓库克隆或下载后，把整个 `chinese-vocab-idiom-library/` 目录放入 WorkBuddy 的技能目录，例如：

- 用户级：`~/.workbuddy/skills/chinese-vocab-idiom-library/`
- 项目级：`<项目>/.workbuddy/skills/chinese-vocab-idiom-library/`

WorkBuddy 会在用户提出与汉字 / 词语 / 成语相关的学习请求时自动调用本技能（触发词如：汉字、字词、词语、成语、字卡、词卡、字源、部首、「XX 是什么意思」、「讲解成语 XX」等）。

## 使用检索脚本

库较大或想精确命中时，可用脚本快速检索（需 Python 3）：

```bash
python3 scripts/search.py "明"          # 按汉字检索
python3 scripts/search.py "pengyou"     # 按拼音（无调）检索
python3 scripts/search.py "huà shé"     # 按拼音（带调、含空格）检索
python3 scripts/search.py "画蛇"         # 按关键字检索成语
python3 scripts/search.py               # 列出库中全部条目
```

脚本会扫描 `references/` 并输出匹配的完整卡片片段，便于直接复用。

## 扩充词库（贡献）

欢迎持续扩充起步库，请**严格沿用各文件的既有格式**追加条目，不要破坏结构：

- 新增汉字 → `references/characters.md`
- 新增词语 → `references/words.md`
- 新增成语 → `references/idioms.md`

优先补充：多音字、易错形声字、易混词辨析、高频常用成语、易错读音成语。

## 说明

- 字库内容为学习参考，非考试标准答案；涉及繁简、异体字差异将简要说明。
- 不确定的字源、出处会标注「通行说法，建议核对《现代汉语词典》等权威出处」。

## License

MIT —— 可自由使用、修改、再分发。
