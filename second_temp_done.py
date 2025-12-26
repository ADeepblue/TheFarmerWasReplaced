from __builtins__ import *
from utils import *
# parameter setting
Cactus_Water_Level = 0.5
world_size = 32

# functions

def safe_move(next_direct):
	global target
	global snake_length
	global direction
	# direct_list = [West,North,East,South]
	temp = move(next_direct)

	if (target[0] == get_pos_x()) and (target[1] == get_pos_y()):
		snake_length += 1
		# quick_print(snake_length)
		target = measure()

	if temp ==False:
		return None

	direction = next_direct
def to_position_Bone_easy(position):
	def back_direct(direction):
		if direction == East:
			return West
		elif direction == West:
			return East
		elif direction == North:
			return South
		elif direction == South:
			return North
		else:
			return None

	def x_x_now_and_turn(x,x_now):
		global direction
		if x_now > x:
			move_plus(West, x_now - x)
			direction = West
		if x_now < x:
			move_plus(East, x - x_now)
			direction = East

	def y_y_now_and_turn(y,y_now):
		global direction
		if y_now > y:
			move_plus(South, y_now - y)
			direction = South
		if y_now < y:
			move_plus(North, y - y_now)
			direction = North

	def move_plus(direction, distance):
		# 前进路上没有障碍
		if distance > 0:
			for _ in range(distance):
				safe_move(direction)

		# if distance < 0:
		# 	for _ in range(abs(distance)):
		# 		safe_move(direction)

	global direction

	if position == None:
		return None

	x = position[0]
	y = position[1]

	x_now = get_pos_x()
	y_now = get_pos_y()
	# 如果不在同列也不在同行,分类讨论时不考虑x,y都相等,这不可能
	if (x != x_now) and (y != y_now):

		if direction == North:
			if y_now < y:
				move_plus(North,y-y_now)

				x_x_now_and_turn(x,x_now)

			else:
				x_x_now_and_turn(x,x_now)

				move_plus(South,y_now-y)
				direction = South


		elif direction == South:
			if y_now > y:
				move_plus(South,y_now-y)
				x_x_now_and_turn(x,x_now)

			else:
				x_x_now_and_turn(x,x_now)

				move_plus(North,y-y_now)
				direction = North

		elif direction == West:
			if x_now > x:
				move_plus(West,x_now-x)
				y_y_now_and_turn(y,y_now)

			else:
				y_y_now_and_turn(y,y_now)
				move_plus(East,x-x_now)
				direction = East

		elif direction == East:
			if x > x_now:
				move_plus(East,x-x_now)
				y_y_now_and_turn(y,y_now)

			else:
				y_y_now_and_turn(y,y_now)
				move_plus(West,x_now-x)
				direction = West

	# 如果x相同,即在同列
	elif x == x_now:

		# 如果方向在东西方向上
		if direction in [West, East]:
			# 上方
			if y - y_now > 0:
				move_plus(North, y - y_now)
				direction = North
			# 下方
			else:
				move_plus(South, y_now - y)
				direction = South


		# 如果同向
		elif ((((y - y_now) > 0) and (direction == North)) or (((y - y_now) < 0) and (direction == South))):
			move_plus(direction, abs(y - y_now))
			# return direction_now
			direction = direction


		# 如果反向
		elif ((((y - y_now) < 0) and (direction == North)) or (((y - y_now) > 0) and (direction == South))):
			# 如果x不在左边缘
			if x_now != 0:
				move(West)
				to_position_Bone_easy(position)
			else:
				move(East)
				to_position_Bone_easy(position)

	# 如果y相同,即在同行
	elif y == y_now:
		# 如果方向在南北方向上
		if direction in [North, South]:
			# 右边
			if x - x_now > 0:
				move_plus(East, x - x_now)
				direction = East
			# 左边
			else:
				move_plus(West, x_now - x)
				direction = West

		# 如果同向
		if ((((x - x_now) > 0) and (direction == East)) or (((x - x_now) < 0) and (direction == West))):
			move_plus(direction, abs(x - x_now))

		else:
			# 如果x不在下边缘
			if y_now != 0:
				move(South)
				to_position_Bone_easy(position)

			else:
				move(North)
				to_position_Bone_easy(position)

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

# set world
# set_world_size(world_size)

# init
# change_hat(Hats.Cactus_Hat)
# change_hat(Hats.Dinosaur_Hat)
# print(measure())

# 是否x优先,上一步是否是x方向走的,如果是,那就y优先走
# turn_flag = 1
# turn_flag = 0
#
# target = measure()
# # print(to_position_Bone(target[0],target[1],turn_flag))
# # print(measure())
# to_position_Bone(3,7,turn_flag)


# direction = East
# direction_list = [West,North,East,South]
# direction_dict = {"left":-1,"none":0,"right":1}
# def direction_control(turn):
#
# 	global direction
# 	global direction_list
# 	global direction_dict



# direction = North
# target = (24,0)
# to_position_Bone_easy(target,direction)


# def bend_to_side(position, direction_now, snake_length):
# 	# temp_direction = to_position_Bone_easy((1, get_world_size() - 1), direction_now)
# 	# temp_direction = to_position_Bone_easy((0, get_world_size() - 1), temp_direction)
# 	temp_direction = to_position_Bone_easy((1, 0), direction_now)
# 	temp_direction = to_position_Bone_easy((0, 0), temp_direction)
#
# 	if snake_length < get_world_size():
# 		temp_direction = to_position_Bone_easy((0, snake_length-1), temp_direction)
# 		direction = to_position_Bone_easy(position, temp_direction)
# 		return direction
# 	else:
# 		temp_direction = to_position_Bone_easy((0, get_world_size()-1), temp_direction)
# 		direction = to_position_Bone_easy(position, temp_direction)
# 	return direction
#
# # init
# change_hat(Hats.Dinosaur_Hat)
#
#
def to_position_mini(position):
	global direction
	x = position[0]
	y = position[1]
	x_now = get_pos_x()
	y_now = get_pos_y()

	if y > y_now:
		for _ in range(y-y_now):
			safe_move(North)

	else:
		for _ in range(y_now-y):
			safe_move(South)

	if x > x_now:
		for _ in range(x-x_now):
			safe_move(East)
		direction = East
	else:
		for _ in range(x_now-x):
			safe_move(West)
		direction = West

def format_eatting():
	global target
	global direction
	x = target[0]
	y = target[1]
	x_now = get_pos_x()
	y_now = get_pos_y()

	if x > x_now and y_now != 0:
		start_x_position_num = ((x+1)//2)*2-1
		# to_position_mini((start_x_position_num,get_world_size()-1))
		to_position_mini((start_x_position_num,get_world_size()-1))
		for step in range((get_world_size()-1)*2):
			target_move = final_move_function()
			safe_move(target_move)

		direction = target_move
		return True
	else:
		return False






change_hat(Hats.Dinosaur_Hat)

target = measure()
snake_length = 0
direction = North
while True:
	# print(snake_length)
	if measure() != None:
		target = measure()


	to_position_mini((0,0))

	if snake_length < get_world_size():
		for step in range(snake_length):
			target_move = final_move_function()
			safe_move(target_move)

		to_position_Bone_easy(target)

	elif snake_length >= get_world_size():
		loop_num = get_world_size()+(((snake_length-get_world_size())/(get_world_size()-1))//2+1)*2*(get_world_size()-1)
		for step in range(loop_num):
			target_move = final_move_function()
			safe_move(target_move)

		while True:
			format_eatting_flag = format_eatting()
			if not format_eatting_flag:
				break



