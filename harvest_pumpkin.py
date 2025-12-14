# 1.5v
## 说明
# 种植胡萝卜并收获胡萝卜

from __builtins__ import *
from utils import *

# main
clear()
size_num = get_world_size()
# till the field
till_all_field(size_num)


square_size = size_num

while True:
	for line_index in range(size_num):
		for row_index in range(size_num):
			if line_index < square_size and row_index < square_size:
				plant(Entities.Pumpkin)
			else:
				plant(Entities.Carrot)

			move(North)

		move(East)
	while True:
		flag = 0
		for i in range(size_num):
			for j in range(size_num):
				if can_harvest() == False:
					plant(Entities.Pumpkin)
					flag += 1

				move(North)
			move(East)
		if flag == 0:
			safe_harvest()
			break


