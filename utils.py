
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

def till_all_field(size_num):
	for r in range(size_num):
		for j in range(size_num):
			safe_harvest()
			till()
			move(North)
		move(East)

def to_position(x,y):
	x_now = get_pos_x()
	y_now = get_pos_y()
	if x_now < x:
		for _ in range(x-x_now):
			move(East)
	elif x_now > x:
		for _ in range(x_now-x):
			move(West)

	if y_now < y:
		for _ in range(y-y_now):
			move(North)
	elif y_now > y:
		for _ in range(y_now-y):
			move(South)