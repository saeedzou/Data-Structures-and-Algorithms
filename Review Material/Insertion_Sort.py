def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
                print(array)
            else:
                break
            
    return array

def insertion_sort_2(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while temp < array[j] and j > -1:
            array[j + 1] = array[j]
            array[j] = temp
            j -= 1
    return array
