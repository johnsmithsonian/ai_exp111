class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start):
        visited = set()
        result = []

        def dfs_helper(node):
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in self.graph.get(node, []):
                    dfs_helper(neighbor)

        dfs_helper(start)
        return result

graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)

dfs_result = graph.dfs(1)
print("DFS:", dfs_result)
