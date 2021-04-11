import pygame
import Circle as obj


WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
SCREEN_SPLIT = 450
FPS = 60
NUMBER_OF_OBJECTS = 5

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


def main():
    pygame.init()
    #dt = FPS
    circles = [obj.Circle() for i in range(NUMBER_OF_OBJECTS)]

    for i in circles:
        obj.Simulation.wall_collision(i)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            screen.fill(WHITE)
            screen.fill((193, 193, 193), right_screen)
            for object in circles:
                object.draw(screen)
                #object.movement(dt)
                #object.wall_collision(circles[object])

            pygame.display.flip()
            clock.tick(FPS)
    pygame.quit()

if __name__ == '__main__':
    main()