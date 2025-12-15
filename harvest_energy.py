from __builtins__ import *
from utils import *

# main
clear()
to_position((0,0))

world_size = get_world_size()

# one line test

## till the field
back_zero()
for line_index in range(world_size):
	safe_turn_to_soil()
	move(East)


back_zero()
## plant sunflowers
for line_index in range(world_size):
	plant(Entities.Sunflower)
	move(East)

## record the energy dict
energy_list = []
back_zero()
for line_index in range(world_size):
	energy_list.append(measure())
	move(East)

# bubble sort the energy list

while True:
	max_leaf = max(energy_list)
	max_index = get_index(energy_list, max_leaf)

	to_position((max_index,0))
	while True:
		if safe_harvest():
			water_the_field(1)
			plant(Entities.Sunflower)
			break

	energy_list[max_index] = measure()
