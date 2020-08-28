# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

# Incorrect, should use 7x7 grid labeled 1-10
class Solution:
  def rand10(self):
    """
    :rtype: int
    """

    output = 0
    for _ in range(10):
      output += rand7()
    return (output % 10) + 1
