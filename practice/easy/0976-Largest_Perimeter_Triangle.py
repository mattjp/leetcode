class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort(reverse=True)
        
        for l in range(len(nums)-2):
            r = l+3
            window = nums[l:r]
            perim = sum(window)
            hyp = max(window)
            if perim - hyp > hyp:
                return perim
            
        return 0
