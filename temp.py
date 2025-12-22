# spawn cactus
from __builtins__ import *
from utils import *

# parameter setting
# Cactus_Water_Level = 0.6

# main
# clear()
#
world_size = 32
set_world_size(world_size)
# till the field
back_zero()
till_in_parallel()

back_zero()
# functions

def plant_cactus_line_task():
	for _ in range(world_size):
		plant(Entities.Cactus)
		move(East)

def bubble_sort_line_task():
	global row_index
	to_position((0, row_index))
	for line_index in range(get_world_size()):
		pre_size = measure()
		for _ in range(get_world_size() - line_index - 1):
			move(East)
			now_size = measure()
			if now_size < pre_size:
				swap(West)
			else:
				pre_size = now_size

		to_position((0, row_index))

def bubble_sort_row_task():
	global line_index
	to_position((line_index, 0))
	for row_index in range(get_world_size()):
		pre_size = measure()
		for _ in range(get_world_size() - row_index - 1):
			move(North)
			now_size = measure()
			if now_size < pre_size:
				swap(South)
			else:
				pre_size = now_size

		to_position((line_index, 0))

# main
# max 32 version
while True:

	# plant cactus
	for _ in range(world_size-1):
		tiny_sleep()
		spawn_drone(plant_cactus_line_task)
		move(North)

	plant_cactus_line_task()
	move(North)
	# wait_for_all_drones_finished()

	back_zero()
	# line sort
	for row_index in range(world_size-1):
		tiny_sleep()
		spawn_drone(bubble_sort_line_task)
		move(North)

	row_index += 1
	bubble_sort_line_task()
	move(North)
	# wait_for_all_drones_finished()

	back_zero()
	move(West)
	# row sort
	for line_index in range(world_size-1,0,-1):
		tiny_sleep()
		spawn_drone(bubble_sort_row_task)
		move(West)

	line_index -= 1
	bubble_sort_row_task()
	move(West)
	wait_for_all_drones_finished()

	safe_harvest()
	break