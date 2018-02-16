import pygame
from settings import *
from slingshot import Slingshot
from ball import ball, Ball
from sprites import rects, hole

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
# Объект рогатки
slingshot = Slingshot((WIDTH // 2, HEIGHT // 4 * 3), 100, 10)
# Объект мячика
Ball(slingshot, 15)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Передача событий рогатке
        slingshot.get_event(event)

    # Обновление положения мячика
    ball.update()

    screen.fill(bg_color)      # Заливка поля
    slingshot.render(screen)   # Прорисовка рогатки
    rects.draw(screen)         # Прорисовка группы прямоугольников
    ball.draw(screen)          # Прорисовка мячика
    hole.draw(screen)          # Прорисовка лунки

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
