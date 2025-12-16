from __builtins__ import *
from utils import *

# main
clear()
world_size = 32
set_world_size(world_size)


# plant all cactus
def line_plant_task():
	for row_index in range(world_size):
		plant(Entities.Cactus)
		move(East)

for _ in range(world_size-1):
	tiny_sleep()
	spawn_drone(line_plant_task)
	move(North)

line_plant_task()

# 判断移动函数
def judge_move_function():
	x = get_pos_x()
	y=  get_pos_y()
	# 最下面一行,除开y=0时全部上移
	if y == 0:
		# 0处
		if x % world_size != 0:
			return West
		else:
			return North
	# 倒数第二行,除开两头,左边边缘上移,右边边缘下移
	elif y==1:
		# 右边边缘
		if (x+1) % world_size ==0:
			return South
		else:
			# 最左边和马上要通上去的地方
			if x % 2 == 0:
				return North
			# 否则右移
			else:
				return East
	# 最上面一行
	elif y == world_size -1:
		# 最左边和偶数位置右移
		if x % 2 ==0:
			return East
		# 最右边和奇数位置下移
		else:
			return South
	# 其余行
	else:
		if x % 2 ==0:
			return North
		else:
			return South


# change hat and start game
while True:
	back_zero()

	change_hat(Hats.Dinosaur_Hat)

	while True:
		target_move = judge_move_function()
		if move(target_move) == False:
			break

	change_hat(Hats.Cactus_Hat)

	break

