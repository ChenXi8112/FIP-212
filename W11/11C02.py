"""11C02-树高度"""

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


def tree_height(level):
    root = build_tree(level)

    def _tree_height(root: TreeNode):
        if not root: return -1
        if (not root.left) and (not root.right):
            return 0
        return 1 + max(_tree_height(root.left), _tree_height(root.right))

    return _tree_height(root)
