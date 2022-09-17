class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Use a PQ of max len N
        """
        n = len(matrix)
        pq = [[matrix[row][0], row, 0] for row in range(n)]
        heapq.heapify(pq)
        
        # We will only do k-1 operations then the head of the PQ is the answer
        for _ in range(k-1):
            val, r, c = heapq.heappop(pq)
            
            # If we haven't reached the end of this row
            if c < n-1:
                heapq.heappush(pq, [matrix[r][c+1], r, c+1])
                
        return pq[0][0]
