class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """
        If we find a decreasing element:
        a) does setting the previous element = element work?
            check to see if the previous previous element is less than element
        b) does setting this element = previous element work?
            check if next element is greater than previous
        If neither of these approaches works, then we know it's impossible
        """
        
        if len(nums) < 3:
            return True
        
        modified = False
        
        # Make optimal first position adjustment
        if nums[1] < nums[0]:
            nums[0] = nums[1]
            modified = True
        
        # Let's assume we will always have 4 elements
        for i in range(2, len(nums)-1):
            # We have a decreasing sequence
            if nums[i] < nums[i-1]:
                if modified:
                    return False
                
                if nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                    modified = True
                    
                elif nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i-1]
                    modified = True
                
                else:
                    return False
                
        # Make optimal last position adjustment
        if nums[-1] < nums[-2]:
            if modified:
                return False
            nums[-1] = nums[-2]
                
        return True
