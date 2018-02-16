import pygame
from settings import HEIGHT, INDENT, fg_color

''' Класс рогатки '''
class Slingshot:
    def __init__(self, center_pos, center_range, shoulder_radius):
        # Дефолтная позиция
        self.center_pos = center_pos
        # Текущая позиция (изначально равна дефолтной)
        self.cur_pos = center_pos
        # Расстояние от центра до плеч рогатки
        self.center_range = center_range

        # Радиус плеча рогатки
        self.shoulder_radius = shoulder_radius
        # Координаты левого плеча
        self.left_shoulder = center_pos[0] - center_range, center_pos[1]
        # Координаты правого плеча
        self.right_shoulder = center_pos[0] + center_range, center_pos[1]

        # Прямоугольник, в котором можно захватывать/отпускать мячик нажатием/отжатием кнопки
        self.capture_rect = pygame.Rect(self.left_shoulder[0] + shoulder_radius + 10, center_pos[1] - 20,
                                        center_range * 2 - shoulder_radius * 2 - 20, 40)
        # Прямоугольник, за пределы которого рогатка не может натягиваться
        self.active_rect = pygame.Rect(self.left_shoulder[0] + shoulder_radius,
                                       center_pos[1] * 2 - HEIGHT + INDENT + 15,
                                       center_range * 2 - shoulder_radius * 2,
                                       (HEIGHT - INDENT - center_pos[1]) * 2 - 30)
        # Флаг, отвечающий за активность рогатки
        self.active = True
        # Флаг, отвечающий за фокусировку (перемещение за курсором) рогатки
        self.focus = False

    ''' Метод, проверяющий выход рогатки при натягивании за пределы активной зоны (self.active_rect) '''
    def check_pos(self, pos):
        x, y = pos
        if x < self.active_rect.left:
            x = self.active_rect.left
        elif x > self.active_rect.right:
            x = self.active_rect.right
        if y < self.active_rect.top:
            y = self.active_rect.top
        elif y > self.active_rect.bottom:
            y = self.active_rect.bottom
        return x, y

    ''' Метод, отрисовывающий рогатку '''
    def render(self, surface):
        # Если рогатка активна, то она рисуется
        if self.active:
            # Здесь можно посмотреть зоны активности и захвата
            # pygame.draw.rect(surface, (255, 0, 0), self.active_rect, 2)
            # pygame.draw.rect(surface, (0, 255, 0), self.capture_rect, 2)
            pygame.draw.line(surface, fg_color, self.left_shoulder, self.cur_pos, 4)
            pygame.draw.line(surface, fg_color, self.right_shoulder, self.cur_pos, 4)
            pygame.draw.circle(surface, fg_color, self.left_shoulder, self.shoulder_radius, 0)
            pygame.draw.circle(surface, fg_color, self.right_shoulder, self.shoulder_radius, 0)

    ''' Метод, отвечающий за обработку событий '''
    def get_event(self, event):
        # Если рогатка активна
        if self.active:
            # Если зажата ЛКМ в области захвата
            if event.type == pygame.MOUSEBUTTONDOWN and \
                    self.capture_rect.collidepoint(*event.pos) and event.button == 1:
                # Рогатка попадает в фокус
                self.focus = True
                # Новой позицией рогатки становится позиция курсора
                self.cur_pos = event.pos

            # Если рогатка в фокусе
            if self.focus:
                # Если мышь двигается
                if event.type == pygame.MOUSEMOTION:
                    # Рогатка двигается вместе с ней
                    self.cur_pos = self.check_pos(event.pos)
                # Если ЛКМ отпускается
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    # Рогатка уходит из-под фокуса
                    self.focus = False
                    # Если кнопка отжата в области захвата
                    if self.capture_rect.collidepoint(*event.pos):
                        # Рогатка возвращается в дефолтную позицию
                        self.cur_pos = self.center_pos
                    else:
                        # Рогатка становится неактивной
                        self.active = False

        # Если рогатка неактивна и нажимается пробел
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Рогатка активируется в дефолтной позиции
                self.active = True
                self.cur_pos = self.center_pos
