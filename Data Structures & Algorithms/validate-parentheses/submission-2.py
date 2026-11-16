class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        clsToOpn = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        for itm in s:
            if itm in clsToOpn:
                if stack and stack[-1] == clsToOpn[itm]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(itm)
        return True if not stack else False