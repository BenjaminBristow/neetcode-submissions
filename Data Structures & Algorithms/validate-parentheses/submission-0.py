class Solution:
    def isValid(self, s: str) -> bool:
        opposite ={"}":"{", "]":"[", ")":"("}
        stack = []
        
        for char in s:
            if len(stack) == 0:
                if char not in opposite.values():
                    return False
                else:
                    stack.append(char)
                    continue

            if char in opposite.keys():
                if opposite[char] == stack[-1]:
                    stack.pop()
                    continue
                else:
                    return False
            
            else:
                stack.append(char)

        if len(stack) == 0: 
            return True 
        else: 
            return False

            
            