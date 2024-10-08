import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/i.jpg")
pygame.display.set_icon(icon)

target_image = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

# Начальная позиция мишени
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Скорость мишени
velocity_x = random.choice([-1, 1]) * random.uniform(0.5, 2)
velocity_y = random.choice([-1, 1]) * random.uniform(0.5, 2)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Очки
score = 0
font = pygame.font.Font(None, 36)


def draw_score():
    score_text = font.render(f'Очки: {score}', True, (0, 0, 0))
    screen.blit(score_text, (10, 10))


running = True
clock = pygame.time.Clock()

while running:
    screen.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                # Опционально изменить скорость при попадании
                velocity_x = random.choice([-1, 1]) * random.uniform(0.5, 2)
                velocity_y = random.choice([-1, 1]) * random.uniform(0.5, 2)
                score += 10  # Добавление очков за попадание

    # Обновление позиции мишени
    target_x += velocity_x
    target_y += velocity_y

    # Отскок от краев
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        velocity_x = -velocity_x
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        velocity_y = -velocity_y

    screen.blit(target_image, (target_x, target_y))
    draw_score()  # Отображение очков
    pygame.display.update()
    clock.tick(60)  # Ограничение FPS до 60

pygame.quit()