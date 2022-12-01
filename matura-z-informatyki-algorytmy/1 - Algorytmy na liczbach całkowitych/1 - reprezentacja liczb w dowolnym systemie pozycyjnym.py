def zamiana(liczba, sys):
    lista=[]
    while(liczba!=0):
        if(liczba%sys==0):
            liczba=liczba/sys
            lista.append("0")
        else:
            liczba=(liczba-1)/sys
            lista.append("1")
    lista.reverse()

    string=""
    for elem in lista:
        string+=elem
    
    return string

             

print(zamiana(5, 9))

