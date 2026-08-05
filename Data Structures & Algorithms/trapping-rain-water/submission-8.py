class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        n = len(height)
        res = 0
        for i in range(0, n):
            while stack and height[i] >= height[stack[-1]]:
                mid = height[stack.pop()]
                if stack:
                    right = height[i]
                    left = height[stack[-1]]
                    width = i - stack[-1] - 1
                    h = min(right, left) - mid
                    res += h * width
            stack.append(i)
        return res