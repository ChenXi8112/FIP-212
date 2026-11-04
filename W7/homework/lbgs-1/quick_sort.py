# W7 分治作业：快速排序（首元素基准简洁版 + 随机化/三路可选）
# 运行：python W7/homework/lbgs-1/quick_sort.py
import random
import sys
import time


# ---------------- 简洁版：第一个元素作基准 ----------------
def quick_sort(arr, depth=0, log=None):
    # depth / log 是可选的“记录用”参数：正常调用 quick_sort(arr) 时行为不变
    if log is not None:
        log.append((depth, len(arr)))
    if len(arr) <= 1:                       # Base Case
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]    # 必须用 arr[1:]，排除基准本身
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left, depth + 1, log) + [pivot] + quick_sort(right, depth + 1, log)


# ---------------- 随机化基准：避免已排序输入退化 ----------------
def quick_sort_random(arr, depth=0, log=None):
    if log is not None:
        log.append((depth, len(arr)))
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return (quick_sort_random(left, depth + 1, log) + equal
            + quick_sort_random(right, depth + 1, log))


# ---------------- 三路分区（弹性）：重复元素只分一次 ----------------
def quick_sort_3way(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quick_sort_3way(less) + equal + quick_sort_3way(greater)


# ---------------- 手工分区验证：pivot = 5 ----------------
def partition_by_value(arr, pivot):
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return left, equal, right


# ---------------- 测试 ----------------
def check_case(name, func, arr, expect):
    try:
        actual = func(list(arr))
    except Exception as exc:
        actual = f"{type(exc).__name__}: {exc}"
    ok = actual == expect
    print(f"  {name:<12} 输入 {str(arr):<28} 预期 {str(expect):<28} 实际 {str(actual):<28} "
          f"{'通过' if ok else '不通过'}")
    return ok


def test_basic():
    print("[基本测试]")
    ok = []
    ok.append(check_case("课件例子", quick_sort, [3, 1, 4, 1, 5, 9, 2, 6], [1, 1, 2, 3, 4, 5, 6, 9]))
    ok.append(check_case("空列表", quick_sort, [], []))
    ok.append(check_case("单个元素", quick_sort, [7], [7]))
    ok.append(check_case("两个元素", quick_sort, [2, 1], [1, 2]))
    ok.append(check_case("全部相等", quick_sort, [3, 3, 3], [3, 3, 3]))
    ok.append(check_case("已排序", quick_sort, [1, 2, 3, 4, 5, 6, 7, 8],
                         [1, 2, 3, 4, 5, 6, 7, 8]))
    ok.append(check_case("逆序", quick_sort, [8, 7, 6, 5, 4, 3, 2, 1],
                         [1, 2, 3, 4, 5, 6, 7, 8]))
    ok.append(check_case("课件例子(随机版)", quick_sort_random, [3, 1, 4, 1, 5, 9, 2, 6],
                         [1, 1, 2, 3, 4, 5, 6, 9]))
    ok.append(check_case("重复元素(三路)", quick_sort_3way, [3, 1, 4, 1, 5, 9, 2, 6, 1, 1, 1],
                         [1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 9]))
    print(f"  → {sum(ok)}/{len(ok)} 通过\n")
    return sum(ok) == len(ok)


def test_against_sorted():
    # 与内置 sorted() 对照：随机生成 60 个列表，长度 0..12
    bad = 0
    for _ in range(60):
        arr = [random.randint(0, 9) for _ in range(random.randint(0, 12))]
        if not (quick_sort(arr) == sorted(arr) == quick_sort_random(arr) == quick_sort_3way(arr)):
            bad += 1
    print(f"[对照 sorted()] 60 个随机列表，三种实现都等于 sorted()："
          f"{'通过' if bad == 0 else f'不通过 {bad} 个'}\n")
    return bad == 0


def show_degradation():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    log = []
    quick_sort(arr, 0, log)
    max_depth = max(d for d, _ in log)
    print(f"[退化测试] 输入 {arr}（已排序），首元素作基准")
    for d in range(max_depth + 1):
        lens = [n for dd, n in log if dd == d]
        print(f"  第 {d} 层：子列表长度 {lens}")
    print(f"  → 调用层数（含最外层）= {max_depth + 1}，最大递归深度 = {max_depth}")
    print(f"  → left 恒为空，right 每次只少 1 个元素：8→7→6→5→4→3→2→1")
    depths = []
    for _ in range(20):
        log = []
        quick_sort_random(arr, 0, log)
        depths.append(max(d for d, _ in log))
    print(f"  → 同一输入换成随机化基准，20 次的递归深度：最小 {min(depths)}、"
          f"平均 {sum(depths) / len(depths):.1f}、最大 {max(depths)}"
          f"（理想约 log2(8) ≈ 3；8 个元素太少，偶尔抽到坏基准仍会变深）")
    print(f"  → 对比：首元素基准固定为 {max_depth} 层，且不会随输入变化\n")
    return max_depth


def show_manual_partition():
    arr = [8, 3, 5, 1, 7, 2, 9, 4]
    pivot = 5
    left, equal, right = partition_by_value(arr, pivot)
    pos = len(left)
    print(f"[手工分区] 列表 {arr}，基准 {pivot}")
    print(f"  left（< 5）  = {left}")
    print(f"  pivot        = {equal}")
    print(f"  right（> 5） = {right}")
    print(f"  → 基准 5 的最终位置：下标 {pos}（第 {pos + 1} 个元素）；"
          f"排序后 {sorted(arr)} 中 5 也在下标 {sorted(arr).index(5)}")
    print(f"  → 验证 left 全部 < 5：{all(x < 5 for x in left)}；"
          f"right 全部 ≥ 5：{all(x >= 5 for x in right)}\n")


def bench(func, arr, repeat=3):
    best = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        func(list(arr))
        dt = time.perf_counter() - t0
        best = dt if best is None else min(best, dt)
    return best


def show_degradation_speed(slow=False):
    print("[退化耗时] 已排序输入，首元素基准 vs 随机基准（每次取 3 轮最快）")
    print(f"  {'n':>4}{'首元素基准':>14}{'随机化基准':>14}")
    sizes = [200, 400, 800] + ([1600] if slow else [])
    old_limit = sys.getrecursionlimit()
    # 已排序输入的首元素基准会递归 n 层，先把上限抬高，跑完再还原
    sys.setrecursionlimit(max(old_limit, 2 * max(sizes) + 100))
    try:
        for n in sizes:
            arr = list(range(n))
            t1 = bench(quick_sort, arr)
            t2 = bench(quick_sort_random, arr)
            print(f"  {n:>4}{t1 * 1000:>12.3f}ms{t2 * 1000:>12.3f}ms")
    finally:
        sys.setrecursionlimit(old_limit)
    print("  → n 每翻一倍，首元素基准约慢 4 倍（O(n²) 退化）；随机化基准接近 O(n log n)\n")


def show_pitfall():
    # 坑：分区写成 arr（没排除基准）→ 基准永远留在 right → 无限递归
    def quick_sort_wrong(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left = [x for x in arr if x < pivot]      # 错：应为 arr[1:]
        right = [x for x in arr if x >= pivot]    # 基准又进了 right
        return quick_sort_wrong(left) + [pivot] + quick_sort_wrong(right)

    print("[坑的复现] 分区写成 arr（不排除基准）→ 无限递归")
    try:
        quick_sort_wrong([3, 1, 2])
    except RecursionError as exc:
        print(f"  RecursionError: {exc}")
        print("  → 原因：pivot 又出现在 right 里，right 长度没变小，递归不收敛")
        print("  → 修正：两边都用 arr[1:]（或按课件把 == pivot 单独放 equal）\n")
        return True
    print("  （没有触发 RecursionError，说明代码有问题）\n")
    return False


def main():
    slow = "--slow" in sys.argv
    print("=" * 96)
    print("W7 作业：快速排序")
    print("=" * 96 + "\n")
    ok = []
    ok.append(test_basic())
    ok.append(test_against_sorted())
    show_manual_partition()
    show_degradation()
    show_degradation_speed(slow)
    ok.append(show_pitfall())
    print(f"汇总：必做测试 {sum(ok)}/{len(ok)} 项通过")


if __name__ == "__main__":
    main()
