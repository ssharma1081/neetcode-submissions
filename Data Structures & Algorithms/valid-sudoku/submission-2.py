class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # map of rowSets
        # map of colSets
        # map of boxSet
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        boxMap = defaultdict(set)

        m = len(board)
        n = len(board[0])

        for i in range(9):
            for j in range(9):
                el = board[i][j]
                if el == '.':
                    continue
                if el in rowMap[i] or el in colMap[j] or el in boxMap[i // 3, j // 3]:
                    return False
                
                rowMap[i].add(el)
                colMap[j].add(el)
                boxMap[i // 3, j // 3].add(el)

        return True