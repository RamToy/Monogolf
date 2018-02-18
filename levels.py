from Monogolf.settings import WIDTH, HEIGHT, INDENT, ball_color
from Monogolf.sprites import BoarderRect, Hole


def add_frames():
    BoarderRect(0, 0, WIDTH - INDENT, INDENT)
    BoarderRect(0, INDENT, INDENT, HEIGHT - INDENT)
    BoarderRect(INDENT, HEIGHT - INDENT, WIDTH - INDENT, INDENT)
    BoarderRect(WIDTH - INDENT, 0, INDENT, HEIGHT - INDENT)


def level_1():
    add_frames()
    # BoarderRect(WIDTH // 2 - 200, HEIGHT // 2 - 150, 400, 100)
    Hole((435, 200), 30, ball_color)


def level_2():
    add_frames()
    BoarderRect(20, 300, 40, 40)
    BoarderRect(160, 300, 720, 40)
    BoarderRect(400, 20, 40, 100)
    BoarderRect(550, 200, 40, 100)
    BoarderRect(700, 20, 40, 100)
    Hole((795, 60), 30, ball_color)


def level_3():
    add_frames()
    BoarderRect(20, 400, 720, 30)
    BoarderRect(160, 300, 720, 30)
    BoarderRect(20, 300, 30, 30)
    BoarderRect(20, 200, 520, 30)
    BoarderRect(650, 200, 230, 30)
    BoarderRect(180, 100, 700, 30)
    BoarderRect(20, 100, 50, 30)
    BoarderRect(740, 400, 30, 110)
    Hole((810, 30), 30, ball_color)


def level_4():
    add_frames()
    BoarderRect(440, 300, 210, 30)
    BoarderRect(620, 330, 30, 180)
    BoarderRect(150, 480, 210, 30)
    BoarderRect(150, 300, 30, 180)
    Hole((510, 230), 30, ball_color)


def level_5():
    add_frames()
    BoarderRect(80, 540, 80, 80)
    BoarderRect(220, 500, 40, 180)
    BoarderRect(220, 400, 240, 40)
    BoarderRect(20, 300, 140, 40)
    BoarderRect(220, 150, 190, 190)
    BoarderRect(220, 50, 190, 40)
    BoarderRect(460, 170, 40, 270)
    Hole((70, 200), 30, ball_color)


def level_6():
    add_frames()


def level_7():
    add_frames()


def level_8():
    add_frames()


def level_9():
    add_frames()


def level_10():
    add_frames()
