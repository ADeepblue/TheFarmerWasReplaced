from __builtins__ import *
from utils import *

# parameter setting
# Cactus_Water_Level = 0.6

# main
# clear()
#
world_size = 32
set_world_size(world_size)
# till the field

def plant_Carrot():
	plant(Entities.Carrot)
	water_the_field(Cautious_Water_Level)

# till_in_parallel()
# for_all(plant_Carrot)
#
# def wait_for_all_drones_finished():
# 	while True:
# 		if num_drones() == 1:
# 			break
#
# wait_for_all_drones_finished()
#
# harvest_all_spawn_loop()
# while True:
# 	do_a_flip()

# def line_plant_task():
# 	for _ in range(world_size):
# 		plant_Carrot()
# 		move(East)
#
# for _ in range(world_size-1):
# 	wait_for(spawn_drone(line_plant_task))
# 	move(North)
#
# line_plant_task()

# def row_harvest_task():
# 	for _ in range(get_world_size()):
# 		safe_harvest()
# 		move(North)


flag = 0


drone_handles = []
def row_harvest_task():
	# 示例行任务：横向遍历一行，收割并向东方向移动
	global drone_handles
	global world_size
	global flag
	for _ in range(get_world_size()):
		safe_harvest()
		move(East)

	print(flag)
	if num_drones() < max_drones():
		tiny_sleep()
		flag += 1
		spawn_drone(row_harvest_task)







# while True:
for _ in range(max_drones()):
	if num_drones() < max_drones():
		tiny_sleep()
		flag += 1
		handle = spawn_drone(row_harvest_task)

		# drone_handles.append(handle)
		move(North)
	else:
		row_harvest_task()
