from cell import Cell
from sudoku_generator import SudokuGenerator


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        # initialize board with SudokuGenerator class
        sudoku = SudokuGenerator(30)
        sudoku.fill_values()
        sudoku.remove_cells()
        board = sudoku.get_board()

        self.grid = [[Cell(board[row][col], row, col, screen) for col in range(9)] for row in range(9)]
        self.selected_row = None
        self.selected_col = None

    def draw(self):
        # Draw the background of the board
        self.screen.fill((255, 255, 255))

        # Draw the cells in the grid
        for row in range(9):
            for col in range(9):
                cell = self.grid[row][col]
                cell.draw()

    def select(self, row, col):
        # unselects any previously selected cell
        if (self.selected_row is not None) and (self.selected_col is not None):
            self.grid[self.selected_row][self.selected_col].selected = False

        # select the new cell
        self.selected_row = row
        self.selected_col = col
        self.grid[self.selected_row][self.selected_col].selected = True

    def click(self, x, y):
        if x < 0 or y < 0 or x > self.width * 50 or y > self.height * 50:
            return None
        row = y // 50
        col = x // 50
        return (row, col)

    def clear(self):
        # first checks if a cell is selected. If no cell is selected, it does nothing.
        if (self.selected_row is not None) and (self.selected_col is not None):
            cell = self.grid[self.selected_row][self.selected_col]
            if cell.value == 0 and cell.sketch == 0:
                return
            """checks whether it has a value or a sketched value. if yes, value is set
            to 0 to clear it. if its a sketched value, sketch val is set to 0 to clear"""
            if cell.value != 0:
                cell.set_cell_value(0)
            if cell.sketch != 0:
                cell.set_cell_value(0)

    def sketch(self, value):
        if self.selected:
            self.grid[self.selected_row[0]][self.selected_col[1]].sketch = value

    def place_number(self, value):
        if self.selected:
            cell = self.grid[self.selected_row[0]][self.selected_col[1]]
            if not cell.original:
                cell.value = value
                cell.sketch = None

    def reset_to_original(self):
        for row in self.grid:
            for cell in row:
                cell.sketch = cell.value

    def is_full(self):
        for row in self.grid:
            for cell in row:
                if cell.value == 0:
                    return False
        return True

    def update_board(self):
        for row in self.grid:
            for cell in row:
                cell.update_value()

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col].value == 0:
                    return (row, col)
        return None

    def check_board(self):  # class method holds copy of the solved sudoku for the current round
        solution = SudokuGenerator.get_solution()  # resets after each generate_sudoku call
        for row in self.grid:
            for cell in row:
                if cell.sketch != solution[cell.col][cell.row]:
                    return False
        return True
