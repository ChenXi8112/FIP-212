"""7C02-逆序雷达"""

def count_inversions(arr):  # 无内层函数解法
    """返回严格逆序对的个数：i < j 且 arr[i] > arr[j]。不修改入参。

    自底向上归并：每轮合并相邻两个有序段，右段元素先出时，
    它与左段剩余元素各构成一个逆序对。时间 O(n log n)，空间 O(n)。
    """
    arr = list(arr)            # 拷贝一份，避免修改原参数，并变为可变对象
    if len(arr) <= 1:
        return 0
    inv = 0
    step = 2                   # 当前归并段长度，逐轮倍增
    while (step // 2) < len(arr):
        for t in range(0, len(arr), step):
            left = arr[t:t+step//2]          # 左有序段
            right = arr[t+step//2:t+step]    # 右有序段
            result, i, j = [], 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:      # 用 <= 保证稳定，相等不算逆序
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
                    inv += len(left) - i     # 右段元素先出，与左段剩余元素各成一对
            result.extend(left[i:])
            result.extend(right[j:])
            arr[t:t+step] = result
        step *= 2
    return inv

if __name__ == "__main__":
    print(count_inversions([5, 4, 3, 2, 1]))

"""
# 无注释版
def count_inversions(arr):
    arr = list(arr)
    if len(arr) <= 1:
        return 0
    inv = 0
    step = 2
    while (step // 2) < len(arr):
        for t in range(0, len(arr), step):
            left = arr[t:t+step//2]
            right = arr[t+step//2:t+step]
            result, i, j = [], 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
                    inv += len(left) - i
            result.extend(left[i:])
            result.extend(right[j:])
            arr[t:t+step] = result
        step *= 2
    return inv
"""
