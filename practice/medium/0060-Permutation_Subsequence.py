class Solution:
  def getPermutation(self, n: int, k: int) -> str:
    """
    This is definitely a cheating way of doing this problem.
    """

    s_int = list(range(1, n+1))
    s_str = list(map(lambda x: str(x), s_int))

    combinations = list(itertools.permutations(s_str, n))
    output = combinations[k-1]
    return ''.join(output)
