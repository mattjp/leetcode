class SnakeGame:

  def __init__(self, width: int, height: int, food: List[List[int]]):
    """
    Initialize your data structure here.
    @param width - screen width
    @param height - screen height 
    @param food - A list of food positions
    E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
    """
    from collections import deque
    self.w = width
    self.h = height
    self.foods = deque(food)
    self.snake = deque([(0,0)]) # snake and invalid could have been an OrderedDict
    self.invalid = set([(0,0)])
    self.score = 0


  def move(self, direction: str) -> int:
    """
    Moves the snake.
    @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
    @return The game's score after the move. Return -1 if game over. 
    Game over when snake crosses the screen boundary or bites its body.
    """

    # this is straight-up awful
    head = self.snake[0]
    new_head = (head[0], head[1])
    if direction == 'U':
      new_head = (new_head[0]-1, new_head[1])
    elif direction == 'L':
      new_head = (new_head[0], new_head[1]-1)
    elif direction == 'R':
      new_head = (new_head[0], new_head[1]+1)
    else:  
      new_head = (new_head[0]+1, new_head[1])

    # check boundaries
    if (
      self.h <= new_head[0] or
      new_head[0] < 0 or 
      self.w <= new_head[1] or 
      new_head[1] < 0
    ):
      return -1

    # eat food, if there is food
    # if no food, remove the tail because the snake does not grow
    if self.foods and new_head == tuple(self.foods[0]):
      self.foods.popleft()
      self.score += 1
    else:
      tail = self.snake.pop()
      self.invalid.remove(tail)

    # see if the head ran into the body
    # this check has to happen after the tail is appended to simulate simultaneous movement
    if new_head in self.invalid:
      return -1

    # add the new head and return score
    self.snake.appendleft(new_head)
    self.invalid.add(new_head)
    return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
