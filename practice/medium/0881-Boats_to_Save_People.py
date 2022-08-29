class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        1. sort and use 2 pointers
        """
        
        people.sort()
        
        ans, light, heavy = 0, 0, len(people)-1
        
        while light <= heavy:
            boat = people[heavy]
            
            # we can only carry 2 people per boat
            if light < heavy and people[light] <= limit - boat:
                boat += people[light]
                light += 1

            heavy -= 1
            ans += 1
            
        return ans
