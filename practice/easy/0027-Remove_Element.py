class Solution:
  def removeElement(self, nums: List[int], val: int) -> int:
    insert_ptr = len(nums)-1
    count = 0
    for i in range(len(nums)):
      top = nums.pop(0)
      if top == val:
        nums.append(top)
        insert_ptr -= 1
      else:
        nums.insert(insert_ptr, top)
        count += 1
    return count
