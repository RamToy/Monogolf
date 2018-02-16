import pygame
from settings import bg_color, fg_color
from math import hypot, sin, cos, atan, pi, sqrt

# Группа одного спрайта с мячиком
ball = pygame.sprite.GroupSingle()


''' Функция, вычисляющая сторону прямоугольника, с которой произошло пересечение '''
def side_collide(pos, rect):
    range_dict = {'left': pos[0] - rect.left,
                  'right': rect.right - pos[0],
                  'top': pos[1] - rect.top,
                  'bottom': rect.bottom - pos[1]}
    # Вычисляет расстояние до каждой из сторон и возвращает минимальное
    min_value = min(range_dict.items(), key=lambda x: x[1])
    return min_value[0]


''' Класс мячика '''
class Ball(pygame.sprite.Sprite):
    def __init__(self, slingshot, radius):
        # Необходимо передавать объект рогатки и сверяться с его состоянием,
        # чтобы перемещать мячик вместе с ней во время натяжки
        self.slingshot = slingshot
        self.radius = 15
        self.color = [255 - (bg_color[c] + fg_color[c]) // 2 for c in range(3)]

        super().__init__(ball)
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, self.color, (radius, radius), radius, 0)
        self.rect = self.image.get_rect()

        '''Изначально до движения мячика все параметры равны нулю'''
        self.one_step = 15        # Длина единичного вектора
        self.speed = 0            # Скорость перемещения для tick()
        self.x_dir = 0            # Направление по оси X
        self.y_dir = 0            # Направление по оси Y
        self.x_step = 0           # Шаг по оси X
        self.y_step = 0           # Шаг по оси Y
        self.alpha = 0            # Угол между вектором движения и осью X
        self.calculated = False   # Флаг, отвечающий за порядок вычислений

    ''' Метод, вычисляющий параметры движения мячика '''
    def calculate(self, start_pos, end_pos):
        # Проекция вектора перемещения ось на X
        x_proj = start_pos[0] - end_pos[0]
        # Проекция вектора перемещения ось на Y
        y_proj = start_pos[1] - end_pos[1]

        # Вычисление угла
        try:
            self.alpha = atan(abs(y_proj / x_proj))
        except ZeroDivisionError:
            self.alpha = pi / 2

        # Направление движения по оси X
        self.x_dir = 1 if x_proj > 0 else (-1 if x_proj < 0 else 0)
        # Направление движения по оси Y
        self.y_dir = 1 if y_proj > 0 else (-1 if y_proj < 0 else 0)

        # Шаг по оси X
        self.x_step = round(cos(self.alpha) * self.one_step)
        # Шаг по оси Y
        self.y_step = round(sin(self.alpha) * self.one_step)

    ''' Метод, обновляюший состояние или положение мячика '''
    def update(self):
        # Если рогатка активна, то мячик перемещается вместе с ней
        if self.slingshot.active:
            self.rect.center = self.slingshot.cur_pos
            # Нажатием пробела игрок возвращает мяч в исходную позицию, значит
            # новые параметры еще не посчитаны, и надо опустить флаг
            self.calculated = False

        # Если рогатка не активна
        else:
            # Если все посчитано, то мячик перемещается по заданным параметрам
            if self.calculated:
                self.rect.move_ip(self.x_step * self.x_dir, self.y_step * self.y_dir)
            # Если нет, то происходит подсчет
            else:
                self.calculate(self.slingshot.center_pos, self.slingshot.cur_pos)
                self.calculated = True
