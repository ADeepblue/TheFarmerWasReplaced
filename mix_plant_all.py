from __builtins__ import *
from utils import *

# main
clear()

limit_water_percent = 0.8
work_size = get_world_size()

def mix_plant():
	to_position(((random() * work_size) // 1, (random() * work_size) // 1))
	while True:
		pre_position = (get_pos_x(), get_pos_y())
		if get_companion() != None:
			next_plant, position = get_companion()
		else:
			to_position(((random() * work_size) // 1, (random() * work_size) // 1))
			break
		to_position(position)

		if (next_plant == Entities.Carrot) and (get_ground_type() != Grounds.Soil):
			till()

		if (next_plant == Entities.Grass) and (get_ground_type() != Grounds.Grassland):
			till()

		plant(next_plant)

		to_position(pre_position)
		water_the_field(limit_water_percent)
		use_item(Items.Fertilizer)

		while True:
			if can_harvest():
				harvest()
				break
			if get_entity_type() == None:
				to_position(((random()*work_size)//1,(random()*work_size)//1))
				break
		quick_print(num_drones())
		to_position(position)


for _ in range(max_drones()):
	do_a_flip()
	spawn_drone(mix_plant)
	if max_drones() == num_drones():
		mix_plant()