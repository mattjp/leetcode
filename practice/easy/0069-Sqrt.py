class Solution:
    """
    SLOW BUT PASSES:
    def mySqrt(self, x: int) -> int:
        y = 1
        while y * y <= x:
            y += 1
        return y-1
    """ 
    
    def mySqrt(self, x: int) -> int:
        
        def binarySearch(l, r, x):
            if l > r:
                return r
            
            m = (l + r) // 2
            if (m * m) > x:
                return binarySearch(l, m-1, x)
            elif (m * m) < x:
                return binarySearch(m+1, r, x)
            else:
                return m
            

        return binarySearch(0, x, x)        
