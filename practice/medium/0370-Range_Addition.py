class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        """
        Update: [start, end, amt]
        
        [0,0,0,0,0]
        [0,2,0,0,-2]
        [0,2,3,0,-2]
        [-2,2,3,2,-2] => [-2, 0, 3, 5, 3]
                        
        
        """
        
        arr = [0] * length
        
        # too slow, how sad
#         for start, end, inc in updates:
#             start = max(0, start)
#             end = min(length, end+1)
#             for i in range(start, end):
#                 arr[i] += inc
#         return arr


        for start, end, inc in updates:   
            # increment only the start index
            arr[start] += inc
            
            # decrement 1 past the end index (if it is within the array boundary)
            end +=1
            if end < len(arr):
                arr[end] -= inc

        # set each index equal to the cumulative sum at that point
        for a in range(1, len(arr)):
            arr[a] += arr[a-1]
        
        return arr
            
        
