class Solution:
  def lastStoneWeight(self, stones: List[int]) -> int:
    negStones = list(map(lambda x: x*-1, stones))
    heapq.heapify(negStones)
    while len(negStones) > 1:
      heaviest = heapq.heappop(negStones)
      secondHeaviest = heapq.heappop(negStones)
      newStone = heaviest - secondHeaviest 
      heapq.heappush(negStones, newStone)
    if len(negStones) == 1:
      return -1 * negStones[0]
    else:
      return 0
