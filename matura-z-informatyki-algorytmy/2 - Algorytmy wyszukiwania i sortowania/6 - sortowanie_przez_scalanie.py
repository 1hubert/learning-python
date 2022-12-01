def merge_sort(arr: list) -> None:
    if len(arr) > 1:
        print('Argument: ', arr)
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # Recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # Merge
        l = 0  # left_arr index
        r = 0  # right_arr index
        m = 0  # merged array index
        while l < len(left_arr) and r < len(right_arr):
            if left_arr[l] < right_arr[r]:
                arr[m] = left_arr[l]
                print('arr[', m, '] = ', left_arr[l])
                l += 1
            else:
                arr[m] = right_arr[r]
                print('arr[', m, '] = ', right_arr[r])
                r += 1
            m += 1

        while l < len(left_arr):
            arr[m] = left_arr[l]

            print('arr[', m, '] = ', left_arr[l])
            l += 1
            m += 1

        while r < len(right_arr):
            arr[m] = right_arr[r]
            print('arr[', m, '] = ', right_arr[r])
            r += 1
            m += 1
    print()


arr = [2, 44, -1, 3333, 2, 0, -12]
merge_sort(arr)
print(arr)
