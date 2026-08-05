class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        windowStart = 0
        mp = {}
        res = 0
        for windowEnd in range(n):
            ch = s[windowEnd]
            if ch in mp and mp[ch] >= windowStart:
                windowStart = mp[ch] + 1
            res = max(res, windowEnd - windowStart + 1)
            mp[ch] = windowEnd
        return res
            