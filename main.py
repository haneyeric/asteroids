import pygame
import constants


def main():
    print("Starting asteroids!")
    # print("Screen width:", constants.SCREEN_WIDTH)
    # print("Screen height:", constants.SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode(
        (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
