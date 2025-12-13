# 1.5v
## 说明
# 种植灌木并收获灌木

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
