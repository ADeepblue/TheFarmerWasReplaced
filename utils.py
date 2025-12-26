
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




