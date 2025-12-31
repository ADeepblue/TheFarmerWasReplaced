# 32无人机版本 4*8
from __builtins__ import *
from utils import *

# parameter setting
# Cautious_Water_Level = 0.6
# Num_line = 4
# Num_row = 8
# single_line_field = get_world_size() / Num_line
# single_row_field = get_world_size() / Num_row
# world_size = 32
# set_world_size(world_size)


# init
clear()



# position_list[]
# def temp_function():
# 	global position
# 	x = position[0]
# 	y = position[1]
# 	to_position(position)
# 	for row_index in range(-3,4):
# 		# 3的时候要是1,所以下面的循环数要是(0,1)
# 		for line_index in range(abs(row_index)-3,4-abs(row_index)):
# 			to_position( ( (x+line_index) , (y+row_index) ) )
# 			safe_turn_to_soil()
#
# for index1 in range(4):
# 	for index2 in range(4):
# 		position = (index1*8,index2*8)
# 		spawn_drone(temp_function)
#
# for index1 in range(4):
# 	for index2 in range(4):
# 		position = (index1*8-4,index2*8-4)
# 		spawn_drone(temp_function)

# def safe_plant_Carrot():
# 	harvest()
# 	if get_ground_type() != Grounds.Soil:
# 		till()
#
# 	plant(Entities.Carrot)
#
# def safe_plant_grass():
# 	harvest()
# 	if get_ground_type() != Grounds.Grassland:
# 		till()
#
# def safe_plant_bush():
# 	harvest()
# 	plant(Entities.Bush)
#
# def safe_plant_tree():
# 	harvest()
# 	plant(Entities.Tree)
#
# def safe_plant(Plant):
# 	if Plant == Entities.Carrot:
# 		safe_plant_Carrot()
#
# 	elif Plant == Entities.Grass:
# 		safe_plant_grass()
#
# 	elif Plant == Entities.Bush:
# 		safe_plant_bush()
#
# 	elif Plant == Entities.Tree:
# 		safe_plant_tree()
#
# 	else:
# 		return None
#
# to_position((5,5))
# position_list = [(5,5),(5,6)]
# while True:
# 	for position in position_list:
# 		to_position(position)
# 		if get_entity_type() != Entities.Grass:
# 			harvest()
#
# 		if get_companion() == None:
# 			safe_harvest()
# 		else:
# 			companion_plant,position_temp = get_companion()
# 			to_position(position_temp)
# 			safe_plant(companion_plant)
# 			to_position(position)
# 			loop_safe_harvest()



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
	direction_list = [South,West,North,East]
	for direction in direction_list:
		position_list.append(get_position())
		# safe_plant(Entities.Grass)
		move(direction)

	while True:
		for position in position_list:
			to_position(position)
			if get_entity_type() != Entities.Grass:
				safe_plant_grass()
				continue
			if get_companion() == None:
				safe_harvest()
			else:
				companion_plant, position_temp = get_companion()
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