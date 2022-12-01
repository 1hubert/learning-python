l = int(input("Podaj liczbe calkowita: "))
l_sqrt = int(l**(1/2))


for i in range(1, l_sqrt+1):


    if l%i==0 and i!=1:
        print("Liczba złożona (",l," = ",i," * ",int(l/i))
        break

    
    if i==l_sqrt:
        print("Liczba pierwsza")
        break














