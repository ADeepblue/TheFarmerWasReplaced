# 1.4v
## 说明
# 种植灌木并收获灌木

from __builtins__ import *

# plant Bush

while True:

    move(North)
    plant(Entities.Bush)

# harvest wood

while True:
    move(North)
    if can_harvest():
        harvest()