"""11A01-有序档案"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    if root is None:
        root = TreeNode(val)
    else:
        # 相等时不插
        if val < root.val:
            root.left = insert(root.left, val)
        elif val > root.val:
            root.right = insert(root.right, val)
    return root


def inorder(root):
    result = []
    if root is None:
        return result
    result.extend(inorder(root.left))
    result.append(root.val)
    result.extend(inorder(root.right))
    return result


def bst_inorder(values):
    # 插入
    root = TreeNode(values[0])
    for value in values[1:]:
        insert(root, value)

    # 遍历
    return inorder(root)
