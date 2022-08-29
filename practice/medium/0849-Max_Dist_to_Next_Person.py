class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_dist = 0
        ans = 0
        l = 0
        for r in range(len(seats)):
            if seats[r] == 1:
                # Catch open left seat
                if l == 0 and seats[l] == 0:
                    ans = r
                    
                # Optimize to sit in middle
                elif (r - l) // 2 > ans:
                    ans = (r - l) // 2
                    
                max_dist = r - l                
                l = r
               
            
        # Catch scenario with open right end seat
        if r - l >= ans and seats[r] == 0:
            ans = r - l

        return ans
