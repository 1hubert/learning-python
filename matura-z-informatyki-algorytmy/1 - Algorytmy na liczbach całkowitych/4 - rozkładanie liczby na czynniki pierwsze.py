liczba=int(input("Podaj int: "))
k=2
czynniki=[]

while(liczba!=1):
    while liczba%k==0:
        czynniki.append(k)
        liczba/=k
    k+=1

print(czynniki)
