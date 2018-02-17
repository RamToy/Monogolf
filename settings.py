from monogolf.design import *

WIDTH = 900     # Ширина окна
HEIGHT = 700    # Высота окна
INDENT = 20     # Длина отступа по краям
bg_color, fg_color = FIELD_COLOR10   # Цвета
ball_color = [255 - (bg_color[c] + fg_color[c]) // 2 for c in range(3)]
