class Solution:
    def expand(self, s: str) -> List[str]:
        """
        {a,b}c{d,e}f
        
        []
        [a, b]
        [ac, bc]
        [acd, bcd, ace, bce]
        [acdf, bcdf, acef, bcef]
        
        
        Use a deque
        Pop from the left, add all necessary suffixes, push to the right
        """
        
        from collections import deque
        
        # Format the input as 2D list
        s = s.replace(',', '')
        options = deque()
        i = 0
        while i < len(s):
            if s[i] == '{':
                lst = []
                i += 1
                while s[i] != '}':
                    lst.append(s[i])
                    i += 1
                options.append(lst)
            else:
                options.append([s[i]])
            i += 1
        
        # Keep a queue of all permutations
        queue = deque(options.popleft())
        
        # Add each option to every member of the queue
        while options:
            option = options.popleft()
            new_queue = deque()
            for o in option:
                for i in range(len(queue)):
                    new_queue.append(queue[i] + o)
            queue = new_queue
            
        return sorted(queue)
