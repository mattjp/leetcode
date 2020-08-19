class Solution:
  def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
    self.output = set()
    self.nums = []

    # get all available numbers
    # if N=1, then all numbers are available
    if N > 1:
      for i in range(K, 10):
        self.nums.extend([i-K, i])
    else: 
      self.nums = range(10)


    def go(cur: str) -> None:
      # once we have enough numbers, we add the current number to the output
      # if it is not there already
      if len(cur) == N:
        if int(cur) not in self.output:
          self.output.add(int(cur))
        return

      # otherwise, iterate through all available numbers, adding and recursing
      # if the difference between the current number and the last added number is K
      for num in self.nums:
        # if nothing has been added, there is no difference to calculate
        if len(cur) == 0:
          # disallow leading zeros, unless N=1
          if num == 0 and N > 1: continue
          else:
            cur += str(num)
            go(cur)
            cur = cur[:-1]
        # assert that the number we're adding is K away from the last added number
        elif abs(int(cur[-1]) - num) == K:
            cur += str(num)
            go(cur)
            cur = cur[:-1]

    go('')
    return list(self.output)
