class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        combination = []

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

        def findCombo(i, current):
            if len(current) == len(digits):
                combination.append(current)
                return
            for c in mapOfNums[digits[i]]:
                findCombo(i + 1, current + c)

        if digits:
            findCombo(0,"")

        return combination

