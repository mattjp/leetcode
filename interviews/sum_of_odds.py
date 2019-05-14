# Add all odd numbers from 1 to A

def solution(A):
  D = {}
  for a in A:
    if a not in D:
      D[a] = 1
    else:
      D[a] += 1
  r = 0
  for k, v in D.items():
    r += (v * (v-1)) / 2
  return int(r)
