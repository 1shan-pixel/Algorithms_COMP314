#sorting a list using selection_sort 

def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i 
        for j in range(i+1, len(arr)):
            if(arr[j]<arr[minimum]):
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i] 
    return arr 

# Example usage
arr = [6,5,4,3,2,1]
sorted_arr = selection_sort(arr)
print(sorted_arr)