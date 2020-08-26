class Solution:
  def fizzBuzz(self, n: int) -> List[str]:
    output = []
    for i in range(1, n+1):
      o = ''
      if i % 3 and i % 5:
        o = str(i)
      else:
        if i % 3 == 0:
          o += 'Fizz'
        if i % 5 == 0:
          o += 'Buzz'
      output.append(o)

    return output
