class Solution:
  def findAnagrams(self, s: str, p: str) -> List[int]:
    from collections import Counter

    output = []
    seen_invalids = set()
    p_counter = Counter(p)
    j = len(p)
    i = 0
    prev_was_anagram = False
    
    while i < len(s)-j+1:
      current = s[i:j+i]
      if i not in output: # don't double up on outputs
        current_counter = Counter(current)
        if hash(tuple(current_counter)) not in seen_invalids:
          if current_counter == p_counter:
            prev_was_anagram = True
            output.append(i)
          else:
            seen_invalids.add(hash(tuple(current_counter)))
            if prev_was_anagram:
              if current[-1] not in p_counter: # if newly added letter never appears in `p`
                i = j-1                        # skip all possible solutions with that letter
              prev_was_anagram = False
      i += 1

    return output
