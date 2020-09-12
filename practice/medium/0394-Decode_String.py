# I got this as a google onsite question in 2016, if that helps anyone reading this
class Solution:
  def decodeString(self, s: str) -> str:

    def read_str(i: int, string: str) -> (str, int):
      """
      return string to be multiplied by k and cursor index
      """
      output = [] # current characters to be appended
      k = '' # multiplier
      while i < len(string) and string[i] != ']': # check for ']' in the case of >1 consecutive ']'

        while string[i].isdigit(): # get the new multiplier, k
          k += string[i]
          i += 1

        if string[i] == '[': # once we have established k, read bracket interior
          o, j = read_str(i+1, string) # o will be final string in bracket
          output.append(o*int(k))
          i = j+1 # move past ']'
          k = '' # reset k for multiple brackets at this level

        else: # normal chars get appended to output
          output.append(string[i])
          i += 1

      return ''.join(output), i # return the output as a string (idk why it's an array), and the cursor

    return read_str(0, s)[0]
