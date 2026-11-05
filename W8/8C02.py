"""8C02-零值滤净"""

from collections import deque


def remove_zeros(nums):
    queue = deque()
    for num in nums:
        if num != 0:
            queue.append(num)
    no_zero_nums = []
    while queue:
        no_zero_nums.append(queue.popleft())
    return no_zero_nums
