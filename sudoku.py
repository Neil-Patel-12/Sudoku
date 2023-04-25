"""
Main (Required)
In addition to the above classes, students will have a sudoku.py file, where the main function will be run.
This file will contain code to create the different screens of the project (game start, game over, and game
in progress), and will form a cohesive project together with the rest of the code.
"""
import pygame
from board import Board

# Initialize Pygame
pygame.init()

# Set the dimensions of the game window
WINDOW_WIDTH = 450
WINDOW_HEIGHT = 500


# Create the game window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set the title of the game window
pygame.display.set_caption("Sudoku")
# icon = pygame.image.load('001-pastime.png')
# pygame.display.set_icon(icon)

# Set the font for the text displayed on the game screen
FONT = pygame.font.Font(None, 30)

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_ORANGE = (235, 180, 52)
BLUE = (52, 79, 235)

# Define the game screens
GAME_START = 0
GAME_IN_PROGRESS = 1
GAME_OVER = 2

# Initialize the game screen
game_screen = GAME_START


# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the coordinates of the mouse click
            x, y = pygame.mouse.get_pos()

            # Handle mouse click based on the current game screen
            if game_screen == GAME_START:
                if 40 < x < 130 and 350 < y < 380:
                    # Start a new easy game
                    board = Board(9, 9, game_window, 1)
                    game_screen = GAME_IN_PROGRESS
                elif 180 < x < 270 and 350 < y < 380:
                    # Start a new medium game
                    board = Board(9, 9, game_window, 40)
                    game_screen = GAME_IN_PROGRESS
                elif 330 < x < 420 and 350 < y < 380:
                    # Start a new hard game
                    board = Board(9, 9, game_window, 50)
                    game_screen = GAME_IN_PROGRESS

        elif game_screen == GAME_IN_PROGRESS:
            # Handle cell selection and number placement

            if 40 < x < 130 and 460 < y < 490:
                # The Reset button will reset the board to its initial state.
                board.reset_to_original()
            elif 180 < x < 270 and 460 < y < 490:
                game_screen = GAME_START
                pass
            elif 330 < x < 420 and 460 < y < 490:
                # The Exit button will end the program.
                pygame.quit()

            # selects a cell
            if board.click(x, y) is not None:
                row_selected, col_selected = board.click(x, y)
                board.select(row_selected, col_selected)

            # sketches a value, can be removed by typing 0 when the cell is selected
            if event.type == pygame.KEYDOWN:
                if event.unicode.isdigit():     # checks if the key pressed is a number
                    num = int(event.unicode)
                    if num in range(0, 10):
                        board.sketch(num)
                elif event.unicode == '\r':     # checks if return key was pressed
                    board.place_number(num)

            # Check if the board is complete
            if board.is_full():
                game_screen = GAME_OVER

            # Update the board display
            board.update_board()

        elif game_screen == GAME_OVER:
            if 200 < x < 340 and 400 < y < 440:
                if Board.check_board(board):
                    pygame.quit()
                else:
                    game_screen = GAME_START



    # Clear the screen
    game_window.fill(BLUE)

    # Draw the appropriate screen based on the current game screen
    if game_screen == GAME_START:
        # Draw the game start screen
        text = FONT.render("Welcome to Sudoku", True, WHITE)
        game_window.blit(text, (150, 150))
        text = FONT.render("Select Game Mode:", True, WHITE)
        game_window.blit(text, (150, 250))
        pygame.draw.rect(game_window, WHITE, (40, 350, 90, 30), 1)
        text = FONT.render("easy", True, WHITE)
        game_window.blit(text, (50, 350))
        pygame.draw.rect(game_window, WHITE, (180, 350, 90, 30), 1)
        text = FONT.render("medium", True, WHITE)
        game_window.blit(text, (190, 350))
        pygame.draw.rect(game_window, WHITE, (330, 350, 90, 30), 1)
        text = FONT.render("hard", True, WHITE)
        game_window.blit(text, (350, 350))

    elif game_screen == GAME_IN_PROGRESS:
        # Draw the game in progress screen
        board.draw()
        pygame.draw.rect(game_window, BLACK, (40, 460, 90, 30), 1)
        text = FONT.render("reset", True, BLACK)
        game_window.blit(text, (50, 460))
        pygame.draw.rect(game_window, BLACK, (180, 460, 90, 30), 1)
        text = FONT.render("restart", True, BLACK)
        game_window.blit(text, (200, 460))
        pygame.draw.rect(game_window, BLACK, (330, 460, 90, 30), 1)
        text = FONT.render("exit", True, BLACK)
        game_window.blit(text, (350, 460))

    elif game_screen == GAME_OVER:
        # Draw the game over screen
        if Board.check_board(board):
            text = FONT.render("Game Won!", True, WHITE)
            game_window.blit(text, (200, 250))
            pygame.draw.rect(game_window, WHITE, (200, 400, 140, 40), 1)
            text = FONT.render("Quit", True, WHITE)
            game_window.blit(text, (220, 410))
        else:
            text = FONT.render("Game Over :(", True, WHITE)
            game_window.blit(text, (200, 250))
            pygame.draw.rect(game_window, WHITE, (200, 400, 140, 40), 1)
            text = FONT.render("Restart", True, WHITE)
            game_window.blit(text, (220, 410))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
