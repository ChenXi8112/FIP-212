"""9A02-急救号牌"""

import heapq

def heap_order(xs):
    heap = []
    for pid, priority in enumerate(xs):
        heapq.heappush(heap, (priority, pid))
    result = []
    while heap:
        result.append(heapq.heappop(heap)[0])
    return result
