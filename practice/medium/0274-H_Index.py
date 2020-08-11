class Solution:
  def hIndex(self, citations: List[int]) -> int:

    # don't have to look at every entry, since `citations` is sorted
    def is_valid(citations, h):
      g = -h if h > 0 else h
      a = citations[g] >= h
      b = citations[g-1] <= h if h < len(citations) else True
      return (a, b)

    # binary search sorted `citations`
    # initial bounds are 0 and length of `citations`
    def binary_search(citations, l, r, best):
      h = (l+r) // 2
      a,b = is_valid(citations, h)
      if a and b:
        best = max(best, h)
      if l == r:
        return best
      if not a:
        return binary_search(citations, l, h, best)
      else:
        return binary_search(citations, h+1, r, best)


    return binary_search(sorted(citations), 0, len(citations), 0) if citations else 0
