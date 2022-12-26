public class Solution {
  public int ClimbStairs(int n) {
    // for the nth stair, add the number of ways to get to n-1 and n-2
    // add the first 2 solutions for simplicity

    if (n < 3) {
      return n;
    }

    int[] stairs = new int[n];
    stairs[0] = 1;
    stairs[1] = 2;
    
    for (int i = 2; i < n; i++) {
      stairs[i] = stairs[i-1] + stairs[i-2];
    }

    return stairs.Last();
  }
}
