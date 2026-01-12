from __builtins__ import *
from utils import *

# parameter setting
Cactus_Water_Level = 1

# init up_flag
up_flag = False
half_bad_pumpkin_list = []
# init the position information,clock_wise
clear()


def safe_plant_Carrot():
	harvest()
	if get_ground_type() != Grounds.Soil:
		till()

	plant(Entities.Carrot)

def safe_plant_grass():
	harvest()
	if get_ground_type() != Grounds.Grassland:
		till()

def safe_plant_bush():
	harvest()
	plant(Entities.Bush)

def safe_plant_tree():
	harvest()
	plant(Entities.Tree)

def safe_plant(Plant):
	if Plant == Entities.Carrot:
		safe_plant_Carrot()

	elif Plant == Entities.Grass:
		safe_plant_grass()

	elif Plant == Entities.Bush:
		safe_plant_bush()

	elif Plant == Entities.Tree:
		safe_plant_tree()

	else:
		return None

def mix_main_task():
	global position
	to_position(position)
	position_list = []
	direction_list = [South,East]
	for direction in direction_list:
		position_list.append(get_position())
		# safe_plant(Entities.Grass)
		safe_water_the_field(Cactus_Water_Level)
		move(direction)

	while True:
		for position in position_list:
			to_position(position)
			# safe_water_the_field(Cactus_Water_Level)

			# if num_items(Items.Wood) < 100:
			# 	safe_plant(Entities.Bush)
			# 	if get_companion() == None:
			# 		print(None)
			# 		safe_harvest()
			# 	else:
			# 		companion_plant, position_temp = get_companion()
			# 		# print(companion_plant)
			# 		# print(position_temp)
			# 		to_position(position_temp)
			# 		safe_plant(companion_plant)
			# 		to_position(position)
			# 		loop_safe_harvest()
			# else:




			if get_entity_type() != Entities.Grass:
				safe_plant_grass()
				continue
			if get_companion() == None:
				print(None)
				harvest()
			else:
				companion_plant, position_temp = get_companion()
				# print(companion_plant)
				# print(position_temp)
				to_position(position_temp)
				safe_plant(companion_plant)
				to_position(position)
				loop_safe_harvest()

			if num_items(Items.Hay) >= 2000000000:
				break

for index1 in range(4):
	for index2 in range(4):
		position = (index1*8,index2*8)
		spawn_drone(mix_main_task)

for index1 in range(4):
	for index2 in range(4):
		if (index1 == 3) and (index2 ==3):
			continue
		else:
			position = (index1*8+4,index2*8+4)
			spawn_drone(mix_main_task)

position = (index1*8+4,index2*8+4)
mix_main_task()

# index1 = 0
# index2 = 0
#
# position = (index1*8,index2*8)
# mix_main_task()