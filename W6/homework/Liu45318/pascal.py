def pascal(n) -> list:
    if n==0:
        return [1]
    prev=pascal(n-1)
    ret=[1]
    for i in range(1,n):
        ret.append(prev[i]+prev[i-1])
    ret.append(1)
    return ret

def slow_pascal(n):
    if n==0:
        return [1]
    ret=[1]
    for i in range(1,n):
        ret.append(slow_pascal(n-1)[i]+slow_pascal(n-1)[i-1])
    ret.append(1)
    return ret

def iter_pascal(n):
    ret=[1]
    for i in range(1,n+1):
        prev=ret.copy()
        ret=[1]
        for j in range(1,i):
            ret.append(prev[j]+prev[j-1])
        ret.append(1)
    return ret

from time import time
st = time()
pascal(100)
print(f'pascal(100) : {time()-st:.4f}s')
st = time()
slow_pascal(9)
print(f'slow_pascal(9) : {time()-st:.4f}s')
st = time()
iter_pascal(100)
print(f'iter_pascal(100) : {time()-st:.4f}s')