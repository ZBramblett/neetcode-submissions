class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if b == "(" or b == "[" or b == "{":
                stack.append(b)
            elif (b == ")" or b == "]" or b == "}") and len(stack) == 0:
                return False
            elif len(stack) > 0:
                if b == ")" and stack.pop() != "(":
                    return False
                elif b == "]" and stack.pop() != "[":
                    return False
                elif b == "}" and stack.pop() != "{":
                    return False

        if len(stack) == 0:
            return True
        else:
            return False


        
        
            