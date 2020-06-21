class Solution:
  def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
    """
    start at bottom right
    establish minimum health for each room given previous rooms
    """

    self.max_i = len(dungeon)-1
    self.max_j = len(dungeon[0])-1
    self.min_hp = [[None for j in range(self.max_j+1)] for i in range(self.max_i+1)]

    for i in range(self.max_i, -1, -1):
      for j in range(self.max_j, -1, -1):
        room      = dungeon[i][j]
        room_min  = 1 if room >= 0 else abs(room)+1
        down      = self.min_hp[i+1][j] if i < self.max_i else float('inf')
        right     = self.min_hp[i][j+1] if j < self.max_j else float('inf')

        if down == right == float('inf'): # populate princess square
          self.min_hp[i][j] = room_min
        else:
          # always take path with smaller required health
          min_required = min(down, right)

          # we get more health in this room than is required to cover all damage
          if room >= min_required: 
            self.min_hp[i][j] = 1
          # we will either get some health (but not enough to cover all damage up to this point) or take damage
          else:
            # we get some health in this room
            if room > 0:
              self.min_hp[i][j] = min_required - room
            # we're taking damage in this room (or it's empty)
            else:
              # we only need 1 health to complete the next room
              if min_required == 1:
                self.min_hp[i][j] = room_min
              # we need more than 1 health to complete the next room
              else: 
                self.min_hp[i][j] = min_required - room

    return self.min_hp[0][0]
