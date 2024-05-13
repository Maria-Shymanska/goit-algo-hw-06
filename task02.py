def dfs(graph, start, visited=None, path=None):
    if visited is None:
        visited = set()
        if path is None:
            path = []
            
    visited.add(start)
    path.append(start)
    
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, path)
            
            return path
        
def bfs(graph, start):
        visited = set()
        queue = [start]
        visited.add(start)
        path = []
        
        while queue:
            vertex = queue.pop(0)
            path.append(vertex)
            
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                
        return path
    
    # Створення графа
graph = {
    1:(1, 2),
    2:(1, 3),
    3:(2, 3),
    4:(2, 4),
    5:(3, 4),
    6:(3, 5),
    7:(4, 5)
}

# Знаходження шляхів за допомогою DFS та BFS
dfs_path = dfs(graph, 1)
bfs_path = bfs(graph, 1)

print("Шлях за допомогою DFS:", dfs_path)
print("Шлях за допомогою BFS:", bfs_path)            