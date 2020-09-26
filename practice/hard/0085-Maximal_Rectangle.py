class Solution:
  def maximalRectangle(self, matrix: List[List[str]]) -> int:
    """
    - treat each column as if it was the baseline for a horizontal histogram (growing left)
    - for each histogram (# columns) record the max rectangle, (leetcode 84)
    - return the max rectangle of all max rectangle problems
    """
    
    def build_histograms(matrix):
      """
      build histograms representing number of consecutive 1s in a row, going left-to-right
      each column in `matrix` will be a row in `output`, as the rows in output are the 
      current counts of consecutive ones up to that point.
      """
      # transpose matrix because we need horizontal (R to L) histograms
      output = [[None]*len(matrix) for _ in range(len(matrix[0]))]

      for i in range(len(matrix)):
        for j in range(len(matrix[0])):
          if matrix[i][j] == '1':
            output[j][i] = 1 # note we're indexing at (j,i)
            if j > 0:
              output[j][i] += output[j-1][i] # add all previously consecutive 1s
          else:
            output[j][i] = 0

      return output
    
    
    def max_rectangle(histogram) -> int:
      """
      given a list of heights (histogram), return the area of the largest 
      rectangle that can be formed.
      using a monotonically-increasing stack, calculate the height of the index 
      to the right (either next smallest height or end-of-array)
      """
      A = 0
      stack = [(0, histogram[0])] # index, height
      
      for i in range(1, len(histogram)):
        j = i
        while stack and histogram[i] < stack[-1][1]:
          j,h = stack.pop()
          A = max(A, h*(i-j))
        stack.append((j, histogram[i])) # index is j, since j <= i
        
      while stack:
        j,h = stack.pop()
        A = max(A, h*(len(histogram)-j))
        
      return A
    

    A = 0
    if len(matrix) < 1:
      return 0
    histograms = build_histograms(matrix)    
    for histogram in histograms:
      A = max(A, max_rectangle(histogram))
    
    return A
