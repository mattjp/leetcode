class Solution:
  def isPerfectSquare(self, num: int) -> bool:
    upper_bound = (num // 2) + 2
    for i in range(1, upper_bound):
      if i*i == num:
        return True
      if i*i > num:
        return False
    return False
  
  # solved using binary search (smarter)
  def isPerfectSquare(self, num: int) -> bool:
    def binarySearch(num):
      start = 0
      end = num
      while start < end:
        mid = start + ((end - start) // 2)
        res = mid * mid
        if res == num:
          return True
        elif res < num:
          start = mid+1
        else:
          end = mid-1
      return False
    return binarySearch(num)
