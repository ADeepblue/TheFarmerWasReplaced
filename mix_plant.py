from __builtins__ import *
from utils import *

# main
clear()

limit_water_percent = 0.8

# set_world_size(3)

while True:
	pre_position = (get_pos_x(),get_pos_y())
	next_plant,position = get_companion()

	to_position(position)

	if (next_plant == Entities.Carrot) and (get_ground_type()!=Grounds.Soil):
		till()

	if (next_plant == Entities.Grass) and (get_ground_type()!=Grounds.Grassland):
		till()

	plant(next_plant)

	to_position(pre_position)
	water_the_field(limit_water_percent)
	use_item(Items.Fertilizer)

	while True:
		if can_harvest():
			harvest()
			break

	to_position(position)