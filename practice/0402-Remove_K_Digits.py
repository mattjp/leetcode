class Solution:
  def removeKdigits(self, num: str, k: int) -> str:
    # always remove the largest number from the first increasing subsequence
    # while k > 0 
    # remove the number from num that results in the smallest new num (too slow)
    # starting at i = 0, while num[i] > num[i+1] i++, then pop num[i]

    if k >= len(num):
      return '0'

    smallest = num
    for _ in range(k):
      i = 0
      while i < len(smallest)-1 and int(smallest[i]) <= int(smallest[i+1]):
        i += 1
      smallest = smallest[:i] + smallest[i+1:]
    return str(int(smallest)) # remove leading zeroes
