class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        """
        Use heap of subsequences
            sorted by largest element, length
        
        Iterate through nums adding to the heap
        
        If we cannot operate successfully on the top of the heap, we iterate
        If we get to the end of the heap, we add a new seq
        
        At the end, if all subsequences are len > 2 we return true
        
        {1,2,3}
        {1,2,3} {3}
        {3,4} {1,2,3}
        
        """
        
        sequences = []
        
        for num in nums:
            while sequences:
                top, length = heapq.heappop(sequences)

                # continue the consecutive run of nums
                if top + 1 == num:
                    heapq.heappush(sequences, (num, length + 1))
                    break

                # start a new run and keep both runs in sequences
                elif top == num:
                    heapq.heappush(sequences, (top, length))
                    heapq.heappush(sequences, (num, 1))
                    break

                # the top sequence is invalid
                else:
                    if length < 3:
                        return False

            # start a new sequence if there are no valid sequences
            if len(sequences) < 1:
                heapq.heappush(sequences, (num, 1))

                        
        # determine if there are any invalid sequences at the end
        while sequences:
            top, length = heapq.heappop(sequences)
            if length < 3:
                return False

        return True
