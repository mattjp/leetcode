public class Solution {
  public bool CanJump(int[] nums) {
    
    int target = 1;

    bool[] canReach = new bool[nums.Length];
    canReach[canReach.Length - 1] = true;

    for (int i = nums.Length - 2; i >= 0; i--) {
      if (nums[i] >= target) {
        canReach[i] = true;
        target = 1;
      } else {
        target++;
      }
    }

    return canReach[0];
  }
}
