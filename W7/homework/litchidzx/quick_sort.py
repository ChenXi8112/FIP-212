import time
import random
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [ x for x in arr[1:] if x < pivot]
    right = [ x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def quick_sort_random(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [ x for x in arr if x < pivot]
    right = [ x for x in arr if x > pivot]
    equal = [ x for x in arr if x == pivot]
    return quick_sort_random(left) + equal + quick_sort_random(right)

def quick_sort_local(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    equal = []
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            equal.append(x)
    return quick_sort_local(left) + equal + quick_sort_local(right)

def quick_sort_Lomuto(arr, lo, hi):
    def Lomuto(arr, lo, hi):
        pivot = arr[hi]
        i = lo
        for j in range(lo, hi):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[hi] = arr[hi], arr[i]
        return i
    if lo >= hi:
        return 
    p = Lomuto(arr, lo, hi)
    quick_sort_Lomuto(arr, lo, p - 1)
    quick_sort_Lomuto(arr, p + 1, hi)
    return arr

def quick_sort_Hoare(arr, lo, hi):
    def Hoare(arr, lo, hi):
        pivot = arr[lo]
        i = lo - 1
        j = hi + 1
        while True:
            i += 1
            while arr[i] < pivot:
                i += 1
            j -= 1
            while arr[j] > pivot:
                j -= 1
            if i >= j:
                return j
            arr[i], arr[j] = arr[j], arr[i]
    if lo >= hi:
        return 
    p = Hoare(arr, lo, hi)
    quick_sort_Hoare(arr, lo, p)
    quick_sort_Hoare(arr, p + 1, hi)
    return arr


    

t1 = time.perf_counter()
print(quick_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , 12, 13, 14, 15, 16, 17, 18, 19, 20]))
t2 = time.perf_counter()
print(quick_sort_random([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , 12, 13, 14, 15, 16, 17, 18, 19, 20]))
t3 = time.perf_counter()
print(quick_sort_local([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , 12, 13, 14, 15, 16, 17, 18, 19, 20]))
t4 = time.perf_counter()
print(quick_sort_Lomuto([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , 12, 13, 14, 15, 16, 17, 18, 19, 20], 0, len([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , 12, 13, 14, 15, 16, 17, 18, 19, 20])-1))
t5 = time.perf_counter()
print(quick_sort_Hoare([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , 12, 13, 14, 15, 16, 17, 18, 19, 20], 0, len([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , 12, 13, 14, 15, 16, 17, 18, 19, 20])-1))
t6 = time.perf_counter()
print(f"{t2-t1:.5f}  {t3-t2:.5f}  {t4-t3:.5f} {t5-t4:.5f} {t6-t5:.5f}")

