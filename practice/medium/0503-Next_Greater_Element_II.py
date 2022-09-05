class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        Append nums to the end of nums to handle wrap around
        Use a stack
        Pop from the top of the stack while it is less than current
        Add current to the top of the stack
        """
        
        L = len(nums)
        stack = []
        output = [-1] * L
        
        # Double the input array
        nums += nums
        
        for i, num in enumerate(nums):
            # Pop from the stack if the top element is smaller than current
            while len(stack) > 0 and num > stack[-1][0]:
                top_num, top_i = stack.pop()
                output[top_i] = num

            # Add current to the stack
            stack.append((num, i % L))
                
        return output
