def bfs(root): #너비우선탐색, 순회
    visited = [] #노드를 담아주기 위한 리스트 생성
    if root is None: #root가 none이면 빈 list 반환
        return visited;
    q = deque() #큐 생성, BFS와 큐는 세트임
    q.append(root) #큐에 트리를 넣음
    while q:
        cur_node = q.popleft() #"접근"을 하기 위한 cur_node, 큐의 왼쪽에 있는것 dequeue해서 root를 뽑음
        visited.append(cur_node.value)

        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    return visited

#접근과 방문은 차이가 있음.

bfs(root)