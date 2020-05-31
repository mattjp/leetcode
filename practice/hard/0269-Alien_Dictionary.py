# This first attempt was not me solving the problem. This was walking through the algorithm.
class Solution:
  def alienOrder(self, words: List[str]) -> str:
    from collections import Counter, deque, defaultdict

    adj_list = defaultdict(set)
    in_degree = Counter({ c: 0 for word in words for c in word }) # counter is unique

    for i in range(len(words)-1):
      first = words[i]
      second = words[i+1]
      for f,s in zip(first, second):
          if f != s: # iterate until characters are different (first difference)
            if s not in adj_list[f]:
              adj_list[f].add(s)
              in_degree[s] += 1
            break # stop looking since we found the first difference
      # else on for-loop runs when `break` is never hit
      # in this instance, it runs when no character in either word is different
      else:
        # since no chars were different, we must check if the second was a prefix of the first
        if len(second) < len(first): 
          return ''

    output = []
    queue = deque([c for c in in_degree if in_degree[c] == 0]) # start with all nodes who have in-degree of 0

    while queue:
      q = queue.popleft()
      output.append(q)
      for p in adj_list[q]:
        in_degree[p] -= 1 # remove this node from the graph
        if in_degree[p] == 0: # add all new top-level nodes to `queue`
          queue.append(p)

    # If not all the letters are in the output, there must be a cycle
    if len(output) < len(in_degree):
        return ''

    return ''.join(output) # return a string
