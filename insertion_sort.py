# The ideas is sort a list like [4,2,3,1] -> [1,2,3,4]

#Let's use insertion sort this time to sort the list

#Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j -= 1 
        arr[j+1] = key
    



            
    return arr

       



array = [5,3,7,2,1]

array = insertion_sort(array)
print(array)
