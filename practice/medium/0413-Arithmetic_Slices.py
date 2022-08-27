class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        count  add
        1      0
        2      1
        3      2
        4      3
        5      4
        6      5
        """
        
        if len(nums) < 3:
            return 0
        
        prev_diff = nums[1] - nums[0]
        count = 1
        total = 0
        ans = 0
        
        for i in range(2, len(nums)):
            diff = nums[i] - nums[i-1]

            if diff == prev_diff:
                count += 1
                total += count-1
            else:
                prev_diff = diff
                if count > 1:
                    ans += total
                count = 1
                total = 0
                
        if count > 1:
            ans += total
                
        return ans
