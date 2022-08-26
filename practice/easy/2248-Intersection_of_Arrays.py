class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = set(nums[0])
        for num in nums[1:]:
            ans = ans.intersection(set(num))
            
        return sorted(list(ans))
