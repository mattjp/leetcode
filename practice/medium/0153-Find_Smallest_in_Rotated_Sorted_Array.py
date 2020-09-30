class Solution:
  def findMin(self, nums: List[int]) -> int:
    """
    do binary search
    if endR > endL: search normally
    if endR < endL: search opposite
    """

    def binary_search(l: int, r: int, n: List[int]):
      """
      since `l` and `r` are inclusive, l will never equal r (i think)
      which is why we have the jacked up conditional
      """
      m = (l+r+1)//2
      if l == m or r == m:
        return min(n[l], n[r])
      
      # if the furthest left thing is greater than the furthest right
      # thing, we BS opposite how we normally would
      if n[l] > n[r]:
        if n[m] > n[l]:
          return binary_search(m, r, n)
        else:
          return binary_search(l, m, n)
      # otherwise, BS to the left 
      # (since the array sub section is currently ordered we can always go left)
      else:
        return binary_search(l, m, n)
        
    return binary_search(0, len(nums)-1, nums)
