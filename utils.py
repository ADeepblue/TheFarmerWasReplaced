
from __builtins__ import *

def single_do(line_index,row_index,size_num):
	if (line_index+row_index) % 2 == 0:
		if line_index < size_num // 2:
			plant(Entities.Tree)
		else:
			plant(Entities.Carrot)
	else:
		save_harvest()

	if get_water() <=0.6:
		use_item(Items.Water)



def save_harvest():
	if can_harvest():
		harvest()