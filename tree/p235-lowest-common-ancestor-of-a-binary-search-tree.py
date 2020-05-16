# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        min_, max_ = (p, q) if p.val < q.val else (q, p)
        if min_.val <= root.val <= max_.val:
            return root
        if max_.val < root.val:
            return self.lowestCommonAncestor(root.left, min_, max_)
        else:
            return self.lowestCommonAncestor(root.right, min_, max_)

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
        node = None if v == 'null' else TreeNode(v)
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
if __name__ == '__main__':
    input_ = [6,2,8,0,4,7,9,"null","null",3,5]
    tree = createTree(input_)
    s=Solution()
    res = s.lowestCommonAncestor(tree, TreeNode(9), TreeNode(4))
    print(res.val)