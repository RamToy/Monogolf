from settings import *
from math import hypot, sin, cos, atan, pi


class Ball:          # МЯЧИК
    def __init__(self, start_pos, end_pos, ball_radius):
        self.color = [255 - (bg_color[c] + fg_color[c]) // 2 for c in range(3)]
        self.r = ball_radius

        self.cur_pos = self.x, self.y = end_pos                   # Текущая позиция мячика (используется при движении)
        self.start_pos = self.start_x, self.start_y = start_pos   # Позиция, из которой был натянут мячик
        self.end_pos = self.end_x, self.end_y = end_pos           # Позиция, в которую был натянут мячик

        x_proj = self.start_x - self.end_x                        # Проекция вектора перемещения ось на X
        y_proj = self.start_y - self.end_y                        # Проекция вектора перемещения ось на Y

        self.one_step = 15                                        # Единичный вектор
        self.speed = hypot(x_proj, y_proj) // self.one_step       # Скорость движения мячика

        self.x_dir = 1 if x_proj > 0 else (-1 if x_proj < 0 else 0)      # Направление движения мяча по оси X
        self.y_dir = 1 if y_proj > 0 else (-1 if y_proj < 0 else 0)      # Направление движения мяча по оси Y

        try:
            self.alpha = atan(abs(y_proj / x_proj))               # Угол между вектором и осью X
        except ZeroDivisionError:                                 # arctg(+- pi / 2) ==> не существует
            self.alpha = pi / 2                                   # Костыль, конечно, но зато точно

        self.x_step = round(cos(self.alpha) * self.one_step) * self.x_dir   # Шаг по оси X
        self.y_step = round(sin(self.alpha) * self.one_step) * self.y_dir   # Шаг по оси Y

        self.field_rect = pygame.Rect(INDENT + self.r, INDENT + self.r,  # Область активного игрового поля
                                      WIDTH - self.r * 2 - INDENT * 2,
                                      HEIGHT - self.r * 2 - INDENT * 2)
        '''Все это можно перелопатить и я этим займусь'''

    def render(self, surface):                    # Отрисовка шарика
        pygame.draw.circle(surface, self.color, self.cur_pos, self.r, 0)

    def move(self):                               # Движение шарика
        self.x += self.x_step
        self.y += self.y_step

        if not self.field_rect.collidepoint(self.x, self.y):      # Если шарик достиг края поля,
            self.x_step, self.y_step = 0, 0                       # то движение прекращается

            if self.x < self.field_rect.left:
                self.x = self.field_rect.left
            elif self.x > self.field_rect.right:
                self.x = self.field_rect.right
            if self.y < self.field_rect.top:
                self.y = self.field_rect.top
            elif self.y > self.field_rect.bottom:
                self.y = self.field_rect.bottom

        self.cur_pos = self.x, self.y
