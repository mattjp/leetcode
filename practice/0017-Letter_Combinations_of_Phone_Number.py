class Solution:
  def letterCombinations(self, digits: str) -> List[str]:
    digit_mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    res = ['']
    for digit in digits:
      letters = digit_mapping[digit]
      res_tmp = []
      for letter in letters:
        for r in res:
          res_tmp.append(r+letter)
      res = res_tmp
    return res if res != [''] else []
