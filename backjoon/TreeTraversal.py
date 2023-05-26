n = int(sys.stdin.readline())
tree = dict()

# 반복문을 통해 트리 생성
for i in range(n):
    root, left, right = map(str, sys.stdin.readline().split())
    tree[root] = left, right

def preorder(n):
    if n is None:
        return
    print(n, end="")
    preorder(n.left)
    preorder(n.right)

def inorder(n):
    if n is None:
        return
    preorder(n.left)
    print(n, end="")
    preorder(n.right)

def postorder(n):
    if n is None:
        return
    preorder(n.left)
    preorder(n.right)
    print(n, end="")

preorder('A')
inorder('A')
postorder('A')