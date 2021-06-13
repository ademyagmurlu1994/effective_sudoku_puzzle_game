import numpy as np
import random as rnd
import utils


class Sudoku:
    def __init__(self):
        pass

    def create_sudoku_full_filled(self):
        main_matrix = utils.create_random_matrix()
        sudoku_matrix = np.zeros((9, 9)).astype("int")

        for row in range(3):
            for col in range(3):
                if col == 0:
                    sudoku_matrix[row * 3: row * 3 + 3, col * 3: col * 3 + 3] = main_matrix
                else:
                    sudoku_matrix[row * 3: row * 3 + 3, col * 3: col * 3 + 3] = np.roll(main_matrix, -col,
                                                                                        axis=0)  # left shift
            main_matrix = np.roll(main_matrix, -1, axis=1)  # right shift

        return sudoku_matrix


    def create_sudoku_empty_some_cells(self):
        sudoku_matrix = self.create_sudoku_full_filled()
        for row in range(sudoku_matrix.shape[0]):
            cleaning_array = utils.create_random_array(4, range=(0, 8))  # some column for cleaning in rows
            for col in cleaning_array:
                sudoku_matrix[row][col] = 0  # 0: clean (empty) cell
        return sudoku_matrix


    def control3x3(self, matrix, start_row, start_col, number) -> bool:
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if matrix[r][c] == number:
                    return False
        return True

    def control9x1(self, matrix, row, col, number) -> bool:
        for index in range(0, 9):
            if matrix[row][index] == number or matrix[index][col] == number:
                return False  # sayı var
        return True


    def check_sudoku_validate(self, sudoku_matrix: np.ndarray, col: int, row: int, number: int) -> bool:
        start_row = int(row / 3) * 3  # start row for detect 3x3 matrix
        start_col = int(col / 3) * 3  # start col for detect 3x3 matrix
        if self.control3x3(sudoku_matrix, start_row, start_col, number):
            if self.control9x1(sudoku_matrix, row, col, number):
                return True
            else:
                return False
        else:
            return False


