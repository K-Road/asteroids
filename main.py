import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    #init
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    dt = 0
    

    #Sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    Shot.containers = (shots,updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

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

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.checkcollision(shot):
                    asteroid.split()
                    shot.kill()

        for sprite in asteroids:
            if sprite.checkcollision(player):
                print("Game over!")
                sys.exit()

        pygame.display.flip()

        #framerate limit 60 fps
        dt = clock.tick(60)/1000 #convert ms to sec


if __name__ == "__main__":
    main()