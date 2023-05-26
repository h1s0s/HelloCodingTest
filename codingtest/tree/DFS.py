def dfs(root):#재귀로 구현
    if root is None:
        return
    dfs(root.left)
    dfs(root.right)

dfs(root)