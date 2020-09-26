class Solution:
  def minMutation(self, start: str, end: str, bank: List[str]) -> int:
    from collections import deque
    
    if end not in bank:
      return -1
    
    if start == end:
      return 0
    
    queue = deque([(start, 0)]) # gene_str, steps
    seen = set(start)
    
    while queue:
      
      gene_str, steps = queue.popleft()
      
      for i in range(len(gene_str)):
        for gene in ['A', 'C', 'T', 'G']:
          mutation = gene_str[:i]+gene+gene_str[i+1:]
          if mutation in bank and mutation not in seen:
            if mutation == end:
              return steps+1
            seen.add(mutation)
            queue.append((mutation, steps+1))
          
    
    return -1
