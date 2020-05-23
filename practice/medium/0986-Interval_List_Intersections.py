class Solution:
  def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    # while A and B both still have elements
    # a = A.top, b = B.top
    # if any part of a is contained by b, add to result, a = A.top
    # vice versa for b
    # if there is no overlap, pop the smaller of the 2

    # reverse for quick push/pop
    A = list(reversed(A))
    B = list(reversed(B))
    output = []

    while len(A) > 0 and len(B) > 0:
      a = A.pop()
      b = B.pop()

      # case 1: a starts before b, b ends after a
      # A: [   ] 2,3
      # B:   [    ] 1,5
      if a[0] < b[0] and a[1] < b[1] and a[1] >= b[0]:
        output.append([b[0], a[1]])
        B.append(b)
            
      # case 2: b starts before a, a ends after b
      # A:   [    ]
      # B: [   ]
      elif b[0] < a[0] and b[1] < a[1] and b[1] >= a[0]:
        output.append([a[0], b[1]])
        A.append(a)
            
      # case 3: a completely contains b
      # A: [    ]
      # B:   [] 
      elif a[0] <= b[0] and a[1] >= b[1]:
        output.append(b)
        A.append(a)
            
      # case 4: b completely contains a
      # A:   []
      # B: [    ]
      elif b[0] <= a[0] and b[1] >= a[1]:
        output.append(a)
        B.append(b)
            
      # case 5: there was no overlap
      # remove the interval that is closer to 0
      # A: [  ]
      # B:     [  ]
      else:
        if a[0] < b[0]:
          B.append(b)
        else:
          A.append(a)

    return output
