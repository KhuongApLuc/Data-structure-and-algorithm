#Q3:Connection
def dfs(graph, node, visited):
    stack = [node]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            for neighbor in graph[v]:
                if not visited[neighbor]:
                    stack.append(neighbor)

def count_connected_components(graph, num_nodes):
    visited = [False] * num_nodes
    component_count = 0
    
    for node in range(num_nodes):
        if not visited[node]:
            dfs(graph, node, visited)
            component_count += 1
    
    return component_count

N, M = map(int, input().split())
graph = {i: [] for i in range(N)}

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

need_ = count_connected_components(graph, N)
a = -1
if M >= N-1: 
    need = need_-1
    print(need)
else: 
    print(a)