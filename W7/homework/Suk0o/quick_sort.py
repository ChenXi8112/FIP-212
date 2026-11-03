def quick_sort(arr:list) -> list:
    if len(arr) <= 1:
        return arr
    sentry = arr[0]#“哨兵”
    left = [x for x in arr[1:] if x <= sentry]#小半部分
    right = [x for x in arr[1:] if x > sentry]#大半部分
    return quick_sort(left) + [sentry] + quick_sort(right)
print(quick_sort(list(map(int, input("请输入一组整数，以空格分隔: ").split()))))


#三路分兵.ver
def quick_sort_threeway(arr:list) -> list:
    if len(arr) <= 1:
        return arr
    sentry = arr[0]#“哨兵”
    left = [x for x in arr[1:] if x < sentry]#小半部分
    mid = [x for x in arr[1:] if x == sentry]#中半部分
    right = [x for x in arr[1:] if x > sentry]#大半部分
    return quick_sort_threeway(left) + mid + quick_sort_threeway(right)

#随机哨兵.ver
def quick_sort_random(arr:list) -> list:
    if len(arr) <= 1:
        return arr
    import random
    sentry = random.choice(arr)#随机选择哨兵
    left = [x for x in arr if x < sentry]#小半部分
    mid = [x for x in arr if x == sentry]#中半部分
    right = [x for x in arr if x > sentry]#大半部分
    return quick_sort_random(left) + mid + quick_sort_random(right)