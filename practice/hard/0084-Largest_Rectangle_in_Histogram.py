class Solution:
  def largestRectangleArea(self, heights: List[int]) -> int:
    """
    idea is to use a monotonically increasing stack
    when an element is found that is smaller than the top of the stack,
      pop until the stack is strictly increasing again.
    with each pop, calculate rectangle area from the index of the popped column
    to the newly added column
    
    https://www.youtube.com/watch?v=VNbkzsnllsU
    """

    A = 0
    stack = [] # (index, height)
    
    for i,height in enumerate(heights):
      j = i # if height is bigger than stack.top, index remains i
      while stack and stack[-1][1] > height: # while stack.top > height
        j, j_height = stack.pop()
        A = max(A, j_height*(i-j)) # calculate area from j forward, assuming j_height is the height
        
      # note that the index appended is j, which could be less than i if we popped from the stack
      # this is because if we did pop, that rectangle technically started at j, not i
      stack.append((j, height))
      
    # now we can just measure each column to the end of the array
    # because there is nothing smaller ahead of the column
    i = len(heights) # measuring to end-of-array now
    while stack:
      j, j_height = stack.pop()
      A = max(A, j_height*(i-j))
      
    return A


#     naive
#     A = 0
#     for i in range(len(heights)):
#       h = heights[i]
#       a = heights[i]
#       for j in range(i+1, len(heights)):
#         h = min(h, heights[j])
#         a = max(h * (1 + j - i), a)
#       A = max(A, a)
#     return A
