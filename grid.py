import pygame


class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 40
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = self.get_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for cols in range(self.num_cols):
                print(self.grid[row][cols], end=" ")
            print()

    def get_colors(self):

        blue = (0, 0, 205)
        red = (255, 0, 0)
        lime = (0, 255, 0)
        orange = (255, 165, 0)
        pink = (255, 0, 255)
        violet = (148, 0, 211)
        aqua = (0, 255, 255)
        aquamarine = (127, 255, 212)

        return [blue, lime, orange, pink, violet, aqua, red, aquamarine]

    def draw(self, screen):
        for row in range(self.num_rows):
            for cols in range(self.num_cols):
                cell_value = self.grid[row][cols]
                cell_rect = pygame.Rect(cols*self.cell_size + 1, row*self.cell_size + 1,
                self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)