from __builtins__ import *
from utils import *
# main

back_zero()
harvest_all_spawn()

clear()

world_size = get_world_size()
Cactus_Water_Level = 0.8

# function to get all indices of a value in a list
def get_index_list(list,value):
	index_list = []
	for index in range(len(list)):
		if list[index] == value:
			index_list.append(index)
	if index_list != []:
		return index_list
	else:
		return None

# sleep

def tiny_sleep():
	move(North)
	move(South)

# till all the field
back_zero()
def line_till_task():
	for _ in range(world_size):
		safe_turn_to_soil()
		water_the_field(Cactus_Water_Level)
		move(East)


for line_index in range(world_size-1):
	tiny_sleep()
	spawn_drone(line_till_task)
	move(North)

line_till_task()





def loop_safe_harvest():
	while True:
		if safe_harvest():
			break

def line_plant_task():
	for _ in range(world_size):
		plant(Entities.Sunflower)
		water_the_field(Cactus_Water_Level)
		move(East)

def line_harvest_task():
	for _ in range(world_size):
		loop_safe_harvest()
		move(East)



# main loop
while True:
# plant all the sunflowers
	back_zero()


	for _ in range(world_size-1):
		tiny_sleep()
		spawn_drone(line_plant_task)
		water_the_field(Cactus_Water_Level)
		move(North)

	line_plant_task()


	for _ in range(world_size-1):
		tiny_sleep()
		spawn_drone(line_harvest_task)
		move(North)

	line_harvest_task()


