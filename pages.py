import os
import sys
import random
import pygame
from Monogolf.levels import *
from Monogolf.design import colors
from Monogolf.ball import ball, Ball
from Monogolf.slingshot import Slingshot
from Monogolf.sprites import rects, hole
from Monogolf.GUI import GUI, Label, Button, TextBox


page_bgcolor = 43, 173, 100
text_color = 251, 254, 255
special_color = 166, 34, 146
unlocked_widget = 250, 100, 0
locked_widget = 140, 140, 140
golden = 255, 219, 77

phrases = ['GG!', 'GJ!', 'WP!']
all_levels = [[level_1, True], [level_2, False], [level_3, False], [level_4, False], [level_5, False],
              [level_6, False], [level_7, False], [level_8, False], [level_9, False], [level_10, False]]
current_level = 0

coins = 10
lives = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


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


images = []
for i in range(len(colors)):
    bg, fg, b = colors[i]
    img = pygame.Surface((110, 60))
    img.fill(bg)
    pygame.draw.circle(img, b, (55, 30), 15, 0)
    images.append([img, True if i == 0 else False])
ilya = load_image('Ilya.png')
artem = load_image('Artem.png')
images.append([ilya, False])
images.append([artem, False])
current_image = 0
current_design = 0

bg_color, fg_color, ball_color = colors[0]


def terminate():
    pygame.quit()
    sys.exit()


def menu_page(surface):
    gui_menu = GUI()

    gui_menu.add_element(Label((270, 30, 150, 100), -1, "mono", (0, 0, 0)))
    gui_menu.add_element(Label((450, 30, 100, 100), -1, "GOLF", text_color))
    play_button = Button((310, 150, 280, 100), unlocked_widget, " Играть", text_color)
    shop_button = Button((310, 320, 280, 100), unlocked_widget, "Магазин", text_color)
    exit_button = Button((650, 600, 170, 60), unlocked_widget, " Выход", text_color)
    developers_button = Button((50, 630, 170, 30), unlocked_widget, " 2018   SilverToy58", text_color)
    tutorial_button = Button((310, 490, 280, 100), unlocked_widget, "   Гайд", text_color)

    gui_menu.add_element(play_button)
    gui_menu.add_element(shop_button)
    gui_menu.add_element(developers_button)
    gui_menu.add_element(tutorial_button)
    gui_menu.add_element(exit_button)

    surface.fill(page_bgcolor)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            gui_menu.get_event(event)

        gui_menu.render(surface)
        pygame.display.flip()

        if play_button.pressed:
            levels_page(surface)
        elif shop_button.pressed:
            store_page(surface)
        elif developers_button.pressed:
            developers_page(surface)
        elif tutorial_button.pressed:
            guide_page(surface)
        elif exit_button.pressed:
            terminate()


def levels_page(surface):
    global current_level

    gui_levels = GUI()
    lvl1 = Button((175, 30, 250, 72), unlocked_widget if all_levels[0][1] else locked_widget,
                  " Level 1", text_color)
    lvl2 = Button((475, 30, 250, 72), unlocked_widget if all_levels[1][1] else locked_widget,
                  " Level 2", text_color)
    lvl3 = Button((175, 150, 250, 72), unlocked_widget if all_levels[2][1] else locked_widget,
                  " Level 3", text_color)
    lvl4 = Button((475, 150, 250, 72), unlocked_widget if all_levels[3][1] else locked_widget,
                  " Level 4", text_color)
    lvl5 = Button((175, 270, 250, 72), unlocked_widget if all_levels[4][1] else locked_widget,
                  " Level 5", text_color)
    lvl6 = Button((475, 270, 250, 72), unlocked_widget if all_levels[5][1] else locked_widget,
                  " Level 6", text_color)
    lvl7 = Button((175, 390, 250, 72), unlocked_widget if all_levels[6][1] else locked_widget,
                  " Level 7", text_color)
    lvl8 = Button((475, 390, 250, 72), unlocked_widget if all_levels[7][1] else locked_widget,
                  " Level 8", text_color)
    lvl9 = Button((175, 510, 250, 72), unlocked_widget if all_levels[8][1] else locked_widget,
                  " Level 9", text_color)
    lvl10 = Button((475, 510, 250, 72), unlocked_widget if all_levels[9][1] else locked_widget,
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

    surface.fill(page_bgcolor)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            gui_levels.get_event(event)

        gui_levels.render(surface)
        pygame.display.flip()

        if back.pressed:
            menu_page(surface)
        elif lvl1.pressed and all_levels[0][1]:
            current_level = 0
            game_page(surface, level_1)
        elif lvl2.pressed and all_levels[1][1]:
            current_level = 1
            game_page(surface, level_2)
        elif lvl3.pressed and all_levels[2][1]:
            current_level = 2
            game_page(surface, level_3)
        elif lvl4.pressed and all_levels[3][1]:
            current_level = 3
            game_page(surface, level_4)
        elif lvl5.pressed and all_levels[4][1]:
            current_level = 4
            game_page(surface, level_5)
        elif lvl6.pressed and all_levels[5][1]:
            current_level = 5
            game_page(surface, level_6)
        elif lvl7.pressed and all_levels[6][1]:
            current_level = 6
            game_page(surface, level_7)
        elif lvl8.pressed and all_levels[7][1]:
            current_level = 7
            game_page(surface, level_8)
        elif lvl9.pressed and all_levels[8][1]:
            current_level = 8
            game_page(surface, level_9)
        elif lvl10.pressed and all_levels[9][1]:
            current_level = 9
            game_page(surface, level_10)


def store_page(surface):
    global bg_color, fg_color, ball_color, coins, images, current_design, current_image
    gui_shop = GUI()
    gui_shop.add_element(Label((300, 20, 310, 100), special_color, " Магазин", text_color))
    gui_shop.add_element(Label((640, 40, 100, 60), -1, " Золото : {}".format(coins), golden))
    gui_shop.add_element(Label((400, 625, 100, 60), -1,
                               " Текущая раскраска : {}".format(current_design + 1), special_color))
    design1 = Button((75, 150, 150, 100),
                     colors[0][1] if images[0][1] else locked_widget,
                     image=images[0][0] if images[0][1] else None)
    design2 = Button((275, 150, 150, 100),
                     colors[1][1] if images[1][1] else locked_widget,
                     "  10" if not images[1][1] else None,
                     golden if not images[1][1] else None,
                     image=images[1][0] if images[1][1] else None)
    design3 = Button((475, 150, 150, 100),
                     colors[2][1] if images[2][1] else locked_widget,
                     "  10" if not images[2][1] else None,
                     golden if not images[2][1] else None,
                     image=images[2][0] if images[2][1] else None)
    design4 = Button((675, 150, 150, 100),
                     colors[3][1] if images[3][1] else locked_widget,
                     "  10" if not images[3][1] else None,
                     golden if not images[3][1] else None,
                     image=images[3][0] if images[3][1] else None)
    design5 = Button((75, 300, 150, 100),
                     colors[4][1] if images[4][1] else locked_widget,
                     "  10" if not images[4][1] else None,
                     golden if not images[4][1] else None,
                     image=images[4][0] if images[4][1] else None)
    design6 = Button((275, 300, 150, 100),
                     colors[5][1] if images[5][1] else locked_widget,
                     "  10" if not images[5][1] else None,
                     golden if not images[5][1] else None,
                     image=images[5][0] if images[5][1] else None)
    design7 = Button((475, 300, 150, 100),
                     colors[6][1] if images[6][1] else locked_widget,
                     "  10" if not images[6][1] else None,
                     golden if not images[6][1] else None,
                     image=images[6][0] if images[6][1] else None)
    design8 = Button((675, 300, 150, 100),
                     colors[7][1] if images[7][1] else locked_widget,
                     "  10" if not images[7][1] else None,
                     golden if not images[7][1] else None,
                     image=images[7][0] if images[7][1] else None)
    design9 = Button((75, 450, 150, 100),
                     colors[8][1] if images[8][1] else locked_widget,
                     "  10" if not images[8][1] else None,
                     golden if not images[8][1] else None,
                     image=images[8][0] if images[8][1] else None)
    design10 = Button((275, 450, 150, 100),
                      colors[9][1] if images[9][1] else locked_widget,
                      "  10" if not images[9][1] else None,
                      golden if not images[9][1] else None,
                      image=images[9][0] if images[9][1] else None)
    design11 = Button((515, 465, 70, 70),
                      unlocked_widget if images[10][1] else locked_widget, None, None,
                      image=images[10][0] if images[10][1] else None)
    design12 = Button((715, 465, 70, 70),
                      unlocked_widget if images[11][1] else locked_widget, None, None,
                      image=images[11][0] if images[11][1] else None)
    text_box1 = TextBox((507, 550, 90, 60), [page_bgcolor[c] - 20 for c in range(3)], special_color)
    text_box2 = TextBox((707, 550, 90, 60), [page_bgcolor[c] - 20 for c in range(3)], special_color)
    back = Button((75, 610, 170, 60), unlocked_widget, "  назад", text_color)

    gui_shop.add_element(design1)
    gui_shop.add_element(design2)
    gui_shop.add_element(design3)
    gui_shop.add_element(design4)
    gui_shop.add_element(design5)
    gui_shop.add_element(design6)
    gui_shop.add_element(design7)
    gui_shop.add_element(design8)
    gui_shop.add_element(design9)
    gui_shop.add_element(design10)
    gui_shop.add_element(design11)
    gui_shop.add_element(design12)
    gui_shop.add_element(text_box1)
    gui_shop.add_element(text_box2)
    gui_shop.add_element(back)

    surface.fill(page_bgcolor)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            gui_shop.get_event(event)

        gui_shop.render(surface)
        pygame.display.flip()

        if back.pressed:
            menu_page(surface)
        elif design1.pressed:
            bg_color, fg_color, ball_color = colors[0]
            current_design = 0
            store_page(surface)
        elif design2.pressed:
            if not images[1][1]:
                if coins >= 10:
                    coins -= 10
                    images[1][1] = True
                    store_page(surface)
            else:
                current_design = 1
                bg_color, fg_color, ball_color = colors[1]
                store_page(surface)

        elif design3.pressed:
            if not images[2][1]:
                if coins >= 10:
                    coins -= 10
                    images[2][1] = True
                    store_page(surface)
            else:
                current_design = 2
                bg_color, fg_color, ball_color = colors[2]
                store_page(surface)
        elif design4.pressed:
            if not images[3][1]:
                if coins >= 10:
                    coins -= 10
                    images[3][1] = True
                    store_page(surface)
            else:
                current_design = 3
                bg_color, fg_color, ball_color = colors[3]
                store_page(surface)
        elif design5.pressed:
            if not images[4][1]:
                if coins >= 10:
                    coins -= 10
                    images[4][1] = True
                    store_page(surface)
            else:
                current_design = 4
                bg_color, fg_color, ball_color = colors[4]
                store_page(surface)
        elif design6.pressed:
            if not images[5][1]:
                if coins >= 10:
                    coins -= 10
                    images[5][1] = True
                    store_page(surface)
            else:
                current_design = 5
                bg_color, fg_color, ball_color = colors[5]
                store_page(surface)
        elif design7.pressed:
            if not images[6][1]:
                if coins >= 10:
                    coins -= 10
                    images[6][1] = True
                    store_page(surface)
            else:
                current_design = 6
                bg_color, fg_color, ball_color = colors[6]
                store_page(surface)
        elif design8.pressed:
            if not images[7][1]:
                if coins >= 10:
                    coins -= 10
                    images[7][1] = True
                    store_page(surface)
            else:
                current_design = 7
                bg_color, fg_color, ball_color = colors[7]
                store_page(surface)
        elif design9.pressed:
            if not images[8][1]:
                if coins >= 10:
                    coins -= 10
                    images[8][1] = True
                    store_page(surface)
            else:
                current_design = 8
                bg_color, fg_color, ball_color = colors[8]
                store_page(surface)
        elif design10.pressed:
            if not images[9][1]:
                if coins >= 10:
                    coins -= 10
                    images[9][1] = True
                    store_page(surface)
            else:
                current_design = 9
                bg_color, fg_color, ball_color = colors[9]
                store_page(surface)
        elif design11.pressed and images[10][1]:
                if current_image == 1:
                    current_image = 0
                else:
                    current_image = 1
        elif design12.pressed and images[11][1]:
                if current_image == 2:
                    current_image = 0
                else:
                    current_image = 2
        elif text_box1.password == '1337' and text_box1.done and not images[10][1]:
            images[10][1] = True
            store_page(surface)
        elif text_box2.password == '1247' and text_box2.done and not images[11][1]:
            images[11][1] = True
            store_page(surface)


def developers_page(surface):
    gui_dev = GUI()
    gui_dev.add_element(Label((70, 70, 200, 60), -1, "Эта ссылка временно не работает...", special_color))
    gui_dev.add_element(Label((70, 480, 200, 50), -1, 'Нажмите "назад",', special_color))
    gui_dev.add_element(Label((70, 520, 200, 50), -1, "чтобы выйти в главное меню.", special_color))
    back = Button((75, 610, 170, 60), unlocked_widget, "  назад", text_color)

    gui_dev.add_element(back)

    surface.fill(page_bgcolor)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            gui_dev.get_event(event)

        gui_dev.render(surface)
        pygame.display.flip()

        if back.pressed:
            menu_page(surface)


def guide_page(surface):
    gui_guide = GUI()
    gui_guide.add_element(Label((30, 70, 200, 50), -1, '"пробел" - начать запуск шарика заново', special_color))
    gui_guide.add_element(Label((30, 200, 200, 50), -1, '"пауза" в правом нижнем углу', special_color))
    gui_guide.add_element(Label((30, 330, 200, 50), -1, '"левая кнопка мыши" - управление запуском шарика', special_color))
    back = Button((300, 640, 150, 40), unlocked_widget, "     назад", text_color)
    gui_guide.add_element(back)

    surface.fill(page_bgcolor)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            gui_guide.get_event(event)

        gui_guide.render(surface)
        pygame.display.flip()

        if back.pressed:
            menu_page(surface)


def page_between_levels(surface):
    global current_level, all_levels
    current_level += 1
    if current_level >= 10:
        won_page(screen)
    all_levels[current_level][1] = True

    gui_lvl = GUI()
    gui_lvl.add_element(Label((150, 50, 620, 100), unlocked_widget, " Уровень пройден", text_color))
    gui_lvl.add_element(Label((300, 170, 350, 300), -1, random.choice(phrases), special_color))
    gui_lvl.add_element(Label((110, 430, 300, 90), -1, "Золото + 10   Всего : {}".format(coins), golden))
    go_to_menu = Button((100, 550, 260, 100), unlocked_widget, "В меню", text_color)
    go_to_next_level = Button((540, 550, 260, 100), unlocked_widget, " Далее", text_color)

    gui_lvl.add_element(go_to_menu)
    gui_lvl.add_element(go_to_next_level)

    surface.fill(page_bgcolor)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            gui_lvl.get_event(event)

        gui_lvl.render(surface)
        pygame.display.flip()

        if go_to_menu.pressed:
            menu_page(surface)
        elif go_to_next_level.pressed:
            game_page(surface, all_levels[current_level][0])


def game_over_page(surface):
    global all_levels, lives, current_level
    gui_over = GUI()
    gui_over.add_element(Label((200, 30, 540, 100), special_color, " Вы проиграли!", text_color))
    gui_over.add_element(Label((50, 170, 540, 60), -1, "К сожалению, у Вас закончились жизни", text_color))
    gui_over.add_element(Label((50, 310, 540, 60), -1, "Можете начать новую игру, перейдя в меню", text_color))
    gui_over.add_element(Label((50, 430, 540, 60), -1, "[ Прогресс покупок сохраняется ]", special_color))
    go_to_menu = Button((100, 550, 260, 100), unlocked_widget, "В меню", text_color)

    gui_over.add_element(go_to_menu)

    all_levels = [[level_1, True], [level_2, False], [level_3, False], [level_4, False], [level_5, False],
                  [level_6, False], [level_7, False], [level_8, False], [level_9, False], [level_10, True]]
    lives = 30
    current_level = 0
    rects.empty()
    hole.empty()

    surface.fill(page_bgcolor)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            gui_over.get_event(event)

        gui_over.render(surface)
        pygame.display.flip()

        if go_to_menu.pressed:
            menu_page(surface)


def won_page(surface):
    global lives
    gui_won = GUI()
    gui_won.add_element(Label((200, 30, 540, 100), special_color, " Вы победили!", text_color))
    gui_won.add_element(Label((50, 190, 540, 60), -1, "Поздравляем, Вы лучше всех!", text_color))
    gui_won.add_element(Label((50, 310, 540, 60), -1, "Можете продолжить игру, перейдя в меню", text_color))
    gui_won.add_element(Label((50, 430, 540, 60), -1, "[ Прогресс покупок сохраняется ]", special_color))
    go_to_menu = Button((100, 550, 260, 100), unlocked_widget, "В меню", text_color)

    gui_won.add_element(go_to_menu)

    lives = 1000

    surface.fill(page_bgcolor)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            gui_won.get_event(event)

        gui_won.render(surface)
        pygame.display.flip()

        if go_to_menu.pressed:
            rects.empty()
            hole.empty()
            menu_page(surface)


def pause_page(surface):
    gui_pause = GUI()
    gui_pause.add_element(Label((380, 210, 140, 70), special_color, "Пауза", text_color))
    gui_pause.add_element(Label((310, 300, 150, 80), -1, "Золото : {}".format(coins), golden))
    go_to_menu = Button((500, 430, 130, 50), unlocked_widget, "В меню", text_color)
    back = Button((270, 430, 170, 50), unlocked_widget, "Вернуться", text_color)

    gui_pause.add_element(go_to_menu)
    gui_pause.add_element(back)

    surface.fill(page_bgcolor, (250, 200, 400, 300))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            gui_pause.get_event(event)

        gui_pause.render(surface)
        pygame.display.flip()

        if go_to_menu.pressed:
            menu_page(surface)
        elif back.pressed:
            break


def game_page(surface, level):
    global rects, hole, coins, lives
    gui_game = GUI()
    gui_game.add_element(Label((40, 620, 70, 50), -1, 'жизни : {}'.format(lives), fg_color))
    gui_game.add_element(Label((40, 570, 70, 50), -1, 'уровень {}'.format(current_level + 1), ball_color))
    pause = Button((830, 630, 40, 40), unlocked_widget, " ||", text_color)

    gui_game.add_element(pause)

    clock = pygame.time.Clock()
    slingshot = Slingshot((WIDTH // 2, HEIGHT // 4 * 3), 100, 10, fg_color)
    if current_image == 0:
        Ball(slingshot, 15, ball_color)
    elif current_image == 1:
        Ball(slingshot, 15, ball_color, ilya)
    elif current_image == 2:
        Ball(slingshot, 15, ball_color, artem)

    level(fg_color, ball_color)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            gui_game.get_event(event)
            slingshot.get_event(event)

        ball.update()
        gui_game.elements[0].text = 'жизни : {}'.format(lives)
        gui_game.elements[1].text = 'уровень {}'.format(current_level + 1)
        surface.fill(bg_color)
        slingshot.render(surface)
        rects.draw(surface)
        hole.draw(surface)
        ball.draw(surface)
        gui_game.render(surface)
        pygame.display.flip()
        clock.tick(30 + ball.sprite.speed * 3)

        if slingshot.restart:
            slingshot.restart = False
            lives -= 1
            if lives <= 0:
                game_over_page(surface)

        elif ball.sprite.hitting:
            coins += 10
            rects.empty()
            hole.empty()
            page_between_levels(surface)

        if pause.pressed:
            pause_page(surface)
            pause.pressed = False


menu_page(screen)
pygame.quit()
