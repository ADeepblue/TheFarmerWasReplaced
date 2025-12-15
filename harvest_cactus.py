
from __builtins__ import *
from utils import *

# main
clear()

# world_size = get_world_size()
world_size = 8

# till the field
for line_index in range(world_size):
	for row_index in range(world_size):
		safe_turn_to_soil()
		move(North)
	to_position((line_index + 1, 0))
# plant the cactus

to_position((0,0))
for line_index in range(world_size):
	for row_index in range(world_size):
		plant(Entities.Cactus)
		move(North)
	to_position((line_index + 1, 0))

# bubble sort main loop

# bubble sort main loop in lines
#复位
to_position((0,0))
for line_index in range(world_size):
	for row_index in range(world_size):
		pre_size = measure()
		for loop_num in range(world_size - row_index - 1):
			move(East)
			now_size = measure()
			if now_size < pre_size:
				swap(West)
			else:
				pre_size = now_size
		# print("END")
		to_position((0,line_index))
	to_position((0,line_index+1))

# bubble sort main loop in rows
# 复位
to_position((0,0))
for row_index in range(world_size):
	for line_index in range(world_size):
		pre_size = measure()
		for loop_num in range(world_size - line_index - 1):
			move(North)
			now_size = measure()
			if now_size < pre_size:
				swap(South)
			else:
				pre_size = now_size
		# print("END")
		to_position((row_index,0))
	to_position((row_index+1,0))

to_position((0,0))
harvest()






