class Solution:
  def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    """
    1. send everyone to their cheaper city
    2. order by difference in cost (bigger diffs at top of priority queue)
    3. while the lists are unbalanced, send people with biggest price difference to the other city
    """

    A = []
    B = []

    for cost in costs:
      (a,b) = cost
      if a <= b:
        heapq.heappush(A, (b-a, cost))
      else:
        heapq.heappush(B, (a-b, cost))

    while len(A) != len(B):
      if len(A) > len(B):
        top = heapq.heappop(A)
        heapq.heappush(B, top)
      else:
        top = heapq.heappop(B)
        heapq.heappush(A, top)

    sum_A = sum(map(lambda a: a[1][0], A))
    sum_B = sum(map(lambda b: b[1][1], B))
    return sum_A + sum_B
