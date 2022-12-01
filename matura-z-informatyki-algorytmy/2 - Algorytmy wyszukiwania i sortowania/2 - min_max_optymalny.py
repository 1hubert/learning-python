l = [2, 2, 11, 3, -3, 2, 55, 1]

larger = []
smaller = []
if l % 2 == 0:
    for i in range(0, len(l), 2):
        if l[i] > l[i+1]:
            larger.append(l[i])
            smaller.append(l[i+1])
        else:
            larger.append(l[i+1])
            smaller.append(l[i])
else:
    for i in range(0, len(l)-1, 2):
        if l[i] > l[i+1]:
            larger.append(l[i])
            smaller.append(l[i+1])
        else:
            larger.append(l[i+1])
            smaller.append(l[i])
    
    larger.append(l[-1])
    smaller.append(l[-1])

max = larger[0]
min = smaller[0]
for i in range(1, len(larger)):
    if larger[i] > max:
        max = larger[i]
    if smaller[i] < min:
        min = smaller[i]

print(larger)
print(smaller)
print(f'Max: {max}')
print(f'Min: {min}')
