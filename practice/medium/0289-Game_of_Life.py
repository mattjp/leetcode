class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def neighbors(board, row, col):
            live = dead = 0
            for r in [row-1, row, row+1]:
                for c in [col-1, col, col+1]:
                    # don't check the current cell
                    if r == row and c == col:
                        continue
                        
                    # the row and col are invalid
                    if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                        continue
                    
                    if board[r][c] == 1:
                        live += 1
                    else:
                        dead += 1

            return (live, dead)
                    
        
        def evaluate(board, live, dead, row, col):
            # find info about neighbors
            live_neighbors, dead_neighbors = neighbors(board, row, col)
            
            # cell is live
            if board[row][col] == 1:
                if live_neighbors < 2:
                    dead.append((row, col))
                elif live_neighbors < 4:
                    live.append((row, col))
                else:
                    dead.append((row, col))
            
            # cell is dead
            else:
                if live_neighbors == 3:
                    live.append((row, col))
                else:
                    dead.append((row, col))
                    
        live = []
        dead = []
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                evaluate(board, live, dead, row, col)

        
        for row, col in live:
            board[row][col] = 1
            
        for row, col in dead:
            board[row][col] = 0
