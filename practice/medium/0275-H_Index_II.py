class Solution:
  def hIndex(self, citations: List[int]) -> int:
    """
    Given an array of citations sorted in ascending order (each citation is a non-negative integer) 
    of a researcher, write a function to compute the researcher's h-index.

    According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her 
    N papers have at least h citations each, and the other N − h papers have no more than 
    h citations each."
    """
    self.output = 0

    # determines if a given `h` is valid
    def valid(citations: List[int], h: int) -> bool:
      x = -h
      y = -(h+1)
      a = citations[x] >= h
      b = citations[y] <= h if abs(y) <= len(citations) else True # handles the case of all citations being > `h`
      return a, b


    # binary search for `h`
    def binarySearch(citations: List[int], l: int, r: int):
      i = (l + r) // 2
      v1, v2 = valid(citations, i)
      if v1 and v2:
        self.output = max(self.output, i) # if both v1 and v2, this is a valid `h`
      if l == r:
        return
      elif v1 and not v2: # if only the upper bound condition is satisfied (h too small), go right
        return binarySearch(citations, i+1, r)
      else: # if only lower bound or neither condition is satisfied (h too big), go left
        return binarySearch(citations, l, i)

    # dumb error checking
    if len(citations) < 1:
      return self.output

    # run driver
    binarySearch(citations, 0, len(citations))
    return self.output        
