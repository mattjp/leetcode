object Solution {

    def maxSubArray(nums: Array[Int]): Int = {
      
      if (nums.nonEmpty)
        // start at index 1
        // pair._1 is current maximum, ._2 is the global maximum
        nums.drop(1).foldLeft((nums(0), nums(0))) {
          case ((cur, max), num) => {
            // subarray sum is either everything we've seen up to and including `i` or max sum starts at `i`
            val sum = Math.max(num, cur + num)
            (sum, Math.max(max, sum)) 
          }
        }._2
      else Int.MinValue
    }
}
