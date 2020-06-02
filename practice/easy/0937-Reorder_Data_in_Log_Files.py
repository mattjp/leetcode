class Solution:
  def reorderLogFiles(self, logs: List[str]) -> List[str]:
    digs = []
    lets = []

    # sort key can take tuples to serve as tie-breakers
    def sort_letter_logs(s: str):
      space = s.find(' ')
      return (s[space:], s[:space])

    for log in logs:
      l = log.split(' ')
      if l[1].isnumeric():
        digs.append(log)
      else:
        lets.append(log)

    # nasty anonymous function
    # lets_sorted = sorted(lets, key=lambda x: (x[x.find(' '):], x[:x.find(' ')]))
    
    lets_sorted = sorted(lets, key=sort_letter_logs)
    return lets_sorted + digs
