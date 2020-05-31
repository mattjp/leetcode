class Solution:
  def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

    # distance formula
    def distance_to_origin(x: int, y: int) -> int:
      from math import sqrt
      return sqrt(x**2 + y**2)

    # make a priority queue of distances
    pq = []
    for x,y in points:
      d = distance_to_origin(x, y)
      heapq.heappush(pq, (d, [x, y]))

    # take the top K distances
    output = []
    for _ in range(K):
      output.append(heapq.heappop(pq)[1])
    return output
