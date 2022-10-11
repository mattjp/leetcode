class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        """
        Create graph of equivalent characters
        For each graph, find the character with the lowest ord
        
        leetcode
        programs
        
        {
            l: l, p
            p: l, p
            e: e, r, o
            r: e, r
            o: e, o
        }
        """
        
        def find_optimal(node, G, optimal):
            search = [node]
            visited = set()
            best = node
            
            while search:
                top = search.pop()
                visited.add(top)
                if ord(top) < ord(best):
                    best = top
                for neighbor in G[top]:
                    if neighbor not in visited:
                        search.append(neighbor)
                        
            for v in visited:
                optimal[v] = best

        G = collections.defaultdict(set)
        
        for a,b in zip(s1, s2):
            G[a].add(b)
            G[b].add(a)
        
        optimal = {}
        
        for node, neighbors in G.items():
            if node not in optimal:
                find_optimal(node, G, optimal)
        
        ans = ""
        
        for ch in baseStr:
            if ch in optimal:
                ans += optimal[ch]
            else:
                ans += ch
                
        return ans
