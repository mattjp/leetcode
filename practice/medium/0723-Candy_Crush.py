class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        """
        1. Find vertical groups, mark cells deleted, return column to crush
        2. Find horizontal groups, mark cells deleted, return columns to crush
        3. Crush all necessary columns
        4. Repeat while there are columns that need to be crushed
        """
        
        def find_vert_column(board, delete, col):
            count = 1
            marked = []
            for r in range(1, len(board)):
                # keep track of consecutive matches
                if board[r][col] != 0 and board[r][col] == board[r-1][col]:
                    count += 1
                else:
                    # mark consecutive matches
                    if count > 2:
                        marked.extend(range(r-count, r)) 
                    count = 1
                    
            # mark consecutive matches one more time
            if count > 2:
                r = len(board)
                marked.extend(range(r-count, r))
                    
            # add all the marked cells
            for m in marked:
                delete.add((m, col))
                
            # return the column to indicate we should crush it
            return col if len(marked) > 0 else None
        
        
        def find_horz_columns(board, delete, row):
            count = 1
            marked = []
            for c in range(1, len(board[0])):
                # keep track of consecutive matches
                if board[row][c] != 0 and board[row][c] == board[row][c-1]:
                    count += 1
                else:
                    # mark consecutive matches
                    if count > 2:
                        marked.extend(range(c-count, c))
                    count = 1
                    
            # mark consecutive matches one more time
            if count > 2:
                c = len(board[0])
                marked.extend(range(c-count, c))
                
            # add all the marked cells
            for m in marked:
                delete.add((row, m))
                
            # return all columns that need to be crushed
            return marked
        
        
        def crush_columns(board, delete, columns):
            for col in columns:
                # this is just a dumb way of getting the number of zeros to add
                count = len(list(filter(lambda d: d[1] == col, delete)))
                # work from the bottom row up
                for row in range(len(board)-1, -1, -1):
                    r = row
                    # if this cell is marked for deletion, bubble up until we find 
                    # a cell not marked for deletion
                    while r >= 0 and (r, col) in delete:
                        r -= 1
                    board[row][col] = board[r][col]
                    
                    # mark any new cells for deletion
                    if (row, col) in delete:
                        delete.add((r, col))

                # set the top as zeros
                for row in range(count):
                    board[row][col] = 0

        
        stable = False
        while not stable:
            columns = set()
            delete = set()
            
            for col in range(len(board[0])):
                c = find_vert_column(board, delete, col)
                if c != None: columns.add(c)
                    
            for row in range(len(board)):
                r = find_horz_columns(board, delete, row)
                if r: columns.update(r)
            
            if len(columns) > 0:
                crush_columns(board, delete, columns)
            else:
                stable = True
                
        return board
