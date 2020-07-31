class Solution:
  def countAndSay(self, n: int) -> str:

    def group(xs: List[str]):
      output = [xs.pop(0)]
      while xs:
        x = xs.pop(0)
        if output[-1][0] == x: output[-1] += x
        else: output.append(x)
      return list(map(lambda l: [str(len(l)), l[0]], output))


    seq = ['1']
    for i in range(1, n):
      g = group(seq)
      seq = functools.reduce(operator.add, g)

    return ''.join(seq)
