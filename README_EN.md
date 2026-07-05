[中文](./README.md) | **English**

# Html-batch-to-md — Batch convert HTML to Markdown

Converts all `.html` / `.htm` files in the current folder to Markdown (`.md`) in one click.
Only processes the folder's root directory — never touches subfolders or files elsewhere. Your original HTML files stay untouched.

## How to use

1. Download `html2md.py` and `run_html2md.bat` into the same folder
2. Put the HTML files you want to convert into that folder
3. Double-click `run_html2md.bat` and wait for it to finish
4. Enjoy! Results are saved in the `md_output` subfolder

## Notes

- Requires Python 3.12 installed (Windows users can get it from [python.org](https://www.python.org))
- On first run, it automatically installs dependencies (markdownify, beautifulsoup4) — keep the window open until done
- Automatically detects UTF-8 / GBK and other Chinese encodings, so garbled text is rarely an issue
