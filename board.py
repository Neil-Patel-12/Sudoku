from cell import Cell
from sudoku_generator import SudokuGenerator


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        # initialize board with SudokuGenerator class
        sudoku = SudokuGenerator(difficulty)
        sudoku.fill_values()
        sudoku.remove_cells()
        self.board = sudoku.get_board()
        # save the board to be able to reset it to its original state
        self.original_board = [row[:] for row in self.board]

        self.grid = [[Cell(self.board[row][col], row, col, screen) for col in range(9)] for row in range(9)]
        self.selected_row = None
        self.selected_col = None
        self.game_started = False

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
        # Clears the value cell. Note that the user can only remove the
        # cell values and sketched value that are filled by themselves

        # first checks if a cell is selected. If no cell is selected, it does nothing.
        if (self.selected_row is not None) and (self.selected_col is not None):
            cell = self.grid[self.selected_row][self.selected_col]
            if cell.value == 0 and cell.sketch == 0:
                return
            # prevents the user from clearing a value that was generated by sudoku_generator
            if self.board[self.selected_row][self.selected_col] != 0:
                return
            """checks whether it has a value or a sketched value. if yes, value is set
            to 0 to clear it. if its a sketched value, sketch val is set to 0 to clear"""
            if cell.value != 0:
                cell.set_cell_value(0)
            if cell.sketch != 0:
                cell.set_sketched_value(0)

    def sketch(self, value):
        # Sets the sketched value of the current selected cell equal to user entered value.
        # It will be displayed in the top left corner of the cell using the draw() function.
        cell_value = self.grid[self.selected_row][self.selected_col].value
        if cell_value == 0:
            self.grid[self.selected_row][self.selected_col].set_sketched_value(value)

    def place_number(self, value):
        # Sets the value of the current selected cell equal to user entered value.
        # Called when the user presses the Enter key.
        cell_value = self.grid[self.selected_row][self.selected_col].value
        if cell_value == 0:
            self.grid[self.selected_row][self.selected_col].set_cell_value(value)
            # reset sketched value to 0 to indicate that the cell value is now fixed
            self.grid[self.selected_row][self.selected_col].sketch = 0

    def reset_to_original(self):
        # Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).
        self.board = [row[:] for row in self.original_board]
        self.grid = [[Cell(self.board[row][col], row, col, self.screen) for col in range(9)] for row in range(9)]

    def is_full(self):
        for row in self.grid:
            for cell in row:
                if cell.value == 0:
                    return False
        return True

    def update_board(self):
        # updates the sudoku 2d board with the information in each cell
        for row in range(9):
            for col in range(9):
                self.board[row][col] = self.grid[row][col].value

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
                if cell.value != solution[cell.row][cell.col]:
                    return False
        return True
