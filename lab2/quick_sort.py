
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [
            i for i in arr[1:] if i <= pivot
        ]  # seperates into two parts , one being greater than pivot and one less than pivot.
        greater = [i for i in arr[1:] if i > pivot]
        return (
            quick_sort(less) + [pivot] + quick_sort(greater)
        )  # uses recursion to sort the list.
