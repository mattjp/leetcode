class Solution:
  def addDigits(self, num: int) -> int:

    x = num # don't modify input
    while len(str(x)) > 1:
      xs = list(str(x)) # convert to array of str
      xs = list(map(int, xs)) # convert str to int
      y = functools.reduce(lambda a,b: a+b, xs) # should have just used `sum`
      x = y

    return x
