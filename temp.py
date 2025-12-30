from __builtins__ import *
from utils import *

# parameter setting
Cactus_Water_Level = 1

# init up_flag
up_flag = False
half_bad_pumpkin_list = []
# init the position information,clock_wise
clear()


def generate_hilbert_path(n):
	"""基于你的正确实现生成路径"""
	path = []
	position = [0, 0]

	up = [0, 1]
	down = [0, -1]
	left = [-1, 0]
	right = [1, 0]

	def move_vec(list_1, list_2):
		return [list_1[0] + list_2[0], list_1[1] + list_2[1]]

	def record_move(direction):
		nonlocal position
		position = move_vec(position, direction)
		path.append(tuple(position))

	def hilbert(n, up, right, down, left):
		if n == 1:
			record_move(up)  # 第一步：向上
			record_move(right)  # 第二步：向右
			record_move(down)  # 第三步：向下
		else:
			hilbert(n - 1, right, up, left, down)
			record_move(up)
			hilbert(n - 1, up, right, down, left)
			record_move(right)
			hilbert(n - 1, up, right, down, left)
			record_move(down)
			hilbert(n - 1, left, down, right, up)

	path.append(tuple(position))  # 起点 (0, 0)
	hilbert(n, up, right, down, left)

	return path




# 生成32x32的5阶希尔伯特曲线
hilbert_path = generate_hilbert_path(5)  # 2^5 = 32
print(get_tick_count())
# print(f"路径长度: {len(hilbert_path)}")  # 应该是 1024

def temp_task():
	to_position(hilbert_path[index*32])
	while True:
		print(num_drones())
for index in range(1,32):
	# print(hilbert_path[index*32])
	spawn_drone(temp_task)

print(num_drones())
to_position((0,0))
while True:
	print(num_drones())