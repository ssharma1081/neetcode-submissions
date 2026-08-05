class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        i = 0
        while i < n - 2:
            target = nums[i] * -1
            head = i + 1
            tail = n - 1
            while head < tail:
                sim = nums[head] + nums[tail]
                if sim == target:
                    res.append([nums[i], nums[head], nums[tail]])
                    while head + 1 < n and nums[head + 1] == nums[head]:
                        head += 1
                    head += 1
                    while tail - 1 > 0 and nums[tail - 1] == nums[tail]:
                        tail -= 1
                    tail -= 1
                elif sim < target:
                    while head + 1 < n and nums[head + 1] == nums[head]:
                        head += 1
                    head += 1
                elif sim > target:
                    while tail - 1 > 0 and nums[tail - 1] == nums[tail]:
                        tail -= 1
                    tail -= 1
            while i + 1 < n and nums[i + 1] == nums[i]:
                i += 1
            i += 1
        return res