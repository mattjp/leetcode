# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        """
        1. check if the current quandrant has ships
        2. if no, base case return 0
        3. else subdivide and return 1 + recurse(4 quadrants)
        """
        
        max_height = topRight.y
        max_width = topRight.x
        seen = set()
        
        def search(top_right, bot_left):
            
            # sketchy math
            if top_right.x < bot_left.x or top_right.y < bot_left.y:
                return 0
            
            # no point in going further
            if not sea.hasShips(top_right, bot_left):
                return 0
            
            # this is a ship
            if top_right.x == bot_left.x and top_right.y == bot_left.y:
                # duplicates (bad math)
                if (top_right.x, top_right.y) not in seen:
                    seen.add((top_right.x, top_right.y))
                    return 1
                else:
                    return 0
            
            
            mid_height = (top_right.y + bot_left.y) // 2
            mid_width = (top_right.x + bot_left.x) // 2
            
            return (
                # upper right
                search(
                    top_right, 
                    Point(min(mid_width+1, max_width), min(mid_height+1, max_height))
                ) +

                # upper left
                search(
                    Point(mid_width, top_right.y), 
                    Point(bot_left.x, min(mid_height+1, max_height))
                ) +

                # lower right
                search(
                    Point(top_right.x, mid_height), 
                    Point(min(mid_width+1, max_width), bot_left.y)
                ) +

                # lower left
                search(Point(mid_width, mid_height), bot_left)
            )
            
            
        return search(topRight, bottomLeft)
