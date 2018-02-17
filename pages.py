import sys
import os
import pygame
from monogolf.settings import *
from monogolf.GUI import GUI, Label, Button
from monogolf.slingshot import Slingshot
from monogolf.ball import ball, Ball
from monogolf.sprites import rects, hole


page_bgcolor = (43, 173, 100)
page_text_color = (251, 254, 255)
page_widget_color = (250, 100, 0)


def terminate():
    pygame.quit()
    sys.exit()


def menu_page(surface):
    gui_menu = GUI()

    gui_menu.add_element(Label((270, 30, 150, 100), -1, "mono", (0, 0, 0)))
    gui_menu.add_element(Label((450, 30, 100, 100), -1, "GOLF", page_text_color))
    play_button = Button((330, 170, 230, 80), page_widget_color, " Играть", page_text_color)
    shop_button = Button((330, 330, 230, 80), page_widget_color, "Магазин", page_text_color)
    exit_button = Button((330, 490, 230, 80), page_widget_color, " Выход", page_text_color)
    developers = Button((365, 620, 165, 30), page_widget_color, " 2018   SilverToy58", page_text_color)

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
            shop_page(surface)
        elif developers.pressed:
            developers_page(surface)
        elif exit_button.pressed:
            terminate()


def levels_page(surface):
    gui_levels = GUI()
    level1 = Button((175, 30, 250, 72), page_widget_color, " Level 1", page_text_color)
    level2 = Button((475, 30, 250, 72), page_widget_color, " Level 2", page_text_color)
    level3 = Button((175, 150, 250, 72), page_widget_color, " Level 3", page_text_color)
    level4 = Button((475, 150, 250, 72), page_widget_color, " Level 4", page_text_color)
    level5 = Button((175, 270, 250, 72), page_widget_color, " Level 5", page_text_color)
    level6 = Button((475, 270, 250, 72), page_widget_color, " Level 6", (140, 140, 140))
    level7 = Button((175, 390, 250, 72), page_widget_color, " Level 7", (140, 140, 140))
    level8 = Button((475, 390, 250, 72), page_widget_color, " Level 8", (140, 140, 140))
    level9 = Button((175, 510, 250, 72), page_widget_color, " Level 9", (140, 140, 140))
    level10 = Button((475, 510, 250, 72), page_widget_color, " Level 10", (140, 140, 140))
    back = Button((375, 640, 150, 40), page_widget_color, "     назад", page_text_color)

    gui_levels.add_element(level1)
    gui_levels.add_element(level2)
    gui_levels.add_element(level3)
    gui_levels.add_element(level4)
    gui_levels.add_element(level5)
    gui_levels.add_element(level6)
    gui_levels.add_element(level7)
    gui_levels.add_element(level8)
    gui_levels.add_element(level9)
    gui_levels.add_element(level10)
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
        elif level1.pressed:
            game_page(surface)


def shop_page(surface):
    gui_shop = GUI()
    design_bg1 = Button((175, 20, 140, 60), page_widget_color, " фон1", page_text_color)
    design_bg2 = Button((20, 120, 140, 60), page_widget_color, " фон2", page_text_color)
    design_bg3 = Button((20, 220, 140, 60), page_widget_color, " фон3", page_text_color)
    design_bg4 = Button((20, 320, 140, 60), page_widget_color, " фон4", page_text_color)
    design_bg5 = Button((20, 420, 140, 60), page_widget_color, " фон5", page_text_color)
    design_bg6 = Button((175, 20, 140, 60), page_widget_color, " фон6", page_text_color)
    design_bg7 = Button((180, 120, 140, 60), page_widget_color, " фон7", page_text_color)
    design_bg8 = Button((180, 220, 140, 60), page_widget_color, " фон8", page_text_color)
    design_bg9 = Button((180, 320, 140, 60), page_widget_color, " фон9", page_text_color)
    design_bg10 = Button((180, 420, 140, 60), page_widget_color, "фон10", page_text_color)
    design_bg11 = Button((340, 20, 140, 60), page_widget_color, "фон11", page_text_color)
    design_bg12 = Button((340, 120, 140, 60), page_widget_color, "фон12", page_text_color)
    design_bg13 = Button((340, 220, 140, 60), page_widget_color, "фон13", page_text_color)
    design_bg14 = Button((340, 320, 140, 60), page_widget_color, "фон14", page_text_color)
    design_bg15 = Button((340, 420, 140, 60), page_widget_color, "фон15", page_text_color)
    back = Button((300, 640, 150, 40), page_widget_color, "     назад", page_text_color)

    gui_shop.add_element(design_bg1)
    gui_shop.add_element(design_bg2)
    gui_shop.add_element(design_bg3)
    gui_shop.add_element(design_bg4)
    gui_shop.add_element(design_bg5)
    gui_shop.add_element(design_bg6)
    gui_shop.add_element(design_bg7)
    gui_shop.add_element(design_bg8)
    gui_shop.add_element(design_bg9)
    gui_shop.add_element(design_bg10)
    gui_shop.add_element(design_bg11)
    gui_shop.add_element(design_bg12)
    gui_shop.add_element(design_bg13)
    gui_shop.add_element(design_bg14)
    gui_shop.add_element(design_bg15)
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
    gui_dev.add_element(Label((70, 70, 250, 50), -1, "Эта ссылка временно не работает...", page_text_color))
    gui_dev.add_element(Label((70, 100, 250, 50), -1, '"назад", чтобы выйти в главное меню', page_text_color))
    back = Button((300, 640, 150, 40), page_widget_color, "     назад", page_text_color)
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


def game_page(surface):
    clock = pygame.time.Clock()
    slingshot = Slingshot((WIDTH // 2, HEIGHT // 4 * 3), 100, 10)
    Ball(slingshot, 15, ball_color)

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
