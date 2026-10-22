from time import time
# count = 0


def pascal(n):
    # global count
    # count += 1
    if n == 0:
        return [1]
    prev = pascal(n-1)
    row = [1] + [prev[i]+prev[i+1] for i in range(n-1)] + [1]
    return row

def pascal_bad(n):
    # global count
    # count += 1
    if n == 0:
        return [1]
    row = [1] + [pascal_bad(n-1)[i]+pascal_bad(n-1)[i+1] for i in range(n-1)] + [1]
    return row

def pascal_iter(n):
    row = [1]
    for i in range(1, n+1):
        row = [1] + [row[j]+row[j+1] for j in range(i-1)] + [1]
    return row


for i in (0, 1, 3, 4):
    print(f'pascal({i})={pascal(i)}')
    print(f'pascal_bad({i})={pascal_bad(i)}')
    print(f'pascal_iter({i})={pascal_iter(i)}')
# pascal(0)=[1]
# pascal_bad(0)=[1]
# pascal_iter(0)=[1]
# pascal(1)=[1, 1]
# pascal_bad(1)=[1, 1]
# pascal_iter(1)=[1, 1]
# pascal(3)=[1, 3, 3, 1]
# pascal_bad(3)=[1, 3, 3, 1]
# pascal_iter(3)=[1, 3, 3, 1]
# pascal(4)=[1, 4, 6, 4, 1]
# pascal_bad(4)=[1, 4, 6, 4, 1]
# pascal_iter(4)=[1, 4, 6, 4, 1]


n = 16
# count = 0
t0_good = time()
print(pascal(n))   # [1, 16, 120, 560, 1820, 4368, 8008, 11440, 12870, 11440, 8008, 4368, 1820, 560, 120, 16, 1]
t1_good = time()
print(f'递归好方法：{t1_good-t0_good}s')   # 递归好方法：1.6450881958007812e-05s
# print(count)

# count = 0
# t0_bad = time()
# print(pascal_bad(n)) # 过慢，已中止
# t1_bad = time()
# print(f'递归坏方法：{t1_bad-t0_bad}s')
# print(count)

t0_iter = time()
print(pascal_iter(n))  # [1, 16, 120, 560, 1820, 4368, 8008, 11440, 12870, 11440, 8008, 4368, 1820, 560, 120, 16, 1]
t1_iter = time()
print(f'迭代法：{t1_iter-t0_iter}s')    # 迭代法：1.1920928955078125e-05s

# print(f'递归坏方法/递归好方法：{(t1_bad-t0_bad)/(t1_good-t0_good)}') # 坏方法过慢，已中止
print(f'迭代法/递归好方法：{(t1_iter-t0_iter)/(t1_good-t0_good)}')   # 迭代法/递归好方法：0.7246376811594203
