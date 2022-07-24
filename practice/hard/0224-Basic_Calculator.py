class Solution:
    def calculate(self, s: str) -> int:
        """
        remove whitespace
        read until +,-,(
            if +,- then save the left number and start reading again
            if ( then recurse, returning the answer
            base case is )
        """

        # Create stack of numbers and operators
        s = s.replace(' ', '')
        stack = []
        num = ''
        for ch in s:
            if ch == '+' or ch == '-' or ch == '(' or ch == ')':
                if num != '':
                    stack.append(int(num))
                stack.append(ch)
                num = ''
            else:
                num += ch
          
        # If there is one last number to append, append it
        if num != '':
            stack.append(int(num))
           
        # Reverse the stack so it behaves like a stack
        stack.reverse()
        
        def solve(stack):
            num = 0
            cur = stack.pop()
            prev_num = cur

            # Continue to pop off stack. Return when ) is reached, or stack is empty.
            while len(stack) > 0 and cur != ')':
                # Do addition/subtraction
                if cur == '+' or cur == '-':
                    coef = 1 if cur == '+' else -1
                    if stack[-1] == '(':
                        stack.pop()
                        num += coef * solve(stack)
                    else:
                        num += coef * stack.pop()
                    stack.append(num)
                    prev_num = num
                    num = 0
                # Start new recursion, push the result to the stack
                elif cur == '(':
                    num = solve(stack)
                    stack.append(num)
                    prev_num = num
                    num = 0
                # Top of stack is just a regular number
                else:
                    num = int(cur)
                # Always pop top of stack
                cur = stack.pop()
                    
            if len(stack) > 0 and cur != ')':
                return stack[0]
            else:
                return prev_num
                
        return solve(stack)        
