from __builtins__ import *

clear()

while True:
	# 场地增加后 往北移动,检测到边缘后自动返回原点重新向北移动
	move(North)
	# 检测收获函数

	if can_harvest():
		harvest()