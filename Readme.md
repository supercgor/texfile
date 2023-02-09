# Here are all my $\LaTeX$ files.

To set up VScode, you may add this into config.

setting.json

    // ======================== LaTeX 设置 BEGIN  ========================
        // bibtex 格式
        "latex-workshop.bibtex-format.tab": "tab",
    
        // 自动编译，全部关闭，当且仅当你认为有需要的时候才会去做编译
        "latex-workshop.latex.autoBuild.run": "never",
        "latex-workshop.latex.autoBuild.cleanAndRetry.enabled": false,
    
        // 这是一些独立的编译选项，可以作为工具被编译方案调用
        "latex-workshop.latex.tools": [
            {
                // Windows 原生安装 TeX Live 2020 的编译选项
                "name": "Windows XeLaTeX",
                "command": "xelatex",
                "args": [
                    "-synctex=1",
                    "-interaction=nonstopmode",
                    "-file-line-error",
                    "-pdf",
                    "%DOCFILE%"
                ]
            },
            {
                // Windows Biber 编译
                "name": "Windows Biber",
                "command": "biber",
                "args": [
                    "%DOCFILE%"
                ]
            },
            {
                // WSL XeLaTeX 编译一般的含有中文字符的文档
                "name": "WSL XeLaTeX",
                "command": "wsl",
                "args": [
                    "/usr/local/texlive/2020/bin/x86_64-linux/xelatex",
                    "-synctex=1",
                    "-interaction=nonstopmode",
                    "-file-line-error",
                    "-pdf",
                    //"-output-directory=%OUTDIR%",
                    //"-aux-directory=%OUTDIR%",
                    "%DOCFILE%"
                ]
            },
            {
                // WSL biber / bibtex 编译带有 citation 标记项目的文档
                "name": "WSL Biber",
                "command": "wsl",
                "args": [
                    "/usr/local/texlive/2020/bin/x86_64-linux/biber",
                    "%DOCFILE%"
                ]
            },
            {
                // macOS 或者 Linux 的简单编译
                // 两种操作系统的操作方式相同
                "name": "macOS / Linux XeLaTeX",
                "command": "xelatex",
                "args": [
                    "-synctex=1",
                    "-interaction=nonstopmode",
                    "-file-line-error",
                    "-pdf",
                    "%DOCFILE%"
                ]
            },
            {
                // macOS 或者 Linux 的索引编译
                // 两种操作系统的操作方式相同
                "name": "macOS / Linux Biber",
                "command": "biber",
                "args": [
                    "%DOCFILE%"
                ]
            }
        ],
    
        // 这是一些编译方案，会出现在 GUI 菜单里
        "latex-workshop.latex.recipes": [
            {
                // 1.1 Windows 编译简单的小文档，这个选项不太常用，因为绝大多数文章都需要有参考文献索引
                "name": "Windows XeLaTeX 简单编译",
                "tools": [
                    "Windows XeLaTeX"
                ]
            },
            {
                // 1.2 Windows 编译带有索引的论文，需要进行四次编译；-> 符号只是一种标记而已，没有程序上的意义
                "name": "Windows xe->bib->xe->xe 复杂编译",
                "tools": [
                    "Windows XeLaTeX",
                    "Windows Biber",
                    "Windows XeLaTeX",
                    "Windows XeLaTeX"
                ]
            },
            {
                // 2.1  WSL 编译简单的小文档，这个选项不太常用，因为我绝大多数文章都需要有引用。
                "name": "XeLaTeX 简单编译",
                "tools": [
                    "WSL XeLaTeX"
                ]
            },
            {
                // 2.2 带有 citation 索引的文档，需要进行四次编译；-> 符号只是一种标记而已，没有程序上的意义
                "name": "xe->bib->xe->xe 复杂编译",
                "tools": [
                    "WSL XeLaTeX",
                    "WSL Biber",
                    "WSL XeLaTeX",
                    "WSL XeLaTeX"
                ]
            },
            {
                // 3.1 macOS 简单 小文档
                "name": "macOS XeLaTeX 简单编译",
                "tools": [
                    "macOS XeLaTeX"
                ]
            },
            {
                // 3.2 macOS 四次编译
                "name": "macOS xe->bib->xe->xe 复杂编译",
                "tools": [
                    "macOS / Linux XeLaTeX",
                    "macOS / Linux Biber",
                    "macOS / Linux XeLaTeX",
                    "macOS / Linux XeLaTeX"
                ]
            }
        ],
    
        "latex-workshop.latex.clean.fileTypes": [
            "*.aux",
            "*.bbl",
            "*.blg",
            "*.idx",
            "*.ind",
            "*.lof",
            "*.lot",
            "*.out",
            "*.toc",
            "*.acn",
            "*.acr",
            "*.alg",
            "*.glg",
            "*.glo",
            "*.gls",
            "*.ist",
            "*.fls",
            "*.log",
            "*.fdb_latexmk"
        ],
        //设置为onFaild 在构建失败后清除辅助文件
        "latex-workshop.latex.autoClean.run": "onBuilt",
    // ======================== LaTeX 设置 END ========================

Then, you have to link the fonts and texmf to special dir

    ln -s /home/supercgor/gitfile/texfile/texmf/ /home/supercgor/texmf
    sudo ln -s /home/supercgor/gitfile/texfile/fonts/ /usr/local/share/fonts