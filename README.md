# html2md — HTML 批量转 Markdown：把当前文件夹里的 `.html` / `.htm` 网页文件,一键批量转成 Markdown(`.md`)。不进子文件夹、不碰别处文件,原始 HTML 一个不动。

## 使用方法

1. 下载 `html2md.py` 和 `run_html2md.bat`,放进同一个文件夹
2. 把要转换的 HTML 文件也放进这个文件夹
3. 双击 `run_html2md.bat`,等待运行完成
4. 享受!转换结果在同目录的 `md_output` 文件夹里

## 说明

- 需要电脑装有 Python 3.12(Windows 可从 [python.org](https://www.python.org) 安装)
- 首次运行会自动联网安装依赖(markdownify、beautifulsoup4),请保持窗口开着别关
- 自动识别 UTF-8 / GBK 等中文编码,乱码问题基本不用管
