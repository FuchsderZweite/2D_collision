import pygame
import Circle as obj


RED = (255, 0, 0)
ORANGE = (239, 131, 84)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
VIOLET = (95, 75, 182)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NUMBER_OF_OBJECTS = 5
circles = [obj.Circle() for i in range(NUMBER_OF_OBJECTS)]

def redraw_window(dt, *screens):
    screen, right_screen = screens

    screen.fill(WHITE)
    screen.fill((193, 193, 193), right_screen)
    for i in circles:
        i.update(dt)
        i.draw(screen)
        i.draw(right_screen)


def main():
    pygame.init()
    WINDOW_WIDTH = 1000
    WINDOW_HEIGHT = 600
    SCREEN_SPLIT = 450
    FPS = 60


    RED = (255, 0, 0)
    ORANGE = (239, 131, 84)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    VIOLET = (95, 75, 182)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
    right_screen = pygame.Rect(600, 0, 400, 900)
    screens = [screen, right_screen]
    scaling = 0.00001
    dt = clock.tick(60) * scaling * FPS



    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        redraw_window(dt, *screens)
        for i in circles:
            obj.Simulation.wall_collision(i)

            #redraw_window(screen, right_screen, dt)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()