from __builtins__ import *
from utils import *


def safe_move(direct):
	global target
	global snake_length
	# direct_list = [West,North,East,South]
	temp = move(direct)

	if (target[0] == get_pos_x()) and (target[1] == get_pos_y()):
		snake_length += 1
		target = measure()

	if temp ==False:
		return None

	return direct

def to_position_Bone_easy(position, direction_now):
	def back_direct(direct):
		if direct == East:
			return West
		elif direct == West:
			return East
		elif direct == North:
			return South
		elif direct == South:
			return North
		else:
			return None

	def x_x_now_and_turn(x,x_now):
		if x_now > x:
			move_plus(West, x_now - x)
			return West
		if x_now < x:
			move_plus(East, x - x_now)
			return East

	def y_y_now_and_turn(y,y_now):
		if y_now > y:
			move_plus(South, y_now - y)
			return South
		if y_now < y:
			move_plus(North, y - y_now)
			return North

	def move_plus(direction, distance):
		# 前进路上没有障碍
		if distance > 0:
			for _ in range(distance):
				safe_move(direction)

		# if distance < 0:
		# 	for _ in range(abs(distance)):
		# 		safe_move(direction)

	if position == None:
		return None

	x = position[0]
	y = position[1]

	x_now = get_pos_x()
	y_now = get_pos_y()
	# 如果不在同列也不在同行,分类讨论时不考虑x,y都相等,这不可能
	if (x != x_now) and (y != y_now):

		if direction_now == North:
			if y_now < y:
				move_plus(North,y-y_now)

				return x_x_now_and_turn(x,x_now)

			else:
				x_x_now_and_turn(x,x_now)

				move_plus(South,y_now-y)
				return South


		elif direction_now == South:
			if y_now > y:
				move_plus(South,y_now-y)
				return x_x_now_and_turn(x,x_now)

			else:
				x_x_now_and_turn(x,x_now)

				move_plus(North,y-y_now)
				return North

		elif direction_now == West:
			if x_now > x:
				move_plus(West,x_now-x)
				return y_y_now_and_turn(y,y_now)

			else:
				y_y_now_and_turn(y,y_now)
				move_plus(East,x-x_now)
				return East

		elif direction_now == East:
			if x > x_now:
				move_plus(East,x-x_now)
				return y_y_now_and_turn(y,y_now)

			else:
				y_y_now_and_turn(y,y_now)
				move_plus(West,x_now-x)
				return West

	# 如果x相同,即在同列
	elif x == x_now:

		# 如果方向在东西方向上
		if direction_now in [West, East]:
			# 上方
			if y - y_now > 0:
				move_plus(North, y - y_now)
				return North
			# 下方
			else:
				move_plus(South, y_now - y)
				return South


		# 如果同向
		elif ((((y - y_now) > 0) and (direction_now == North)) or (((y - y_now) < 0) and (direction_now == South))):
			move_plus(direction_now, abs(y - y_now))
			return direction_now


		# 如果反向
		elif ((((y - y_now) < 0) and (direction_now == North)) or (((y - y_now) > 0) and (direction_now == South))):
			# 如果x不在左边缘
			if x_now != 0:
				move(West)
				direction = to_position_Bone_easy(position, West)
				return direction
			else:
				move(East)
				direction = to_position_Bone_easy(position, West)
				return direction

	# 如果y相同,即在同行
	elif y == y_now:
		# 如果方向在南北方向上
		if direction_now in [North, South]:
			# 右边
			if x - x_now > 0:
				move_plus(East, x - x_now)
				return East
			# 左边
			else:
				move_plus(West, x_now - x)
				return West

		# 如果同向
		if ((((x - x_now) > 0) and (direction_now == East)) or (((x - x_now) < 0) and (direction_now == West))):
			move_plus(direction_now, abs(x - x_now))
			return direction_now

		else:
			# 如果x不在下边缘
			if y_now != 0:
				move(South)
				direction = to_position_Bone_easy(position, West)
				return direction
			else:
				move(North)
				direction = to_position_Bone_easy(position, West)
				return direction

def bend_to_side(position, direction_now, snake_length):
	# temp_direction = to_position_Bone_easy((1, get_world_size() - 1), direction_now)
	# temp_direction = to_position_Bone_easy((0, get_world_size() - 1), temp_direction)
	temp_direction = to_position_Bone_easy((1, 0), direction_now)
	temp_direction = to_position_Bone_easy((0, 0), temp_direction)

	if snake_length < get_world_size():
		temp_direction = to_position_Bone_easy((0, snake_length-1), temp_direction)
		direction = to_position_Bone_easy(position, temp_direction)

	else:
		temp_direction = to_position_Bone_easy((0, get_world_size()-1), temp_direction)
		direction = to_position_Bone_easy(position, temp_direction)
	return direction

def final_move_function():
	x = get_pos_x()
	y=  get_pos_y()
	# 最下面一行,除开y=0时全部上移
	if y == 0:
		# 0处
		if x % get_world_size() != 0:
			return West
		else:
			return North
	# 倒数第二行,除开两头,左边边缘上移,右边边缘下移
	elif y==1:
		# 右边边缘
		if (x+1) % get_world_size() ==0:
			return South
		else:
			# 最左边和马上要通上去的地方
			if x % 2 == 0:
				return North
			# 否则右移
			else:
				return East
	# 最上面一行
	elif y == get_world_size() -1:
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

# main
change_hat(Hats.Dinosaur_Hat)

direction = North
snake_length = 0
target = measure()
while True:
	# print(snake_length)
	if snake_length <= 4:
		direction = to_position_Bone_easy(target,direction)
		# snake_length += 1
	elif (snake_length > 4) and(snake_length < 1.5*get_world_size()):
		direction = bend_to_side(target,direction,snake_length)
		# snake_length += 1
	elif (snake_length >= 1.5* get_world_size()) and (snake_length <get_world_size()*(get_world_size()-3)):
		direction = to_position_Bone_easy((0,0),direction)
		for step in range(snake_length):
			target_move = final_move_function()

		direction = to_position_Bone_easy(target,direction)
		# snake_length += 1

	else:
		while True:
			target_move = final_move_function()
			if move(target_move) == False:
				change_hat(Hats.Cactus_Hat)
				break






