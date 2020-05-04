class Solution:
  def findComplement(self, num: int) -> int:
    b_num = bin(num)[2:]
    rev_comp = ''

    for b in b_num:
      if b == '1':
        rev_comp = '0' + rev_comp
      else:
        rev_comp = '1' + rev_comp

    res = 0
    for i,b in enumerate(rev_comp):
      if b == '1':
        res += 2**i
    return res
