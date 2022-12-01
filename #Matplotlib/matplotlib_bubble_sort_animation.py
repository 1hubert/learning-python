import random
import time

import matplotlib.pyplot as plt
import matplotlib.animation as animation


def one_step_of_bubble_sorting(lst):
    elem_count = len(lst)
    for i in range(elem_count - 1):
        for z in range(0, elem_count - i - 1):
            if lst[z] > lst[z + 1]:
                lst[z], lst[z + 1] = lst[z + 1], lst[z]
                return lst


n = 30
names = []
values = []

for i in range(n):
    names.append(i + 1)
    values.append(i + 1)
random.shuffle(values)

fig = plt.figure()
barcollection = plt.bar(names, values)


def animate(index_of_the_frame):
    y = one_step_of_bubble_sorting(values)
    if y is None:
        time.sleep(1)
        exit()
    print(y)
    for x, z in enumerate(barcollection):
        z.set_height(y[x])


anim = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
