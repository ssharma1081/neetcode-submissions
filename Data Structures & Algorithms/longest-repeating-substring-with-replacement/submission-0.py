class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        n = len(s)
        res = 0
        for c in charSet:
            l = 0
            count = 0
            for r in range(n):
                if c == s[r]:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                res = max(res, r - l + 1)
        return res
