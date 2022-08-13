class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        from collections import defaultdict
        
        invalid = defaultdict(int)
        times = {}  # time -> name -> cities
        
        # create the map of time, name, cities
        for transaction in transactions:
            t = transaction.split(',')
            name = t[0]
            time = int(t[1])
            amnt = int(t[2])
            city = t[3]

            if time not in times:
                times[time] = {}
            if name not in times[time]:
                times[time][name] = set()
                
            times[time][name].add(city)

        # find invalid transactions
        for transaction in transactions:
            tr = transaction.split(',')
            name = tr[0]
            time = int(tr[1])
            amnt = int(tr[2])
            city = tr[3]
            
            s = ','.join([name,str(time),str(amnt),city])
            
            # duh
            if amnt > 1000:
                invalid[s] += 1
                continue
            
            # check invalid time range
            for t in range(time-60, time+61):
                # there was a transaction at this time
                if t in times:
                    # if it was not made by this person, we don't care
                    if name not in times[t]:
                        continue
                    # if there were multiple cities at this time or the city 
                    # in the current transaction was not the same city
                    if len(times[t][name]) > 1 or city not in times[t][name]:
                        invalid[s] += 1
                        break
        
        # unpack
        res = []
        for k,v in invalid.items():
            for _ in range(v):
                res.append(k)
                
        return res
