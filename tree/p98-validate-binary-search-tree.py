# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def createTree(values: list) -> TreeNode:
    first_layer = []
    second_layer = []
    layer_head = 1
    now_layer = 1
    next_layer_head = layer_head + 2 ** now_layer
    root = values.pop(0)
    if root == 'null':
        return None
    head = TreeNode(root)
    first_layer.append(head)
    for idx, v in enumerate(values):
        if v == 'null':
            node = None
        else:
            node = TreeNode(v)
        if idx >= next_layer_head - 1:
            now_layer, layer_head = now_layer + 1, next_layer_head
            next_layer_head = layer_head + 2 ** now_layer
            first_layer, second_layer = second_layer, []
        f_idx = int((idx - layer_head + 1) // 2)
        f_res = (idx - layer_head + 1) % 2
        if f_res == 0:
            first_layer[f_idx].left = node
        else:
            first_layer[f_idx].right = node
        second_layer.append(node)
    return head


class Solution:
    def recursive(self, root: TreeNode, min_, max_):
        if root is None:
            return True
        if (min_ < root.val < max_) is False:
            return False
        return self.recursive(root.left, min_, root.val) and self.recursive(root.right, root.val, max_)

    def isValidBST(self, root: TreeNode) -> bool:
        return self.recursive(root, float('-inf'), float('inf'))


class Solution2:
    def inorder(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if not self.inorder(root.left):
            return False
        if self.pre is not None and not self.pre < root.val:
            return False
        self.pre = root.val
        return self.inorder(root.right)

    def isValidBST(self, root: TreeNode) -> bool:
        self.pre = None
        return self.inorder(root)


if __name__ == '__main__':
    input_ = [6, 2, 8, 0, 4, 7, 9, "null", "null", 3, 5]
    tree = createTree(input_)
    print(tree)
    a = TreeNode(0)
    c = TreeNode(-1)
    a.right = c
    s = Solution2()
    res = s.isValidBST(a)
    print(res)
