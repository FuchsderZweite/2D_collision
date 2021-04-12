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

def redraw_window(screen, right_screen, dt):
    screen.fill(WHITE)
    screen.fill((193, 193, 193), right_screen)
    for i in circles:
        #i.update(dt)
        i.draw(screen)


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
    scaling = 0.00001
    dt = clock.tick(60) * scaling * FPS



    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            redraw_window(screen, right_screen, dt)
            for i in circles:
                obj.Simulation.wall_collision(i)





            pygame.display.flip()
            clock.tick(FPS)
    pygame.quit()

if __name__ == '__main__':
    main()