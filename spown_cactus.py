from __builtins__ import *
from utils import *

# parameter setting
Cactus_Water_Level = 0.6

# main
clear()

world_size = get_world_size()

# till the field

def row_till_task():
    for row_index in range(world_size):
        safe_turn_to_soil()
        water_the_field(Cactus_Water_Level)
        move(North)


for line_index in range(world_size):
    while True:
        if spawn_drone(row_till_task):
            move(East)
            break


