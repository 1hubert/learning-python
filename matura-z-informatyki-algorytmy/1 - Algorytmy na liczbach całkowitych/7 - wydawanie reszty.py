nominaly = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
reszta = []


def wydaj_reszte(do_wydania):
    i=0
    while(do_wydania>0):
        if(do_wydania-nominaly[i])>=0.0:
            do_wydania-=nominaly[i]
            reszta.append(nominaly[i])
            #print("nominaly ",nominaly[i])
            #print("reszta ",zaplacono)
        else:
            if(i+1<len(nominaly)):
                
                i=i+1
                #print("i = ",i)
            else:
                break
    print("___________")
    for elem in reszta:
        print(elem)
    return do_wydania
                
#do_zaplacenia = float(input("do zapłacenia "))
zaplacono = float(input("zaplacono "))
do_wydania = wydaj_reszte(zaplacono)
