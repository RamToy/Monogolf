import sys
import random
import pygame
from Monogolf.settings import *
from Monogolf.GUI import GUI, Label, Button
from Monogolf.slingshot import Slingshot
from Monogolf.ball import ball, Ball
from Monogolf.sprites import rects, hole
from Monogolf.levels import *


page_bgcolor = 43, 173, 100
base_text_color = 251, 254, 255
special_color = 166, 34, 146
unlocked_widget = 250, 100, 0
locked_widget = 140, 140, 140

phrases = ['GG!', 'GJ!', 'WP!']
all_levels = [[level_1, True], [level_2, False], [level_3, False], [level_4, False], [level_5, False],
              [level_6, False], [level_7, False], [level_8, False], [level_9, False], [level_10, False]]
current_level = 0

images = []
for i in range(len(colors)):
    bg, fg, b = colors[i]
    image = pygame.Surface((110, 60))
    image.fill(bg)
    pygame.draw.circle(image, b, (55, 30), 15, 0)
    images.append([image, True if i == 0 else False])


def terminate():
    pygame.quit()
    sys.exit()


def menu_page(surface):
    gui_menu = GUI()

    gui_menu.add_element(Label((270, 30, 150, 100), -1, "mono", (0, 0, 0)))
    gui_menu.add_element(Label((450, 30, 100, 100), -1, "GOLF", base_text_color))
    play_button = Button((330, 170, 230, 80), unlocked_widget, " Играть", base_text_color)
    shop_button = Button((330, 330, 230, 80), unlocked_widget, "Магазин", base_text_color)
    exit_button = Button((330, 490, 230, 80), unlocked_widget, " Выход", base_text_color)
    developers = Button((365, 620, 165, 30), unlocked_widget, " 2018   SilverToy58", base_text_color)

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
                  " Level 1", base_text_color)
    lvl2 = Button((475, 30, 250, 72), unlocked_widget if all_levels[1][1] else locked_widget,
                  " Level 2", base_text_color)
    lvl3 = Button((175, 150, 250, 72), unlocked_widget if all_levels[2][1] else locked_widget,
                  " Level 3", base_text_color)
    lvl4 = Button((475, 150, 250, 72), unlocked_widget if all_levels[3][1] else locked_widget,
                  " Level 4", base_text_color)
    lvl5 = Button((175, 270, 250, 72), unlocked_widget if all_levels[4][1] else locked_widget,
                  " Level 5", base_text_color)
    lvl6 = Button((475, 270, 250, 72), unlocked_widget if all_levels[5][1] else locked_widget,
                  " Level 6", base_text_color)
    lvl7 = Button((175, 390, 250, 72), unlocked_widget if all_levels[6][1] else locked_widget,
                  " Level 7", base_text_color)
    lvl8 = Button((475, 390, 250, 72), unlocked_widget if all_levels[7][1] else locked_widget,
                  " Level 8", base_text_color)
    lvl9 = Button((175, 510, 250, 72), unlocked_widget if all_levels[8][1] else locked_widget,
                  " Level 9", base_text_color)
    lvl10 = Button((475, 510, 250, 72), unlocked_widget if all_levels[9][1] else locked_widget,
                   " Level 10", base_text_color)
    back = Button((365, 620, 170, 60), unlocked_widget, "  назад", base_text_color)

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
    gui_shop = GUI()
    gui_shop.add_element(Label((300, 20, 310, 100), special_color, " Магазин", base_text_color))
    design1 = Button((75, 150, 150, 100), colors[0][1] if images[0][1] else locked_widget,
                     image=images[0][0] if images[0][1] else None)
    design2 = Button((275, 150, 150, 100), colors[1][1] if images[1][1] else locked_widget,
                     image=images[1][0] if images[1][1] else None)
    design3 = Button((475, 150, 150, 100), colors[2][1] if images[2][1] else locked_widget,
                     image=images[2][0] if images[2][1] else None)
    design4 = Button((675, 150, 150, 100), colors[3][1] if images[3][1] else locked_widget,
                     image=images[3][0] if images[3][1] else None)
    design5 = Button((75, 300, 150, 100), colors[4][1] if images[4][1] else locked_widget,
                     image=images[4][0] if images[4][1] else None)
    design6 = Button((275, 300, 150, 100), colors[5][1] if images[5][1] else locked_widget,
                     image=images[5][0] if images[5][1] else None)
    design7 = Button((475, 300, 150, 100), colors[6][1] if images[6][1] else locked_widget,
                     image=images[6][0] if images[6][1] else None)
    design8 = Button((675, 300, 150, 100), colors[7][1] if images[7][1] else locked_widget,
                     image=images[7][0] if images[7][1] else None)
    design9 = Button((75, 450, 150, 100), colors[8][1] if images[8][1] else locked_widget,
                     image=images[8][0] if images[8][1] else None)
    design10 = Button((275, 450, 150, 100), colors[9][1] if images[9][1] else locked_widget,
                      image=images[9][0] if images[9][1] else None)
    back = Button((75, 610, 170, 60), unlocked_widget, "  назад", base_text_color)

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


def developers_page(surface):
    gui_dev = GUI()
    gui_dev.add_element(Label((70, 70, 250, 50), -1, "Эта ссылка временно не работает...", special_color))
    gui_dev.add_element(Label((70, 100, 250, 50), -1, '"назад", чтобы выйти в главное меню', special_color))
    back = Button((300, 640, 150, 40), unlocked_widget, "     назад", base_text_color)
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
    gui_lvl.add_element(Label((150, 50, 620, 100), unlocked_widget, " Уровень пройден", base_text_color))
    gui_lvl.add_element(Label((220, 150, 400, 400), -1, random.choice(phrases), special_color))
    go_to_menu = Button((100, 550, 260, 100), unlocked_widget, "В меню", base_text_color)
    go_to_next_level = Button((540, 550, 260, 100), unlocked_widget, " Далее", base_text_color)

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
    global rects
    global hole
    clock = pygame.time.Clock()
    slingshot = Slingshot((WIDTH // 2, HEIGHT // 4 * 3), 100, 10)
    Ball(slingshot, 15, ball_color)
    level()

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
        clock.tick(60)

        if ball.sprite.hitting:
            rects.empty()
            hole.empty()
            page_between_levels(surface)
