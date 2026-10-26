import time
def pascal(n):
    if n == 0:
        return [1]
    prev = pascal(n-1)
    lst = [1]
    for i in range(len(prev)-1):
        lst.append(prev[i]+prev[i+1])
    lst.append(1)
    return lst

def pascal_bad(n):
    if n == 0:
        return [1]
    lst = [1]
    for i in range(n - 1):
        lst.append(pascal_bad(n - 1)[i] + pascal_bad(n - 1)[i + 1])
    lst.append(1)
    return lst

def pascal_iter1(n):
    lst = [1]
    for _ in range(n):
        new_lst = [1]
        for i in range(len(lst)-1):
            new_lst.append(lst[i]+lst[i+1])
        new_lst.append(1)
        lst = new_lst
    return lst

def pascal_iter2(n):
    lst = [1]
    for i in range(n):
        lst.append(int(lst[i] * (n - i) / (i + 1)))
    return lst

st = time.time()
print(pascal(500))
t1 = time.time()
print(pascal_bad(9))
t2 = time.time()
print(pascal_iter1(500))
t3 = time.time()
print(pascal_iter2(500))
t4 = time.time()
print(f"pascal(500): {t1-st:.3f}\npascal_bad(9) : {t2-t1:.3f}\niterate1(500) : {t3-t2:.3f}\niterate2(500) : {t4-t3:.3f}")