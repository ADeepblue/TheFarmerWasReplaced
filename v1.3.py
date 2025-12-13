# -*- coding =utf-8 -*-
# @Time :2025/12/13 下午1:05
# @Author : deepblue
# @Files:v1.3.py
# @Software: PyCharm

# 1.4v
## 说明
# 种植灌木并收获灌木

from __builtins__ import *

while True:

    # 场地增加后 往北移动,检测到边缘后自动返回原点重新向北移动
    move(North)
    # 检测收获函数

    if can_harvest():
        harvest()