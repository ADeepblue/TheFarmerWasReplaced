from __builtins__ import *
from utils import *

# main
clear()
set_world_size(8)
world_size = get_world_size()

def row_plant_task():
	to_position((line_index,0))
	for row_index in range(world_size):
		plant(Entities.Bone)
		move(North)

for line_index in range(world_size):
	if num_drones() < max_drones():
		spawn_drone(row_plant_task)
	else:
		row_plant_task()