class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        mp = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: math.trunc(a / b)
        }
        for token in tokens:
            if token in mp:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = mp[token](operand1, operand2)
                stack.append(result)
            else:
                stack.append(int(token))
            
        return stack[-1]
