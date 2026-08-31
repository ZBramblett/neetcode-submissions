class Solution:
    def isValid(self, s: str) -> bool:
        #Need a hashmap to map the correct opening and closing brackets
        #Need a stack to keep track of the most recently seen open brack

        stack = []
        hashmap = {")": "(", "]": "[", "}": "{"}

        for bracket in s:
            if bracket in hashmap:
                if stack and stack[-1] == hashmap[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return True if not stack else False

        

            