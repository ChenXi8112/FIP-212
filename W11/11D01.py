"""11D01-查找路径"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        node = TreeNode(val)
        if self.root is None:
            self.root = node
            return
        cur = self.root
        while True:
            if val < cur.val:
                if cur.left is None:
                    cur.left = node
                    return
                cur = cur.left
            elif val > cur.val:
                if cur.right is None:
                    cur.right = node
                    return
                cur = cur.right
            else:
                # 编号互异，正常情况下不会走到这里；重复值直接忽略
                return

    def search_path(self, target):
        path = []
        cur = self.root
        while cur is not None:
            path.append(cur.val)
            if target == cur.val:
                return path
            cur = cur.left if target < cur.val else cur.right
        path.append(-1)
        return path
