"""9C02-双向月台"""

from collections import deque

def simulate_deque(ops):
    dq = deque()
    result = []
    i = 0
    while i < len(ops):
        if ops[i] == 'L':
            dq.appendleft(ops[i+1])
            i += 2
        elif ops[i] == 'R':
            dq.append(ops[i+1])
            i += 2
        elif ops[i] == 'DL':
            if dq:
                result.append(dq.popleft())
            i += 1
        elif ops[i] == 'DR':
            if dq:
                result.append(dq.pop())
            i += 1
    return result
