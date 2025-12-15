# 1.8v
# till the field, plant the carrot and get hay and wood

from __builtins__ import *
from utils import *
clear()
world_size = get_world_size()
def harvest_column():
	for _ in range(world_size):
		safe_harvest()
		move(North)

while True:
	if spawn_drone(harvest_column):
		move(East)