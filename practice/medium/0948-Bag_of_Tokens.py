class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        """
        While our power > lowest token, play that token, gain 1 score
        Save highest score
        While we can't play any more tokens, flip the token with the highest power
        
        I think we can do this with 2 pointers, if the array is sorted
        """
        
        tokens.sort()
        
        l = 0
        r = len(tokens)-1
        hi_score = 0
        cur_score = 0
        
        while l <= r:
            if tokens[l] <= power:
                power -= tokens[l]
                cur_score += 1
                hi_score = max(hi_score, cur_score)
                l += 1
            elif cur_score > 0:
                power += tokens[r]
                cur_score -= 1
                r -= 1
            else:
                return hi_score
            
        return hi_score
        
