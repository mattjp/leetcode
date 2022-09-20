class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        put A, B, and C in PQ
        pop the largest of the 3
        add the value to a stack [ch, count]
        if count is 2 then add the next most frequent char
        if there is no next most frequent char then end
        """
        
        
        # Assert we start with no 0s in the PQ
        pq = [[-val, ch] for val, ch in zip([a,b,c],["a","b","c"]) if val > 0]
        heapq.heapify(pq)
        stack = []
        
        while pq:
            count, val = heapq.heappop(pq)
            count *= -1
            
            # Empty stack
            if len(stack) < 1:
                stack.append([val, 1])
                if count > 1:
                    heapq.heappush(pq, [-(count-1), val])
                
            # Top of stack is match
            elif stack[-1][0] == val:
                
                # Top of stack has only been added once
                if stack[-1][1] < 2:
                    stack[-1][1] += 1
                    if count > 1:
                        heapq.heappush(pq, [-(count-1), val])
                    
                # Top of stack has been added twice
                else:
                    
                    # No other char to add
                    if len(pq) < 1:
                        return "".join([ch*count for ch,count in stack])
                    
                    # Add next most frequent char
                    else:
                        c, v = heapq.heappop(pq)
                        c *= -1
                        stack.append([v, 1])
                        if c > 1:
                            heapq.heappush(pq, [-(c-1), v])
                        heapq.heappush(pq, [-count, val])
                
            # Top of stack is not a match
            else:
                stack.append([val, 1])
                if count > 1:
                    heapq.heappush(pq, [-(count-1), val])
                
                
        return "".join([ch*count for ch,count in stack])
