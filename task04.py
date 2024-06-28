import tkinter as tk
from tkinter import messagebox

class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.root.configure(bg='lightgray')  # Set background color
        self.board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        self.entries = [[None]*9 for _ in range(9)]
        self.create_grid()
        self.display_grid()

    def create_grid(self):
        for row in range(9):
            for col in range(9):
                entry = tk.Entry(self.root, width=5, justify='center', font=('Arial', 18), bg='lightblue')  # Set entry background color
                entry.grid(row=row, column=col, padx=1, pady=1, sticky='nsew')
                self.entries[row][col] = entry

        solve_button = tk.Button(self.root, text="Solve", command=self.solve_sudoku, bg='lightgreen')  # Set button background color
        solve_button.grid(row=9, column=0, columnspan=9, pady=20)
        
        clear_button = tk.Button(self.root, text="Clear", command=self.clear_grid, bg='lightcoral')  # Set button background color
        clear_button.grid(row=10, column=0, columnspan=9, pady=10)

    def clear_grid(self):
        for row in range(9):
            for col in range(9):
                self.entries[row][col].delete(0, tk.END)

    def read_grid(self):
        for row in range(9):
            for col in range(9):
                value = self.entries[row][col].get()
                self.board[row][col] = int(value) if value else 0

    def display_grid(self):
        for row in range(9):
            for col in range(9):
                self.entries[row][col].delete(0, tk.END)
                if self.board[row][col] != 0:
                    self.entries[row][col].insert(0, str(self.board[row][col]))

    def solve_sudoku(self):
        self.read_grid()
        if self.solve():
            self.display_grid()
        else:
            messagebox.showinfo("Sudoku Solver", "No solution exists for the given puzzle.")

    def solve(self):
        empty = self.find_empty_location()
        if not empty:
            return True
        row, col = empty

        for num in range(1, 10):
            if self.is_safe(num, row, col):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = 0
        return False

    def find_empty_location(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return (row, col)
        return None

    def is_safe(self, num, row, col):
        # Check row
        if any(self.board[row][x] == num for x in range(9)):
            return False
        # Check column
        if any(self.board[x][col] == num for x in range(9)):
            return False
        # Check 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        if any(self.board[i][j] == num for i in range(start_row, start_row + 3) for j in range(start_col, start_col + 3)):
            return False
        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolver(root)
    root.mainloop()
