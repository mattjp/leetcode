class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Remember that the selected index does not count towards either L or R        
        R = sum(nums[1:])
        L = 0
        i = 0
        
        while i < len(nums)-1 and R != L:
            i += 1
            L += nums[i-1]
            R -= nums[i]
            
            
        return i if R == L else -1
