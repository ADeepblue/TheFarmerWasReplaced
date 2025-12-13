# game

## 1.1v

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
Hats.Purple_Hat
Hats.Green_Hat
Hats.Brown_Hat
```


```python
from __builtins__ import *

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
其中Entities翻译是实体方块,Bush是丛,解释成灌木丛