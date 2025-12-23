from __builtins__ import *
from utils import *

# parameters
filename = "temp"
sim_unlocks = Unlocks
base_num = 10000
sim_items = {Items.Carrot:base_num,Items.Hay:base_num,Items.Fertilizer:1000000000,Items.Water:1000000000,Items.Power:1000000000,Items.Carrot:10000000000}
sim_global = {'Cactus_Water_Level' : 0.5,'world_size' : 32}
seed=0
speedup=10
runtime = simulate(filename,sim_unlocks,sim_items,sim_global,seed,speedup)