class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        """
        Take a random node A
        B = Furthest distance starting at A
        C = Furthest distance starting at B
        Result = Dist from B to C
        """
        
        def search(start, graph):
            cache = set()
            max_depth = 0
            ans = start
            queue = [(start, 0)]
            
            while queue:
                cur, depth = queue.pop()
                cache.add(cur)
                
                if depth > max_depth:
                    max_depth = depth
                    ans = cur
                
                neighbors = graph[cur]
                
                for n in neighbors:
                    if n not in cache:
                        queue.append((n, depth+1))
                        
            return ans, max_depth
        
        
        if len(edges) < 1:
            return 0
        
        nodes = collections.defaultdict(int)
        graph = collections.defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            nodes[u] += 1
            nodes[v] += 1
            
        A = edges[0][0]
        B, _ = search(A, graph)
        C, C_depth = search(B, graph)
        
        return C_depth
