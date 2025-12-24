
from __builtins__ import *
# parameter setting
Cautious_Water_Level = 0.6

def main_do(line_index,row_index,size_num):
	if (line_index+row_index) % 2 == 0:
		if line_index < size_num // 2:
			plant(Entities.Tree)
		else:
			plant(Entities.Carrot)
	else:
		safe_harvest()

	if get_water() <=0.6:
		use_item(Items.Water)


# harvest function
## safe harvest, no loop
def safe_harvest():
	if can_harvest():
		harvest()
		return True
	return False

## loop safe harvest, if cannot harvest, keep trying
def loop_safe_harvest():
	while True:
		if safe_harvest():
			break

## harvest all with spawn drone,in parallel, keep trying final version

def harvest_all_spawn_loop():
	def line_harvest_task():
		for _ in range(get_world_size()):
			loop_safe_harvest()
			move(East)

	for _ in range(get_world_size()):
		tiny_sleep()
		spawn_drone(line_harvest_task)
		move(North)

	line_harvest_task()

## harvest all with spawn drone,in parallel, single try version
def harvest_all_spawn():
	def line_harvest_task():
		for _ in range(get_world_size()):
			safe_harvest()
			move(East)

	for _ in range(get_world_size()-1):
		tiny_sleep()
		spawn_drone(line_harvest_task)
		move(North)

	line_harvest_task()

# till function

## only use for and varable
def till_all_field(size_num):
	for r in range(size_num):
		for j in range(size_num):
			safe_harvest()
			till()
			move(East)
		move(East)

## use parallel, final version
def till_in_parallel():
	def row_till_task():
		for _ in range(get_world_size()):
			safe_turn_to_soil()
			move(East)

	for _ in range(get_world_size()-1):
		tiny_sleep()
		spawn_drone(row_till_task)
		move(North)
	row_till_task()
	move(North)

# single, safe till function
def safe_turn_to_soil():
	if get_ground_type() != Grounds.Soil:
		safe_harvest()
		till()


# water the field, single function
def water_the_field(limit_water_percent):
	if get_water() <=limit_water_percent:
		use_item(Items.Water)



# position function

## get postion,set
def get_position():
	return (get_pos_x(),get_pos_y())


## to one position
def to_position(position):
	x = position[0]
	y = position[1]
	x_now = get_pos_x()
	y_now = get_pos_y()
	# 如果x_now在 8,world_size是10,x是2
	if get_world_size()-x_now+x < x_now-x:
		for _ in range(get_world_size()-x_now+x):
			move(East)
	# 如果x_now在2,world_size是10,x是8
	elif get_world_size()-x+x_now < x - x_now:
		for _ in range(get_world_size()-x+x_now):
			move(West)
	else:
		if x_now < x:
			for _ in range(x-x_now):
				move(East)
		elif x_now > x:
			for _ in range(x_now-x):
				move(West)

	if get_world_size()-y_now+y < y_now - y:
		for _ in range(get_world_size()-y_now+y):
			move(North)
	elif get_world_size()-y+y_now < y - y_now:
		for _ in range(get_world_size()-y+y_now):
			move(South)
	else:
		if y_now < y:
			for _ in range(y-y_now):
				move(North)
		elif y_now > y:
			for _ in range(y_now-y):
				move(South)

## to zero zero position
def back_zero():
	to_position((0, 0))

# get index in list
def get_index(list_,value):
	for index in range(len(list_)):
		if list_[index] == value:
			return index
	return None


# for all function,input function f
def for_all(f):
	def row():
		for _ in range(get_world_size()):
			f()
			move(East)
		f()
	for _ in range(get_world_size()-1):
		tiny_sleep()
		spawn_drone(row)
		move(North)
	row()

# little delay function, for spawn drone safety
def tiny_sleep():
	move(North)
	move(South)

# If do so quickly, some drones may not work successfully, specially like check between rows and lines
def wait_for_all_drones_finished():
	while True:
		if num_drones() == 1:
			break


def to_position_Bone_easy(position, direction_now):
	def move_plus(direction,distance):
		# 前进路上没有障碍
		for step in range(distance):
			safe_move(direction)

	if position == None:
		return None

	x = position[0]
	y = position[1]

	x_now = get_pos_x()
	y_now = get_pos_y()
	# 如果不在同列也不在同行,分类讨论时不考虑x,y都相等,这不可能
	if (x != x_now) and (y != y_now):
		if direction_now in [North,South]:

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
		elif direction_now in [West,East]:

			if y_now < y:
				move_plus(North,y - y_now)

			elif y_now > y:
				move_plus(South,y_now
				          - y)

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
				move_plus(East,x-x_now)
				return East
			# 左边
			else:
				move_plus(West,x_now-x)
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

def safe_move(direct):
	direct_list = [West,North,East,South]
	if move(direct) == False:
		index = get_index(direct_list,direct)
		if move(direct_list[(index+1) % 4]):
			return direct_list[(index+1) % 4]
		elif move(direct_list[(index-1) % 4]):
			return direct_list[(index-1) % 4]
		else:
			change_hat(Hats.Gold_Hat)
			return None

	return direct