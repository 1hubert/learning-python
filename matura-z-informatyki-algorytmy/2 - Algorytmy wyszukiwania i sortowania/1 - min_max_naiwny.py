l = [2, 3, 11, 3, -3, 2, 55, 1]

min = l[0]
max = l[0]
for elem in l[1:]:
    if elem > max:
        max = elem
    elif elem < min:
        min = elem

print(f'Max: {max}')
print(f'Min: {min}')
