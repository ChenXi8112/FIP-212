"""7A02-闪电幂"""

def power(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 1:
        return power(x, n-1) * x
    else:
        x_sqrt = power(x, n//2)
        return x_sqrt * x_sqrt