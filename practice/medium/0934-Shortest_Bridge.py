class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        BFS from every node in one island, 
        take the shortest BFS dist
        """
        
        from collections import deque
        
        source = set()
        
        def find_source_island(grid, row, col):
            queue = deque([(row, col)])
            
            while queue:
                top_row, top_col = queue.popleft()
                
                if (top_row, top_col) in source:
                    continue
                
                source.add((top_row, top_col))
                
                for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    r, c = top_row + i, top_col + j
                    if (r >= 0 and 
                        c >= 0 and 
                        r < len(grid) and 
                        c < len(grid[0]) and
                        grid[r][c] == 1):
                        queue.append((r, c))
                

        # 1. Find coordinates of source island
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    find_source_island(grid, row, col)
                    break
            # We only need to find one island
            if len(source) > 0:
                break

        
        # 2. Using source island, do BFS from each node until dest island reached
        queue = deque(list(map(lambda s: (s[0], s[1], 0), source)))

        # This is dumb duplication
        while queue:
            row, col, dist = queue.popleft()
                            
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r, c = row + i, col + j
                if (r >= 0 and 
                    c >= 0 and 
                    r < len(grid) and 
                    c < len(grid[0])):
                    
                    if grid[r][c] == 1 and (r, c) not in source:
                        return dist
                    
                    if (r, c) not in source:
                        source.add((r, c))
                        queue.append((r, c, dist + 1))
                        
        return -1
