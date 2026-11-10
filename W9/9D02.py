"""9D02-急诊分诊"""

import heapq

def triage_order(priorities):
    heap = []
    for sequence, priority in enumerate(priorities):
        heapq.heappush(heap, (priority, sequence))
    result = []
    while heap:
        result.append(heapq.heappop(heap)[1] + 1)
    return result
