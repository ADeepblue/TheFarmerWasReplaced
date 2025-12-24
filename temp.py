from __builtins__ import *
from utils import *

# parameter setting
Cactus_Water_Level = 0.5
world_size = 32

# set world
# set_world_size(world_size)

# init
clear()
change_hat(Hats.Dinosaur_Hat)


# print(measure())

def safe_move(direct):
	if move(direct) == False:
		change_hat(Hats.Gold_Hat)


def to_position_Bone(x, y, x_or_not):
	x_now = get_pos_x()
	y_now = get_pos_y()
	if x_now < x:
		for _ in range(x - x_now):
			safe_move(East)
	elif x_now > x:
		for _ in range(x_now - x):
			safe_move(West)

	if y_now < y:
		for _ in range(y - y_now):
			safe_move(North)
	elif y_now > y:
		for _ in range(y_now - y):
			safe_move(South)

	return not x_or_not


def to_position_Bone_easy(position, direction_now):
	def move_plus(direction,distance):
		# 前进路上没有障碍
		flag = 0
		for step in range(distance):
			safe_move(direction)

	x = position[0]
	y = position[1]

	x_now = get_pos_x()
	y_now = get_pos_y()
	# 如果不在同列也不在同行,分类讨论时不考虑x,y都相等,这不可能
	if (x != x_now) and (y != y_now):
		if direction_now in [North,South]:

			if x_now < x:
				move_plus(East,x - x_now)

			elif x_now > x:
				move_plus(West,x_now - x)

			if y_now < y:
				move_plus(North,y - y_now)
				return North

			elif y_now > y:
				move_plus(South,y_now - y)
				return South

		elif direction_now in [West,East]:

			if y_now < y:

				move_plus(North,y - y_now)

			elif y_now > y:
				move_plus(South,y_now - y)

			if x_now < x:
				move_plus(East,x - x_now)
				return East
			elif x_now > x:
				move_plus(West,x_now - x)
				return West

	# 如果x相同,即在同列
	elif x == x_now:

		# 如果方向在东西方向上
		if direction_now in [West,East]:
			# 上方
			if y-y_now > 0:
				move_plus(North,y-y_now)
				return North
			# 下方
			else:
				move_plus(South,y_now-y)
				return South


		# 如果同向
		elif ( (((y-y_now) > 0) and (direction_now == North)) or (((y-y_now) < 0) and (direction_now == South)) ):
			move_plus(direction_now,abs(y-y_now))
			return direction_now


		# 如果反向
		elif ( (((y-y_now) < 0) and (direction_now == North)) or (((y-y_now) > 0) and (direction_now == South)) ):
			# 如果x不在左边缘
			if x_now != 0:
				move(West)
				direction = to_position_Bone_easy(position,West)
				return direction
			else:
				move(East)
				direction = to_position_Bone_easy(position,West)
				return direction

	# 如果y相同,即在同行
	elif y == y_now:
		# 如果方向在南北方向上
		if direction_now in [North,South]:
			# 右边
			if x-x_now > 0:
				move_plus(East,y-y_now)
				return East
			# 左边
			else:
				move_plus(West,y_now-y)
				return West

		# 如果同向
		if ( (((x-x_now) > 0) and (direction_now == East)) or (((x-x_now) < 0) and (direction_now == West)) ):
			move_plus(direction_now,abs(x-x_now))
			return direction_now

		else:
			# 如果x不在下边缘
			if y_now != 0:
				move(South)
				direction = to_position_Bone_easy(position,West)
				return direction
			else:
				move(North)
				direction = to_position_Bone_easy(position,West)
				return direction


target = measure()

direction = to_position_Bone_easy(target,North)

