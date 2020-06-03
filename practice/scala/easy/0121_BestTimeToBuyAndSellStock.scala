object Solution {

  def maxProfit(prices: Array[Int]): Int = {
    // return type of .foldLeft will be (minCost, maxProfit)
    prices.foldLeft((Int.MaxValue, 0)) {
      // return type of tuple with the current price
      case ((minMin, maxProfit), price) =>
        val curMin = if (price < minMin) price else minMin
        val curProfit = 
            if (price - curMin > maxProfit) price - curMin
            else maxProfit
        (curMin, curProfit)
    }._2
  }
}
