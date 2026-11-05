"""8C01-废土厨房"""

from collections import deque


def simulate_kitchen(ops):
    queue = deque()
    result = []

    i = 0
    while i < len(ops):
        token = ops[i]
        if token == 'E':
            queue.append(ops[i + 1])
            i += 2
        elif token == 'D':
            result.append(queue.popleft())
            i += 1
        else:
            i += 1

    return result
