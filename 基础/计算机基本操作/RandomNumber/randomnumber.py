#！/usr/bin/env python
# ---*--- coding: utf-8 ---*---


import random

 
random.random()

random.uniform(0, 1)

random.randint(1, 10)


data_set = [i for i in range(1, 101)]
random.choice(data_set)

# replace = no
random.sample(data_set, 10)

# random disturbe
random.shuffle(data_set)