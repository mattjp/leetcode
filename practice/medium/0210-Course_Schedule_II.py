class Solution:
  def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    for each course - build its prereq list
    if a course is invalid return []
    for each prereq in each prereq list - add to total list if it has not been added yet
    
    DFS - when all neighbors have been checked, add to final output
    leave nodes in a 'visited but not added' state to check if there is a cycle
    
    Do in-degree like Alien dictionary
    """  
    from collections import defaultdict, deque

    in_degree = {i: 0 for i in range(numCourses)}
    adj_matrix = defaultdict(list)
    for u,v in prerequisites:
      adj_matrix[v].append(u)
      in_degree[u] += 1
      
    queue = deque()

    for k,v in in_degree.items():
      if v == 0: 
        queue.append(k)
      
    output = []
    while queue:
      course = queue.popleft()
      output.append(course)
      in_degree.pop(course)
      for adj in adj_matrix[course]:
        in_degree[adj] -= 1
        if in_degree[adj] == 0:
          queue.append(adj)
      
    return output if len(in_degree) == 0 else []
