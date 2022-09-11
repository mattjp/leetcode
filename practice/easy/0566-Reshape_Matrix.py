class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        if m*n != r*c:
            return mat
        
        ans = [[None] * c for _ in range(r)]
        vals = []
        
        for row in range(m):
            for col in range(n):
                vals.append(mat[row][col])
        
        i = 0
        for row in range(r):
            for col in range(c):
                ans[row][col] = vals[i]
                i += 1
        
        return ans
        
