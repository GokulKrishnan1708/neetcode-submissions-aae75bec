class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for cell in row:
                if cell == '.':
                    continue
                if cell in seen: 
                    return False
                seen.add(cell)
        for column in range(9):
            seen = set()
            for row in range(9):
                cell = board[row][column]
                if cell == '.':
                    continue
                if cell in seen:
                    return False
                seen.add(cell)
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        cell = board[box_row +i][box_col + j]
                        if cell == '.':
                            continue
                        if cell in seen:
                            return False
                        seen.add(cell)
        return True