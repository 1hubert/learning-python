def fibo_iter(kolejnych):
    if kolejnych==1:
        return [1]
    
    liczby = [1, 1]
    for i in range(kolejnych-2):
        liczby.append(liczby[i]+liczby[i+1])
    return liczby


def fibo_iter2(n):
    liczby=[]
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
        liczby.append(a)
    return liczby


def fibo_rekur(numer):
    if numer == 0:
        return 0

    elif numer == 1:
        return 1

    else:
        return fibo_rekur(numer-1)+fibo_rekur(numer-2)
    

def fibo_rekur2(numer):
    if numer <= 2:
        return 1
    else:
        return fibo_rekur2(numer-1)+fibo_rekur2(numer-2)

def fibo_rekur2_lista(numer):
    liczby=[]
    for i in range(1, numer+1):
        
        liczby.append(fibo_rekur2(i))

    return liczby


class FibIter:

    def __init__(self, n):
        self.n = n
        

    def __iter__(self):
        self.i = 0
        self.a, self.b = 0, 1
        return self
    
    def __next__(self):
        if self.n != self.i:
            self.i += 1
            self.a, self.b = self.b, self.a + self.b
            return self.a
        raise StopIteration
        


class FibIterGen:

    def __init__(self, n):
        self.n = n
        

    def __iter__(self):
        self.i = 0
        self.a, self.b = 0, 1

        for i in range(self.n):
            self.a, self.b = self.b, self.a + self.b
            yield self.a

print(fibo_rekur2_lista(5))




