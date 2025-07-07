def binary_search(arr,key_value) -> int:
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = (start + end) // 2

        mid_val = arr[mid]

        if mid_val == key_value:
            return mid
        elif key_value < mid_val:
            end = mid - 1
        elif key_value > mid_val:
            start = mid + 1

    return -1

sorted_numbers = [11,22,33,44,55,66,77,88,99]
key = 77
index_found = binary_search(sorted_numbers,key)

print(f'Position of {key} is at {index_found}')