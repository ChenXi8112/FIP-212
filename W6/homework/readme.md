# W6 递归作业：提交到本仓库

把本周作业放在 `W6/homework/你的GitHub用户名/` 中，通过 Pull Request（PR）提交到 [seasideGargantua/FIP-212](https://github.com/seasideGargantua/FIP-212) 的 `main` 分支，等待教师审阅。

按课堂安排由每组记录员提交一份；如果教师要求个人提交，则每人提交一份。文件夹使用提交者的 GitHub 用户名，不使用学号、手机号等个人信息。

## 1. 准备作业文件

目录结构如下（把 `YOUR_GITHUB_USERNAME` 换成你的实际 GitHub 用户名）：

```text
W6/
└── homework/
    ├── readme.md                  ← 公共提交指南，请保留
    └── YOUR_GITHUB_USERNAME/      ← 只在自己的文件夹内修改
        ├── pascal.py
        └── README.md
```

`pascal.py` 提交本周**整行**杨辉三角实现：

- `pascal(n)`：输入非负整数，返回第 n 行列表；`n == 0` 返回 `[1]`；每层先把上一行计算一次并存入变量，再拼新行。
- `pascal_iter(n)`：提交迭代版。任务单的课后要求是“递归好写法 + 迭代版代码 + 速度对比”；尚未完成的部分须如实标注“未完成”。本周不要求格子版 `pascal(n, k)`。
- 用 `n = 0、1、3、4` 检查递归版，并对已完成的迭代版做同样检查。预期结果依次为 `[1]`、`[1, 1]`、`[1, 3, 3, 1]`、`[1, 4, 6, 4, 1]`。只有**实际运行且核对过**，才写“通过”。
- 坏写法计时代码可选，不要让默认运行一直卡在大输入上；小输入开始，过慢时中止并如实记录。

在你自己的 `README.md` 中填写：

1. 组别及分工（或注明个人提交），递归版与迭代版完成情况。
2. 手工推演 `pascal(0)` 到 `pascal(3)` 的每一行；说明课件坏写法计算 `pascal_bad(3)` 时，`pascal_bad(2)` 出现几次，以及为什么。
3. 测试输入、预期结果、**实际结果**及运行命令。
4. 一个错误示范：错误现象、原因、修改方法，以及用哪个测试验证修复。
5. 坏写法与好写法的速度对比及解释（几句话）：填写实际测量的输入、耗时、环境与运行次数；未运行的写“未测量”，过慢中止的写“已中止”，未完成的比较如实注明。理论调用次数应标注“理论推导”，不能当成实测耗时。
6. AI 使用说明：未使用则写“未使用”；使用了则说明工具、引用了哪个文件（`@pascal.py` 或等价引用）、AI 帮助的部分、自己手写与验证的部分。按课件要求最多让 AI 生成一种实现，另一种由本人手写。

## 2. Fork 并下载自己的副本

1. 登录 GitHub，打开 [本仓库](https://github.com/seasideGargantua/FIP-212)，点击右上角 **Fork → Create fork**，创建到自己账号。
2. 安装 Git 和 Python。在终端执行下列命令，先把所有 `YOUR_GITHUB_USERNAME` 换成你的实际用户名：

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/FIP-212.git
cd FIP-212
git remote add upstream https://github.com/seasideGargantua/FIP-212.git
git remote -v
```

检查：`origin` 指向**你的 Fork**，`upstream` 指向**教师仓库**。Fork、克隆与 PR 的关系可参考 [GitHub 官方 Fork 教程](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project)。

**以前已经克隆过？** 直接进入原有 `FIP-212` 目录，不要重复克隆。先运行 `git status`；若有已有修改，先妥善提交或保存，再切换分支。用 `git remote -v` 检查地址；已有 `upstream` 就不要重复 `remote add`。没有时才添加上面的 `upstream`。

## 3. 从教师仓库最新版本建立作业分支

确认现有修改已妥善保存、工作区干净，再执行：

```bash
git fetch upstream
git switch -c w6-YOUR_GITHUB_USERNAME upstream/main
```

这样即使你的 Fork 很早就创建，也会从教师仓库最新的 `main` 开始。若分支已存在并且这是同一份作业，使用 `git switch w6-YOUR_GITHUB_USERNAME` 继续；不要丢弃原有修改或覆盖分支。

创建自己的目录。macOS / Linux / Git Bash：

```bash
mkdir -p W6/homework/YOUR_GITHUB_USERNAME
```

Windows PowerShell：

```powershell
New-Item -ItemType Directory -Force W6/homework/YOUR_GITHUB_USERNAME
```

将你的 `pascal.py` 和作业说明 `README.md` 复制到该目录。不要覆盖 `W6/homework/readme.md`，不要修改其他同学的文件。

## 4. 本地运行、检查并上传

在仓库根目录运行自己的代码：

```bash
python3 W6/homework/YOUR_GITHUB_USERNAME/pascal.py
```

Windows 可将 `python3` 换成 `python` 或 `py`。确认脚本实际执行了上述测试；只有函数定义而没有调用，直接运行可能没有输出。把真实输出写入自己的 `README.md`。

检查文件后，只暂存自己的两个文件：

```bash
git status
git diff
git add W6/homework/YOUR_GITHUB_USERNAME/pascal.py W6/homework/YOUR_GITHUB_USERNAME/README.md
git diff --cached --check
git diff --cached --name-only
git diff --cached
```

确认暂存区只有自己目录中的两个作业文件；若出现其他已暂存文件，先用 `git restore --staged 文件路径` 撤出暂存区（会保留文件内容）。`git diff` 不显示尚未跟踪文件的内容，因此也要在编辑器中检查新文件。

```bash
git commit -m "W6: submit recursion homework by YOUR_GITHUB_USERNAME"
git push -u origin w6-YOUR_GITHUB_USERNAME
```

若 Git 首次要求身份，按提示配置自己的 Git 提交姓名与邮箱。HTTPS 推送需要 GitHub 身份验证，跟随浏览器或 Git Credential Manager 登录；已安装 GitHub CLI 的同学也可使用 `gh auth login`。GitHub 账号密码不能直接用作 Git 推送密码；不要把密码或令牌写入作业文件、命令示例或 PR。

## 5. 在 GitHub 发起 PR

推送后打开**你的 Fork**，点击 **Compare & pull request**；也可进入教师仓库的 **Pull requests → New pull request → compare across forks**。按 [GitHub 官方说明](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request-from-a-fork) 选择：

| 项目 | 应选内容 |
| --- | --- |
| base repository（接收作业） | `seasideGargantua/FIP-212` |
| base（目标分支） | `main` |
| head repository（你的作业） | `你的用户名/FIP-212` |
| compare（你的分支） | `w6-你的用户名` |

PR 标题可用 `W6 作业：你的用户名（组别）`。先看 **Files changed**，确认只包含自己的作业文件，再点击 **Create pull request**。PR 说明可用下面的模板，勾选前务必实际完成：

```markdown
## 本次作业
- 提交者 / 组别：
- 文件目录：W6/homework/我的GitHub用户名/
- 已完成内容：
- 未完成内容及原因：

## 验证
- [ ] 运行并核对了递归版 n=0、1、3、4
- [ ] 已完成的迭代版通过同样测试；若未完成，已在说明中标注
- [ ] README 中记录了手工推演、错误与修复、真实测试结果
- [ ] 速度对比区分了实测、理论推导和未测量
- [ ] 已如实说明 AI 使用情况
- [ ] Files changed 只包含自己的作业文件

运行命令：
实际结果：
需要老师帮助的问题：
```

把 **PR 链接**按课堂要求交给教师。PR 创建成功表示“已提交待审阅”；由教师决定是否合并，请不要自行点击 Merge。

## 6. 收到修改意见后怎么办？

在本地**同一个作业分支**修改，重新运行测试，再执行：

```bash
git add W6/homework/YOUR_GITHUB_USERNAME/pascal.py W6/homework/YOUR_GITHUB_USERNAME/README.md
git diff --cached --check
git diff --cached
git commit -m "W6: address review feedback"
git push
```

原 PR 会自动更新，不必为同一份修改重复创建 PR。在 PR 下说明改了什么、如何验证，等待教师再次审阅。

## 常见问题

- **推送提示没有权限**：用 `git remote -v` 检查 `origin` 是否误指向教师仓库；应推送到自己的 Fork，再发 PR。
- **找不到分支 / 提示没有差异**：确认已经 commit 并 push；再检查 PR 的接收方向和 compare 分支，不能把自己的 `main` 当成作业分支。
- **只在本地完成了作业**：commit 只保存到本地；push 上传到自己的 Fork；创建 PR 才是向教师仓库提交。
- **文件放错位置**：应为 `W6/homework/你的GitHub用户名/`；公共 `readme.md` 是本教程，自己的说明文件放在个人目录内。
- **出现冲突**：先保存工作，查看冲突文件；不确定时把报错和 PR 链接交给教师，不要强推或覆盖他人文件。
