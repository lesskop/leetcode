class Solution:
    def valid_digits(self, line: list[str]) -> bool:
        line = [int(num) for num in line if num != '.']
        return len(set(line)) == len(line)

    def valid_rows(self, board: list[list[str]]) -> bool:
        for row in board:
            if not self.valid_digits(row):
                return False
        return True

    def valid_columns(self, board: list[list[str]]) -> bool:
        for col in [list(column) for column in zip(*board)]:
            if not self.valid_digits(col):
                return False
        return True

    def valid_boxes(self, board: list[list[str]]) -> bool:
        boxes = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                boxes.append(box)

        for box in boxes:
            if not self.valid_digits(box):
                return False
        return True

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        if self.valid_rows(board) and self.valid_columns(board) and self.valid_boxes(board):
            return True
        else:
            return False
