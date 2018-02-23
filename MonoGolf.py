import os
import sys
import random
import pygame
from Monogolf.levels import *
from Monogolf.settings import *
from Monogolf.design import colors
from Monogolf.ball import ball, Ball
from Monogolf.slingshot import Slingshot
from Monogolf.sprites import rects, hole
from Monogolf.GUI import GUI, Label, Button, ImageButton, TextBox

locked_widget = 140, 140, 140
coin_color = 255, 219, 77

# Создание экземпляра картинки "заблокированной раскраски"
pygame.font.init()
blocked_image = pygame.Surface((110, 60))
blocked_image.fill(locked_widget)
font = pygame.font.Font(None, 80)
font = font.render("10", 5, coin_color)
blocked_image.blit(font, (25, 8))


def create_image_list():
    """ Создание картинок с сочетаниями цветов """
    imgs = []
    for color_set in colors:
        bg, fg, b, nbg, nfg = color_set
        img = pygame.Surface((110, 60))
        img.fill(bg)
        pygame.draw.circle(img, b, (55, 30), 15, 0)
        # Значения добавляются в парах: [картинка] - [флаг разблокированности]
        imgs.append([img, True if not imgs else False])
    # 2 лика величайших
    imgs += [[ilya, False], [artem, False]]
    return imgs


def terminate():
    """ Выход из программы """
    pygame.quit()
    sys.exit()


class Game:
    """ Основной класс игры """

    def __init__(self, surface):
        # Основной холст
        self.surface = surface
        # Картинки раскрасок
        self.images = create_image_list()
        # Уровни представляют собой пары значений (аналогично create_image_list)
        self.all_levels = [[level_list[i], True if i == 9 else False] for i in range(len(level_list))]
        # Текущий уровень
        self.current_level = 0
        # Текущая раскраска
        self.current_design = 0
        # Текущая картинка шарика
        self.current_image = None
        # Текущие цвета
        self.bg_color, self.fg_color, self.ball_color, \
            self.n_bg_color, self.n_fg_color = colors[0]
        # Золото
        self.coins = 10
        # Жизни
        self.lives = 1

    def buy_or_select_design(self, index):
        """ Обработка взаимодействий с конпками магазина """
        # Если раскраска не разблокирована и надо ее купить
        if not self.images[index][1]:
            # Проверка и изъятие денежных средств
            if self.coins >= 10:
                self.coins -= 10
                # Разблокировка
                self.images[index][1] = True
                # Новая раскраска - теперь текущая раскраска
                self.current_design = index
                self.bg_color, self.fg_color, self.ball_color, \
                    self.n_bg_color, self.n_fg_color = colors[index]
                return True
        # Если раскраска уже разблокированна и надо ее выбрать
        elif self.current_design != index:
            self.current_design = index
            self.bg_color, self.fg_color, self.ball_color,\
                self.n_bg_color, self.n_fg_color = colors[index]
            return True
        return False

    def check_lives(self):
        """ Проверка жизней """
        self.lives -= 1
        if self.lives <= 0:
            self.lose_page()

    def menu_page(self):
        """ Главное меню """
        gui_menu = GUI()
        gui_menu.add_element(Label((270, 30, 150, 100), -1, "mono", self.fg_color))
        gui_menu.add_element(Label((450, 30, 100, 100), -1, "GOLF", self.ball_color))
        play_button = Button((310, 150, 280, 100), self.fg_color, " Играть", self.n_bg_color)
        shop_button = Button((310, 320, 280, 100), self.fg_color, "Магазин", self.n_bg_color)
        exit_button = Button((670, 620, 170, 60), self.fg_color, " Выход", self.n_bg_color)
        developers_button = Button((30, 620, 220, 60), self.fg_color, "SilverToy58", self.n_bg_color)
        tutorial_button = Button((280, 490, 350, 80), self.fg_color, "Информация", self.n_bg_color)

        gui_menu.add_element(play_button)
        gui_menu.add_element(shop_button)
        gui_menu.add_element(developers_button)
        gui_menu.add_element(tutorial_button)
        gui_menu.add_element(exit_button)

        self.surface.fill(self.bg_color)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                gui_menu.get_event(event)

            gui_menu.render(self.surface)
            pygame.display.flip()

            if play_button.pressed:
                self.levels_page()
            elif shop_button.pressed:
                self.store_page()
            elif developers_button.pressed:
                self.developers_page()
            elif tutorial_button.pressed:
                self.guide_page()
            elif exit_button.pressed:
                terminate()

    def levels_page(self):
        """ Страница выбора уровня """
        gui_levels = GUI()
        lvl1 = Button((175, 30, 250, 72), self.fg_color if self.all_levels[0][1] else locked_widget,
                      " Level 1", self.n_bg_color)
        lvl2 = Button((475, 30, 250, 72), self.fg_color if self.all_levels[1][1] else locked_widget,
                      " Level 2", self.n_bg_color)
        lvl3 = Button((175, 150, 250, 72), self.fg_color if self.all_levels[2][1] else locked_widget,
                      " Level 3", self.n_bg_color)
        lvl4 = Button((475, 150, 250, 72), self.fg_color if self.all_levels[3][1] else locked_widget,
                      " Level 4", self.n_bg_color)
        lvl5 = Button((175, 270, 250, 72), self.fg_color if self.all_levels[4][1] else locked_widget,
                      " Level 5", self.n_bg_color)
        lvl6 = Button((475, 270, 250, 72), self.fg_color if self.all_levels[5][1] else locked_widget,
                      " Level 6", self.n_bg_color)
        lvl7 = Button((175, 390, 250, 72), self.fg_color if self.all_levels[6][1] else locked_widget,
                      " Level 7", self.n_bg_color)
        lvl8 = Button((475, 390, 250, 72), self.fg_color if self.all_levels[7][1] else locked_widget,
                      " Level 8", self.n_bg_color)
        lvl9 = Button((175, 510, 250, 72), self.fg_color if self.all_levels[8][1] else locked_widget,
                      " Level 9", self.n_bg_color)
        lvl10 = Button((475, 510, 250, 72), self.fg_color if self.all_levels[9][1] else locked_widget,
                       " Level 10", self.n_bg_color)
        back = Button((365, 620, 170, 60), self.fg_color, "  назад", self.n_bg_color)

        gui_levels.add_element(lvl1)
        gui_levels.add_element(lvl2)
        gui_levels.add_element(lvl3)
        gui_levels.add_element(lvl4)
        gui_levels.add_element(lvl5)
        gui_levels.add_element(lvl6)
        gui_levels.add_element(lvl7)
        gui_levels.add_element(lvl8)
        gui_levels.add_element(lvl9)
        gui_levels.add_element(lvl10)
        gui_levels.add_element(back)

        self.surface.fill(self.bg_color)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    back.pressed = True
                gui_levels.get_event(event)

            gui_levels.render(self.surface)
            pygame.display.flip()

            if back.pressed:
                self.menu_page()
            elif lvl1.pressed and self.all_levels[0][1]:
                self.current_level = 0
                self.game_page(level_1)
            elif lvl2.pressed and self.all_levels[1][1]:
                self.current_level = 1
                self.game_page(level_2)
            elif lvl3.pressed and self.all_levels[2][1]:
                self.current_level = 2
                self.game_page(level_3)
            elif lvl4.pressed and self.all_levels[3][1]:
                self.current_level = 3
                self.game_page(level_4)
            elif lvl5.pressed and self.all_levels[4][1]:
                self.current_level = 4
                self.game_page(level_5)
            elif lvl6.pressed and self.all_levels[5][1]:
                self.current_level = 5
                self.game_page(level_6)
            elif lvl7.pressed and self.all_levels[6][1]:
                self.current_level = 6
                self.game_page(level_7)
            elif lvl8.pressed and self.all_levels[7][1]:
                self.current_level = 7
                self.game_page(level_8)
            elif lvl9.pressed and self.all_levels[8][1]:
                self.current_level = 8
                self.game_page(level_9)
            elif lvl10.pressed and self.all_levels[9][1]:
                self.current_level = 9
                self.game_page(level_10)

    def store_page(self):
        """ Магазин """
        gui_shop = GUI()
        gui_shop.add_element(Label((300, 20, 310, 100), self.ball_color, " Магазин", self.fg_color))
        gui_shop.add_element(Label((640, 40, 100, 60), -1, " Золото : {}".format(self.coins), coin_color))
        gui_shop.add_element(Label((640, 475, 20, 50), -1,
                                   "1" if self.current_image == ilya else ("2" if self.current_image == artem else ""),
                                   self.ball_color))
        gui_shop.add_element(Label((400, 625, 100, 60), -1,
                                   " Текущая расцветка : {}".format(self.current_design + 1), self.ball_color))

        design0 = ImageButton((75, 150, 150, 100), colors[0][1], self.images[0][0])
        design1 = ImageButton((275, 150, 150, 100),
                              colors[1][1] if self.images[1][1] else locked_widget,
                              self.images[1][0] if self.images[1][1] else blocked_image)
        design2 = ImageButton((475, 150, 150, 100),
                              colors[2][1] if self.images[2][1] else locked_widget,
                              self.images[2][0] if self.images[2][1] else blocked_image)
        design3 = ImageButton((675, 150, 150, 100),
                              colors[3][1] if self.images[3][1] else locked_widget,
                              self.images[3][0] if self.images[3][1] else blocked_image)
        design4 = ImageButton((75, 300, 150, 100),
                              colors[4][1] if self.images[4][1] else locked_widget,
                              self.images[4][0] if self.images[4][1] else blocked_image)
        design5 = ImageButton((275, 300, 150, 100),
                              colors[5][1] if self.images[5][1] else locked_widget,
                              self.images[5][0] if self.images[5][1] else blocked_image)
        design6 = ImageButton((475, 300, 150, 100),
                              colors[6][1] if self.images[6][1] else locked_widget,
                              self.images[6][0] if self.images[6][1] else blocked_image)
        design7 = ImageButton((675, 300, 150, 100),
                              colors[7][1] if self.images[7][1] else locked_widget,
                              self.images[7][0] if self.images[7][1] else blocked_image)
        design8 = ImageButton((75, 450, 150, 100),
                              colors[8][1] if self.images[8][1] else locked_widget,
                              self.images[8][0] if self.images[8][1] else blocked_image)
        design9 = ImageButton((275, 450, 150, 100),
                              colors[9][1] if self.images[9][1] else locked_widget,
                              self.images[9][0] if self.images[9][1] else blocked_image)

        image_button1 = ImageButton((515, 465, 70, 70), self.fg_color if self.images[10][1] else locked_widget,
                                    self.images[10][0] if self.images[10][1] else None)
        image_button2 = ImageButton((715, 465, 70, 70), self.fg_color if self.images[11][1] else locked_widget,
                                    self.images[11][0] if self.images[11][1] else None)
        text_box1 = TextBox((505, 550, 90, 60), [self.bg_color[c] + 20 for c in range(3)], self.ball_color)
        text_box2 = TextBox((705, 550, 90, 60), [self.bg_color[c] + 20 for c in range(3)], self.ball_color)
        back = Button((75, 610, 170, 60), self.fg_color, "  назад", self.n_bg_color)

        gui_shop.add_element(design0)
        gui_shop.add_element(design1)
        gui_shop.add_element(design2)
        gui_shop.add_element(design3)
        gui_shop.add_element(design4)
        gui_shop.add_element(design5)
        gui_shop.add_element(design6)
        gui_shop.add_element(design7)
        gui_shop.add_element(design8)
        gui_shop.add_element(design9)
        gui_shop.add_element(image_button1)
        gui_shop.add_element(image_button2)
        gui_shop.add_element(text_box1)
        gui_shop.add_element(text_box2)
        gui_shop.add_element(back)

        self.surface.fill(self.bg_color)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    back.pressed = True
                gui_shop.get_event(event)

            gui_shop.render(self.surface)
            pygame.display.flip()

            if back.pressed:
                self.menu_page()
            elif design0.pressed:
                if self.buy_or_select_design(0):
                    self.store_page()
            elif design1.pressed:
                if self.buy_or_select_design(1):
                    self.store_page()
            elif design2.pressed:
                if self.buy_or_select_design(2):
                    self.store_page()
            elif design3.pressed:
                if self.buy_or_select_design(3):
                    self.store_page()
            elif design4.pressed:
                if self.buy_or_select_design(4):
                    self.store_page()
            elif design5.pressed:
                if self.buy_or_select_design(5):
                    self.store_page()
            elif design6.pressed:
                if self.buy_or_select_design(6):
                    self.store_page()
            elif design7.pressed:
                if self.buy_or_select_design(7):
                    self.store_page()
            elif design8.pressed:
                if self.buy_or_select_design(8):
                    self.store_page()
            elif design9.pressed:
                if self.buy_or_select_design(9):
                    self.store_page()
            elif image_button1.pressed and self.images[10][1]:
                self.current_image = None if self.current_image == ilya else ilya
                self.store_page()
            elif image_button2.pressed and self.images[11][1]:
                self.current_image = None if self.current_image == artem else artem
                self.store_page()
            elif text_box1.password == "1337" and text_box1.done and not self.images[10][1]:
                self.images[10][1] = True
                self.current_image = ilya           # Защита 10/10
                self.store_page()
            elif text_box2.password == "1247" and text_box2.done and not self.images[11][1]:
                self.images[11][1] = True
                self.current_image = artem
                self.store_page()

    def guide_page(self):
        """ Информация """
        gui_guide = GUI()
        back = Button((365, 620, 170, 60), self.fg_color, "  назад", self.n_bg_color)
        gui_guide.add_element(back)

        self.surface.fill(self.bg_color)
        self.surface.blit(guide, (0, 0))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    back.pressed = True
                gui_guide.get_event(event)

            gui_guide.render(self.surface)
            pygame.display.flip()

            if back.pressed:
                self.menu_page()

    def developers_page(self):
        """ Страница разработчиков """
        gui_dev = GUI()
        gui_dev.add_element(Label((70, 70, 200, 60), -1,
                                  "Эта ссылка временно не работает...", self.ball_color))
        gui_dev.add_element(Label((70, 480, 200, 50), -1,
                                  'Нажмите "назад", чтобы выйти в главное меню.', self.ball_color))
        back = Button((75, 610, 170, 60), self.fg_color, "  назад", self.n_bg_color)

        gui_dev.add_element(back)

        self.surface.fill(self.bg_color)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    back.pressed = True
                gui_dev.get_event(event)

            gui_dev.render(self.surface)
            pygame.display.flip()

            if back.pressed:
                self.menu_page()

    def game_page(self, level):
        """ Основной игровой цикл """
        gui_game = GUI()
        gui_game.add_element(Label((40, 620, 70, 50), -1, "жизни : {}".format(self.lives), self.fg_color))
        gui_game.add_element(Label((40, 570, 70, 50), -1, "уровень {}".format(self.current_level + 1), self.ball_color))
        pause = Button((835, 635, 40, 40), self.n_fg_color, " II", self.n_bg_color)

        gui_game.add_element(pause)

        clock = pygame.time.Clock()
        slingshot = Slingshot((WIDTH // 2, HEIGHT // 4 * 3), 100, 10, self.fg_color)
        # Проверка изображений
        if self.current_image is None:
            Ball(slingshot, 15, self.ball_color)
        else:
            Ball(slingshot, 15, self.ball_color, self.current_image)
        # Вызов уровня
        level(self.fg_color, self.ball_color)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pause.pressed = True
                gui_game.get_event(event)
                slingshot.get_event(event)

            ball.update()
            # Обновление показателей
            gui_game.elements[0].text = "жизни : {}".format(self.lives)
            gui_game.elements[1].text = "уровень {}".format(self.current_level + 1)
            # Отрисовка
            self.surface.fill(self.bg_color)
            slingshot.render(self.surface)
            rects.draw(self.surface)
            hole.draw(self.surface)
            ball.draw(self.surface)
            gui_game.render(self.surface)
            pygame.display.flip()

            clock.tick(30 + ball.sprite.speed * 3)
            # Обработка перезапуска
            if slingshot.restart:
                slingshot.restart = False
                self.check_lives()
            # Обработка попадания
            elif ball.sprite.hitting:
                self.coins += 10
                self.page_between_levels()
            # Обработка паузы
            if pause.pressed:
                self.pause_page()
                pause.pressed = False

    def page_between_levels(self):
        """ Страница при переходе между уровнями """
        self.current_level += 1
        if self.current_level >= 10:
            self.won_page()
        self.all_levels[self.current_level][1] = True

        # Очистка старого поля
        rects.empty()
        hole.empty()

        gui_lvl = GUI()
        gui_lvl.add_element(Label((150, 50, 620, 100), self.fg_color, " Уровень пройден", self.n_bg_color))
        gui_lvl.add_element(Label((300, 170, 350, 300), -1, random.choice(["GG!", "GJ!", "WP!"]), self.ball_color))
        gui_lvl.add_element(Label((110, 430, 300, 90), -1, "Золото + 10   Всего : {}".format(self.coins),
                                  self.ball_color if self.current_design == 9 else coin_color))
        go_to_menu = Button((100, 550, 260, 100), self.fg_color, "В меню", self.n_bg_color)
        go_to_next_level = Button((540, 550, 260, 100), self.fg_color, " Далее", self.n_bg_color)

        gui_lvl.add_element(go_to_menu)
        gui_lvl.add_element(go_to_next_level)

        self.surface.fill(self.bg_color)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                gui_lvl.get_event(event)

            gui_lvl.render(self.surface)
            pygame.display.flip()

            if go_to_menu.pressed:
                self.menu_page()
            elif go_to_next_level.pressed:
                self.game_page(self.all_levels[self.current_level][0])

    def pause_page(self):
        """ Пауза """
        gui_pause = GUI()
        gui_pause.add_element(Label((375, 210, 160, 70), self.n_fg_color, " Пауза", self.n_bg_color))
        gui_pause.add_element(Label((300, 280, 150, 70), -1, "Начать заново", self.n_bg_color))
        gui_pause.add_element(Label((370, 340, 150, 70), -1, "[Space]", self.n_bg_color))
        go_to_menu = Button((500, 430, 130, 50), self.fg_color, "В меню", self.n_bg_color)
        back = Button((270, 430, 170, 50), self.fg_color, "Вернуться", self.n_bg_color)

        gui_pause.add_element(go_to_menu)
        gui_pause.add_element(back)

        self.surface.fill(self.n_fg_color, (240, 190, 420, 320))
        self.surface.fill([self.bg_color[c] - 10 for c in range(3)], (250, 200, 400, 300))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    back.pressed = True
                gui_pause.get_event(event)

            gui_pause.render(self.surface)
            pygame.display.flip()

            if go_to_menu.pressed:
                # Если игрок выходит в меню, то отнимается 1 жизнь
                self.check_lives()
                self.menu_page()
            elif back.pressed:
                break

    def lose_page(self):
        """ Проигрыш """
        gui_over = GUI()
        gui_over.add_element(Label((200, 30, 540, 100), self.ball_color, " Вы проиграли!", self.fg_color))
        gui_over.add_element(Label((150, 180, 540, 50), -1, "К сожалению, у Вас закончились жизни", self.fg_color))
        gui_over.add_element(Label((120, 230, 540, 50), -1,
                                   "Можете начать новую игру, перейдя в меню", self.fg_color))
        gui_over.add_element(Label((140, 310, 540, 60), -1, "[ Прогресс покупок сохраняется ]", self.ball_color))
        go_to_menu = Button((100, 550, 260, 100), self.fg_color, "В меню", self.n_bg_color)

        gui_over.add_element(go_to_menu)

        # Игра начинается заново (игровые показатели обнуляются)
        self.all_levels = [[level_list[i], True if i == 0 else False] for i in range(len(level_list))]
        self.lives = 30
        self.current_level = 0
        rects.empty()
        hole.empty()

        self.surface.fill(self.bg_color)
        screen.blit(aquaman, (550, 370))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                gui_over.get_event(event)

            gui_over.render(self.surface)
            pygame.display.flip()

            if go_to_menu.pressed:
                self.menu_page()

    def won_page(self):
        """ Победа """
        gui_won = GUI()
        gui_won.add_element(Label((200, 30, 540, 100), self.ball_color, " Вы победили!", self.fg_color))
        gui_won.add_element(Label((230, 180, 540, 50), -1, "Поздравляем, Вы лучше всех!", self.fg_color))
        gui_won.add_element(Label((130, 230, 540, 50), -1, "Можете продолжить игру, перейдя в меню", self.fg_color))
        gui_won.add_element(Label((140, 360, 540, 60), -1, "[ Прогресс покупок сохраняется ]", self.ball_color))
        go_to_menu = Button((100, 550, 260, 100), self.fg_color, "В меню", self.n_bg_color)

        gui_won.add_element(go_to_menu)

        # Надо вставить сюда ачивку
        self.lives = 1000
        rects.empty()
        hole.empty()

        self.surface.fill(self.bg_color)
        screen.blit(wildsponge, (450, 440))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                gui_won.get_event(event)

            gui_won.render(self.surface)
            pygame.display.flip()

            if go_to_menu.pressed:
                self.menu_page()


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MonoGolf")


def load_image(name, colorkey=None):
    fullname = os.path.join("data", name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as err:
        print("Cannot load file", name)
        raise SystemExit(err)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


pygame.display.set_icon(load_image("MG.png"))
guide = load_image("guide.png")
artem = load_image("Artem.png")
ilya = load_image("Ilya.png")
aquaman = load_image("aquaman.png")
wildsponge = load_image("wildsponge.png")

new_game = Game(screen)
new_game.menu_page()

pygame.quit()
