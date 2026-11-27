"""11D02-验证BST"""

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


def is_valid_bst(level):
    """判断层序列表对应的二叉树是否为严格二叉搜索树。"""
    root = build_tree(level)

    def validate(node):
        valid = True
        if not node: return True
        if node.left:
            valid = valid and node.left.val < node.val
        if node.right:
            valid = valid and node.right.val > node.val
        valid = valid and validate(node.left) and validate(node.right)
        return valid

    return validate(root)
