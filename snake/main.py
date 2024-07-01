from operator import index, indexOf
import random
import pygame


def generate_snake_color(index):
    return 255 if 50 + index * 10 > 255 else 50 + index * 10


def generate_fruit_lcoation():
    valid = False
    fruit_location = pygame.Vector2(0, 0)
    while not valid:
        fruit_location = pygame.Vector2(
            snake_size * random.randint(1, int(screen.get_width() / snake_size) - 2),
            snake_size * random.randint(1, int(screen.get_height() / snake_size) - 2),
        )

        if fruit_location not in snake_segments:
            valid = True
    return fruit_location


pygame.init()

snake_size = 16
screen = pygame.display.set_mode((snake_size * 10, snake_size * 10))
clock = pygame.time.Clock()
running = True


snake_segments = [pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)]

size = 3

direction = pygame.Vector2(0, -1)
alive = True
fruit = generate_fruit_lcoation()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if (event.key == pygame.K_w or event.key == pygame.K_UP) and direction.y != 1:
                direction = pygame.Vector2(0, -1)
            if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and direction.y != -1:
                direction = pygame.Vector2(0, 1)
            if (event.key == pygame.K_a or event.key == pygame.K_LEFT) and direction.x != 1:
                direction = pygame.Vector2(-1, 0)
            if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and direction.x != -1:
                direction = pygame.Vector2(1, 0)
    if (
        snake_segments[-1].x < 0 + snake_size
        or snake_segments[-1].x > screen.get_width() - snake_size - snake_size
        or snake_segments[-1].y < 0 + snake_size
        or snake_segments[-1].y > screen.get_height() - snake_size - snake_size
    ):
        running = False

    screen.fill("black")
    pygame.draw.rect(
        screen,
        "white",
        pygame.Rect(0, 0, screen.get_width(), screen.get_height()),
        snake_size,
    )

    if alive:
        snake_head = snake_segments[-1] + direction * snake_size
        if snake_segments.count(snake_head) > 0:
            running = False
        if snake_head == fruit:
            size += 1
            valid = False
            fruit = generate_fruit_lcoation()

        snake_segments.append(snake_head)
        snake_segments = snake_segments[-size:]

        pygame.draw.rect(
            screen, "red", pygame.Rect(fruit.x, fruit.y, snake_size, snake_size)
        )

        for segment in snake_segments:
            # draw the player
            pygame.draw.rect(
                screen,
                (0, generate_snake_color(indexOf(snake_segments, segment)), 0),
                pygame.Rect(segment.x, segment.y, snake_size, snake_size),
            )

   

    pygame.display.flip()
    clock.tick(size)

pygame.quit()
