class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        """
        For each num, we need the count, first and last index
        """
        
        m = {}
        
        for i, num in enumerate(nums):
            if num in m:
                count, first, last = m[num]
                m[num] = (count+1, first, i)
            else:
                m[num] = (1, i, i)
                
        # sort based on greatest degree and smallest length
        sm = sorted(m.values(), key=lambda v: (-v[0], v[2]-v[1]))[0]
        
        return 1 + sm[2] - sm[1]
        
