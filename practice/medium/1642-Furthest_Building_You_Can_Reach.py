class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        TOO SLOW:
        bricks = 5, ladders = 1
        H [  4,    2,    7,    6,    9,    14,   12 ]
            [5,2] [5,2] [5,1] [5,1] [2,1]
                        [0,2] [0,2] [0,1]
                                    [5,0]

        For each buildling, keep a list of the ways we could have arrived
        If the list is empty, we know we can't make it any further
        """
        
        """
        Use ladders until you don't have ladders left
        Replace smallest ladder with bricks, if possible
        Otherwise, use bricks for the next climb
        Repeat until no more ladders, bricks cannot make next gap
        """
        
        used_ladders = []
        
        for i in range(len(heights)-1):
            # print(f"Building {i}, height: {heights[i]}")
            # print(f"Bricks: {bricks}, Ladders: {ladders}, Used: {used_ladders}")
            
            dist = heights[i+1] - heights[i]
            
            if dist < 1:
                continue
                
            # Always default to using a ladder
            if ladders > 0:
                heapq.heappush(used_ladders, dist)
                ladders -= 1
                
            else:
                # There is a ladder we can potentially swap for bricks
                if used_ladders:
                    
                    # The distance is smaller than the smallest ladder
                    if dist <= used_ladders[0]:
                        if dist <= bricks:
                            bricks -= dist
                        else:
                            return i
                    
                    # The smallest ladder is smaller than the distance
                    else:
                        if bricks >= used_ladders[0]:
                            d = heapq.heappop(used_ladders)
                            heapq.heappush(used_ladders, dist)
                            bricks -= d
                        else:
                            return i

                # We only have bricks
                else:
                    if dist <= bricks:
                        bricks -= dist
                    else:
                        return i
                    
        # We made it to the end
        return len(heights)-1
        
