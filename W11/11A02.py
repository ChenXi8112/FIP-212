"""11A02-层序扫描"""

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree(level):
    """按层序列表建树，-1 表示空结点。"""
    if not level or level[0] == -1:
        return None

    root = TreeNode(level[0])
    queue = deque([root])
    index = 1

    while queue and index < len(level):
        node = queue.popleft()

        if index < len(level):
            left_val = level[index]
            index += 1
            if left_val != -1:
                node.left = TreeNode(left_val)
                queue.append(node.left)

        if index < len(level):
            right_val = level[index]
            index += 1
            if right_val != -1:
                node.right = TreeNode(right_val)
                queue.append(node.right)

    return root


def level_order(root):
    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


root = build_tree(list(map(int, input().split())))
print(*level_order(root))
