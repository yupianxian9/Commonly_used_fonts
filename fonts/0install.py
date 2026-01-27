#!/usr/bin/env python3
"""
简化版字体安装脚本
"""

import os
import sys
import shutil
import platform
from pathlib import Path

# 支持的字体格式
FONT_EXTS = {'.ttf', '.otf', '.ttc', '.otc', '.woff', '.woff2'}

def get_font_dir():
    """获取字体目录"""
    system = platform.system()
    home = Path.home()
    
    if system == 'Windows':
        # Windows用户字体目录
        return home / 'AppData' / 'Local' / 'Microsoft' / 'Windows' / 'Fonts'
    elif system == 'Darwin':
        # macOS用户字体目录
        return home / 'Library' / 'Fonts'
    else:
        # Linux用户字体目录
        return home / '.local' / 'share' / 'fonts'

def install_fonts_simple():
    """简化安装函数"""
    font_dir = get_font_dir()
    font_dir.mkdir(parents=True, exist_ok=True)
    
    current_dir = Path.cwd()
    font_files = [f for f in current_dir.iterdir() 
                  if f.is_file() and f.suffix.lower() in FONT_EXTS]
    
    if not font_files:
        print("未找到字体文件！")
        return
    
    print(f"找到 {len(font_files)} 个字体文件")
    print(f"将安装到: {font_dir}\n")
    
    installed = 0
    for font in font_files:
        dest = font_dir / font.name
        if dest.exists():
            print(f"跳过: {font.name} (已存在)")
            continue
        
        try:
            shutil.copy2(font, dest)
            print(f"安装: {font.name}")
            installed += 1
        except Exception as e:
            print(f"失败: {font.name} - {e}")
    
    print(f"\n完成！成功安装 {installed} 个字体")
    
    # 提示
    if platform.system() == 'Linux':
        print("\n提示: 运行 'fc-cache -fv ~/.local/share/fonts' 更新字体缓存")

if __name__ == "__main__":
    install_fonts_simple()