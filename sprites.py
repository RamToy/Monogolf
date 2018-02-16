import pygame
from settings import *

# Группа спрайтов с прямоугольниками
rects = pygame.sprite.Group()

''' Класс спрайта прямоугольника '''
class BoarderRect(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        super().__init__(rects)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        self.image.fill(fg_color)


# Рамки
BoarderRect(0, 0, WIDTH - INDENT, INDENT)
BoarderRect(0, INDENT, INDENT, HEIGHT - INDENT)
BoarderRect(INDENT, HEIGHT - INDENT, WIDTH - INDENT, INDENT)
BoarderRect(WIDTH - INDENT, 0, INDENT, HEIGHT - INDENT)
