def merge(arr1, arr2):
    arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            arr.append(arr2[j])
            j += 1
        else:
            arr.append(arr1[i])
            i += 1
    while i < len(arr1):
        arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        arr.append(arr2[j])
        j += 1
    return arr

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid_index = int(len(arr) / 2)
    left = merge_sort(arr[:mid_index])
    right = merge_sort(arr[mid_index:])
    return merge(left, right)