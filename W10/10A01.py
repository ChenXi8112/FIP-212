"""10A01-向量内积"""

def inner_product(a, b):
    s = 0
    for i, j in zip(a, b):
        s += i * j
    return s
