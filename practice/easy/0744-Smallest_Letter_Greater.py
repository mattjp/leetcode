class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = 0
        while i < len(letters) and ord(letters[i]) <= ord(target):
            i += 1

        best = i if i < len(letters) else 0
        return letters[best]
        
