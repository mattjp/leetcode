class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        """
        1. sort the slots (same as putting into heaps)
        2. use pointers (popping from heap is weird)
        3. calculate the overlap
        4. if the overlap is >= duration then return overlap start, duration
        5. if the overlap is < duration inc the ptr that ends earlier
        6. break ties by earlier start
        7. if you run out of one heap return empty
        """
        
        # pointers
        a = b = 0
        
        # sort bc we need earliest
        A = sorted(slots1)
        B = sorted(slots2)

        # go while we still have options        
        while a < len(A) and b < len(B):
            
            # take the top of each heap
            start_a, end_a = A[a]
            start_b, end_b = B[b]
            
            # calculate overlap
            min_end = min(end_a, end_b)
            max_start = max(start_a, start_b)
            overlap = min_end - max_start
            
            # return if we find an overlap that works
            if overlap >= duration:
                return [max_start, max_start + duration]
            
            # increment the pointer of the timeslot that ends earlier
            if end_a < end_b:
                a += 1
            elif end_a > end_b:
                b += 1
            else:
                # if they end at the same time, increment whichever starts earlier
                if start_a < start_b:
                    a += 1
                elif start_a > start_b:
                    b += 1
                else:
                    a += 1
                    b += 1
                    
        return []
