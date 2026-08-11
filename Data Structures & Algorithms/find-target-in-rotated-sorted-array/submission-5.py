[3,4,5,1,2]

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        pivot = -1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                # left half
                l = mid + 1

            else:
                # right half
                r = mid

        if target >= nums[l] and target <= nums[-1]:
            r = len(nums) - 1
        else : 
            r = l - 1 if l > 0 else 0
            l = 0

        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                res = mid
                break
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return res

        