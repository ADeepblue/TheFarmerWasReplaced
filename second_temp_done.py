# 32无人机版本 4*8
from __builtins__ import *
from utils import *

# parameter setting
# Cautious_Water_Level = 0.6
# Num_line = 4
# Num_row = 8
# single_line_field = get_world_size() / Num_line
# single_row_field = get_world_size() / Num_row
# world_size = 32
# set_world_size(world_size)


# init
clear()

for row_index in range(get_world_size()):
	for line_index in range(get_world_size()):
		to_position((row_index,line_index))
		quick_print(get_companion())