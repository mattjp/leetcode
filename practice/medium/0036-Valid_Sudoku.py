class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def validate_row(board, r):
            seen = set()
            
            row = board[r]
            for n in row:
                if n != "." and n in seen:
                    return False
                seen.add(n)
            return True
        
        
        def validate_col(board, c):
            seen = set()
            
            for r in range(9):
                n = board[r][c]
                if n != "." and n in seen:
                    return False
                seen.add(n)
            return True
        
        
        def validate_square(board, r, c):
            seen = set()
            
            for row in range(r, r+3):
                for col in range(c, c+3):
                    n = board[row][col]
                    if n != "." and n in seen:
                        return False
                    seen.add(n)
            return True
            
        
        # Validate rows and columns
        for i in range(9):
            if not validate_row(board, i) or not validate_col(board, i):
                return False
            
        # Validate squares
        for r in range(9):
            for c in range(9):
                if r % 3 == 0 and c % 3 == 0:
                    if not validate_square(board, r, c):
                        return False
                    
        # Everything is valid 
        return True
