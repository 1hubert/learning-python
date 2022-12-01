func1 = lambda x: x ** 2

do_podniesienia_do_potegi = [2, 3, 4, 11, 22]
print(max(map(func1, do_podniesienia_do_potegi)))

print('2,3'.split(','))


seq = [1, 2, 3, 4]

result   = map(lambda x: x % 2 != 0, seq)
print(list(result))  # [True, False, True, False]

result = filter(lambda x: x % 2 == 0, seq)  
print(list(result))  # [2, 4]


fruits = {'banana'}

fruits.add('apple')
print(fruits)  # {'banana', 'apple'}

fruits.remove('banana')
print(fruits)  # {'apple'}

fruits.discard("blackberry")
print(fruits)  # {'apple'}  (without error!)
a = 'xd'
b = 'xd'
print()