import pygame
from Node import Node

pygame.init()


##Colors definition
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (242, 255, 0)
BLACK = (0, 0, 0)
PURPLE = (161, 3, 252)
AQUA = (0, 255, 255)

class MainWindow:
    def __init__(self, width):
        self.width=width
        self.height=width
        self.display=pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Path Finder")

    def make_grid(self, rows, width):
        grid = []
        gap = width // rows
        for i in range(rows):
            grid.append([])
            for j in range(rows):
                node = Node(i, j, gap, rows)
                grid[i].append(node)
        return grid

    def run(self):
        self.running = True
        clock = pygame.time.Clock()
        while self.running:
            dt = clock.tick(40) / 1000.0
            pygame.display.flip()


mainWindow = MainWindow(800)

while True:
    mainWindow.run()