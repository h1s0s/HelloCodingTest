def preorder(cur_node):
    if cur_node is None:
        return
    print(cur_node.value)
    preorder(cur_node.left)
    preorder(cur_node.right)

def inorder(cur_node):
    if cur_node is None:
        return
    preorder(cur_node.left)
    print(cur_node.value)
    preorder(cur_node.right)

def postorder(cur_node):
    if cur_node is None:
        return
    preorder(cur_node.left)
    preorder(cur_node.right)
    print(cur_node.value)
