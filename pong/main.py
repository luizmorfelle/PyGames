import random
import pygame
import math
from ball import Ball

from player import Player

pygame.init()

WIDTH, HEIGHT = 900, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Pong")
running = True
enemy_score = 0
player_score = 0

player = Player(0, 0, 20, 100, 5)
enemy = Player(880, 0, 20, 100, 5)
ball = Ball(400, 300, 10, math.radians(0), 3)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.move("up", screen)
    elif keys[pygame.K_DOWN]:
        player.move("down", screen)
    else:
        player_speed = 0
        
    ball.move()

    screen.fill("black")
    
    player.draw(screen)
    enemy.draw(screen)
    ball.draw(screen)
    
    
    pygame.display.flip()
    clock.tick(60)
