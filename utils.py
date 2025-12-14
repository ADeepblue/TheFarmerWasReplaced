
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
