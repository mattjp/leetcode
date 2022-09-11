class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Put 2 iterators on either end
        Perform 3-Sum with the right 3 iterators
        Inc the leftmost iterator and repeat
        """
        
        ans = set()
        
        nums.sort()
        
        # Iterate the leftmost pointer forwards
        for L in range(len(nums)-3):
            
            # Iterate the rightmost pointer backwards
            for R in range(len(nums)-1, L+2, -1):
                r = R-1
                l = L+1
                
                # Using the 2 boarders {L, R} iterate {l, r} to find possible solutions
                while l < r:
                    x = nums[R]+nums[r]+nums[l]+nums[L]
                    if x == target:
                        ans.add(f"{nums[R]},{nums[r]},{nums[l]},{nums[L]}")
                        l += 1
                    elif x > target:
                        r -= 1
                    else:
                        l += 1
        
        return [a.split(',') for a in ans]
