class Solution:
  def getRow(self, rowIndex: int) -> List[int]:

    # sum the previous row
    def create_row(prev_row):
      row = [1]
      for i in range(1, len(prev_row)):
        row.append(prev_row[i] + prev_row[i-1])
      row.append(1)
      return row

    # update `row` with the newly calculated row
    row = [1]
    for i in range(1, rowIndex+1):
      row = create_row(row)

    return row
