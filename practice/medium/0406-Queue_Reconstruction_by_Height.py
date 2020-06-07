class Solution:
  def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
    # sort shortest to tallest, with ties being broken by a larger
    # p[1] (number of people in front) value
    # this is so when the second sort happens, we know the p[1] = 0
    # people are in the right spot already
    queue = sorted(people, key=lambda p: (p[0], -p[1]))

    # iterate backwards through the queue
    i = len(queue)-1
    while i >= 0:
      person = queue[i]
      # if there are no people with height >= in front of this person
      # we can assume they're in the correct location
      if person[1] != 0:
        # move this person back the number of spots in line equal to the
        # number of people with height >= this person
        queue.insert(1+i+person[1], person)
        queue.pop(i)
      i -= 1

    return queue
