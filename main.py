import pygame
from monogolf.settings import *
from monogolf.pages import menu_page

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

menu_page(screen)

pygame.quit()
