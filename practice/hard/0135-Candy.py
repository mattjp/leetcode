class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        Maintain 2 arrays, one passing left to right and the other right to left
        For L2R, make sure that each node has more candy than the one to its left
            if its rating is higher
        Same for R2L but reversed
        Take the larger of L2R and R2L for each index
        """
        leftRight = [1]
        rightLeft = [1]
        
        for i in range(0, len(ratings)-1):
            if ratings[i+1] > ratings[i]:
                leftRight.append(leftRight[-1]+1)
            else:
                leftRight.append(1)
        
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                rightLeft.append(rightLeft[-1]+1)
            else:
                rightLeft.append(1)
                
        rightLeft = rightLeft[::-1] # Make it actually represent right to left
        
        c = 0
        for i in range(len(ratings)):
            c += max(leftRight[i], rightLeft[i])
            
        return c
