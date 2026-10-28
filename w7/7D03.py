"""7D03-通用弦截法（为什么不是废土弦截法？！）"""

def secant(f, x0, x1, eps):
    # 海象运算符（x := expr）：既是表达式又是赋值式；x 为变量名，expr 为一个表达式
    # 含义是整体作为一个表达式返回 expr 的值，并将表达式 expr 的值赋给 x 变量
    while abs(f_curr := f(x1)) >= eps:
        x0, x1 = x1, x1 - f_curr * (x1-x0) / (f_curr - f(x0))   # 此处不处理零除
    return x1

if __name__ == '__main__':
    expr_list = [
        lambda x: x ** 2 - 2,
        lambda x: x ** 3 - 5 * x + 1,
        lambda x: x ** 2 - 3 * x - 1,
    ]

    for expr in expr_list:
        print(f"{secant(expr, 1.0, 3.0, 1e-6):.3f}")
