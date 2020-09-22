class Solution:

  def __init__(self, nums: List[int]):
    self.orig = nums


  def reset(self) -> List[int]:
    """
    Resets the array to its original configuration and return it.
    """
    return self.orig


  def shuffle(self) -> List[int]:
    """
    Returns a random shuffling of the array.
    """

    # this works but is also probably cheating
    # from random import sample
    # return sample(self.orig, k=len(self.orig))

    # actual solution
    from random import randint
    orig = self.orig.copy()
    for i in range(len(orig)):
      r = randint(0, len(orig)-1)
      orig[i], orig[r] = orig[r], orig[i]
    return orig


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
