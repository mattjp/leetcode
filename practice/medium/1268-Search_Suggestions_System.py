class Solution:
  def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    """
    keep all products that match searchWord, thus far
    remove words from search space that do not match the 
    current searchWord prefix
    """
    relevant = sorted(products)
    output = []
    for i,ch in enumerate(searchWord):
      updated = []
      for r in relevant:
        if i < len(r) and r[i] == ch:
          updated.append(r)
      output.append(updated[:3])
      relevant = updated
      
    return output
