import tkinter as tk
from tkinter import *
import time
import numpy as np
from Sudoku import Sudoku

class Gui:
    def __init__(self, sudoku_matrix, root):
        self.sudoku_matrix = sudoku_matrix
        self.textbox_sudoku_matrix =  np.ndarray(shape=(9, 9)).astype('object')
        self.root = root
        self.sudoku = Sudoku()
        self.lbl_check = self.label()
        self.entry_matrix = np.ndarray(shape=(9, 9)).astype(tk.Entry)

    def label(self):
        label = Label(self.root, relief=RAISED)
        label.grid(row=1, column=10)
        return label

    def callback(self, var):
        value = var.get()
        index = np.where(self.textbox_sudoku_matrix == str(var))
        row = index[0][0]
        col = index[1][0]

        if value.isnumeric():
            if int(value) not in range(1, 10):
                self.entry_matrix[row][col].delete(0)
                value = value[len(value) - 1]

            if self.sudoku.check_sudoku_validate(self.sudoku_matrix, row=row, col=col, number=int(value)):
                self.sudoku_matrix[row][col] = value
                self.lbl_check.config(bg="#32ba60", fg='#fafafa', font=('Arial', 16, 'bold'))
                self.entry_matrix[row][col].config(bg="green", fg='#fafafa')
                self.lbl_check['text'] = "Number is valid"

            elif self.entry_matrix[row][col] != 0:
                self.lbl_check.config(bg="#cf2b2b", fg='#fafafa', font=('Arial', 16, 'bold'))
                self.entry_matrix[row][col].config(bg="red", fg='#fafafa')
                self.lbl_check['text'] = "Number is not valid"
        else:
            self.entry_matrix[row][col].delete(0)


    def create_table(self, root, sudoku_matrix):
        for row in range(len(sudoku_matrix)):
            for col in range(len(sudoku_matrix[0])):
                var = StringVar()
                self.textbox_sudoku_matrix[row][col] = str(var)
                var.trace("w", lambda name, index, mode, var=var: self.callback(var))
                e = Entry(root, width=3, fg='blue',
                               font=('Arial', 16, 'bold'), textvariable=var, justify="center")

                e.grid(row=row, column=col)
                if sudoku_matrix[row][col] == 0:
                    e.config(bg="#000000", fg="white")
                    e.insert(END, '')
                else:
                    e.insert(END, sudoku_matrix[row][col])

                self.entry_matrix[row][col] = e