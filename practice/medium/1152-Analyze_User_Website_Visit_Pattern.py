class Solution:
  def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
    from collections import Counter, defaultdict
    from itertools import combinations
    
    # sort by timestamp, so we don't have to use BSTs
    data = sorted(zip(username, timestamp, website), key=lambda x: x[1])
    
    # load websites in consecutive order for each user
    user_data = defaultdict(list)
    for u,_,w in data:
      user_data[u].append(w)
    
    # find 3-sequences for each user
    three_seqs = []
    for d in user_data.values():
      n = len(d)
      if n < 3:
        continue
      three_seqs.extend(list(set(combinations(d, 3)))) # list(set(...)) in order to de-dupe

    # counter.most_common() returns list of tuples: ((3-seq), count)
    # sort primarily by count, then lexicographically
    # negative because sorting in Python is always min-first
    counter = Counter(three_seqs)
    most_visited = sorted(counter.most_common(), key=lambda x: (-x[1], x[0]))
    return most_visited[0][0]
