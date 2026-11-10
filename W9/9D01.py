"""9D01-环形缓冲区"""

def simulate_ring(capacity, ops):
    q = [None] * capacity
    front = rear = count = 0
    result = []
    i = 0
    while i < len(ops):
        if ops[i] == 'E':
            if count < capacity:
                q[rear] = ops[i+1]
                rear = (rear + 1) % capacity
                count += 1
            i += 2
        elif ops[i] == 'D':
            if count > 0:
                result.append(q[front])
                q[front] = None
                front = (front + 1) % capacity
                count -= 1
            i += 1
    return result
