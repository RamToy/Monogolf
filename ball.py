import pygame
from math import hypot, sin, cos, atan, pi
from Monogolf.sprites import rects, hole


# Группа одного спрайта с мячиком
ball = pygame.sprite.GroupSingle()


def side_collide(pos, rect):
    """ Функция, вычисляющая сторону прямоугольника, с которой произошло пересечение """

    range_dict = {"left": pos[0] - rect.left,
                  "right": rect.right - pos[0],
                  "top": pos[1] - rect.top,
                  "bottom": rect.bottom - pos[1]}
    # Вычисляет расстояние до каждой из сторон и возвращает минимальное
    min_value = min(range_dict.items(), key=lambda x: x[1])
    return min_value[0]


class Ball(pygame.sprite.Sprite):
    """ Класс мячика """

    def __init__(self, slingshot, radius, color):
        # Необходимо передавать объект рогатки и сверяться с его состоянием,
        # чтобы перемещать мячик вместе с ней во время натяжки
        self.slingshot = slingshot
        self.radius = radius
        self.color = color

        super().__init__(ball)
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, self.color, (radius, radius), radius, 0)
        self.rect = self.image.get_rect()

        # Изначально до движения мячика все параметры равны нулю
        self.one_step = 15        # Длина единичного вектора
        self.speed = 0            # Скорость перемещения для tick()
        self.x_dir = 0            # Направление по оси X
        self.y_dir = 0            # Направление по оси Y
        self.x_step = 0           # Шаг по оси X
        self.y_step = 0           # Шаг по оси Y
        self.angle = 0            # Угол между вектором движения и осью X
        self.calculated = False   # Флаг, отвечающий за порядок вычислений
        self.hitting = False      # Флаг, отвечающий за попадпние в лунку

    def calculate(self, start_pos, end_pos):
        """ Метод, вычисляющий параметры движения мячика """

        # Проекция вектора перемещения ось на X
        x_proj = start_pos[0] - end_pos[0]
        # Проекция вектора перемещения ось на Y
        y_proj = start_pos[1] - end_pos[1]

        # Вычисление угла
        try:
            self.angle = atan(abs(y_proj / x_proj))
        except ZeroDivisionError:
            self.angle = pi / 2

        # Вычисление скорости
        self.speed = hypot(x_proj, y_proj) // self.one_step

        # Направление движения по оси X
        self.x_dir = 1 if x_proj > 0 else (-1 if x_proj < 0 else 0)
        # Направление движения по оси Y
        self.y_dir = 1 if y_proj > 0 else (-1 if y_proj < 0 else 0)

        # Шаг по оси X
        self.x_step = round(cos(self.angle) * self.one_step)
        # Шаг по оси Y
        self.y_step = round(sin(self.angle) * self.one_step)

    def update(self):
        """ Метод, обновляюший состояние или положение мячика """

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

        # Пересечение мячика с группой прямоугольников
        rect_collide = pygame.sprite.spritecollideany(self, rects)

        # Если мячик пересекается с прямоугольником
        if rect_collide:
            # Сторона, с которой пересекается мячик
            value = side_collide(self.rect.center, rect_collide.rect)
            if value == "left":
                self.x_dir = -1
            elif value == "right":
                self.x_dir = 1
            elif value == "top":
                self.y_dir = -1
            elif value == "bottom":
                self.y_dir = 1
            """Небольшое пояснение: я не стал делать так, что, например, при столкновении с горизонтальными 
               сторонами направление по оси Y меняется на противоположное [self.y_dir = -self.y_dir], т.к.
               при таком раскладе у меня возникал баг, когда при попадании в угол рамки мяч застревал там
               и начинал мандражировать, бегая по всей рамке в одну сторону."""

        self.hitting = pygame.sprite.collide_circle(self, hole.sprite)
