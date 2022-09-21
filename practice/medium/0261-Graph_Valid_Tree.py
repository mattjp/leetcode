class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        A tree is a graph with no cycles.
        We must attempt to detect a cycle.
        
        We can BFS from a random node and assert that all (not parent) nodes being added are new
        
        We should also assert that every node is indeed reached.
        """
        
        if len(edges) < 1:
            return n == 1
        
        
        start = edges[0][0]
        visited = set()
        queue = collections.deque([(start, None)])        
        graph = collections.defaultdict(list)
        
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        
        while queue:
            node, parent = queue.popleft()
            
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                elif neighbor in visited:
                    return False
                else:
                    queue.append((neighbor, node))
                    
        return n == len(visited)
