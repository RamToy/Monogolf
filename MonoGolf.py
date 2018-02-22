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

page_bgcolor = 43, 173, 100
text_color = 255, 255, 255
special_color = 166, 34, 146
unlocked_widget = 250, 100, 0
locked_widget = 140, 140, 140
coin_color = 255, 219, 77

pygame.font.init()
blocked_image = pygame.Surface((110, 60))
blocked_image.fill(locked_widget)
font = pygame.font.Font(None, 80)
font = font.render("10", 5, coin_color)
blocked_image.blit(font, (25, 8))


def create_image_list():
    imgs = []
    for bg, fg, b in colors:
        img = pygame.Surface((110, 60))
        img.fill(bg)
        pygame.draw.circle(img, b, (55, 30), 15, 0)
        imgs.append([img, True if not imgs else False])
    imgs += [[ilya, False], [artem, False]]
    return imgs


def terminate():
    pygame.quit()
    sys.exit()


class Game:
    def __init__(self, surface):
        self.surface = surface
        self.images = create_image_list()
        self.all_levels = [[level_list[i], True if i == 0 else False] for i in range(len(level_list))]
        self.current_level = 0
        self.current_image = 0
        self.current_design = 0
        self.bg_color, self.fg_color, self.ball_color = colors[0]
        self.coins = 10
        self.lives = 30

    def buy_or_select_design(self, index):
        if not self.images[index][1]:
            if self.coins >= 10:
                self.coins -= 10
                self.images[index][1] = True
                return True
        elif self.current_design != index:
            self.current_design = index
            self.bg_color, self.fg_color, self.ball_color = colors[index]
            return True
        return False

    def check_lives(self):
        self.lives -= 1
        if self.lives <= 0:
            self.game_over_page()

    def menu_page(self):
        gui_menu = GUI()
        gui_menu.add_element(Label((270, 30, 150, 100), -1, "mono", (0, 0, 0)))
        gui_menu.add_element(Label((450, 30, 100, 100), -1, "GOLF", text_color))
        play_button = Button((310, 150, 280, 100), unlocked_widget, " Играть", text_color)
        shop_button = Button((310, 320, 280, 100), unlocked_widget, "Магазин", text_color)
        exit_button = Button((670, 620, 170, 60), unlocked_widget, " Выход", text_color)
        developers_button = Button((30, 620, 220, 60), unlocked_widget, "SilverToy58", text_color)
        tutorial_button = Button((280, 490, 350, 80), unlocked_widget, "Информация", text_color)

        gui_menu.add_element(play_button)
        gui_menu.add_element(shop_button)
        gui_menu.add_element(developers_button)
        gui_menu.add_element(tutorial_button)
        gui_menu.add_element(exit_button)

        self.surface.fill(page_bgcolor)
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
        gui_levels = GUI()
        lvl1 = Button((175, 30, 250, 72), unlocked_widget if self.all_levels[0][1] else locked_widget,
                      " Level 1", text_color)
        lvl2 = Button((475, 30, 250, 72), unlocked_widget if self.all_levels[1][1] else locked_widget,
                      " Level 2", text_color)
        lvl3 = Button((175, 150, 250, 72), unlocked_widget if self.all_levels[2][1] else locked_widget,
                      " Level 3", text_color)
        lvl4 = Button((475, 150, 250, 72), unlocked_widget if self.all_levels[3][1] else locked_widget,
                      " Level 4", text_color)
        lvl5 = Button((175, 270, 250, 72), unlocked_widget if self.all_levels[4][1] else locked_widget,
                      " Level 5", text_color)
        lvl6 = Button((475, 270, 250, 72), unlocked_widget if self.all_levels[5][1] else locked_widget,
                      " Level 6", text_color)
        lvl7 = Button((175, 390, 250, 72), unlocked_widget if self.all_levels[6][1] else locked_widget,
                      " Level 7", text_color)
        lvl8 = Button((475, 390, 250, 72), unlocked_widget if self.all_levels[7][1] else locked_widget,
                      " Level 8", text_color)
        lvl9 = Button((175, 510, 250, 72), unlocked_widget if self.all_levels[8][1] else locked_widget,
                      " Level 9", text_color)
        lvl10 = Button((475, 510, 250, 72), unlocked_widget if self.all_levels[9][1] else locked_widget,
                       " Level 10", text_color)
        back = Button((365, 620, 170, 60), unlocked_widget, "  назад", text_color)

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

        self.surface.fill(page_bgcolor)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
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
        gui_shop = GUI()
        gui_shop.add_element(Label((300, 20, 310, 100), special_color, " Магазин", text_color))
        gui_shop.add_element(Label((640, 40, 100, 60), -1, " Золото : {}".format(self.coins), coin_color))
        gui_shop.add_element(Label((400, 625, 100, 60), -1,
                                   " Текущая расцветка : {}".format(self.current_design + 1), special_color))

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

        image_button1 = ImageButton((515, 465, 70, 70), unlocked_widget if self.images[10][1] else locked_widget,
                                    self.images[10][0] if self.images[10][1] else None)
        image_button2 = ImageButton((715, 465, 70, 70), unlocked_widget if self.images[11][1] else locked_widget,
                                    self.images[11][0] if self.images[11][1] else None)
        text_box1 = TextBox((507, 550, 90, 60), [page_bgcolor[c] - 20 for c in range(3)], special_color)
        text_box2 = TextBox((707, 550, 90, 60), [page_bgcolor[c] - 20 for c in range(3)], special_color)
        back = Button((75, 610, 170, 60), unlocked_widget, "  назад", text_color)

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

        self.surface.fill(page_bgcolor)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
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
                self.current_image = 0 if self.current_image == 1 else 1
            elif image_button2.pressed and self.images[11][1]:
                self.current_image = 0 if self.current_image == 2 else 2
            elif text_box1.password == '1337' and text_box1.done and not self.images[10][1]:
                self.images[10][1] = True
                self.store_page()
            elif text_box2.password == '1247' and text_box2.done and not self.images[11][1]:
                self.images[11][1] = True
                self.store_page()

    def guide_page(self):
        gui_guide = GUI()
        back = Button((365, 620, 170, 60), unlocked_widget, "  назад", text_color)
        gui_guide.add_element(back)

        self.surface.fill(page_bgcolor)
        self.surface.blit(load_image('guide.png'), (0, 0))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                gui_guide.get_event(event)

            gui_guide.render(self.surface)
            pygame.display.flip()

            if back.pressed:
                self.menu_page()

    def developers_page(self):
        gui_dev = GUI()
        gui_dev.add_element(Label((70, 70, 200, 60), -1,
                                  "Эта ссылка временно не работает...", special_color))
        gui_dev.add_element(Label((70, 480, 200, 50), -1,
                                  'Нажмите "назад", чтобы выйти в главное меню.', special_color))
        back = Button((75, 610, 170, 60), unlocked_widget, "  назад", text_color)

        gui_dev.add_element(back)

        self.surface.fill(page_bgcolor)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                gui_dev.get_event(event)

            gui_dev.render(self.surface)
            pygame.display.flip()

            if back.pressed:
                self.menu_page()

    def game_page(self, level):
        gui_game = GUI()
        gui_game.add_element(Label((40, 620, 70, 50), -1, 'жизни : {}'.format(self.lives), self.fg_color))
        gui_game.add_element(Label((40, 570, 70, 50), -1, 'уровень {}'.format(self.current_level + 1), self.ball_color))
        pause = Button((835, 635, 40, 40), unlocked_widget, " II", text_color)

        gui_game.add_element(pause)

        clock = pygame.time.Clock()
        slingshot = Slingshot((WIDTH // 2, HEIGHT // 4 * 3), 100, 10, self.fg_color)
        if self.current_image == 0:
            Ball(slingshot, 15, self.ball_color)
        elif self.current_image == 1:
            Ball(slingshot, 15, self.ball_color, ilya)
        elif self.current_image == 2:
            Ball(slingshot, 15, self.ball_color, artem)

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

            gui_game.elements[0].text = 'жизни : {}'.format(self.lives)
            gui_game.elements[1].text = 'уровень {}'.format(self.current_level + 1)

            self.surface.fill(self.bg_color)
            slingshot.render(self.surface)
            rects.draw(self.surface)
            hole.draw(self.surface)
            ball.draw(self.surface)
            gui_game.render(self.surface)
            pygame.display.flip()

            clock.tick(30 + ball.sprite.speed * 3)

            if slingshot.restart:
                slingshot.restart = False
                self.check_lives()

            elif ball.sprite.hitting:
                self.coins += 10
                self.page_between_levels()

            if pause.pressed:
                self.pause_page()
                pause.pressed = False

    def page_between_levels(self):
        self.current_level += 1
        if self.current_level >= 10:
            self.won_page()
        self.all_levels[self.current_level][1] = True

        rects.empty()
        hole.empty()

        gui_lvl = GUI()
        gui_lvl.add_element(Label((150, 50, 620, 100), unlocked_widget, " Уровень пройден", text_color))
        gui_lvl.add_element(Label((300, 170, 350, 300), -1, random.choice(['GG!', 'GJ!', 'WP!']), special_color))
        gui_lvl.add_element(Label((110, 430, 300, 90), -1, "Золото + 10   Всего : {}".format(self.coins), coin_color))
        go_to_menu = Button((100, 550, 260, 100), unlocked_widget, "В меню", text_color)
        go_to_next_level = Button((540, 550, 260, 100), unlocked_widget, " Далее", text_color)

        gui_lvl.add_element(go_to_menu)
        gui_lvl.add_element(go_to_next_level)

        self.surface.fill(page_bgcolor)
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
        gui_pause = GUI()
        gui_pause.add_element(Label((380, 210, 140, 70), special_color, "Пауза", text_color))
        gui_pause.add_element(Label((300, 280, 150, 70), -1, "Начать заново", text_color))
        gui_pause.add_element(Label((370, 340, 150, 70), -1, "[Space]", text_color))
        go_to_menu = Button((500, 430, 130, 50), unlocked_widget, "В меню", text_color)
        back = Button((270, 430, 170, 50), unlocked_widget, "Вернуться", text_color)

        gui_pause.add_element(go_to_menu)
        gui_pause.add_element(back)

        self.surface.fill(special_color, (240, 190, 420, 320))
        self.surface.fill(page_bgcolor, (250, 200, 400, 300))
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
                self.check_lives()
                self.menu_page()
            elif back.pressed:
                break

    def game_over_page(self):
        gui_over = GUI()
        gui_over.add_element(Label((200, 30, 540, 100), special_color, " Вы проиграли!", text_color))
        gui_over.add_element(Label((50, 170, 540, 60), -1, "К сожалению, у Вас закончились жизни", text_color))
        gui_over.add_element(Label((50, 310, 540, 60), -1, "Можете начать новую игру, перейдя в меню", text_color))
        gui_over.add_element(Label((50, 430, 540, 60), -1, "[ Прогресс покупок сохраняется ]", special_color))
        go_to_menu = Button((100, 550, 260, 100), unlocked_widget, "В меню", text_color)

        gui_over.add_element(go_to_menu)

        self.all_levels = [[level_list[i], True if i == 0 else False] for i in range(len(level_list))]
        self.lives = 30
        self.current_level = 0
        rects.empty()
        hole.empty()

        self.surface.fill(page_bgcolor)
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
        gui_won = GUI()
        gui_won.add_element(Label((200, 30, 540, 100), special_color, " Вы победили!", text_color))
        gui_won.add_element(Label((50, 190, 540, 60), -1, "Поздравляем, Вы лучше всех!", text_color))
        gui_won.add_element(Label((50, 310, 540, 60), -1, "Можете продолжить игру, перейдя в меню", text_color))
        gui_won.add_element(Label((50, 430, 540, 60), -1, "[ Прогресс покупок сохраняется ]", special_color))
        go_to_menu = Button((100, 550, 260, 100), unlocked_widget, "В меню", text_color)

        gui_won.add_element(go_to_menu)

        self.lives = 1000
        rects.empty()
        hole.empty()

        self.surface.fill(page_bgcolor)
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
pygame.display.set_caption('MonoGolf')


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as err:
        print('Cannot load file', name)
        raise SystemExit(err)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


pygame.display.set_icon(load_image('MG.png'))
artem = load_image('Artem.png')
ilya = load_image('Ilya.png')

new_game = Game(screen)
new_game.menu_page()

pygame.quit()
