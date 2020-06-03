class Solution:
  def reverse(self, x: int) -> int:
    int_max = 2**31 - 1
    int_min = -2**31
    
    if x >= int_max or x <= int_min:
      return 0

    a = str(x)[::-1]

    if x < 0:
      a = '-' + a[:-1]
    
    # make sure the reversed integer is within the bounds
    return int(a) if int(a) < int_max and int(a) > int_min else 0
