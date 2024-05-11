N, M, V = map(int, input().split())

graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited = [0] * (N+1)

def bfs(V):
    queue = [V]
    visited[V] = 1
    while queue:
        node = queue.pop(0)
        print(node, end= ' ')
        for i in range(1, N+1):
            if visited[i] == 0 and graph[node][i] == 1:
                queue.append(i)
                visited[i] = 1

bfs(V)