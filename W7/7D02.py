"""7D02-废土快排"""

def quick_sort(arr):
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
    return quick_sort(less) + equal + quick_sort(greater)

if __name__ == '__main__':
    print(quick_sort([3, 1, 4, 1, 5, 9, 2, 6]))
