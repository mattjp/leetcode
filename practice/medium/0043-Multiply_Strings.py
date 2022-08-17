class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        result = 0
        
        for i, m in enumerate(reversed(num1)):
            x = int(m) * 10**i
            
            for j, n in enumerate(reversed(num2)):
                y = int(n) * 10**j
                result += (x * y)

                
        return str(result)
        
