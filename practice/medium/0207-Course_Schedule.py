class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

    # build dependency graph
    dependencies = {}
    for u,v in prerequisites:
      if u not in dependencies:
        dependencies[u] = []    
      dependencies[u].append(v)

    # check if it's possible to take a single class
    def possible(current: int, seen) -> bool:
      # cycle detected
      if current in seen:
          return False

      # course has no dependencies
      if current not in dependencies:
          return True

      # add this class to pre-requiste list for the current class
      seen.add(current)

      # for each dependency check its validity
      for i in dependencies[current]:
        if not possible(i, seen):
          return False
        if i in seen:
          seen.remove(i)
      return True


    return all(possible(i, set()) for i in range(numCourses))
