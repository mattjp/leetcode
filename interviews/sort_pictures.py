# Takes an array of "Pictures" with metadata and sorts them
# Format: ???

def tSort(t):
  return t[2]

def solution(S):
  L = S.split("\n")
  photos = {}
  index = 0
  res = [""] * len(L)

  for l in L:
    city = l.split(",")[1]
    l = l.split(",")
    l.append(index)
    if city not in photos:
      photos[city] = [l]
    else:
      photos[city].append(l)
    index += 1

  for k, v in photos.items():
    v.sort(key=tSort)
    for i, photo in enumerate(v):
      x = i+1
      if len(v) > 9 and len(v) < 100:
        if x < 10:
          x = "0" + str(x)
        elif len(v) > 99:
          if x < 10:
            x = "00" + str(x)
          elif x < 100:
            x = "0" + str(x)
      photo[0] = photo[1] + str(x) + "." + photo[0].split(".")[1]
      res[photo[3]] = photo[0]

  strRes = ""
  for r in res:
    strRes += r[1:] + "\n"

  return strRes
