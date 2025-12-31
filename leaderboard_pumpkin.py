from __builtins__ import *
from utils import *

# parameter setting
Cactus_Water_Level = 1

# init up_flag
up_flag = False
half_bad_pumpkin_list = []
# init the position information,clock_wise
clear()

East_position_list_CCW = [(1,1),(2,3),(3,1),(4,3),(5,1)]
West_postion_list_CCW = [(2,6),(3,4),(4,6),(5,4),(6,6)]
South_position_list_CCW = [(1,2),(1,3),(1,4),(1,5),(1,6),(3,2),(3,3),(3,5),(3,6),(5,2),(5,3),(5,5),(5,6)]
North_position_list_CCW = [(2,1),(2,2),(2,4),(2,5),(4,1),(4,2),(4,4),(4,5),(6,1),(6,2),(6,3),(6,4),(6,5)]

East_position_list_CW = [(1,6),(2,4),(3,6),(4,4),(5,6)]
West_postion_list_CW = [(2,1),(3,3),(4,1),(5,3),(6,1)]
South_position_list_CW = [(2,2),(2,3),(2,5),(2,6),(4,2),(4,3),(4,5),(4,6),(6,2),(6,3),(6,4),(6,5),(6,6)]
North_position_list_CW = [(1,1),(1,2),(1,3),(1,4),(1,5),(3,1),(3,2),(3,4),(3,5),(5,1),(5,2),(5,4),(5,5)]

# init
def not_false_true(bool_symbol):
	if bool_symbol:
		return False
	elif not bool_symbol:
		return True
	else:
		return None


def check_position_in_list(position, position_list):
	x = position[0]
	y = position[1]
	x_mod = x % 8
	y_mod = y % 8
	if (x_mod, y_mod) in position_list:
		return True
	else:
		return False

def check_CCW_direction(position):
	if check_position_in_list(position,East_position_list_CCW):
		return East

	elif check_position_in_list(position,West_postion_list_CCW):
		return West

	elif check_position_in_list(position,North_position_list_CCW):
		return North

	elif check_position_in_list(position,South_position_list_CCW):
		return South


def check_CW_direction(position):
	if check_position_in_list(position,East_position_list_CW):
		return East

	elif check_position_in_list(position,West_postion_list_CW):
		return West

	elif check_position_in_list(position,North_position_list_CW):
		return North

	elif check_position_in_list(position,South_position_list_CW):
		return South

def sub_drone_till_and_plant_task():
	global up_flag

	for _ in range(18):
		only_turn_to_soil()
		plant(Entities.Pumpkin)
		if get_water() <= Cautious_Water_Level:
			use_item(Items.Water)

		if up_flag:
			direction = check_CW_direction(get_position())
			move(direction)
		else:
			direction = check_CCW_direction(get_position())
			move(direction)

def sub_plant_task():
	global up_flag

	for _ in range(18):
		plant(Entities.Pumpkin)
		if get_water() <= Cautious_Water_Level:
			use_item(Items.Water)

		if up_flag:
			direction = check_CW_direction(get_position())
			move(direction)
		else:
			direction = check_CCW_direction(get_position())
			move(direction)


def sub_check_bad_pumpkin():
	global up_flag
	bad_pumpkin_list = []
	for _ in range(18):
		if not can_harvest():
			plant(Entities.Pumpkin)
			bad_pumpkin_list.append(get_position())
		safe_water_the_field(Cautious_Water_Level)

		if up_flag:
			direction = check_CW_direction(get_position())
			move(direction)
		else:
			direction = check_CCW_direction(get_position())
			move(direction)

	return bad_pumpkin_list

def sub_kill_bad_pumpkin():
	global half_bad_pumpkin_list
	while True:
		if num_items(Items.Pumpkin) >= 200000000:
			break

		temp_list = []
		for position in half_bad_pumpkin_list:
			to_position(position)
			if not can_harvest():
				plant(Entities.Pumpkin)
				if len(half_bad_pumpkin_list) ==1 and num_items(Items.Fertilizer) >= 2:
					# use_item(Items.Weird_Substance)
					use_item(Items.Fertilizer)
					# use_item(Items.Weird_Substance)
				temp_list.append(position)

		half_bad_pumpkin_list = temp_list

		if len(temp_list) == 0:
			break


def main_task():
	global up_flag
	global half_bad_pumpkin_list
	start_postion = (index2*8+1,index1*8+3)
	to_position(start_postion)
	# (1,3)
	# 负责下半部分
	up_flag = True
	move(North)
	spawn_drone(sub_drone_till_and_plant_task)

	move(South)
	up_flag = False
	sub_drone_till_and_plant_task()

	while True:

		if num_items(Items.Pumpkin) >= 200000000:
			break
		# check bad pumpkin
		to_position(start_postion)
		up_flag = True
		move(North)
		sub_drone = spawn_drone(sub_check_bad_pumpkin)

		move(South)
		up_flag = False
		main_bad_pumpkin_list = sub_check_bad_pumpkin()

		while True:
			if has_finished(sub_drone):
				half_bad_pumpkin_list = wait_for(sub_drone)
				break


		sub_drone = spawn_drone(sub_kill_bad_pumpkin)



		while True:
			temp_list = []
			for position in main_bad_pumpkin_list:
				to_position(position)
				if not can_harvest():
					plant(Entities.Pumpkin)
					if len(half_bad_pumpkin_list) == 1 and num_items(Items.Fertilizer) >= 2:
						use_item(Items.Weird_Substance)
						use_item(Items.Fertilizer)
						use_item(Items.Weird_Substance)

					temp_list.append(position)

			main_bad_pumpkin_list = temp_list

			if len(temp_list) == 0:
				break

		while True:
			if has_finished(sub_drone):
				wait_for(sub_drone)
				break

		safe_harvest()


def quick_print_position():
	print(get_position())

to_position((0,2))



for index1 in range(4):
	for index2 in range(4):
		tiny_sleep()
		if not ((index1==3) and (index2==3)):
			spawn_drone(main_task)

main_task()
