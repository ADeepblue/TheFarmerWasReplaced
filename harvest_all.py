from __builtins__ import *
from utils import *

# main

back_zero()

def line_harvest_task():
	for _ in range(get_world_size()):
		safe_harvest()
		move(East)

for _ in range(get_world_size()-1):
	tiny_sleep()
	spawn_drone(line_harvest_task)
	move(North)

line_harvest_task()