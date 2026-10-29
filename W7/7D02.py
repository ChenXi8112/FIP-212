"""7D02-废土快排"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = []
    equal = [pivot]
    greater = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            less.append(arr[i])
        elif arr[i] == pivot:
            equal.append(arr[i])
        else:
            greater.append(arr[i])
    return quick_sort(less) + equal + quick_sort(greater)

if __name__ == '__main__':
    print(quick_sort([3, 1, 4, 1, 5, 9, 2, 6]))
