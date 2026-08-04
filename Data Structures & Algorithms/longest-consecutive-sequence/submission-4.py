class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        
        store = defaultdict(int)
        res = 0

        for num in nums:
            if not store[num]:
            
                store[num] = store[num - 1] + store[num + 1] + 1

                store[num - store[num - 1]] = store[num]

                store[num + store[num + 1]] = store[num]

                res = max(res, store[num])

        return res
            