from __builtins__ import *
from utils import *
# main
clear()

world_size = get_world_size()
Cactus_Water_Level = 0.6

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

# plant all the sunflowers
back_zero()
def line_plant_task():
    for _ in range(world_size):
        plant(Entities.Sunflower)
        move(East)

for line_index in range(world_size):
    tiny_sleep()
    spawn_drone(line_plant_task)
    move(North)

line_plant_task()


# build the energy list
energy_list = []
spawn_drone_list = []

# init list
for _ in range(world_size):
    spawn_drone_list.append(None)

for _ in range(world_size):
    temp_list = []
    energy_list.append(None)

# record energy task
def line_record_energy_task():
    to_position((0,line_index))
    temp_list = []
    for row_index in range(world_size):
        temp_list.append(measure())
        move(East)

    return temp_list

# 放飞所有无人机
for row_index in range(world_size-1):
    tiny_sleep()
    spawn_drone_list[row_index] = spawn_drone(line_record_energy_task)
    move(North)
# 最后一条线自己执行

energy_list[world_size-1] = line_record_energy_task()

# line_record_energy_task()

tiny_sleep()

for line_index in range(1,world_size):
    if has_finished(spawn_drone_list[line_index]):
        temp_list = wait_for(spawn_drone_list[line_index])
        energy_list[line_index] = temp_list

quick_print(energy_list)


