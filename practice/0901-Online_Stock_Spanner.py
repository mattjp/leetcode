class StockSpanner:
  def __init__(self):
    self.day = 0     # use dicts instead of lists for lookup
    self.prices = {} # all previous prices
    self.spans = {}  # all previous spans


  def next(self, price: int) -> int:
    output = 0
    self.prices[self.day] = price
    self.spans[self.day] = 1
    i = self.day
    while i >= 0 and self.prices[i] <= price:
      span = self.spans[i]
      output += span
      i -= span # go back `span` days, since we know cur.price >= prev.price

    self.spans[self.day] = output
    self.day += 1
    return output

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
