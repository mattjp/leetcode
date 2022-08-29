class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        L = len(arr) / 2
        m = {}
        
        for a in arr:
            if a not in m:
                m[a] = 0
            m[a] += 1
        
        n = list(map(lambda i: (-i[1], i[0]), m.items()))
        
        heapq.heapify(n)
        
        rm = 0
        ans = 0
        while n and rm < L:
            count, _ = heapq.heappop(n)
            rm -= count
            ans += 1
            
        return ans
