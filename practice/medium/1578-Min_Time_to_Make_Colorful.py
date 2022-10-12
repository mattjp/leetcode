class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        """
        Use stack, {color, time}
        If next color matches color on top of stack, add smaller of 2 times to answer
        """
        
        cost = 0
        stack = [[colors[0], neededTime[0]]]
        
        for color, time in zip(list(colors)[1:], neededTime[1:]):
            if stack[-1][0] == color:
                tmin = min(stack[-1][1], time)
                tmax = max(stack[-1][1], time)
                stack[-1][1] = tmax  # Never remove the color with the highest cost
                cost += tmin  # Always remove the smaller of the 2 costs
            else:
                stack.append([color, time])
                
        return cost
