class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        1. create stack, push (ch, count) count+1 if ch matches top of stack
        2. if count == k, pop k times
        """
        
        stack = []
        
        for ch in s:
            if len(stack) == 0:
                stack.append([ch, 1])
            elif stack[-1][0] == ch:
                stack.append([ch, stack[-1][1]+1])
            else:
                stack.append([ch, 1])
            
            if stack[-1][1] == k:
                l = len(stack)-k
                stack = stack[:l]
                
        return ''.join(list(map(lambda st: st[0], stack)))
