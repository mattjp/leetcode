class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        """
        Need decreasing to i and increasing from i
        Can use decreasing stack to find candidates
        For each candidate check if next items are increasing
        """
        
        stack = collections.deque()
        dec_candidates = set()
        inc_candidates = set()
        
        if time == 0:
            return range(len(security))
        
        # Find decreasing candidates
        for i in range(len(security) - time + 1):
            # Valid candidate
            if len(stack) == time + 1:
                dec_candidates.add(i-1)
                stack.popleft()
            
            # Reset stack if non-decreasing element
            if len(stack) > 0 and security[i] > stack[-1]:
                stack = collections.deque()
                
            # Add next element
            stack.append(security[i])
            
        # Reset the stack
        stack.clear()
            
        # Find increasing candidates
        for i in range(time, len(security)):
            # Valid candidate
            if len(stack) == time + 1:
                inc_candidates.add(i - 1 - time)
                stack.popleft()
            
            # Reset stack if non-increasing element
            if len(stack) > 0 and security[i] < stack[-1]:
                stack = collections.deque()
                
            # Add next element
            stack.append(security[i])
            
        # Check if last elements are valid
        if len(stack) == time + 1:
            inc_candidates.add(len(security) - (time + 1))
        
        return list(dec_candidates.intersection(inc_candidates))
        
