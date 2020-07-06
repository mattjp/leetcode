class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    num = 0
    b = 1
    for d in digits[::-1]:
      num += d * b
      b *= 10 

    output = []
    num += 1
    while num > 0:
      o = num % 10
      num //= 10
      output.insert(0, o)

    return output
