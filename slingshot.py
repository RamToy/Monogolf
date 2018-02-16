from settings import *


class Slingshot:      # РОГАТКА
    def __init__(self, center_pos, ball_radius, shoulder_radius):

        self.shoulder_r = shoulder_radius                # Радиус плечей рогатки
        self.ball_r = ball_radius                        # Радиус мячика
        self.ball_color = [255 - (bg_color[c] + fg_color[c]) // 2 for c in range(3)]  # Цвет мячика
        # Вычисляется как негатив между средним арифметическим между цветом фона и цветом переднего плана

        self.center_pos = self.x, self.y = center_pos    # Дефолтная позиция рогатки
        self.center_range = 100                          # Рассояние от центра до каждого плеча рогатки

        self.left = self.x - self.center_range           # X координата левого плеча
        self.right = self.x + self.center_range          # Y координата левого плеча

        # Область, в которой можно захватить шарик
        self.capture_rect = pygame.Rect(self.left + 10 + self.shoulder_r, self.y - 30,
                                        self.right - self.left - self.shoulder_r * 2 - 20, 60)
        # Область, в пределах которой можно перемещать шарик
        self.active_rect = pygame.Rect(self.left + self.shoulder_r,
                                       self.y - HEIGHT + self.y + self.ball_r + INDENT,
                                       self.right - self.left - self.shoulder_r * 2,
                                       (HEIGHT - self.y - self.ball_r - INDENT) * 2)
        self.cur_pos = self.center_pos                   # Текущая позиция шарика

    def render(self, surface):        # Отрисовка рогатки
        # pygame.draw.rect(surface, pygame.Color('red'), self.active_rect, 4)      # Здесь можно посмотреть
        # pygame.draw.rect(surface, pygame.Color('greed'), self.active_rect, 4)    # эти самые зоны
        pygame.draw.line(surface, fg_color, (self.left, self.y), self.cur_pos, 4)
        pygame.draw.line(surface, fg_color, (self.right, self.y), self.cur_pos, 4)
        pygame.draw.circle(surface, fg_color, (self.left, self.y), self.shoulder_r, 0)
        pygame.draw.circle(surface, fg_color, (self.right, self.y), self.shoulder_r, 0)
        pygame.draw.circle(surface, self.ball_color, self.cur_pos, self.ball_r, 0)

    def update(self, new_pos=None):    # Обновляет положение рогатки
        if new_pos is None:
            self.cur_pos = self.center_pos    # Дефолтное положение
        else:
            x, y = new_pos
            rect = self.active_rect
            x = rect.left if x < rect.left else (rect.right if x > rect.right else x)  # Проверки на выход за
            y = rect.top if y < rect.top else (rect.bottom if y > rect.bottom else y)  # пределы щоны
            self.cur_pos = x, y
