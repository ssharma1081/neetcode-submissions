class Solution:
    def findMin(self, nums: List[int]) -> int:
        # the most important thing here is to break out of the loop
        [5,6,1,2,3,4]
        l  = 0
        r = len(nums) - 1

        # array wasn't rotated
        if nums[0] <= nums[-1]: return nums[0]

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] < nums[0]:
                r = mid - 1
            else:
                l = mid + 1

