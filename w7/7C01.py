"""7C01-频段重复次数"""

# 双函数求上下界，推荐
def count_freq(arr, target):
    n = len(arr)

    def lower_bound(lo, hi):
        # 在 [lo, hi) 中找第一个 >= target 的位置
        if lo >= hi:
            return lo
        mid = (lo + hi) // 2
        if arr[mid] < target:
            return lower_bound(mid + 1, hi)
        return lower_bound(lo, mid)

    def upper_bound(lo, hi):
        # 在 [lo, hi) 中找第一个 > target 的位置
        if lo >= hi:
            return lo
        mid = (lo + hi) // 2
        if arr[mid] <= target:
            return upper_bound(mid + 1, hi)
        return upper_bound(lo, mid)

    return upper_bound(0, n) - lower_bound(0, n)

if __name__ == "__main__":
    print(count_freq([1, 2, 2, 2, 3, 4], 2))

"""
# 无内层函数版，切片效率低下，不推荐
def count_freq(arr, target):
    if not arr:
        return 0

    mid = len(arr) // 2
    if arr[0] == arr[-1]:
        return len(arr) if arr[0] == target else 0
    if arr[mid] < target:
        return count_freq(arr[mid+1:], target)
    elif arr[mid] > target:
        return count_freq(arr[:mid], target)
    else:
        return count_freq(arr[:mid], target) + count_freq(arr[mid:], target)

# 递归计数，使用下标，可用
def count_freq(arr, target):
    if not arr: return 0
    def _count_freq(left, right):
        if right < left:
            return 0

        mid = (left + right) // 2
        if arr[left] == arr[right]:
            return (right - left + 1) if arr[left] == target else 0
        if arr[mid] < target:
            return _count_freq(left=mid+1, right=right)
        elif arr[mid] > target:
            return _count_freq(left=left, right=mid-1)
        else:
            return (_count_freq(left=left, right=mid-1) +
                    _count_freq(left=mid+1, right=right) +
                    1)
    return _count_freq(0, len(arr)-1)
"""
