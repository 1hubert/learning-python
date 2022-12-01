def czy_doskonala(x):
    list = []
    for i in range(1, int(x/2)+1):
        if (x%i==0):
            list.append(i)
    sum=0
    for elem in list:
        sum+=elem
    if sum==x:
        print("ta liczba jest doskonala")
    else:
        print("ta liczba nie jest doskonała")

czy_doskonala(28)



            
