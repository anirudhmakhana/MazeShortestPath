import pygame
from Node import Node
from pyswip import Prolog

pygame.init()



##Colors definition
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

wall = []

class MainWindow:
    def __init__(self, width):
        self.width = width
        self.height = width
        self.display = pygame.display.set_mode((self.width, self.height))
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

    def draw_grid(self, win, rows, width):
        gap = width // rows
        for i in range(rows):
            pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
            for j in range(rows):
                pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

    def draw(self, win, grid, rows, width):
        win.fill(WHITE)

        for row in grid:
            for spot in row:
                spot.draw(win)

        self.draw_grid(win, rows, width)
        pygame.display.update()

    def get_clicked_pos(self, pos, rows, width):
        gap = width // rows
        y, x = pos

        row = y // gap
        col = x // gap

        return row, col

    def run(self, win, width):
        ROWS = 8
        grid = self.make_grid(ROWS, width)

        start = None
        end = None

        run = True
        while run:
            self.draw(win, grid, ROWS, width)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if pygame.mouse.get_pressed()[0]:  # LEFT
                    pos = pygame.mouse.get_pos()
                    row, col = self.get_clicked_pos(pos, ROWS, width)
                    spot = grid[row][col]
                    if not start and spot != end:
                        start = spot
                        start.make_start()

                    elif not end and spot != start:
                        end = spot
                        end.make_end()

                    elif spot != end and spot != start:
                        spot.make_barrier()
                        prolog.assertz("move_pos(PrevX,PrevY,PrevX,Y) :- Y is PrevY-1. % move one position Up")
                        prolog.assertz("move_pos(PrevX,PrevY,X,PrevY) :- X is PrevX+1. % move one position right")
                        prolog.assertz("move_pos(PrevX,PrevY,PrevX,Y) :- Y is PrevY+1. % move one position down")
                        prolog.assertz("move_pos(PrevX,PrevY,X,PrevY) :- X is PrevX-1. % move one position left")

                        prolog.assertz("notvisited(_, []) :- !.")
                        prolog.assertz("notvisited(X, [H|T]) :-  X \= H, notvisited(X, T).")
                        prolog.assertz("findGoalPath(X,Y,X,Y,GoalPath,GoalPath).")
                        prolog.assertz("findGoalPath(PrevX,PrevY,X,Y,AlreadyVisitedPath,GoalPath) :- barrier(NextX,NextY), move_pos(PrevX,PrevY,NextX,NextY),")
                        prolog.assertz("notvisited(barrier(NextX,NextY),AlreadyVisitedPath),")
                        prolog.assertz("findGoalPath(NextX,NextY,X,Y,[barrier(NextX,NextY)|AlreadyVisitedPath],GoalPath).")
                        prolog.assertz(f"barrier({row},{col})")
                        #print(list(prolog.query("findGoalPath(0, 0, 2, 0, [], Path)")))


                elif pygame.mouse.get_pressed()[2]:  # RIGHT
                    prolog.consult("algorithm.pl")
                    temp = prolog.query("findGoalPath(0, 0, 2, 0, [], Path)")
                    print(temp)
                    # pos = pygame.mouse.get_pos()
                    # row, col = self.get_clicked_pos(pos, ROWS, width)
                    # spot = grid[row][col]
                    # #spot.reset()
                    # if spot == start:
                    #     start = None
                    # elif spot == end:
                    #     end = None
        #print(list(prolog.query("findGoalPath(5, 4, 7, 3, [], Path)")))
        pygame.quit()

if __name__ == '__main__':
    WIDTH = 800
    prolog = Prolog()
    prolog.consult("algorithm.pl")
    WIN = pygame.display.set_mode((WIDTH, WIDTH))
    mainWindow = MainWindow(WIDTH)
    mainWindow.run(WIN, WIDTH)
