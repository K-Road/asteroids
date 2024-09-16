import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    #init
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    #Sprite groups
    updatable = pygame.sprite.Group(player)
    drawable = pygame.sprite.Group(player)

    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        for sprite in updatable:
            sprite.update(dt)

        screen.fill(BLACK)    

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        #framerate limit 60 fps
        dt = clock.tick(60)/1000 #convert ms to sec


if __name__ == "__main__":
    main()