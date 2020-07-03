class Solution:
  def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
    cells_old = cells
    cells_new = []        
    seen = set()
    cell_order = [] 

    # repr() gets the string reprsentation of the list
    # iterate until a loop is found
    while repr(cells_old) not in seen:
      seen.add(repr(cells_old))
      cell_order.append(cells_old)

      # find the new cell arrangement
      cells_new.append(0)
      for i in range(1, len(cells_old)-1):
        if cells_old[i-1] == cells_old[i+1]: cells_new.append(1)
        else: cells_new.append(0)
      cells_new.append(0)

      # copy over and repeat
      cells_old = cells_new
      cells_new = []

    # subtract the first `m` cell orderings that are not part of the loop
    to_subtract = 0
    while cell_order:
      if cell_order[0] != cells_old:
        cell_order.pop(0)
        to_subtract += 1
      else: break

    # after the initial `m` cells are gone, we take the index of the modulo of the 
    # remaining cells, since we're just going around in a loop
    n = N - to_subtract
    return cell_order[n % len(cell_order)]
