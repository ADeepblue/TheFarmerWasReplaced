# game

## 1.1v

## 先前版本说明

clear() 移除农场的一切,将无人机移动回(0,0),草帽换回草帽

pet_thepiggy() 摸小猪

harvest(),收获函数,可以从草地收获物品草,Hay

do_a_filp(),无人机翻转,杂技表演



### 说明
因为无人机收获加速,草没来得及长出来,来不及收获,需要增加检测函数,如下

```python
from __builtins__ import *

while True:
    # 检测收获函数
    if can_harvest():
        harvest()
```

## 1.2v

## 解锁了帽子
更换帽子的函数
```python
from __builtins__ import *
change_hat(Hats.Gray_Hat)
```

灰帽子只是一种,还有以下
```python
from __builtins__ import *
Hats.Purple_Hat
Hats.Green_Hat
Hats.Brown_Hat
```

增加了无人机的采收速度,但是草没来得及长出来,来不及收获,需要增加检测函数,如下,其中,can_harvest()是检测是否能收获

```python
from __builtins__ import *

clear()

while True:
    # 场地增加后 往北移动,检测到边缘后自动返回原点重新向北移动
    move(North)
    # 检测收获函数

    if can_harvest():
        harvest()
```

## 1.3v

## 说明
种植功能解锁
```python
from __builtins__ import *
plant(Entities.Bush)
```
其中Entities翻译是实体方块,Bush是丛,解释成灌木丛,覆盖原有植物

## 1.4v
初始版本代码

```python
# 1.4v
## 说明
# 种植灌木并收获灌木

from __builtins__ import *

# plant Bush

flag = 0
while True:

    flag += 1
    move(North)
    plant(Entities.Bush)

    if flag >= 3:
        break

# harvest wood

while True:
    move(North)
    if can_harvest():
        harvest()
```
但是因为未解锁变量,不可使用,切版本

思路为先种植再收获,代码分开,新建一个代码文件

### 种植
```python
# plant Bush
from __builtins__ import *
while True:

    move(North)
    plant(Entities.Bush)
```

### 收获

```python
# harvest wood
from __builtins__ import *

while True:
    move(North)
    if can_harvest():
        harvest()
```

收获内容足够后,解锁运算符

内容如下:

运算符
算术运算符：+, -, *, /, //, %, **
比较运算符：==, !=, <=, >=, <, >
布尔运算符：not, and, or

后续追加可行版本
```python
from __builtins__ import *

clear()

while True:
    move(North)
    plant(Entities.Bush)
    if can_harvest():
        harvest()
    move(North)
    plant(Entities.Bush)
    if can_harvest():
        harvest()
    move(North)
    plant(Entities.Bush)
    if can_harvest():
        harvest()

```


## 1.5v
解锁胡萝卜

由于木材还不够,解锁变量需要35个胡萝卜,这个过程需要木头,是一份胡萝卜需要一个干草和一个木材,所以先得收获35个木材,通过以上函数
实现完毕后

胡萝卜
------------------------
调用 plant(Entities.Carrot) 函数可以种植胡萝卜。在种植胡萝卜之前你必须先耕地，只需调用 till() 函数即可耕地，将地块变为 Grounds.Soil 。再次调用 till() 则会将地块变回 Grounds.Grassland。

种植胡萝卜所需的耗材是干草和木材。请注意：调用 plant(Entities.Carrot) 函数种植胡萝卜时，这些耗材（干草和木材）会被消耗一定数量。

循环代码
```python
# 1.5v
## 说明
# 种植胡萝卜并收获胡萝卜

from __builtins__ import *

clear()

till()
move(North)
till()
move(North)
till()
move(North)

while True:
    move(North)
    plant(Entities.Carrot)
    if can_harvest():
        harvest()
    move(North)
    plant(Entities.Carrot)
    if can_harvest():
        harvest()
    move(North)
    plant(Entities.Carrot)
    if can_harvest():
        harvest()
```
现在都可以自动化了,其实挺舒服

解锁变量名后,可以使用for循环,不用那么麻烦了

另外,解锁了感官,还有扩展了土地面积

get_pos_x()
get_pos_y()
num_items(item)可以获取物品数量
get_entity_type可以返回类型,比如说
get_entity_type() == Entities.Bush
get_world_size()可以返回土地大小
None
断点debug

## 1.6v
all in one

```python
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
```

解锁了浇树,还有函数,还有树
# 1.7v
```python
from __builtins__ import *
clear()
size_num = get_world_size()


def single_do(line_index,row_index,size_num):
	if (line_index+row_index) % 2 == 0:
		if line_index < size_num // 2:
			plant(Entities.Tree)
		else:
			plant(Entities.Carrot)
	else:
		save_harvest()

	if get_water() <=0.5:
		use_item(Items.Water)

def save_harvest():
	if can_harvest():
		harvest()

# till the field in second row
for line_index in range(size_num):
	for row_index in range(size_num):
		if (line_index+row_index) % 2 == 0:
			till()
		else:
			save_harvest()
		move(North)
	move(East)

#main loop
while True:
	for line_index in range(size_num):
		for row_index in range(size_num):
			save_harvest()
			single_do(line_index,row_index,size_num)
			move(North)
		move(East)
```
更新了树木版本的1

## harvest_wood

草目混种版本代码

```python
# 种植灌木并收获灌木,顺带收获草

from __builtins__ import *
from utils import *
from utils import safe_harvest
clear()
size_num = get_world_size()
at_least_percent = 0.9

def do(line_index,row_index,size_num):
	if (line_index+row_index) % 2 == 0:
		plant(Entities.Tree)
	else:
		safe_harvest()

	if get_water() <=at_least_percent:
		use_item(Items.Water)



# till the field in second row
for line_index in range(size_num):
	for row_index in range(size_num):
		safe_harvest()
		if (line_index+row_index) % 2 == 0:
			till()

		move(North)
	move(East)

#main loop

while True:
	for line_index in range(size_num):
		for row_index in range(size_num):
			safe_harvest()
			do(line_index,row_index,size_num)
			move(North)
		move(East)
```

无法密集种植,会延迟时间



fertilizer版本代码

跳过


## 冒泡排序错误版本
```python
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
```
但是最后意识到,似乎,从右到左不可行,就是不能右到左直接扫过来,起始位置比较重要


## 并行无人机
巨型农场

这个极其强大的解锁项让你能够使用多架无人机。

和以前一样，一开始只有一架无人机。额外的无人机必须先被生成，且程序终止后便会消失。
每架无人机运行的都是自己独立的程序。新无人机可以使用 spawn_drone(function) 函数生成。

def drone_function():
    move(North)
    do_a_flip()

spawn_drone(drone_function)

以上代码会在运行 spawn_drone(function) 命令的无人机所在位置生成一架新的无人机。新无人机随后开始执行指定的函数，完成后便会自动消失。

无人机之间不会相互碰撞。

使用 max_drones() 获取可同时存在的无人机数量上限。
使用 num_drones() 获取农场上已有的无人机数量。

最大尺寸32

```python
from __builtins__ import *
x = 0
def fun():
	global x
	x += 1
	return x

drone_1 = spawn_drone(fun)
out = wait_for(drone_1)
quick_print(drone_1)
quick_print(out)
```
可行,再次读写出

index示范,避免搞混

row_index |
row_index |
row_index |
			-------------------------------------
			line_index      lineindex


[[12,10,11,13,14,10,12,7,14,7,10,9,13,10,13,15,14,12,13,9,14,15,11,8,15,11,15,10,14,12,7,14],
[12,14,7,10,10,9,14,9,14,13,7,12,10,12,9,9,14,13,8,13,8,11,12,10,14,14,8,14,15,7,7,13],
[12,14,11,15,12,15,13,10,9,12,9,8,10,9,11,8,12,11,12,8,10,7,9,13,9,14,14,11,8,11,15,11],
[13,8,7,13,9,12,11,10,12,10,15,8,14,13,9,9,9,8,10,13,14,12,11,13,15,8,10,14,10,15,13,10],
[10,13,14,13,8,10,11,11,7,14,8,15,13,12,10,7,11,15,7,13,7,14,11,11,11,7,11,15,10,12,12,14],
[11,15,13,12,14,7,11,10,14,10,14,14,12,9,13,8,12,13,14,10,8,7,9,14,15,11,12,15,9,8,11,10],
[13,14,10,10,14,9,11,13,12,7,9,9,15,14,12,11,14,13,11,10,15,14,12,12,12,10,8,10,9,13,9,9],
[14,9,15,12,14,7,7,8,13,11,11,12,9,12,7,7,13,14,15,11,10,13,13,15,12,10,9,10,8,12,8,7],
[15,15,7,15,13,11,7,7,9,13,9,14,8,13,14,9,15,15,14,8,8,7,10,10,10,8,10,13,10,7,15,15],
[13,12,8,10,10,14,12,10,14,9,10,7,10,7,8,12,7,13,7,9,13,12,14,10,8,7,15,9,15,11,15,12],
[8,8,9,11,13,14,9,14,11,12,11,8,7,7,11,10,7,8,14,13,7,8,10,12,12,10,10,15,10,10,15,8],
[7,10,11,10,15,8,8,8,10,12,15,13,7,15,15,13,14,7,14,7,15,13,7,8,14,10,15,12,10,15,11,9],
[13,12,9,13,15,9,12,10,10,10,10,9,9,11,11,11,8,12,7,9,15,8,14,14,15,9,14,12,7,12,15,15],
[9,13,10,7,9,10,10,7,8,9,14,12,12,15,11,7,11,8,13,12,8,8,14,14,11,7,11,11,9,7,10,11],
[8,15,7,13,7,14,7,12,7,8,10,9,10,7,8,12,10,15,12,7,9,7,12,12,11,8,15,9,8,11,15,8],
[12,11,7,9,11,15,14,12,10,11,10,10,15,9,12,8,15,14,14,14,8,8,9,9,7,11,11,12,7,13,15,14],
[13,11,9,9,12,11,12,15,14,10,8,14,8,11,12,7,12,15,9,14,7,14,14,12,13,12,13,11,12,14,10,13],
[12,15,13,11,12,12,10,13,9,9,12,9,8,15,10,10,11,7,12,9,13,14,12,14,15,8,15,14,8,12,7,11],
[11,10,13,10,11,8,14,8,11,14,8,11,12,11,13,13,15,10,12,14,12,11,8,13,12,14,9,13,14,7,7,14],
[12,13,13,15,7,14,15,10,10,15,14,8,10,10,10,9,9,9,10,14,9,7,9,10,14,11,13,7,13,8,8,9],
[7,9,8,13,12,15,7,9,12,7,12,12,8,8,11,13,14,13,12,12,8,14,8,10,11,10,14,12,7,13,14,13],
[13,10,9,9,9,8,15,15,13,14,14,12,9,10,9,14,12,10,14,10,12,14,15,8,7,14,15,11,14,12,7,9],
[9,13,9,10,12,14,10,14,9,8,15,7,14,12,9,14,14,7,15,15,13,13,12,8,10,10,7,13,12,10,12,9],
[15,11,15,9,13,7,14,7,10,8,14,11,12,14,7,8,14,7,15,10,10,8,14,9,10,10,11,13,10,14,11,11],
[7,13,9,11,7,13,13,10,9,13,7,7,12,8,10,15,15,7,9,11,13,7,8,7,12,8,11,10,14,10,15,10],
[11,9,14,13,14,14,15,11,7,8,14,10,13,10,7,9,13,9,7,8,7,9,15,14,7,11,14,8,14,12,11,8],
[15,15,10,12,12,15,15,12,14,9,11,7,7,9,10,12,11,11,12,14,7,15,8,12,11,13,13,9,13,9,11,10],
[14,10,9,12,13,9,12,11,13,13,8,14,15,10,7,8,14,12,14,10,15,7,15,7,8,15,12,11,12,9,15,8],
[8,12,13,10,14,7,12,11,15,14,14,15,9,9,11,15,14,13,8,15,9,7,14,11,15,8,14,15,11,10,10,15],
[14,9,14,15,8,10,9,11,11,12,15,7,9,8,15,10,14,11,8,7,8,9,8,7,7,12,13,9,8,11,15,7],
[13,8,15,7,12,8,10,14,12,10,15,11,14,11,7,11,15,8,15,14,14,8,12,11,12,11,13,15,15,8,8,13],
[9,12,15,9,14,10,9,15,10,8,14,15,12,7,12,14,12,10,14,10,13,10,7,9,7,10,10,13,11,7,15,9]]


## 特性

```python
from __builtins__ import *
flag = 1

def function1():
	global flag
	quick_print("function1 start", flag)
	flag += 1
	quick_print("function1 end", flag)

function1()
quick_print("main after function1", flag)
```

输出结果很令人惊喜
function1 start 1
function1 end 2
main after function1 2

也就是说,子无人机可以通过函数传递的方式改变外部变量的值,不需要一定传递句柄,那这就很方便了


还有一个
```python
from __builtins__ import *
from utils import *
flag = 0
drone_handles = []
def row_harvest_task():
	# 示例行任务：横向遍历一行，收割并向东方向移动
	global drone_handles
	global world_size
	global flag
	for _ in range(get_world_size()):
		safe_harvest()
		move(East)

	quick_print(flag)
	quick_print(num_drones(),max_drones())
	if num_drones() <= max_drones():
		tiny_sleep()
		flag += 1
		spawn_drone(row_harvest_task)


# while True:
for _ in range(max_drones()):
	if num_drones() < max_drones():
		tiny_sleep()
		flag += 1
		handle = spawn_drone(row_harvest_task)

		# drone_handles.append(handle)
		move(North)
	else:
		row_harvest_task()
```

很惊喜的发现,无人机能实现自我增值,可能在迷宫中遇到岔路的时候会很有用,但是,这样写,边界情况,无人机数量满了,然后32驾无人机,在最边界的情况,无人机要消失的时候,因为无法32+1变33导致消失前无法释放无人机,效果还不如主动控制,不过也是一种可行思路就是了

玩到这里稍稍有点累了,花了精力探索编程农场的内存模型了到头来

## 治愈植物成就

```python
from __builtins__ import *
from utils import *

# parameter setting
Cactus_Water_Level = 0
world_size = 32

# set world
# set_world_size(world_size)

# init

harvest_all_spawn()
clear()
## till the field
back_zero()
till_in_parallel()


to_position((4,4))
plant(Entities.Bush)
use_item(Items.Weird_Substance)
use_item(Items.Weird_Substance)
```

## 仙人掌反向排序成就
```python
from __builtins__ import *
from utils import *

# parameter setting
Cactus_Water_Level = 0
world_size = 4

# set world
set_world_size(world_size)

# init

harvest_all_spawn()
clear()
## till the field
back_zero()
till_in_parallel()


# functions
def plant_cactus_line_task():
	for _ in range(world_size):
		plant(Entities.Cactus)
		move(East)

def bubble_sort_line_task():
	global row_index
	to_position((0, row_index))
	for line_index in range(get_world_size()):
		pre_size = measure()
		for _ in range(get_world_size() - line_index - 1):
			move(East)
			now_size = measure()
			if now_size < pre_size:
				pre_size = now_size
			else:
				swap(West)

		to_position((0, row_index))

def bubble_sort_row_task():
	global line_index
	to_position((line_index, 0))
	for row_index in range(get_world_size()):
		pre_size = measure()
		for _ in range(get_world_size() - row_index - 1):
			move(North)
			now_size = measure()
			if now_size < pre_size:
				pre_size = now_size
			else:
				swap(South)
		to_position((line_index, 0))

# main loop
# max 32 version
while True:

	# plant cactus
	for _ in range(world_size-1):
		tiny_sleep()
		spawn_drone(plant_cactus_line_task)
		move(North)

	plant_cactus_line_task()
	move(North)
	# wait_for_all_drones_finished()

	back_zero()
	# line sort
	for row_index in range(world_size-1):
		tiny_sleep()
		spawn_drone(bubble_sort_line_task)
		move(North)

	row_index += 1
	bubble_sort_line_task()
	move(North)
	# wait_for_all_drones_finished()

	back_zero()
	move(West)
	# row sort
	for line_index in range(world_size-1,0,-1):
		tiny_sleep()
		spawn_drone(bubble_sort_row_task)
		move(West)

	line_index -= 1
	bubble_sort_row_task()
	move(West)
	wait_for_all_drones_finished()

	safe_harvest()
```

## 栈溢出成就
```python
def bomb():
    bomb()

bomb()
```

## 导入循环
```python
# temp.py file
# only for achieve
from second_temp_done import *
```
```python
# second_temp_done.py file
from temp import *
```

## 帽子成就
```python
from __builtins__ import *
from utils import *

# parameter setting
Cactus_Water_Level = 0
world_size = 32

# set world
# set_world_size(world_size)

# init

Hats_list = [Hats.Brown_Hat,Hats.Cactus_Hat,Hats.Carrot_Hat,Hats.Gold_Hat,Hats.Golden_Cactus_Hat]

to_position((5,5))

def wear_hat():
    change_hat(hat)
    while True:
        do_a_flip()

for hat in Hats_list:
    tiny_sleep()
    spawn_drone(wear_hat)
```

## 一分钟10亿木材
```python
from __builtins__ import *
from utils import *

# parameter setting
Cactus_Water_Level = 0.8
world_size = 32

# set world
# set_world_size(world_size)

# init
clear()
def plant_bush_and_tree():
    x,y = get_position()
    if (x+y) % 2 ==0:
        plant(Entities.Tree)
        water_the_field(Cactus_Water_Level)
    else:
        plant(Entities.Bush)
        water_the_field(Cactus_Water_Level)



back_zero()
def line_plant_task():
    while True:
        for _ in range(world_size):
            safe_harvest()
            plant_bush_and_tree()
            move(East)


for _ in range(world_size-1):
    tiny_sleep()
    spawn_drone(line_plant_task)
    move(North)

line_plant_task()
```

## 快速巨型南瓜的最终版本

```python
# 32无人机版本 4*8
from __builtins__ import *
from utils import *

# parameter setting
Cautious_Water_Level = 0.6
Num_line = 5
Num_row = 8
single_line_field = get_world_size() / Num_line
single_row_field = get_world_size() / Num_row
world_size = 32
set_world_size(world_size)


# init
# clear()

# till the field
back_zero()
till_in_parallel()

back_zero()

# main
def single_plant_task():
	to_position((line_num_index*single_line_field,row_num_index*single_row_field))
	# plant the pumpkin
	for row_index in range(single_row_field):
		for line_index in range(single_line_field):
			plant(Entities.Pumpkin)
			water_the_field(Cautious_Water_Level)
			move(East)
		to_position((line_num_index * single_line_field, row_num_index * single_row_field+ row_index+1))

		quick_print(row_num_index,(line_num_index * single_line_field, row_num_index * single_row_field))
	to_position((line_num_index * single_line_field, row_num_index * single_row_field))
	# check bad pumpkin

	bad_pumpkin_list = []

	for row_index in range(single_row_field):
		for line_index in range(single_line_field):
			if can_harvest() == False:
				plant(Entities.Pumpkin)
				bad_pumpkin_list.append(get_position())

			move(East)
		to_position((line_num_index * single_line_field, row_num_index * single_row_field+row_index+1))

	to_position((line_num_index * single_line_field, row_num_index * single_row_field))

	# kill all the bad pumpkin

	while True:
		temp_list = []
		for position in bad_pumpkin_list:
			to_position(position)
			if not can_harvest():
				plant(Entities.Pumpkin)
				temp_list.append(position)

		bad_pumpkin_list = temp_list

		if len(temp_list) == 0:
			break


for row_num_index in range(Num_row):
	for line_num_index in range(Num_line):
		# quick_print(row_num_index,line_num_index)
		if (line_num_index != Num_line-1) or (row_num_index != Num_row-1):
			tiny_sleep()
			spawn_drone(single_plant_task)
			# single_plant_task()

# 不需要加一,因为上面已经加过了
# line_num_index += 1

single_plant_task()

wait_for_all_drones_finished()
back_zero()
safe_harvest()
```

但是打算优化成6*6的了,所以即将弃用

# 贪吃蛇现在待解决的问题
绕路的时候,如果一旦路上有遇到苹果,就直接完蛋了,因为会提前吃掉苹果,而不知道苹果在那,导致下一次measure函数信息丢失,衔接不上了,

合适的话,最好是,如果是遇到堵塞,新建寻路算法,break原有的算法循环,snake_length主动加一


```python
loop_num = get_world_size()+(((snake_length-get_world_size())/(get_world_size()-1))//2+1)*2*(get_world_size()-1)
```

其中这个loop num是指,先判断长度大于边长了,先把最左边的提出来,后面的因为要给下面的回流通留空隙,所以是32-1,然后又有因为最好每次是从上面出来的,所以1到61全部填充为62
所以是蛇长减去32,出来的数取除31再整除2,但是是要浮点向上取整,所以整除的话得加1,出来的基数再乘以62即可


现有另一个format eat需要x对齐,就是x为1的时候从1下手,2的时候也从1下手,单数下手,双数上,但是不希望多判断了,直接写下手的数

```python
start_x_position_num = ((x+1)//2)*2-1
```


## 内存模型
```python
from __builtins__ import *
from utils import *

# parameter setting
Cactus_Water_Level = 0.5
world_size = 32

# set world
# set_world_size(world_size)

# init


def temp_task():
	while True:
		print(get_flag())
		do_a_flip()
		print(flag)

def get_flag():
	return flag


flag = 0
to_position((30,31))
spawn_drone(temp_task)
move(East)
while True:
	print(flag)
	do_a_flip()
	flag+=1

```
上面一份代码,临时无人机一直只会打印0,说明其实主环境都隔离了,等于是,在外部新建了一个主环境变量的副本,然后执行,并不能大环境互通

但是现在又有
```python
from __builtins__ import *
from utils import *

# parameter setting
Cactus_Water_Level = 0.5
world_size = 32

# set world
# set_world_size(world_size)

# init


def temp_task():
	global flag
	while True:
		flag +=1
		handle = spawn_drone(handle_task)
		print(flag)
		while True:
			if has_finished(handle):
				print(wait_for(handle))
				break


def handle_task():
	global flag
	to_position((27, 31))
	do_a_flip()
	return flag


flag = 0
to_position((30,31))
spawn_drone(temp_task)
move(East)
while True:
	print(flag)
	do_a_flip()
	do_a_flip()
	flag+=1

```

寄存变量也是如此,直接global一下,在全局放一个变量,函数内赋值一次即可
```python
from __builtins__ import *
from utils import *

# parameter setting
Cactus_Water_Level = 0.5
world_size = 32

# set world
# set_world_size(world_size)

# init


def temp_task():
	global flag
	global temp_flag
	temp_flag = 5
	while True:
		flag +=1
		handle = spawn_drone(handle_task)
		print(flag)
		while True:
			if has_finished(handle):
				print(wait_for(handle))
				break


def handle_task():
	global temp_flag
	global flag
	to_position((27, 31))
	# do_a_flip()
	print(temp_flag)
	return flag

temp_flag = 2
flag = 0
to_position((30,31))
spawn_drone(temp_task)
move(East)
while True:
	print(flag)
	do_a_flip()
	do_a_flip()
	flag+=1
	
```


无人机生成链条如下
主无人机->次级无人机->第二次级无人机
其中,第二次级无人机的global继承的次级无人机的内存模型,很显然handle task并不会打印主环境里的flag的值,这里也就以为着
通过次级无人机生成从无人机是可行的,那么基本就有解了,挑战南瓜刷榜的时候,只要生成一架,然后第二架无人机变成前一架的从属即可


## 布置场地
通过excel模拟,32=1+6+2+6+2+6+2+6+1
也就是左下的边界坐标分别是(1,1),(1,9),(1,17),(1,25)
但是我其实希望次级无人机的位置在中央,也就是左下角往上走两格的地方

1 2 3 4 5 6
↓ →→↓ →→↓ ↑
↓ ↑ ↓ ↑ ↓ ↑
→→↑ →→↑ →→↑

路径如上,由于可重复性,这个可以当作扫描的路

所以起始位置如下(1,3),(1,11),(1,19),(1,27)

      (1,1)
往右坐标(0,0),(1,2),(2,0),(3,2),(4,0)
实际坐标(1,1),(2,3),(3,1),(4,3),(5,1)
