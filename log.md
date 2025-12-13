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

后续追加



## 1.5v
解锁胡萝卜

由于木材还不够,解锁变量需要35个胡萝卜,这个过程需要木头,是一份胡萝卜需要一个干草和一个木材,所以先得收获35个木材,通过以上函数
实现完毕后

胡萝卜
------------------------
调用 plant(Entities.Carrot) 函数可以种植胡萝卜。在种植胡萝卜之前你必须先耕地，只需调用 till() 函数即可耕地，将地块变为 Grounds.Soil 。再次调用 till() 则会将地块变回 Grounds.Grassland。

种植胡萝卜所需的耗材是干草和木材。请注意：调用 plant(Entities.Carrot) 函数种植胡萝卜时，这些耗材（干草和木材）会被消耗一定数量。

但好像意识到一个事,不需要通过for循环来搞定,只要能重复收获就行了