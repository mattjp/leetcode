class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        from collections import deque
        
        M = len(grid)
        N = len(grid[0])
        
        seen = set()
        
        def get_size(grid, row, col):
            size = 0
            queue = deque([(row, col)])
            
            while queue:
                r, c = queue.popleft()
                
                if r < 0 or c < 0 or r > M-1 or c > N-1:
                    continue
                    
                if grid[r][c] != 1:
                    continue
                    
                if (r, c) in seen:
                    continue
                    
                size += 1
                seen.add((r, c))
                
                for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                    queue.append((nr, nc))
                    
            return size
        
        
        ans = 0
        for row in range(M):
            for col in range(N):
                ans = max(ans, get_size(grid, row, col))
                
        return ans
