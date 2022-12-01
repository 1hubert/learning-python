liczba = 0
arr = [2, 1, 3, 5, 4]
n = len(arr)
p = 2000000000/n  # zakres jednego kubełka
kubelki = [[] for i in arr]
# przedziały dla kolejnych kubełkow: 
# [0, p), [p, 2p), [2p, 3p), ..., [(n-1)p, n*p)

for i in range(n):
    kubelki_index = int(arr[i]//p)
    kubelki[kubelki_index].append(arr[i])

for i in range(n):
    if len(kubelki[i]) > 1:
        kubelki[i] = sorted(kubelki[i])

for i in range(n):
    for j in range(len(kubelki[i])):
        print(kubelki[i][j])
