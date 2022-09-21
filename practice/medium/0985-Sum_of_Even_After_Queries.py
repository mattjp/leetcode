class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        # Initial sum of even numbers
        total = sum([n for n in nums if n % 2 == 0])
        ans = []
        
        for val,i in queries:
            original = nums[i]
            updated = nums[i] + val
            
            # Case 1. original was odd and updated is odd - do nothing
            if original % 2 == 1 and updated % 2 == 1:
                nums[i] = updated
                ans.append(total)
            
            # Case 2. original was odd and updated is even - add new even value to total
            elif original % 2 == 1 and updated % 2 == 0:
                total += updated
                nums[i] = updated
                ans.append(total)
            
            # Case 3. original was even and updated is odd - remove old even value from total
            elif original % 2 == 0 and updated % 2 == 1:
                total -= original
                nums[i] = updated
                ans.append(total)
            
            # Case 4. original was even and updated is even - remove old even value and add new even value
            else:
                total -= original
                total += updated
                nums[i] = updated
                ans.append(total)
            
        return ans
