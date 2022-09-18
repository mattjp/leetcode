class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        """
        BFS from starting position
        Keep a PQ with the lowest distance on top
        Maintain a cache of visited cells, do not revisit any cell 
        """
        
        # Account for the new boundary
        M, N = len(maze)+2, len(maze[0])+2
        
        
        def addBoundary(maze):
            """
            Add a boundary of walls to the maze to make calculation easier
            """
            maze.insert(0, [1] * N)
            maze.append([1] * N)
            for r in range(1, M-1):
                maze[r].insert(0, 1)
                maze[r].append(1)    
        
        
        def travel(maze, row, col, x, y):
            """
            Add y to row and x to col until wall reached
            """
            while maze[row][col] == 0:
                row += y
                col += x
            
            return [row-y, col-x]  # don't return a wall
            
        # Add boundary of 1s
        addBoundary(maze)
        
        # Start/dest changed due to new boundary
        destination = [d+1 for d in destination]
        start = [s+1 for s in start]
        visited = set()
        
        # [dist, row, col]
        pq = [[0, start[0], start[1]]]
        
        while pq:
            dist, row, col = heapq.heappop(pq)
            
            visited.add((row, col))
            
            for x,y in [[-1,0], [1,0], [0,-1], [0,1]]:
                new_row, new_col = travel(maze, row, col, x, y)
                new_dist = abs(row - new_row) + abs(col - new_col)
                total_dist = dist + new_dist
                
                # If we are at the destination then we've solved the problem
                if new_row == destination[0] and new_col == destination[1]:
                    return total_dist
                
                # Try the new cell if we have not visited previously
                if (new_row, new_col) not in visited:
                    heapq.heappush(pq, [total_dist, new_row, new_col])
          
        # We've tried every path
        return -1
