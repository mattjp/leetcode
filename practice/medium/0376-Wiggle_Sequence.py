class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
        Use a stack
        If there are 2 nums that don't follow the pattern,
        Keep the num that has the largest diff to the previous
        """
        
        stack = [[nums[0], 0]]
        
        for num in nums[1:]:
            d = num - stack[-1][0]
            
            # Difference is positive
            if d > 0:
                if stack[-1][1] <= 0:
                    stack.append([num, d])
                else:
                    prev_num, prev_d = stack.pop()
                    stack.append([max(num, prev_num), max(d, prev_d)])
            
            # Difference is negative
            elif d < 0:
                if stack[-1][1] >= 0:
                    stack.append([num, d])
                else:
                    prev_num, prev_d = stack.pop()
                    stack.append([min(num, prev_num), min(d, prev_d)])
            
            # Numbers are the same, no-op
            else:
                continue
                
        return len(stack)
