class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        open = {'{', '(', '['}

        stack = []

        for c in s:
            if c not in open:
                if len(stack) > 0:
                    popped = stack.pop()
                    if popped != mp[c]:
                        return False
                else:
                    return False
            else:
                stack.append(c)
            
        return len(stack) == 0
