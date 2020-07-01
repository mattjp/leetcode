class Solution:
  def partitionLabels(self, S: str) -> List[int]:
    #    ababcbacadefegdehijhklij
    # a: |-------|                [0,8]
    # b:  |---|                   [1,5]
    # c:     |--|                 [4,7] 
    # d:          |----|          [9,14]
    # e:           |----|         [10,15]
    # f:            |             [11,11]
    # g:              |           [13,13]
    # h:                 |--|     [16,19]
    # i:                  |----|  [17,22]
    # j:                   |----| [18,23]
    # k:                     |    [20,20]
    # l:                      |   [21,21]

    seen = set()
    segments = []
    S_reversed = S[::-1]

    for i,ch in enumerate(S):
      if ch not in seen:
        j = len(S) - 1 - S_reversed.index(ch) # find last index of the given char
        segments.append([i,j])
        seen.add(ch)

    output = [segments.pop(0)]
    while segments:
      top = segments.pop(0)
      if top[0] > output[-1][1]:
        output.append(top) # no overlap, therefore end of the current segment
      else:
        output[-1][1] = max(output[-1][1], top[1]) 

    return list(map(lambda x: x[1]-x[0]+1, output)) # return the lengths of the segments
