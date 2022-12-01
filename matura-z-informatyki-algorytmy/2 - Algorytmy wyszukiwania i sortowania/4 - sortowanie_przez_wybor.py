def selection_sort_min_idx(arr: list) -> None:
    n = len(arr)

    for i in range(n-1):
        
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                      
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def selection_sort_max_idx(arr: list) -> None:
    n = len(arr)

    for i in range(n-1):

        max_idx = n-i-1
        for j in range(n-i-1):
            if arr[j] > arr[max_idx]:
                max_idx = j
        
        arr[n-i-1], arr[max_idx] = arr[max_idx], arr[n-i-1]
    
    return arr


arr = [64, -25, 12, 22, -11]
selection_sort_max_idx(arr)
print(arr)
