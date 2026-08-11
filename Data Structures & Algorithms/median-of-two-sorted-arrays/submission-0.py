class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N = len(nums1) + len(nums2)
        
        ptr1 = 0
        ptr2 = 0

        i = 0

        res = []
        
        while i <= N // 2:

            num1 = float('inf')
            num2 = float('inf')
            
            if ptr1 < len(nums1):
                num1 = nums1[ptr1]

            if ptr2 < len(nums2):
                num2 = nums2[ptr2]

            if num1 <= num2 and num1 != float('inf'):
                ptr1 += 1
                mins = num1
            elif num2 < num1 and num2 != float('inf'):
                ptr2 += 1
                mins = num2

            if mins == float('inf'):
                break

            res.append(mins)

            i += 1
        median = 0
        if N % 2 == 0:
            median = (res[-1] + res[-2]) / 2
        else:
            median = res[-1]

        return median
        