
#G를 인접리스트로 구현
graph = {
    'A' : ['B', 'C', 'D'],
    'B' : ['A', 'C', 'D'],
    'C' : ['B'],
    'D' : ['A', 'B'],
    'E' : ['A'],
}
bfs(graph, 'A')

def bfs(graph, start_v):
    visited = [start_v]
    queue = deque(start_v)
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited
