import pygame
from settings import *

# Группа спрайтов с прямоугольниками
rects = pygame.sprite.Group()
# Группа спрайтов с полигонами
polygons = pygame.sprite.Group()

''' Класс спрайта прямоугольника '''
class BoarderRect(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        super().__init__(rects)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        self.image.fill(fg_color)


''' Класс спрайта полигона (будет использоваться в основном для треугольников и ромбов) '''
class BoarderPolygon(pygame.sprite.Sprite):
    def __init__(self, points):
        super().__init__(polygons)
        self.points = points
        # X и Y координаты точек
        x_list = [i[0] for i in points]
        y_list = [i[1] for i in points]
        # Прямоугольник полигона
        self.rect = pygame.Rect(min(x_list), min(y_list),
                                max(x_list) - min(x_list) + 1, max(y_list) - min(y_list) + 1)
        self.image = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA, 32)
        # Новые точки с учетом координат холста
        surface_points = [(i[0] - self.rect.x, i[1] - self.rect.y) for i in points]
        pygame.draw.polygon(self.image, fg_color, surface_points, 0)
        # Список с линиями полигона
        self.lines = [(points[i], points[i-1]) for i in range(len(points)-1, -1, -1)]


# Рамки
BoarderRect(0, 0, WIDTH - INDENT, INDENT)
BoarderRect(0, INDENT, INDENT, HEIGHT - INDENT)
BoarderRect(INDENT, HEIGHT - INDENT, WIDTH - INDENT, INDENT)
BoarderRect(WIDTH - INDENT, 0, INDENT, HEIGHT - INDENT)

# Тестовый образец ромба
BoarderPolygon([(150, 250), (250, 350), (350, 250), (250, 150)])
