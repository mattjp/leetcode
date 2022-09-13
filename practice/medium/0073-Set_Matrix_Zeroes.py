class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        def convert(row, col):
            for c in range(len(matrix[row])):
                if matrix[row][c] != 0:
                    matrix[row][c] = None
                    
            for r in range(len(matrix)):
                if matrix[r][col] != 0:
                    matrix[r][col] = None
                    
            
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    convert(row, col)
                    
        # print(matrix)
        
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == None:
                    matrix[row][col] = 0
