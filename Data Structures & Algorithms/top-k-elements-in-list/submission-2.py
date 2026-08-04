class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        freqBucket = [[] for i in range(len(nums) + 1)]
        freqMap = Counter(nums)


        for num in freqMap:
            freqBucket[freqMap[num]].append(num)
        
        for j in range(len(freqBucket) - 1, -1, -1):
            if len(freqBucket[j]) > 0:
                for num in freqBucket[j]:
                    res.append(num)
                    if len(res) == k:
                        return res
        return res