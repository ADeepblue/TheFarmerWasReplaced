from __builtins__ import *
from utils import *

# main
clear()

to_position((0,0))


world_size = get_world_size()
# till the field and plant the cactus

for line_index in range(get_world_size()):
	till()
	plant(Entities.Cactus)
	move(East)
	
# bubble sort main loop
pre_size = measure()
for line_index in range(world_size):
	pre_size = measure()
	print(measure())
	for loop_num in range(world_size - line_index -1):
		move(East)
		print(measure())
		now_size = measure()
		if now_size < pre_size:
			swap(West)
		else:
			pre_size = now_size
	print("END")
	to_position((0,0))

harvest()




