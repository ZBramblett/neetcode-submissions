class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        mapOfNums = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def backTrack(i, current):
            if len(current) == len(digits):
                res.append(current)
                return
            
            for n in mapOfNums[digits[i]]:
                backTrack(i + 1, current + n)
            
        if digits:
            backTrack(0, "")
        
        return res