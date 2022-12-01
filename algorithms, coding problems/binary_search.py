import random
import  time


def naive_search(l, target):
    for i, elem in enumerate(l):
        if elem == target:
            return i
    return -1


def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l)-1
    
    if high < low:  # this only happens when there's no target in the list
        return -1

    midpoint = (low+high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        return binary_search(l, target, midpoint+1, high)


length = 10000  # 10 000
sorted_list = set()
while len(sorted_list) < length:
    sorted_list.add(random.randint(-3*length, 3*length))

sorted_list = sorted(list(sorted_list))

start = time.time()
for target in sorted_list:
    naive_search(sorted_list, target)
end = time.time()
print(f'Total time for {length} calls of naive search: {end-start}')
print(f'Avg time for {length} calls of naive search: {(end-start)/length}')

start = time.time()
for target in sorted_list:
    binary_search(sorted_list, target)
end = time.time()
print(f'Total time for {length} calls of binary search: {end-start}')
print(f'Avg time for {length} calls of binary search: {(end-start)/length}')