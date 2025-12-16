from __builtins__ import *
from utils import *

# parameter setting
# Cactus_Water_Level = 0.6

# main
# clear()
#
world_size = 8
set_world_size(world_size)
# till the field

def judge_move_function():
	x = get_pos_x()
	y=  get_pos_y()
	# 最下面一行,除开y=0时全部上移
	if y == 0:
		# 0处
		if x % world_size != 0:
			move(West)
		else:
			move(North)
	# 倒数第二行,除开两头,左边边缘上移,右边边缘下移
	elif y==1:
		# 右边边缘
		if (x+1) % world_size ==0:
			move(South)
		else:
			# 最左边和马上要通上去的地方
			if x % 2 == 0:
				move(North)
			# 否则右移
			else:
				move(East)
	# 最上面一行
	elif y == world_size -1:
		# 最左边和偶数位置右移
		if x % 2 ==0:
			move(East)
		# 最右边和奇数位置下移
		else:
			move(South)
	# 其余行
	else:
		if x % 2 ==0:
			move(North)
		else:
			move(South)

while True:
	judge_move_function()