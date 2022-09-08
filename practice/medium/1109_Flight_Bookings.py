class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """
        Obvious solution is too slow:
        
        ans = [0] * n
        
        for first, last, seats in bookings:
            for i in range(first-1, last):
                ans[i] += seats
                
        return ans
        """
        
        
        ans = [0] * (n+1)  # Use n+1 to make the array logic simple 
        
        # Just remember to add x seats starting at a given index
        #  and remove the x seats after the last index
        for first, last, seats in bookings:
            ans[first-1] += seats
            ans[last] -= seats
    
        # Sum from L->R since we kept track of where seats were added/subtracted
        for i in range(1, len(ans)):
            ans[i] += ans[i-1]
        
        return ans[:-1]  # Remove the last index we used to simplify
