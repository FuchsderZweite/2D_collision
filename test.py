import pygame
import numpy as np
from random import randint, randrange
from itertools import combinations
import Circle as obj


WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
SCREEN_SPLIT = 450
FPS = 60
NUM_OF_CIRCLES = 3

RED = (255, 0, 0)
ORANGE = (239, 131, 84)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
VIOLET = (95, 75, 182)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



def update(screen, circles):
    color = (255, 255, 255)
    radius = 10
    for obj in circles:
        obj.r[0] = obj.r[0] + 1
        obj.r[1] = obj.r[1] + 1
        return pygame.draw.circle(screen, color, (obj.r[0], obj.r[1]), radius)





def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),
                                     pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
    right_screen = pygame.Rect(600, 0, 400, 900)
    screens = [screen, right_screen]
    scaling = 0.00001
    dt = clock.tick(60) * scaling * FPS

    circles = [obj.Circle for i in range(NUM_OF_CIRCLES)]
    sim = obj.Simulation()


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.fill((0, 0, 0))
        for i in circles:
            obj.Circle.draw(i, screen)
            sim.check_wall()


        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    quit()






if __name__ == '__main__':
    main()