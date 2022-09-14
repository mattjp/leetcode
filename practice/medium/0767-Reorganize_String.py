class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        Collect all of the characters (ordered by frequency)
        Round-robin insert them into the result string
        
        
        Put all of the chars in a PQ ordered by frequency
        Pop the top 2 from the PQ
        Add the chars to the result, push the new frequencies back onto the PQ
        """
        
        from collections import Counter, deque
        
        ans = ""
        
        chars = [(-v, k) for k,v in Counter(s).items()]
        heapq.heapify(chars)
        
        while chars:
            if len(chars) < 2:
                count, ch = heapq.heappop(chars)
                if -count == 1 and (len(ans) == 0 or ans[-1] != ch):
                    ans += ch
                else:
                    return ""
            else:
                count1, ch1 = heapq.heappop(chars)
                count2, ch2 = heapq.heappop(chars)
                
                ans += ch1
                ans += ch2
                
                if -count1 > 1:
                    heapq.heappush(chars, (count1+1, ch1))
                if -count2 > 1:
                    heapq.heappush(chars, (count2+1, ch2))
                    
        return ans
        
