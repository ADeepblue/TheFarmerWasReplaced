from __builtins__ import *
from utils import *

# parameters
filename = "temp"
sim_unlocks = Unlocks
base_num = 0
sim_items = {Items.Carrot:base_num,Items.Hay:base_num,Items.Fertilizer:1000000000,Items.Water:1000000000,Items.Power:1000000000,Items.Cactus:base_num}
sim_global = {'Cactus_Water_Level' : 0.5,'world_size' : 32}
seed=5
speedup=50000
runtime = simulate(filename,sim_unlocks,sim_items,sim_global,seed,speedup)
# quick_print(get_tick_count())