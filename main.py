import pygame
import Circle as obj


WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
FPS = 60
NUMBER_OF_OBJECTS = 2

RED = (255, 0, 0)
ORANGE = (239, 131, 84)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
VIOLET = (95, 75, 182)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)



def main():
    pygame.init()

    circles = [obj.Circle() for i in range(NUMBER_OF_OBJECTS)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False




            screen.fill(WHITE)
            for object in circles:
                object.draw(screen)
            pygame.display.flip()
            clock.tick(FPS)
    pygame.quit()

if __name__ == '__main__':
    main()