# 1.5v
## 说明
# 种植胡萝卜并收获胡萝卜

from __builtins__ import *
from utils import *

# main
clear()
size_num = get_world_size()
# till the field
till_all_field(size_num)


square_size = size_num

while True:
	# plant the pumpkin first
	for line_index in range(size_num):
		for row_index in range(size_num):
			if line_index < square_size and row_index < square_size:
				plant(Entities.Pumpkin)
			else:
				plant(Entities.Carrot)

			move(North)

		move(East)

	# check the pumpkin
	bad_pumpkin_list = []
	for line_index in range(size_num):
		for row_index in range(size_num):
			if can_harvest() == False:
				plant(Entities.Pumpkin)
				bad_pumpkin_list.append([line_index,row_index])

			move(North)
		move(East)

	while True:
		temp_list = []
		for position_list in bad_pumpkin_list:
			x = position_list[0]
			y = position_list[1]
			to_position((x,y))
			if not can_harvest():
				plant(Entities.Pumpkin)
				temp_list.append([x,y])
				bad_pumpkin_list = temp_list

		if len(temp_list) == 0:
			safe_harvest()
			to_position((0,0))
			break





