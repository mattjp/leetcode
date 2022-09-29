class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Alternately, binary search to the closest number to x
        Then use 2 pointers to take the L,R value that is closest
        If the L value is taken, append to front of deque
        If the R value is taken, append to end of deque
        """
        
        d = [(abs(a-x), a) for a in arr]
        heapq.heapify(d)
        
        k_closest = heapq.nsmallest(k, d)
        
        return sorted([v for _,v in k_closest])
