"""11C01-三序对拍"""

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


def three_orders(level):
    """返回二叉树的前序、中序、后序遍历序列。"""
    preorder = []
    inorder = []
    postorder = []

    def preorder_dfs(node):
        if not node:
            return
        preorder.append(node.val)
        preorder_dfs(node.left)
        preorder_dfs(node.right)

    def inorder_dfs(node):
        if not node:
            return
        inorder_dfs(node.left)
        inorder.append(node.val)
        inorder_dfs(node.right)

    def postorder_dfs(node):
        if not node:
            return
        postorder_dfs(node.left)
        postorder_dfs(node.right)
        postorder.append(node.val)

    root = build_tree(level)
    preorder_dfs(root)
    inorder_dfs(root)
    postorder_dfs(root)

    return preorder, inorder, postorder


if __name__ == "__main__":
    level = [1, 2, 3, 4, 5, -1, -1, -1, -1, -1]
    preorder, inorder, postorder = three_orders(level)
    print(preorder)
    print(inorder)
    print(postorder)
