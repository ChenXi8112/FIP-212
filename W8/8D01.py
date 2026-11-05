"""8D01-废土撤销"""

def simulate_undo(ops):
    result = []

    i = 0
    while i < len(ops):
        token = ops[i]
        if token == 'TYPE':
            result.append(ops[i + 1])
            i += 2
        elif token == 'UNDO':
            if len(result) > 0: # 栈空则忽略
                result.pop()
            i += 1
        else:
            i += 1

    return result
