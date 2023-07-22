def pivot(arr, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if arr[i] < arr[pivot_index]:
            swap_index += 1
            arr[swap_index], arr[i] = arr[i], arr[swap_index]
    arr[swap_index], arr[pivot_index] = arr[pivot_index], arr[swap_index]
    return swap_index

def __quick_sort(arr, left, right):
    if left < right:
        pivot_index = pivot(arr, left, right)
        __quick_sort(arr, left, pivot_index - 1)
        __quick_sort(arr, pivot_index + 1, right)
    return arr

def quick_sort(arr):
    return __quick_sort(arr, 0, len(arr) - 1)