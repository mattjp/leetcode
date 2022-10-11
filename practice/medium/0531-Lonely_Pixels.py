class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        
        from collections import defaultdict
        
        M, N = len(picture), len(picture[0])
        
        rows = defaultdict(int)
        cols = defaultdict(int)
        
        for r in range(M):
            for c in range(N):
                if picture[r][c] == "B":
                    rows[r] += 1
                    cols[c] += 1
                   
        ans = 0
        
        for r in range(M):
            for c in range(N):
                if picture[r][c] == "B":
                    if rows[r] == 1 and cols[c] == 1:
                        ans += 1
                        
        return ans
