class Solution:
  def dailyTemperatures(self, T: List[int]) -> List[int]:
    """
    when is the next item larger than me?
    use a stack? append index difference
    
    73
    74 (74 > 73) therefore pop and append(len(stack))
    75
    75, 71
    75, 71, 69
    75, 72 (69 is popped (append 1), 71 is popped (append 2))
    76 (72 popped, 75 popped)
    76, 73 (append zero for len stack)
    """
    
    stack = [] # (temp, index)
    output = [0] * len(T)
    
    for t,temp in enumerate(T):
      # print(stack)
      while stack and temp > stack[-1][0]:
        _, u = stack.pop()
        # output.append(t-u)
        output[u] = t-u
        
      stack.append((temp, t))
      
    # output.extend([0]*len(stack))
    return output
