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

# 不逆序
not_reverse_flag = True

pre_size = measure()
for line_index in range(world_size):

	# 从左到右
	if not_reverse_flag:
		for loop_num in range(world_size - line_index -1):
			move(East)
			print(measure())
			now_size = measure()
			if now_size < pre_size:
				swap(West)
			else:
				pre_size = now_size
		print("S")
	# 从右到左
	else:
		for loop_num in range(world_size - line_index):
			move(West)
			print(measure())
			now_size = measure()
			if now_size > pre_size:
				swap(East)
			else:
				pre_size = now_size
		print("E")

	not_reverse_flag = not not_reverse_flag

harvest()




