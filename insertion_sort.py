#using insertion sort to sort a list 


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key <arr[j]:
            arr[j+1] = arr[j]
            j = j  -1 # dont forget to put such stopping conditions. 
        arr[j+1] = key
    return arr 

# Example usage
arr = [6,5,4,3,2,1]
sorted_arr = insertion_sort(arr)
print(sorted_arr)


