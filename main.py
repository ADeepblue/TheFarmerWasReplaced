# 1.6v
# till the field, plant the carrot and get hay and wood

from __builtins__ import *
clear()
size_num = get_world_size()


def single_do(line_index,row_index,size_num):
	if (line_index+row_index) % 2 == 0:
		if line_index < size_num // 2:
			plant(Entities.Tree)
		else:
			plant(Entities.Carrot)
	else:
		save_harvest()

	if get_water() <=0.5:
		use_item(Items.Water)

def save_harvest():
	if can_harvest():
		harvest()

# till the field in second row
for line_index in range(size_num):
	for row_index in range(size_num):
		if (line_index+row_index) % 2 == 0:
			till()
		else:
			save_harvest()
		move(North)
	move(East)

#main loop
while True:
	for line_index in range(size_num):
		for row_index in range(size_num):
			save_harvest()
			single_do(line_index,row_index,size_num)
			move(North)
		move(East)
