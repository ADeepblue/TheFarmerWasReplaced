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