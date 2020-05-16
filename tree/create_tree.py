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
