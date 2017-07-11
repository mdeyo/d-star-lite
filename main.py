import heapq
import pygame

from graph import Node, Graph
from grid import GridWorld
from utils import stateNameToCoords
from d_star_lite import initDStarLite, moveAndRescan

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY1 = (145, 145, 102)
GRAY2 = (77, 77, 51)
BLUE = (0, 0, 80)

colors = {
    0: WHITE,
    1: GREEN,
    -1: GRAY1,
    -2: GRAY2
}

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 40
HEIGHT = 40

# This sets the margin between each cell
MARGIN = 5

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0)  # Append a cell

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[1][5] = 1

# Initialize pygame
pygame.init()

X_DIM = 12
Y_DIM = 12
VIEWING_RANGE = 3


# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [(WIDTH + MARGIN) * X_DIM + MARGIN,
               (HEIGHT + MARGIN) * Y_DIM + MARGIN]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("D* Lite Path Planning")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

if __name__ == "__main__":
    graph = GridWorld(X_DIM, Y_DIM)
    s_start = 'x1y2'
    s_goal = 'x5y4'
    goal_coords = stateNameToCoords(s_goal)

    graph.setStart(s_start)
    graph.setGoal(s_goal)
    k_m = 0
    s_last = s_start
    queue = []

    graph, queue, k_m = initDStarLite(graph, queue, s_start, s_goal, k_m)

    s_current = s_start
    pos_coords = stateNameToCoords(s_current)

    basicfont = pygame.font.SysFont('Comic Sans MS', 36)

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # print('space bar! call next action')
                s_new, k_m = moveAndRescan(
                    graph, queue, s_current, VIEWING_RANGE, k_m)
                if s_new == 'goal':
                    print('Goal Reached!')
                    done = True
                else:
                    # print('setting s_current to ', s_new)
                    s_current = s_new
                    pos_coords = stateNameToCoords(s_current)
                    # print('got pos coords: ', pos_coords)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                if(graph.cells[row][column] == 0):
                    graph.cells[row][column] = -1

        # Set the screen background
        screen.fill(BLACK)

        # Draw the grid
        for row in range(Y_DIM):
            for column in range(X_DIM):
                color = WHITE
                # if grid[row][column] == 1:
                #     color = GREEN
                pygame.draw.rect(screen, colors[graph.cells[row][column]],
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
                node_name = 'x' + str(column) + 'y' + str(row)
                if(graph.graph[node_name].g != float('inf')):
                    # text = basicfont.render(
                    # str(graph.graph[node_name].g), True, (0, 0, 200), (255,
                    # 255, 255))
                    text = basicfont.render(
                        str(graph.graph[node_name].g), True, (0, 0, 200))
                    textrect = text.get_rect()
                    textrect.centerx = int(
                        column * (WIDTH + MARGIN) + WIDTH / 2) + MARGIN
                    textrect.centery = int(
                        row * (HEIGHT + MARGIN) + HEIGHT / 2) + MARGIN
                    screen.blit(text, textrect)

        # fill in goal cell with GREEN
        pygame.draw.rect(screen, GREEN, [(MARGIN + WIDTH) * goal_coords[0] + MARGIN,
                                         (MARGIN + HEIGHT) * goal_coords[1] + MARGIN, WIDTH, HEIGHT])
        # print('drawing robot pos_coords: ', pos_coords)
        # draw moving robot, based on pos_coords
        robot_center = [int(pos_coords[0] * (WIDTH + MARGIN) + WIDTH / 2) +
                        MARGIN, int(pos_coords[1] * (HEIGHT + MARGIN) + HEIGHT / 2) + MARGIN]
        pygame.draw.circle(screen, RED, robot_center, int(WIDTH / 2) - 2)

        # draw robot viewing range
        pygame.draw.rect(
            screen, BLUE, [robot_center[0] - VIEWING_RANGE * (WIDTH + MARGIN), robot_center[1] - VIEWING_RANGE * (HEIGHT + MARGIN), 2 * VIEWING_RANGE * (WIDTH + MARGIN), 2 * VIEWING_RANGE * (HEIGHT + MARGIN)], 2)

        # Limit to 60 frames per second
        clock.tick(20)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
