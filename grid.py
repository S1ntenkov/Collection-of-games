class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 40
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]

    def print_grid(self):
        for row in range(self.num_rows):
            for cols in range(self.num_cols):
                print(self.grid[row][cols], end = " ")
            print()
