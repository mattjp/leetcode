class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # 2, 2, 2, 100, 100, 1 | k=3
        
        if k >= len(cardPoints):
            return sum(cardPoints)
        
        L = cardPoints[:k]
        R = cardPoints[-k:][::-1] # reverse R to make access simpler
        
        l = result = sum(L)
        r = 0
        result = l
        for d in range(k):
            l -= L[-(d+1)]
            r += R[d]
            result = max(result, l+r)     
            
        return result
