from time import time

def pascal(n):
    if n < 0:
        raise ValueError("n 必须是非负整数")
    if n == 0:
        return [1]
    
    prev_row = pascal(n - 1)
    curr_row = [1]
    
    for i in range(len(prev_row) - 1):
        curr_row.append(prev_row[i] + prev_row[i + 1])
        
    curr_row.append(1)
    return curr_row


def pascal_iter(n):
    if n < 0:
        raise ValueError("n 必须是非负整数")
        
    row = [1]
    for _ in range(n):
        row = [1] + [x + y for x, y in zip(row, row[1:])] + [1]
    return row


def pascal_bad(n):
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    
    return [1] + [pascal_bad(n-1)[i] + pascal_bad(n-1)[i+1] for i in range(n-1)] + [1]


if __name__ == "__main__":
    test_ns = [0, 1, 2, 3, 4]
    
    print("=== 基础测试 ===")
    for n in test_ns:
        print(f"n={n} (迭代版): {pascal_iter(n)}")
        print(f"n={n} (递归版): {pascal(n)}")
    
    print("\n=== 性能测试 ===")
    
    test_n = 20
    
    start = time()
    pascal_iter(test_n)
    end = time()
    print(f"迭代版 pascal_iter({test_n}) 耗时: {end - start:.6f} 秒")
    
    start = time()
    pascal(test_n)
    end = time()
    print(f"递归版 pascal({test_n}) 耗时: {end - start:.6f} 秒")
    
    print(f"即将测试坏版本 pascal_bad({test_n})...")
    start = time()
    pascal_bad(test_n)
    end = time()
    print(f"错误版 pascal_bad({test_n}) 耗时: {end - start:.6f} 秒")