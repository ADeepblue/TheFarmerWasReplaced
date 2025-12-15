from __builtins__ import *
from utils import *

# main
clear()

to_position((0,0))


world_size = get_world_size()
# till the field and plant the cactus
while True:
	back_zero()

	plant(Entities.Bush)

	substance = world_size*2**(num_unlocked(Unlocks.Mazes)-1)
	use_item(Items.Weird_Substance,substance)

	x,y = measure()
	direction = [North,East,South,West]
	index = 0

	while True:
		x_now = get_pos_x()
		y_now = get_pos_y()
		if (x_now==x) and (y_now==y):
			# do_a_flip()
			harvest()
			break
		# 可以直行可以左转时选左转,同时index+=1
		if can_move(direction[index%4]) and can_move(direction[(index+1)%4]):
			move(direction[(index+1)%4])
			index += 1
		# 可以直行不能左转时直行,index不变
		elif can_move(direction[index%4]) and not can_move(direction[(index+1)%4]):
			move(direction[index%4])
		# 不能直行只能左转时左转
		elif not can_move(direction[index%4]) and can_move(direction[(index+1)%4]):
			move(direction[(index+1)%4])
			index += 1
		# 不能直行不能左转时往右看
		elif not can_move(direction[index%4]) and not can_move(direction[(index+1)%4]):
			index += 3
		else:
			index += 1