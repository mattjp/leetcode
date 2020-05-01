class Solution:
  def longestCommonSubsequence(self, text1: str, text2: str) -> int: 
    # DP[i][j] => longest common subsequence of (text1[:i], text2[:j])
    # abcde, ace
    #
    #       i 'b' 'ba' 'bac' 'bacd' 'bacde'
    #  j       0   1    2     3      4
    # 'a'   0 ''  'a'  'a'   'a'    'a'    = 1
    # 'ac'  1 ''  'a'  'ac'  'ac'   'ac'   = 2
    # 'ace' 2 ''  'a'  'ac'  'ac'   'ace'  = 3
    # if the last letter matches in both substrs, len for this grid is +1 from left or above
    # otherwise len for this grid is just what left or above was
        
    DP = [['' for i in range(len(text1))] for j in range(len(text2))]

    for i in range(len(text1)):
      if text2[0] in text1[:i+1]:
        DP[0][i] = text2[0]
        
    for j in range(len(text2)):
      if text1[0] in text2[:j+1]:
        DP[j][0] = text1[0]
        
    for i in range(1, len(text1)):
      for j in range(1, len(text2)):
        x, y, z = len(DP[j][i-1]), len(DP[j-1][i]), len(DP[j-1][i-1])
        if text1[i] == text2[j] and x == y == z:
          new_str = DP[j][i-1] + text1[i]
          DP[j][i] = new_str
        else:
          if len(DP[j][i-1]) > len(DP[j-1][i]):
            DP[j][i] = DP[j][i-1]
          else:
            DP[j][i] = DP[j-1][i]
              
    return len(DP[len(text2)-1][len(text1)-1])
        
