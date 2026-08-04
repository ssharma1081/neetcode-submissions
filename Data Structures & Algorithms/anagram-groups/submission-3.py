class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stored = defaultdict(list)
        for word in strs:
            freqMap = [0] * 26
            for ch in word:
                freqMap[ord(ch) - ord('a')] += 1
            stored[str(freqMap)].append(word)
        return list(stored.values())


