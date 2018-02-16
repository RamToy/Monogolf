import pygame
from settings import bg_color, fg_color
from math import hypot, sin, cos, atan, pi, sqrt
from sprites import rects, polygons

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


''' Функция, определяющая пересечение окружности с линией.
    Примечание заключается в том, что я нашел это в интернете и толком не разбирался.
    Покрутив эту штуку, я увидел, что функция определяет именно пересечения прямой 
    (а не отрезка) с окружностью, поэтому с невыпуклыми многоугольниками лучше не связываться.
    Но, т.к. планируются использоваться только треугольники и ромбы, этого вполне хватит.'''
def circle_and_line_intersection(r, circle_pos, point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    cx, cy = circle_pos
    
    a = (x2 - x1)**2 + (y2 - y1)**2
    b = 2 * ((x2 - x1) * (x1 - cx) + (y2 - y1) * (y1 - cy))
    c = cx**2 + cy**2 + x1**2 + y1**2 - 2 * (cx * x1 + cy * y1) - r**2
    i = b**2 - 4 * a * c

    if i >= 0.0:
        return True
    return False


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
    def calculate(self, start_pos, end_pos, reflection=False):
        # Проекция вектора перемещения ось на X
        x_proj = start_pos[0] - end_pos[0]
        # Проекция вектора перемещения ось на Y
        y_proj = start_pos[1] - end_pos[1]

        # Вычисление угла
        try:
            agle = atan(abs(y_proj / x_proj))
        except ZeroDivisionError:
            agle = pi / 2

        # Флаг reflection со значением True должен передавться, когда происходит отражение
        # мячика от стороны многоугольника, то есть в силу вступает второй угол между
        # этой стороной и осью X
        if reflection:
            # Эту формулу я вывел сам, но работает не очень исправно
            # (В данном случае agle - угол между стороной и осью X)
            self.alpha = 2 * agle - self.alpha
        else:
            # (В данном случае agle - основной угол движения мячика)
            self.alpha = agle
            # Также здесь в первый раз вычисляется скорость
            self.speed = hypot(x_proj, y_proj) // self.one_step

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
                self.calculate(self.slingshot.center_pos, self.slingshot.cur_pos, False)
                self.calculated = True

        # Пересечение мячика с группой прямоугольников
        rect_collide = pygame.sprite.spritecollideany(self, rects)
        # Пересечение мячика с группой многоугольников
        polygon_collide = pygame.sprite.spritecollideany(self, polygons)

        # Если мячик пересекается с прямоугольником
        if rect_collide:
            # Сторона, с которой пересекается мячик
            value = side_collide(self.rect.center, rect_collide.rect)
            if value == 'left':
                self.x_dir = -1
            elif value == 'right':
                self.x_dir = 1
            elif value == 'top':
                self.y_dir = -1
            elif value == 'bottom':
                self.y_dir = 1
            '''Небольшое пояснение: я не стал делать так, что, например, при столкновении с горизонтальными 
               сторонами направление по оси Y меняется на противоположное [self.y_dir = -self.y_dir], т.к.
               при таком раскладе у меня возникал баг, когда при попадании в угол рамки мяч застревал там
               и начинал мандражировать, бегая по всей рамке в одну сторону.'''

        # Если мячик пересекается с моногоугольником
        if polygon_collide:
            # В цикле проверяются пересечения сторон многоугольника с окружностью шарика
            for line in polygon_collide.lines:
                if circle_and_line_intersection(self.radius, self.rect.center, *line):
                    # Вычисляются новые параметры шарика
                    self.calculate(*line, reflection=True)   # Происходит отражение, поэтому reflection=True
                    # Эта строчка нужна только для того, чтобы передать координаты
                    # стороны в главный цикл, затем нарисовать ее ==>> см. main.py
                    #
                    # return line
