# program to perfom linear search recursively 


def linear_search(arr,n, x):
    if n<0: 
        return -1
    if arr[n] == x:
        return n 
    return linear_search(arr,n-1,x)

a = linear_search([1,2,3,4,5,6,7,8,9],8,8)

print(a) #prints the index of 8 in the list 
