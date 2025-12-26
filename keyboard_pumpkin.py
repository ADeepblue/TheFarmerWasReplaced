# 16无人机版本 4*8
from __builtins__ import *
from utils import *

# parameter setting
Cautious_Water_Level = 0.6
Num_line = 4
Num_row = 4
single_line_field = 7
single_row_field = 7
world_size = 32
set_world_size(world_size)


# init
# clear()

# till the field
back_zero()
till_in_parallel()

back_zero()

# main
def single_plant_task():
	while True:
		to_position((line_num_index*single_line_field,row_num_index*single_row_field))
		# plant the pumpkin
		for row_index in range(single_row_field-1):
			for line_index in range(single_line_field-1):
				plant(Entities.Pumpkin)
				water_the_field(Cautious_Water_Level)
				move(East)
			to_position((line_num_index * single_line_field, row_num_index * single_row_field+ row_index+1))

			quick_print(row_num_index,(line_num_index * single_line_field, row_num_index * single_row_field))
		to_position((line_num_index * single_line_field, row_num_index * single_row_field))
		# check bad pumpkin

		bad_pumpkin_list = []

		for row_index in range(single_row_field-1):
			for line_index in range(single_line_field-1):
				if can_harvest() == False:
					plant(Entities.Pumpkin)
					bad_pumpkin_list.append(get_position())

				move(East)
			to_position((line_num_index * single_line_field, row_num_index * single_row_field+row_index+1))

		to_position((line_num_index * single_line_field, row_num_index * single_row_field))

		# kill all the bad pumpkin

		while True:
			temp_list = []
			for position in bad_pumpkin_list:
				to_position(position)
				if not can_harvest():
					plant(Entities.Pumpkin)
					temp_list.append(position)

			bad_pumpkin_list = temp_list

			if len(temp_list) == 0:
				safe_harvest()
				break

		if num_items(Items.Pumpkin) >= 200000000:
			break

for row_num_index in range(Num_row):
	for line_num_index in range(Num_line):
		# quick_print(row_num_index,line_num_index)
		if (line_num_index != Num_line-1) or (row_num_index != Num_row-1):
			tiny_sleep()
			spawn_drone(single_plant_task)
			# single_plant_task()

# 不需要加一,因为上面已经加过了
# line_num_index += 1

single_plant_task()