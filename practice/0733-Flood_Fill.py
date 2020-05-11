class Solution:
  def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    from copy import copy
    max_r = len(image)
    max_c = len(image[0])
    mod_img = copy(image)
    colored = set()
    target = image[sr][sc]
    pixels = [(sr, sc)]
    while len(pixels) > 0:
      (r,c) = pixels.pop()
      if (r,c) not in colored:
        mod_img[r][c] = newColor
        colored.add((r,c))
        if r-1 >= 0 and (r-1,c) not in colored and image[r-1][c] == target:
          pixels.append((r-1,c))
        if r+1 < max_r and (r+1,c) not in colored and image[r+1][c] == target:
          pixels.append((r+1,c))
        if c-1 >= 0 and (r,c-1) not in colored and image[r][c-1] == target:
          pixels.append((r,c-1))
        if c+1 < max_c and (r,c+1) not in colored and image[r][c+1] == target:
          pixels.append((r,c+1))
    return mod_img
