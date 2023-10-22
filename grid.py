import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 40
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.get_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for cols in range(self.num_cols):
                print(self.grid[row][cols], end=" ")
            print()

    def draw(self, screen):
        for row in range(self.num_rows):
            for cols in range(self.num_cols):
                cell_value = self.grid[row][cols]
                cell_rect = pygame.Rect(cols*self.cell_size + 1, row*self.cell_size + 1,
                self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)