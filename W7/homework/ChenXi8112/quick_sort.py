import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left) + [pivot] + quick_sort(right)

def quick_sort_3way(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = []
    equal = []
    greater = []
    for x in arr:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)
    return quick_sort_3way(less) + equal + quick_sort_3way(greater)

def quick_sort_random(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    less = []
    equal = []
    greater = []
    for x in arr:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)
    return quick_sort_random(less) + equal + quick_sort_random(greater)

if __name__ == '__main__':
    print(quick_sort([3, 1, 4, 1, 5, 9, 2, 6]))
    print(quick_sort_3way([3, 1, 4, 1, 5, 9, 2, 6]))
    print(quick_sort_random([3, 1, 4, 1, 5, 9, 2, 6]))
