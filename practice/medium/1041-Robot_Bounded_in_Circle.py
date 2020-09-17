class Solution:
  def isRobotBounded(self, instructions: str) -> bool:
    """
    hypothesis - if robot does not return to (0,0) after max 4 iterations; return False
    turns out the hypothesis was correct.
    """
    
    directions = [[0,1], [1,0], [0,-1], [-1,0]] # up, right, down, left
    direction = 0
    robot = [0, 0]
    
    for i in range(4):
      for instruction in instructions:
        if instruction == 'G':
          robot = list(map(lambda x: x[0]+x[1], zip(robot, directions[direction]))) # add the 2 arrays
        elif instruction == 'L':
          direction = (direction-1) % 4 # modulus math: -1 % 4 = 3
        else:
          direction = (direction+1) % 4
          
      if robot == [0, 0]: # we've completed a loop after a full set of instructions
        return True
      
    return False
