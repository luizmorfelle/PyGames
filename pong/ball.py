import math
from random import randint
import pygame


class Ball:
    x = 0
    y = 0
    radius = 0
    angle = 0
    speed = 0
    colission_points = []

    def __init__(self, x, y, radius, angle, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.angle = angle
        self.speed = speed
        self.colission_points = self.generate_colission_points()

    def move(self):
        if self.y <= 0 or self.y >= 600:
            self.bounce_horizontal()
        if self.x <= 0 or self.x >= 900:
            self.restart(400, 300)
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

    def bounce(self):
        self.angle = math.pi - self.angle

    def bounce_horizontal(self):
        self.angle = -self.angle

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", (self.x, self.y), self.radius)

    def generate_colission_points(self):
        points = []
        for i in [0, 45, 90, 135, 180, 225, 270, 315]:
            x = self.x + self.radius * math.cos(i)
            y = self.y + self.radius * math.sin(i)
            points.append((x, y))
        return points
    
    def restart(self, x, y):
        self.x = 400
        self.y = 300
        self.speed = 3
        self.angle = math.radians(randint(0,360))
        self.colission_points = self.generate_colission_points()