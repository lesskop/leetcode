class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """Do not return anything, modify board in-place instead."""

        def find_empty_cell() -> tuple[int, int] | None:
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        return row, col

            return None

        def value_is_valid(value: int, row: int, col: int) -> bool:
            row_ok = all(str(value) != board[row][j] for j in range(9))
            if not row_ok:
                return False

            col_ok = all(str(value) != board[i][col] for i in range(9))
            if not col_ok:
                return False

            box_row, box_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    if str(value) == board[i][j]:
                        return False

            return True

        def backtrack() -> bool:
            empty_cell = find_empty_cell()
            if empty_cell is None:
                return True

            row, col = empty_cell

            for value in range(1, 10):
                if value_is_valid(value, row, col):
                    board[row][col] = str(value)

                    if backtrack():
                        return True

                    board[row][col] = '.'

            return False

        backtrack()
