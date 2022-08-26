class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """
        Let's just do a naive BFS and see if it times out
        
        Plot twist, it was too slow
        
        Every matrix starts like below (possible, moves):
        
        2,1  1,1  1,1  2,1
        
        1,1  0,1  0,1  1,1
        
        1,1  0,1  0,1  1,1
        
        2,1  1,1  1,1  2,1
        
        ===
        
        For every new move, we can add the total possiblities from 4 neighbors
        to the original possibilities for this cell
        
        4,2  4,2  4,2  4,2
        
        4,2  2,2  2,2  4,2
        
        4,2  2,2  2,2  4,2
        
        4,2  4,2  4,2  4,2
        
        ===
        
        10,3  11,3  4,2  4,2
        
        4,2  12,3  2,2  4,2
        
        4,2  2,2  2,2  4,2
        
        4,2  4,2  4,2  4,2
        
        """
        
        # Helper
        def get_root_val(row, col):
            ans = 0
            if row == 0:
                ans += 1
            if row == m-1:
                ans += 1
            if col == 0:
                ans += 1
            if col == n-1:
                ans += 1
            return ans
        
        
        # Helper
        def get_neighbor_sum(row, col, prev):
            ans = 0
            if row-1 >= 0:
                ans += prev[row-1][col]
            if row+1 < m:
                ans += prev[row+1][col]
            if col-1 >= 0:
                ans += prev[row][col-1]
            if col+1 < n:
                ans += prev[row][col+1]
            return ans
        
        
        # Stupid edge case
        if maxMove == 0:
            return 0
        
        # Build the initial matrix
        prev = []
        for row in range(m):
            prev.append([])
            for col in range(n):
                prev[row].append(get_root_val(row, col))
                

        # For each move, update the possibilities for each cell
        for move in range(1, maxMove):
            cur = []
            for row in range(m):
                cur.append([])
                for col in range(n):
                    root_val = get_root_val(row, col)
                    neighbor_sum = get_neighbor_sum(row, col, prev)
                    cur[row].append(root_val + neighbor_sum)
            prev = cur
        

        return prev[startRow][startColumn] % 1_000_000_007
