def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Example usage
arr = [5, 2, 9, 1, 7, 6, 3]
sorted_arr = quick_sort(arr)
print(sorted_arr)

# co pilot code for now , will do it on my own later on. 