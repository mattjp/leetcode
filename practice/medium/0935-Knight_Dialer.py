class Solution:
    def knightDialer(self, n: int) -> int:
        
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            # 5: [],  # who cares about 5
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        
        def count_sequences(start_position, num_hops):
            cache = {}

            def helper(position, num_hops):
                if (position, num_hops) in cache:
                    return cache[(position, num_hops)]

                elif num_hops == 0:
                    return 1

                else:
                    num_sequences = 0
                    for neighbor in moves[position]:
                        num_sequences += helper(neighbor, num_hops - 1)

                    cache[(position, num_hops)] = num_sequences
                    return num_sequences
                
            res = helper(start_position, num_hops)
            return res
            
        if n == 1:
            return 10
        
        else:
            result = 0
            for position in moves.keys():
                result += count_sequences(position, n-1)
                
            return (result % 1_000_000_007)
