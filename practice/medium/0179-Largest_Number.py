class Solution:
  def largestNumber(self, nums: List[int]) -> str:
    from functools import cmp_to_key, reduce
    
    def sort_func(AA: str, BB: str):
      A = AA
      B = BB
      i = 0
      while len(A) < len(B):
        A += A[i]
        i += 1
      i = 0
      while len(B) < len(A):
        B += B[i]
        i += 1
      
      for a,b in zip(A,B):
        if a > b:
          return 1
        if a < b: 
          return -1
        
      # handle case where wrap-around is the same
      # ex. [212, 12]
      return 1 if AA[-1]+BB[0] > AA[0]+BB[-1] else -1

    
    strs = list(map(str, nums))
    strs.sort(key=cmp_to_key(sort_func), reverse=True) # python3 doesn't support `cmp`, use functools
    num = reduce(lambda a,b: a+b, strs)
    
    while num[0] == '0' and len(num) > 1: # remove leading zeroes
      num = num[1:]
      
    return num
