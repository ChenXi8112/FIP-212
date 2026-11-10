"""9C01-窗口峰值"""

from collections import deque

def window_max(nums, k):
    result = []
    dq = deque()    # 存索引
    for i, num in enumerate(nums):
        if dq and dq[0] + k <= i:   # 去过期数据
            dq.popleft()
        while dq and num > nums[dq[-1]]:  # 去小数据，保持降序
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
