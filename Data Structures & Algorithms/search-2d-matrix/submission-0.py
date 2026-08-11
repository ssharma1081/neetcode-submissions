class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix)
        row = -1
        for i in range(rows):
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                row = i
                break;
        
        if row == -1:
            return False

        l = 0
        r = len(matrix[row]) - 1

        while l <= r:
            m = l + (r - l) // 2
            el = matrix[row][m]
            if el == target:
                return True
            elif target < el:
                r = m - 1
            else:
                l = m + 1

        return False
