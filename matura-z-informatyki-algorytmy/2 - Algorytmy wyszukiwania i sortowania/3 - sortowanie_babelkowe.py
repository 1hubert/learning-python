def bubble_sort(arr: list) -> None:
    n = len(arr)

    for i in range(0, n-1):
        for x in range(0, n-i-1):
            if arr[x] > arr[x+1]:
                arr[x], arr[x+1] = arr[x+1], arr[x]


arr = [-1, 3, -2, 66, -17]
bubble_sort(arr)
print(arr)
