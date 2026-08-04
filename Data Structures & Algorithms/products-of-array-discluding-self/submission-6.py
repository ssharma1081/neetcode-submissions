class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * (len(nums))
        right = [0] * (len(nums))

        prev = 1
        for i in range(0, len(left)):
            left[i] = nums[i] * prev
            prev = left[i]

        prev = 1
        for i in range(len(right) - 1, -1, -1):
            right[i] = nums[i] * prev
            prev = right[i]
        
        res = [0] * len(nums)

        for i in range(0, len(nums)):
            if i == 0:
                res[i] = right[i + 1]
                continue
            if i == len(nums) - 1:
                res[i] = left[i - 1]
                continue
            res[i] = left[i - 1] * right[i + 1]
        
        return res