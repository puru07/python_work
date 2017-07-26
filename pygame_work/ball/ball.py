import sys
import pygame
from pygame.locals import *

pygame.init()

size = width, height = 640, 480
speedup = [0, -2]
speeddown = [0, 2]
speedleft = [-2, 0]
speedright = [2, 0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
move_ticker = 0

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if (event.type == K_LEFT) and ballrect.left > 0:
                ballrect = ballrect.move(speedleft)
            if (event.type == K_RIGHT) and ballrect.right < width:
                ballrect = ballrect.move(speedright)
            if (event.type == K_UP) and ballrect.top > 0:
                ballrect = ballrect.move(speedup)
            if (event.type == K_DOWN) and ballrect.bottom < height:
                ballrect = ballrect.move(speeddown)

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        if move_ticker == 0 and ballrect.left > 0:
            move_ticker = 5
            ballrect = ballrect.move(speedleft)
    elif keys[K_RIGHT]:
        if move_ticker == 0 and ballrect.right < width:
            move_ticker = 5
            ballrect = ballrect.move(speedright)
    elif keys[K_DOWN]:
        if move_ticker == 0 and ballrect.bottom < height:
            move_ticker = 5
            ballrect = ballrect.move(speeddown)
    elif keys[K_UP]:
        if move_ticker == 0 and ballrect.top > 0:
            move_ticker = 5
            ballrect = ballrect.move(speedup)

    if move_ticker > 0:
        move_ticker -= 1        
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()


