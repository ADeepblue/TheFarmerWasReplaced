from __builtins__ import *
from utils import *

# main

for row_index in range(get_world_size()):
	for line_index in range(get_world_size()):
		safe_harvest()
		move(North)
	move(East)