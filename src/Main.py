import pygame
## import fibo


##fibo.fib(10)



screen = pygame.display.set_mode((1024, 768))

gem = pygame.image.load('/home/pi/python_games/gem2.png')
gem2 = pygame.image.load('/home/pi/python_games/gem1.png')
screen.blit(gem, (50,100))
screen.blit(gem2, (10, 100))
pygame.display.flip()

clock = pygame.time.Clock()


# move gem here
for i in range(1000):
    clock.tick(100)
    print ("clock tick ", i)

    #clear screen
    screen.fill((0, 0, 0))

    #set the gem to new location
    screen.blit(gem, (i + 50, 0))
    screen.blit(gem2, (i + 10, 0))

    #refresh the screen
    pygame.display.flip()