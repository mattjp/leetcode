class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        Create bi-directional graph
        """
        
        from collections import defaultdict
        
        # create graph of a->b, b->a
        graph = defaultdict(list)
        for i, (a, b) in enumerate(equations):
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))

        
        # Function to DFS and find an answer if one exists
        def dfs(cur, res, target, seen):
            # No point in ever retrying for a given query
            seen.add(cur)
            
            for g in graph[cur]:
                if g[0] == target:
                    return True, res * g[1]
                
                if g[0] not in seen:
                    found, ans = dfs(g[0], res * g[1], target, seen) 
                    if found:
                        return True, ans
                    
            # Base case
            return False, -1
                
        
        # Evaluate all queries
        result = []
        for a, b in queries:
            found, ans = dfs(a, 1, b, set())
            result.append(ans)
            
        return result
