def merge_sort(array):
    if(len(array)==1):
        return array
    half = len(array)//2
    left_array = merge_sort(array[:half])
    right_array = merge_sort(array[half:])
    return merge(left_array,right_array)


def merge(left,right):
    sorted_array = []
    left_pos, right_pos = 0 , 0 
    while left_pos < len(left) and right_pos < len(right):
        if left[left_pos]<right[right_pos]:
            sorted_array.append(left[left_pos])
            left_pos = left_pos + 1 
        else : 
            sorted_array.append(right[right_pos])
            right_pos = right_pos + 1 
    sorted_array.extend(left[left_pos:])
    sorted_array.extend(right[right_pos:])

    return sorted_array


array = [1,3,5,2,60,42,0]

ar = merge_sort(array)
print(ar)

