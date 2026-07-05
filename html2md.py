# -*- coding: utf-8 -*-
# 批量把【当前文件夹里】的 HTML 转成 Markdown(.md)
# 只处理本文件夹【根目录】下的 .html / .htm —— 绝不进子文件夹,绝不碰别处的文件
# 用法:把本文件、bat 和你的 html 放同一文件夹,双击 bat 即可。
# 结果存到同目录下的 md_output 子文件夹,原 html 文件一个不动。

import sys
import importlib.util
import subprocess
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


def ensure(import_name, pip_spec):
    """缺组件就自动 pip 安装"""
    if importlib.util.find_spec(import_name) is None:
        print(f"首次运行,正在安装 {pip_spec} …(要联网下载,请稍等,别关窗口)\n")
        subprocess.check_call([sys.executable, "-m", "pip", "install"] + pip_spec.split())
        print()


ensure("markdownify", "markdownify")
ensure("bs4", "beautifulsoup4")

from bs4 import BeautifulSoup
from markdownify import markdownify as to_md

base = Path(__file__).resolve().parent
out_dir = base / "md_output"


def read_text(p: Path) -> str:
    """尽量正确地读出网页文字(兼容 UTF-8 和中文 GBK 等编码)"""
    data = p.read_bytes()
    for enc in ("utf-8-sig", "utf-8", "gb18030"):
        try:
            return data.decode(enc)
        except UnicodeDecodeError:
            continue
    try:
        from charset_normalizer import from_bytes
        best = from_bytes(data).best()
        if best is not None:
            return str(best)
    except Exception:
        pass
    return data.decode("utf-8", errors="replace")


# 只扫当前文件夹【根目录】—— 用 iterdir,绝不递归子文件夹
htmls = sorted(
    p for p in base.iterdir()
    if p.is_file() and p.suffix.lower() in (".html", ".htm")
)

if not htmls:
    print("当前文件夹里没找到 .html / .htm 文件。")
    print(f"请把网页文件和本程序放在同一个文件夹:\n  {base}")
else:
    out_dir.mkdir(exist_ok=True)
    print(f"找到 {len(htmls)} 个 HTML 文件。")
    print("范围:只转当前文件夹,不进子目录、不碰别处。开始——\n")
    ok = 0
    for h in htmls:
        try:
            soup = BeautifulSoup(read_text(h), "html.parser")
            # 去掉脚本/样式等噪音,转出来更干净
            for tag in soup(["script", "style", "noscript"]):
                tag.decompose()
            md = to_md(str(soup), heading_style="ATX")
            # 收尾:去行尾空格 + 压掉多余空行
            md = "\n".join(line.rstrip() for line in md.splitlines())
            while "\n\n\n" in md:
                md = md.replace("\n\n\n", "\n\n")
            (out_dir / (h.stem + ".md")).write_text(md.strip() + "\n", encoding="utf-8")
            print(f"  ✓ {h.name}  →  {h.stem}.md")
            ok += 1
        except Exception as e:
            print(f"  ✗ {h.name}  失败: {e}")
    print(f"\n完成:成功 {ok}/{len(htmls)} 个。结果在这个文件夹里:\n  {out_dir}")
