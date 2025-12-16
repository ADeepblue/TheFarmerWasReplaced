from __builtins__ import *
from utils import *

# parameter setting
Cactus_Water_Level = 0

# main
clear()

world_size = get_world_size()

# till the field


def row_till_task():
	to_position((line_index,0))
	for _ in range(world_size):
		safe_turn_to_soil()
		water_the_field(Cactus_Water_Level)
		move(North)


for line_index in range(world_size):
	if num_drones() < max_drones():
		spawn_drone(row_till_task)
	else:
		while True:
			if num_drones() < max_drones():
				spawn_drone(row_till_task)
				break

# plant the cactus

def row_plant_task():
	to_position((line_index,0))
	for _ in range(world_size):
		plant(Entities.Cactus)
		move(North)

back_zero()

for line_index in range(world_size):
	if num_drones() < max_drones():
		spawn_drone(row_plant_task)
	else:
		while True:
			if num_drones() < max_drones():
				spawn_drone(row_plant_task)
				break

# bubble sort main loop

# parallel task
while True:
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