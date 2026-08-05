class Solution:
    # If heights[i] is smaller, then any future container using index i will have a smaller width, and its height is still at most heights[i]. So it cannot produce a larger area than the current pair. Therefore, we can safely discard the smaller height and move that pointer inward. The same logic applies when heights[j] is smaller.
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