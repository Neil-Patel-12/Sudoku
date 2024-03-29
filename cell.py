import pygame


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketch = 0
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketch = value

    def draw(self):
        font = pygame.font.SysFont('calibri', 40)
        # draws the cell when it contains a number value
        if self.value != 0:
            text = font.render(str(self.value), True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (75 + (self.col-1) * 50, 75 + (self.row-1) * 50)
            self.screen.blit(text, text_rect)

        # highlights the border of the selected cell
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(50 + (self.col - 1) * 50,
                                                                   50 + (self.row - 1) * 50, 50, 50), 4)

        # prints to the screen a sketched value in the cell
        if self.sketch != 0:
            text = font.render(str(self.sketch), True, (128, 128, 128))
            text_rect = text.get_rect()
            text_rect.center = (75 + (self.col-1) * 50, 75 + (self.row-1) * 50)
            self.screen.blit(text, text_rect)

        # draw the gridlines for the entire array
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(50 + (self.col-1) * 50, 50 + (self.row-1) * 50, 50, 50), 1)

        bold = 4  # Thickness of the bold gridlines

        # Makes every 3rd  vertical line bold to differentiate boxes
        if (self.col + 1) % 3 == 0 and self.col != 8:
            pygame.draw.line(self.screen, (0, 0, 0), ((self.col + 1) * 50, 0 ), ((self.col + 1)* 50, 450), width=bold)

            # Makes every 3rd horizontal line bold to differentiate boxes
        if (self.row + 1) % 3 == 0 and self.row != 8:
            pygame.draw.line(self.screen, (0, 0, 0), (0, (self.row + 1) * 50), (450, (self.row + 1) * 50), width=bold)
