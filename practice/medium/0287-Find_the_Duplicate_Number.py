class Solution:
  def findDuplicate(self, nums: List[int]) -> int:
    """
    do tortise and hare using the value of each index as a singly-linked list
    since nums is [1,n-1] 0 is the entrace to the list containing the cycle
    """

    tortise = hare = 0
    tortise = nums[tortise]
    hare = nums[nums[hare]]

    # hare double speed
    while tortise != hare:
      tortise = nums[tortise]
      hare = nums[nums[hare]]

    # reset tortise and go equal speed
    tortise = 0
    while tortise != hare:
      tortise = nums[tortise]
      hare = nums[hare]

    return tortise
