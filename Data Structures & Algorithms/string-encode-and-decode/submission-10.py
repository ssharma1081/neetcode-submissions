class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            freq = ''
            j = i
            while j < len(s) and s[j] != '#':
                freq += s[j]
                j += 1
            word = s[j + 1: j + 1 + int(freq)]
            res.append(word)
            i = j + int(freq) + 1
            
        
        return res
