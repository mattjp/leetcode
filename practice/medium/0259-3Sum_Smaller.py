class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        """
        1. Sort ascending
        2. Use 3 iterators
            r goes from R -> L
            inner loop from 0 to r-1 (start, end)
        3. If the condition is satisfied in the inner loop, we know
            it will be satisfied for all number between start and end
        4. Increment start if the condition is satisfied
        5. Decrement end if the condition is not satisfied
        """
        
        ans = 0
        nums.sort()
        
        for r in range(len(nums)-1, 1, -1):
            start, end = 0, r - 1
            while end > start:
                if nums[start] + nums[end] + nums[r] < target:
                    ans += end - start
                    start += 1
                else:
                    end -= 1
                    
        return ans
