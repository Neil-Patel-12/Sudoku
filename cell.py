import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketch = 0

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketch = value

    def draw(self):
        font = pygame.font.SysFont('calibri', 40)
        text = font.render(str(self.value), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (75 + self.col * 50, 75 + self.row * 50)
        self.screen.blit(text, text_rect)
        if self.sketch != 0:
            text = font.render(str(self.sketch), True, (128, 128, 128))
            text_rect = text.get_rect()
            text_rect.center = (75 + self.col * 50 + 20, 75 + self.row * 50 + 20)
            self.screen.blit(text, text_rect)
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(50 + self.col * 50, 50 + self.row * 50, 50, 50), 1)