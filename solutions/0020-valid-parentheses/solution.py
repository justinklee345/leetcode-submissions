class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == ')' or c == ']' or c == '}':
                if len(stack) != 0:
                    if stack[-1] == '(' and c == ')':
                        stack.pop()
                    elif stack[-1] == '[' and c == ']':
                        stack.pop()
                    elif stack[-1] == '{' and c == '}':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(c)
        if len(stack) == 0:
            return True
        return False
            
