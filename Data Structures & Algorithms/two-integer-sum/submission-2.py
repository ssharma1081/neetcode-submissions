class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stored = {}
        for (i, num) in enumerate(nums):
            if (target - num) in stored:
                return [stored[target - num], i]
            stored[num] = i
