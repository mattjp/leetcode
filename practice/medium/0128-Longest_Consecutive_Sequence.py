class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        MEMORY LIMIT EXCEEDED
        Get the min and max
        Create an ordered dict from range(min, max) where the value is True/False
        Iterate through nums setting key = True for each num
        Iterate through the ordered dict keeping track of the longest streak of True values
        
        CORRECT
        Put each num into a map where the value=1
            Value will keep track of the largest streak seen by that num
        """
        
        
        m = {}
        best = 0
        for num in nums:
            m[num] = 1
        
        for num in nums:
            # we're in the middle of a sequence we've encountered before, skip this num
            if m[num] == None:
                continue

            i = num
            cur = 0
            while i in m:
                # this num has been visited before, add the previous best length and break
                if m[i] > 1:
                    cur += m[i]
                    break
                # this num has not been visited, increment counter by 1 and marked as visited
                else:
                    cur += 1
                    i += 1
                    m[i] = None # mark as visited

            m[num] = cur # set the first node as the length of the sequence
            best = max(best, cur)
            
        return best
