import pygame
from Monogolf.settings import *

# Группа спрайтов с прямоугольниками
rects = pygame.sprite.Group()
# Группа одного спрайта с лункой
hole = pygame.sprite.GroupSingle()


class BoarderRect(pygame.sprite.Sprite):
    """ Класс спрайта прямоугольника """

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        super().__init__(rects)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        self.image.fill(fg_color)


class Hole(pygame.sprite.Sprite):
    """ Класс спрайта лунки """

    def __init__(self, pos, radius, color):
        super().__init__(hole)
        self.pos = pos
        self.radius = radius
        self.color = color
        self.rect = pygame.Rect(self.pos[0] - radius // 2, self.pos[1] - radius // 2, radius, radius)
        self.image = pygame.Surface((2 * radius, 2 * radius),  pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, color, (radius, radius), radius, 0)
