# def f1(func):

#     def wrapper():
#         print('Started')
#         func()
#         print('Ended')
    
#     return wrapper

# def f2(func):
#     print('Started')
#     func()
#     print('Ended')

# def f():
#     print('Helllllll\'o kitty')

# aaa = f1(f)

# aaa()





"""code for testing decorator chaining
def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner
 
def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner
 
@decor1
@decor
def num():
    return 10
 
print(num())  # returns 400

# The above example is similar to setting the funcion value to decor1(decor(num))
"""





from genericpath import samestat
import mailbox
import time

def timer(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        val = func(*args, **kwargs)
        print(f'Function took {time.time() - start} to run.')
        return val

    return wrapper

@timer
def x_to_the_power_of_n(x, n=2):
    return x ** n

# (2: positional argument, n=2: keyword argument)
print(x_to_the_power_of_n(2, n=2))






def executor(func):

    def wrapper(*args, **kwargs):
        print(f'EXECUTINGG {func} with positional arguments: {args} and keyword arguments: {kwargs if list(kwargs) else [None]}')
        return func(*args, **kwargs)

    return wrapper

def battle_cry(func):
    
    def wrapper(*args, **kwargs):
        print('LETS BEGIN DA FUNKTIONE!!!!111111')
        val = func(*args, **kwargs)
        print('DA FUNKTIONE ENDO')
        return val
    
    return wrapper

def anotha_one(func):

    def wrapper(*args, **kwargs):
        print('-----------------start---------------')
        val = func(*args, **kwargs)
        print('-----------------end---------------')
        return val
    
    return wrapper

@anotha_one
@battle_cry
@executor
def witcher_hunter(age, name='Zygmunta'):
    print(f'HANTINGU {name}, {age} years old. WE WILL KIRU HER!!')

witcher_hunter(119, name='Olla')




class Numerki:
    def __init__(self, x):
        self.x = x

    def multiply_by_10(func):
        def wrapper(*args):
            print(args)
            return func(*args) * 10
        return wrapper

    def add_1(func):
        def wrapper(*args):
            return func(*args) + 1
        return wrapper

    def substract_3(func):
        def wrapper(*args):
            return func(*args) - 3
        return wrapper

    def divide_by_2(func):
        def wrapper(*args):
            return func(*args) / 2
        return wrapper

    @substract_3
    @add_1
    @divide_by_2
    @multiply_by_10
    def do_stuff(self):
        return self.x

#n = Numerki(1)
# pytanie: co zwróci:
#print(n.do_stuff())





from functools import wraps
def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
   """does some math"""
   return x + x * x

print(f.__name__)  # prints 'f'
print(f.__doc__)   # prints 'does some math'