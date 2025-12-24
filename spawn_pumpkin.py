from __builtins__ import *
from utils import *

# main
clear()
world_size = get_world_size()
# till the field
def row_till_task():
	to_position((line_index,0))
	for _ in range(world_size):
		safe_turn_to_soil()
		move(North)


for line_index in range(world_size):
	if num_drones() < max_drones():
		spawn_drone(row_till_task)
	else:
		while True:
			if num_drones() < max_drones():
				spawn_drone(row_till_task)
				break
#main loop
while True:
	# plant the pumpkin
	def row_plant_task():
		to_position((line_index,0))
		for _ in range(world_size):
			plant(Entities.Pumpkin)
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

	#check the pumpkin
	bad_pumpkin_list = []
	for line_index in range(world_size):
		for row_index in range(world_size):
			if can_harvest() == False:
				plant(Entities.Pumpkin)
				bad_pumpkin_list.append([line_index,row_index])

			move(North)
		to_position((line_index+1,0))

	while True:
		temp_list = []
		for position_list in bad_pumpkin_list:
			x = position_list[0]
			y = position_list[1]
			to_position((x, y))
			if not can_harvest():
				plant(Entities.Pumpkin)
				temp_list.append([x, y])
				bad_pumpkin_list = temp_list

		if len(temp_list) == 0:
			safe_harvest()
			to_position((0, 0))
			break

	break