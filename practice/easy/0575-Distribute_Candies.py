class Solution:
  def distributeCandies(self, candies: int, num_people: int) -> List[int]:
    people = [0] * num_people
    p = 0
    c = 1

    while candies > 0:
      people[p] += min(c, candies)
      candies -= c
      c += 1
      p = (p+1) % num_people
    return people
