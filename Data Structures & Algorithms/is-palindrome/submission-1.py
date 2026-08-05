class Solution:
    def isPalindrome(self, s: str) -> bool:
        head = 0
        tail = len(s) - 1
        while head <= tail:
            if not s[head].isalnum():
                head += 1
                continue
            if not s[tail].isalnum():
                tail -= 1
                continue
            print(s[head])
            print(s[tail])
            if s[head].lower() != s[tail].lower():
                return False
            head += 1
            tail -= 1
        return True
