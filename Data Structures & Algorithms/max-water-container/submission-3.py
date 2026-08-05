class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        head = 0
        tail = n - 1
        while head < tail:
            area = (tail - head) * min(heights[head], heights[tail])
            res = max(res , area)
            if heights[head] <= heights[tail]:
                head += 1
            else:
                tail -= 1
        return res