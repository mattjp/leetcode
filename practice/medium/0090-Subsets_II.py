class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        ans.add('')
        
        # We sort first in order to not add duplicates
        nums.sort()
        
        for num in nums:
            to_add = []
            for a in ans:
                if len(a) > 0:
                    to_add.append(f"{a},{str(num)}")
                else:
                    to_add.append(str(num))
            for t in to_add:
                ans.add(t)
            ans.add(str(num))
        
        return [a.split(',') for a in ans]
