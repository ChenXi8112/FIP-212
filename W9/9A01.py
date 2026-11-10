"""9A01-环形四格"""

def two_dequeues(vals):
    q = [None] * 4
    front = rear = count = 0
    for i in vals:
        # 既然要求了对4取余为什么要已满则忽略？
        if rear < 4 and count < 4:
            q[rear] = i
            rear = (rear + 1) % 4
            count += 1
    result = []
    for _ in range(2):
        if count > 0:
            result.append(q[front])
            q[front] = None
            front = (front + 1) % 4
            count -= 1
    return result
