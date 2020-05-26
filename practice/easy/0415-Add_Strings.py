class Solution:
  def addStrings(self, num1: str, num2: str) -> str:
    mappings = {
      '0': 0,
      '1': 1,
      '2': 2,
      '3': 3,
      '4': 4,
      '5': 5,
      '6': 6,
      '7': 7,
      '8': 8,
      '9': 9
    }
    
    arr1 = list(num1)
    arr2 = list(num2)
    
    output = ''
    carry = 0
    while len(arr1) > 0 or len(arr2) > 0:
      ch1 = arr1.pop() if len(arr1) > 0 else '0'
      ch2 = arr2.pop() if len(arr2) > 0 else '0'
      val1 = mappings[ch1]
      val2 = mappings[ch2]
      x = val1 + val2 + carry
      carry = x // 10
      x %= 10
      output = str(x) + output # just did str() 'cause making mappings is tedious

    if carry == 1:
      output = str(carry) + output

    return output
