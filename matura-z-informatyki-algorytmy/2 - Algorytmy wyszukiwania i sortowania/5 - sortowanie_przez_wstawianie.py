def insert_sort(arr: list) -> None:
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1


arr = [64, -25, 12, 22, -11]
insert_sort(arr)
print(arr)
