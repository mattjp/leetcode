class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
        use a stack
        if ( then add to stack
        if ) and top of stack is ( then pop and +1 to ans and add 1 to stack
        if ) and top of stack is num then pop and *2
        
        
        (
        ((
        (((
        ((1
        (2
        4
        """
        
        stack = []
        
        for ch in s:
            if ch == '(':
                stack.append(ch)
            else:
                # simplest case, () yields 1
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    # add all numbers that will be multiplied by 2
                    num = stack.pop()
                    while stack[-1] != '(':
                        num += stack.pop()

                    # remove (
                    stack.pop()
                    stack.append(num * 2)
        
        return sum(stack)
        
