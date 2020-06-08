object Solution {
  def isPowerOfTwo(n: Int): Boolean = {

    def loop(m: Int): Boolean = {
      if (m > 0 && m % 2 == 0) loop(m/2)
      else {
        if (m == 1) true
        else false
      }
    }

    return loop(n)
  }
}
