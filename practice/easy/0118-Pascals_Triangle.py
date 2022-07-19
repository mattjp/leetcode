class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        def go(row):
            if row == 1:
                return [[1]]
            elif row == 2:
                return [[1], [1, 1]]
            else:
                result = go(row-1)
                prev_row = result[-1]
                new_row = [1]
                for i in range(1, len(prev_row)):
                    new_row.append(prev_row[i-1] + prev_row[i])
                new_row.append(1)
                result.append(new_row)
                return result
            
        return go(numRows)
