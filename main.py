from tkinter import *
import time
import numpy as np
from Sudoku import Sudoku
from Gui import Gui

if __name__ == "__main__":

    sudoku = Sudoku()
    sudoku_matrix = sudoku.create_sudoku_empty_some_cells()

    root = Tk()
    gui = Gui(sudoku_matrix, root)
    gui.create_table(root, sudoku_matrix)

    root.mainloop()

