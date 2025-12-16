from __builtins__ import *
from utils import *

# parameter setting
# Cactus_Water_Level = 0.6

# main
# clear()
#
world_size = 8
set_world_size(world_size)
# till the field

def plant_Carrot():
	plant(Entities.Carrot)
	water_the_field(Cautious_Water_Level)

till_in_parallel()
for_all(plant_Carrot)

def wait_for_all_drones_finished():
	while True:
		if num_drones() == 1:
			break

wait_for_all_drones_finished()

harvest_all_spawn_loop()
while True:
	do_a_flip()