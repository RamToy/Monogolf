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

phrases = ['GG!', 'GJ!', 'WP!']
all_levels = [[level_1, True], [level_2, False], [level_3, False], [level_4, False], [level_5, True],
              [level_6, False], [level_7, False], [level_8, False], [level_9, False], [level_10, False]]
current_level = 0

money = 10

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
fps = 60


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


ilya = load_image('Ilya.png')
artem = load_image('Artem.png')

images = []
for i in range(len(colors)):
    bg, fg, b = colors[i]
    img = pygame.Surface((110, 60))
    img.fill(bg)
    pygame.draw.circle(img, b, (55, 30), 15, 0)
    images.append([img, True if i == 0 else False, True if i == 0 else False])
images.append([ilya, False, False])
images.append([artem, False, False])
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
    exit_button = Button((310, 490, 280, 100), unlocked_widget, " Выход", text_color)
    developers = Button((365, 640, 165, 30), unlocked_widget, " 2018   SilverToy58", text_color)

    gui_menu.add_element(play_button)
    gui_menu.add_element(shop_button)
    gui_menu.add_element(developers)
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
        elif developers.pressed:
            developers_page(surface)
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
    global bg_color, fg_color, ball_color
    gui_shop = GUI()
    gui_shop.add_element(Label((300, 20, 310, 100), special_color, " Магазин", text_color))
    design1 = Button((75, 150, 150, 100),
                     colors[0][1] if images[0][1] else locked_widget,
                     image=images[0][0] if images[0][1] else None)
    design2 = Button((275, 150, 150, 100),
                     colors[1][1] if images[1][1] else locked_widget,
                     "  10" if not images[1][1] else None,
                     (255, 219, 77) if not images[1][1] else None,
                     images[1][0] if images[1][1] else None)
    design3 = Button((475, 150, 150, 100),
                     colors[2][1] if images[2][1] else locked_widget,
                     "  10" if not images[2][1] else None,
                     (255, 219, 77) if not images[1][1] else None,
                     images[2][0] if images[2][1] else None)
    design4 = Button((675, 150, 150, 100),
                     colors[3][1] if images[3][1] else locked_widget,
                     "  10" if not images[3][1] else None,
                     (255, 219, 77) if not images[1][1] else None,
                     images[3][0] if images[3][1] else None)
    design5 = Button((75, 300, 150, 100),
                     colors[4][1] if images[4][1] else locked_widget,
                     "  10" if not images[4][1] else None,
                     (255, 219, 77) if not images[1][1] else None,
                     images[4][0] if images[4][1] else None)
    design6 = Button((275, 300, 150, 100),
                     colors[5][1] if images[5][1] else locked_widget,
                     "  10" if not images[5][1] else None,
                     (255, 219, 77) if not images[1][1] else None,
                     images[5][0] if images[5][1] else None)
    design7 = Button((475, 300, 150, 100),
                     colors[6][1] if images[6][1] else locked_widget,
                     "  10" if not images[6][1] else None,
                     (255, 219, 77) if not images[1][1] else None,
                     images[6][0] if images[6][1] else None)
    design8 = Button((675, 300, 150, 100),
                     colors[7][1] if images[7][1] else locked_widget,
                     "  10" if not images[7][1] else None,
                     (255, 219, 77) if not images[1][1] else None,
                     images[7][0] if images[7][1] else None)
    design9 = Button((75, 450, 150, 100),
                     colors[8][1] if images[8][1] else locked_widget,
                     "  10" if not images[8][1] else None,
                     (255, 219, 77) if not images[1][1] else None,
                     images[8][0] if images[8][1] else None)
    design10 = Button((275, 450, 150, 100),
                      colors[9][1] if images[9][1] else locked_widget,
                      "  10" if not images[9][1] else None,
                      (255, 219, 77) if not images[1][1] else None,
                      images[9][0] if images[9][1] else None)
    design11 = Button((515, 465, 70, 70),
                      unlocked_widget if images[10][1] else locked_widget, None, None,
                      images[10][0] if images[10][1] else None)
    design12 = Button((715, 465, 70, 70),
                      unlocked_widget if images[11][1] else locked_widget, None, None,
                      images[11][0] if images[11][1] else None)
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
        elif design1.pressed and images[0][1]:
            bg_color, fg_color, ball_color = colors[0]
        elif design2.pressed and images[1][1]:
            bg_color, fg_color, ball_color = colors[1]
        elif design3.pressed and images[2][1]:
            bg_color, fg_color, ball_color = colors[2]
        elif design4.pressed and images[3][1]:
            bg_color, fg_color, ball_color = colors[3]
        elif design5.pressed and images[4][1]:
            bg_color, fg_color, ball_color = colors[4]
        elif design6.pressed and images[5][1]:
            bg_color, fg_color, ball_color = colors[5]
        elif design7.pressed and images[6][1]:
            bg_color, fg_color, ball_color = colors[6]
        elif design8.pressed and images[7][1]:
            bg_color, fg_color, ball_color = colors[7]
        elif design9.pressed and images[8][1]:
            bg_color, fg_color, ball_color = colors[8]
        elif design10.pressed and images[9][1]:
            bg_color, fg_color, ball_color = colors[9]
        elif text_box1.password == '1337' and text_box1.done:
            images[10][1] = True
            store_page(surface)
        elif text_box2.password == '1247' and text_box2.done:
            images[11][1] = True
            store_page(surface)


def developers_page(surface):
    gui_dev = GUI()
    gui_dev.add_element(Label((70, 70, 250, 50), -1, "Эта ссылка временно не работает...", special_color))
    gui_dev.add_element(Label((70, 100, 250, 50), -1, '"назад", чтобы выйти в главное меню', special_color))
    back = Button((300, 640, 150, 40), unlocked_widget, "     назад", text_color)
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


def page_between_levels(surface):
    global current_level
    global all_levels
    all_levels[current_level][1] = True

    gui_lvl = GUI()
    gui_lvl.add_element(Label((150, 50, 620, 100), unlocked_widget, " Уровень пройден", text_color))
    gui_lvl.add_element(Label((220, 150, 400, 400), -1, random.choice(phrases), special_color))
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
            current_level += 1
            game_page(surface, all_levels[current_level][0])


def game_page(surface, level):
    global rects, hole, money
    clock = pygame.time.Clock()
    slingshot = Slingshot((WIDTH // 2, HEIGHT // 4 * 3), 100, 10, fg_color)
    if images[10][1]:
        Ball(slingshot, 15, ball_color, ilya)
    elif images[11][1]:
        Ball(slingshot, 15, ball_color, artem)
    else:
        Ball(slingshot, 15, ball_color)
    level(fg_color, ball_color)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            slingshot.get_event(event)

        ball.update()

        surface.fill(bg_color)
        slingshot.render(surface)
        rects.draw(surface)
        hole.draw(surface)
        ball.draw(surface)

        pygame.display.flip()
        clock.tick(30 + ball.sprite.speed * 3)

        if ball.sprite.hitting:
            money += 10
            rects.empty()
            hole.empty()
            page_between_levels(surface)
