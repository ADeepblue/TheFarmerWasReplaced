# 1.6v
# till the field, plant the carrot and get hay and wood

from __builtins__ import *
clear()
size_num = get_world_size()

# till the field in second row
move(East)
for index in range(size_num):
    till()
    move(North)

# back to the (0,0)
move(West)

#main loop
while True:
    for line_index in range(size_num):
        for row_index in range(size_num):
            if line_index == 0:
                if can_harvest():
                    harvest()
                plant(Entities.Bush)
                move(North)
            elif line_index == 1:
                if can_harvest():
                    harvest()
                plant(Entities.Carrot)
                move(North)
            else:
                if can_harvest():
                    harvest()
                move(North)


        move(East)
