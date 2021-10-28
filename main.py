import pygame
import random

pygame.init()

SIZE = 710
pygame.display.set_caption("Path Finder")
WIN = pygame.display.set_mode((SIZE, SIZE))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (242, 255, 0)
BLACK = (0, 0, 0)
PURPLE = (161, 3, 252)
AQUA = (0, 255, 255)


class Node:
    def __init__(self, row, col, SIZE, total_rows):
        # variables for displaying
        self.row = row
        self.col = col
        self.total_rows = total_rows
        self.SIZE = SIZE
        self.color = WHITE

        # variables for a_star_algorithm
        self.f_score = float("inf")
        self.g_score = float("inf")
        self.camefrom = None
        self.neighbors = []

        # for generating the maze
        self.visited = False

    def get_pos(self):
        return (self.row, self.col)

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == YELLOW

    def is_end(self):
        return self.color == GREEN

    def is_visited(self):
        return self.visited

    def make_visited(self):
        self.visited = True

    def make_current(self):
        self.color = RED

    def make_path(self):
        self.color = PURPLE

    def make_barrier(self):
        self.color = BLACK

    def make_start(self):
        self.color = YELLOW
        self.f_score = 0
        self.g_score = 0

    def make_open(self):
        self.color = AQUA

    def make_closed(self):
        self.color = RED

    def make_end(self):
        self.color = GREEN

    def update_neighbors(self, grid):  # updating the neighbors for a_star algortihm
        pass

    def check_neighbors(self, grid):  # returns the neighbors which are not visted(for making the maze)
        pass

    def draw(self, WIN):
        pygame.draw.rect(WIN, self.color, (self.row * self.SIZE, self.col * self.SIZE, self.SIZE, self.SIZE))

    def reset(self):
        if self.is_start():
            self.f_score = float("inf")
            self.g_score = float("inf")
        self.color = WHITE





