import pygame


class Player:
    x = 0
    y = 0
    width = 0
    height = 0
    speed = 0
    score = 0
    rect = None

    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        

    def move(self, direction, screen):
        if direction == "up":
            if (self.y - self.speed) <= 0:
                self.y = 0
            else:
                self.y -= self.speed

        elif direction == "down":
            if (self.y + self.height + self.speed) >= screen.get_height():
                self.y = screen.get_height() - self.height
            else:
                self.y += self.speed

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, "blue", (self.x, self.y, self.width, self.height))

    def collidepoint(self, point):
        if (self.x <= point[0] <= self.x + self.width) and (
            self.y <= point[1] <= self.y + self.height
        ):
            return True
        else:
            return False
