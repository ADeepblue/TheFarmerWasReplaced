# 种植灌木并收获灌木,顺带收获草

from __builtins__ import *
from utils import *
from utils import safe_harvest
clear()
size_num = get_world_size()
at_least_percent = 1

def do(line_index,row_index,size_num):
	if (line_index+row_index) % 2 == 0:
		plant(Entities.Tree)
	else:
		safe_harvest()

	if get_water() <=at_least_percent:
		use_item(Items.Water)



# till the field in second row
for line_index in range(size_num):
	for row_index in range(size_num):
		safe_harvest()
		if (line_index+row_index) % 2 == 0:
			till()

		move(North)
	move(East)

#main loop

while True:
	for line_index in range(size_num):
		for row_index in range(size_num):
			safe_harvest()
			do(line_index,row_index,size_num)
			move(North)
		move(East)
