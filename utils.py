
from __builtins__ import *

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


def safe_harvest():
	if can_harvest():
		harvest()
		return True
	return False

def till_all_field(size_num):
	for r in range(size_num):
		for j in range(size_num):
			safe_harvest()
			till()
			move(North)
		move(East)



def water_the_field(limit_water_percent):
	if get_water() <=limit_water_percent:
		use_item(Items.Water)

def safe_turn_to_soil():
	if get_ground_type() != Grounds.Soil:
		safe_harvest()
		till()

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

def back_zero():
	to_position((0, 0))

def get_index(list,value):
	for index in range(len(list)):
		if list[index] == value:
			return index
	return None


def for_all(f):
	def row():
		for _ in range(get_world_size()-1):
			f()
			move(North)
		f()
	for _ in range(get_world_size()-1):
		if not spawn_drone(row):
			row()
		move(East)