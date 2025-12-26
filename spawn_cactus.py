from __builtins__ import *
from utils import *

# parameter setting
Cactus_Water_Level = 0

# main
clear()

world_size = get_world_size()

# till the field

till_in_parallel()

back_zero()

# plant the cactus
while True:
	def row_plant_task():
		to_position((line_index,0))
		for _ in range(world_size):
			plant(Entities.Cactus)
			move(North)

	back_zero()

	for line_index in range(world_size-1):
		if num_drones() < max_drones():
			spawn_drone(row_plant_task)
		else:
			while True:
				if num_drones() < max_drones():
					spawn_drone(row_plant_task)
					break

	if get_world_size() > max_drones()-1:
		line_index = world_size -1
		row_plant_task()

	wait_for_all_drones_finished()

	# bubble sort main loop

	# parallel task

	def bubble_sort_line_task():
		#复位
		to_position((0,line_index))
		for row_index in range(world_size):
			pre_size = measure()
			for _ in range(world_size - row_index - 1):
				move(East)
				now_size = measure()
				if now_size < pre_size:
					swap(West)
				else:
					pre_size = now_size
			# print("END")
			to_position((0,line_index))

	# bubble sort main loop in lines
	for line_index in range(world_size):
		if num_drones() < max_drones():
			spawn_drone(bubble_sort_line_task)
		else:
			while True:
				if num_drones() < max_drones():
					spawn_drone(bubble_sort_line_task)
					break

	back_zero()

	# bubble sort main loop in rows
	while True:
		if num_drones() == 1:
			break
	def bubble_sort_row_task():
		# 复位
		to_position((row_index,0))
		for line_index in range(world_size):
			pre_size = measure()
			for _ in range(world_size - line_index - 1):
				move(North)
				now_size = measure()
				if now_size < pre_size:
					swap(South)
				else:
					pre_size = now_size
			# print("END")
			to_position((row_index,0))

	# bubble sort main loop in rows
	for row_index in range(world_size):
		if num_drones() < max_drones():
			spawn_drone(bubble_sort_row_task)
		else:
			while True:
				if num_drones() < max_drones():
					spawn_drone(bubble_sort_row_task)
					break

	while True:
		if num_drones() == 1:
			break

	safe_harvest()