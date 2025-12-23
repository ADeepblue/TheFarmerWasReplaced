from __builtins__ import *
from utils import *

# parameter setting
Cactus_Water_Level = 0.5
world_size = 32

# set world
# set_world_size(world_size)

# init
clear()
def plant_bush_and_tree():
	x,y = get_position()
	if (x+y) % 2 ==0:
		# plant(Entities.Tree)
		water_the_field(Cactus_Water_Level)
	else:
		# plant(Entities.Bush)
		water_the_field(Cactus_Water_Level)



back_zero()
def line_plant_task():
	while True:
		for _ in range(world_size):
			safe_harvest()
			plant_bush_and_tree()
			move(East)


for _ in range(world_size-1):
	tiny_sleep()
	spawn_drone(line_plant_task)
	move(North)

line_plant_task()




