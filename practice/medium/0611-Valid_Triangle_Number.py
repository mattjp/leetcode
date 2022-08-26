class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        0. sort
        1. iterate from R -> L
        2. create start at 0, end at r - 1
        3. if end + start > r then triangle is vaild, and all subsequent
            ends are valid
        """
        
        nums.sort()
        ans = 0
        
        for c in range(len(nums)-1, 1, -1):
            a, b = 0, c-1
            while a < b:
                if nums[a] + nums[b] > nums[c]:
                    ans += b - a
                    b -= 1
                else:
                    a += 1
        return ans
        
