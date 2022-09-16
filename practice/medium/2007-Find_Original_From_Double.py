class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        """
        Take the lowest value from changed
        Check if the doubled value exists in changed
        If not, the solution is impossible
        If so, pop the doubled value and add the original to the result
        """
        
        from collections import Counter, deque
        from sortedcontainers import SortedDict
        
        # If the array has an odd number of elements, the problem is impossible
        if len(changed) % 2:
            return []
        
        sorted_vals = SortedDict(Counter(changed))
        
        ans = []
        
        # Remove zeroes, if num zeroes is odd, the problem is impossible
        num_zeroes = 0
        if 0 in sorted_vals:
            num_zeroes = sorted_vals.pop(0)
            if num_zeroes % 2:
                return []
            ans += [0] * (num_zeroes // 2)
                
            
        i = 0
        stop = (len(changed) - num_zeroes) // 2
        
        while i < stop:
            val, count = sorted_vals.popitem(0)
            target = val * 2
            
            # Double val does not exist
            if target not in sorted_vals:
                return []
            
            # Not enough double vals 
            if sorted_vals[target] < count:
                return []
            
            # Add the val to the output
            ans += [val] * count
            
            # Subtract the number of times val appeared from its double
            sorted_vals[target] -= count
            
            # If the double has been exhausted, don't add it badk to the vals
            if sorted_vals[target] == 0:
                sorted_vals.pop(target)
            
            # We only need to account for half of the vals
            i += count
        
        return ans
