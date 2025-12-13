# 1.8v
# till the field, plant the carrot and get hay and wood

from __builtins__ import *
from utils import *
clear()
size_num = get_world_size()


# till the field in second row
for line_index in range(size_num):
	for row_index in range(size_num):
		if (line_index+row_index) % 2 == 0:
			till()
		else:
			safe_harvest()
		move(North)
	move(East)

#main loop
while True:
	for line_index in range(size_num):
		for row_index in range(size_num):
			safe_harvest()
			main_do(line_index, row_index, size_num)
			move(North)
		move(East)
