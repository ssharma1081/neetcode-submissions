class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        windowStart = 0
        res = 0
        for windowEnd in range(len(s)):
            if s[windowEnd] in seen:
                while windowStart <= windowEnd and s[windowStart] != s[windowEnd]:
                    seen.remove(s[windowStart])
                    windowStart += 1
                windowStart += 1
                # seen.remove(s[windowStart])
            seen.add(s[windowEnd])
            res = max(res, windowEnd - windowStart + 1)
        return res