from Monogolf.settings import WIDTH, HEIGHT, INDENT
from Monogolf.sprites import BoarderRect, Hole


def add_frames(fg):
    BoarderRect(0, 0, WIDTH - INDENT, INDENT, fg)
    BoarderRect(0, INDENT, INDENT, HEIGHT - INDENT, fg)
    BoarderRect(INDENT, HEIGHT - INDENT, WIDTH - INDENT, INDENT, fg)
    BoarderRect(WIDTH - INDENT, 0, INDENT, HEIGHT - INDENT, fg)


def level_1(fg, ball):
    add_frames(fg)
    Hole((WIDTH // 2 - 30, 200), 30, ball)


def level_2(fg, ball):
    add_frames(fg)
    BoarderRect(20, 300, 40, 40, fg)
    BoarderRect(160, 300, 720, 40, fg)
    BoarderRect(400, 20, 40, 100, fg)
    BoarderRect(550, 200, 40, 100, fg)
    BoarderRect(700, 20, 40, 100, fg)
    Hole((780, 60), 30, ball)


def level_3(fg, ball):
    add_frames(fg)
    BoarderRect(160, 300, 720, 30, fg)
    BoarderRect(20, 300, 30, 30, fg)
    BoarderRect(20, 200, 520, 30, fg)
    BoarderRect(650, 200, 230, 30, fg)
    BoarderRect(180, 100, 700, 30, fg)
    BoarderRect(20, 100, 50, 30, fg)
    BoarderRect(160, 330, 30, 100, fg)
    Hole((810, 30), 30, ball)


def level_4(fg, ball):
    add_frames(fg)
    BoarderRect(480, 150, 210, 30, fg)
    BoarderRect(660, 180, 30, 180, fg)
    BoarderRect(690, 330, 190, 30, fg)
    BoarderRect(190, 330, 210, 30, fg)
    BoarderRect(190, 150, 30, 180, fg)
    BoarderRect(20, 150, 170, 30, fg)
    Hole((550, 70), 30, ball)


def level_5(fg, ball):
    add_frames(fg)
    BoarderRect(80, 480, 80, 80, fg)
    BoarderRect(220, 450, 40, 230, fg)
    BoarderRect(220, 290, 280, 40, fg)
    BoarderRect(20, 290, 200, 40, fg)
    BoarderRect(220, 100, 200, 130, fg)
    BoarderRect(460, 100, 40, 230, fg)
    BoarderRect(600, 500, 40, 180, fg)
    BoarderRect(600, 400, 280, 40, fg)
    BoarderRect(685, 500, 50, 50, fg)
    BoarderRect(785, 500, 50, 50, fg)
    BoarderRect(685, 600, 50, 50, fg)
    BoarderRect(785, 600, 50, 50, fg)
    BoarderRect(600, 100, 100, 100, fg)
    BoarderRect(750, 100, 100, 100, fg)
    BoarderRect(600, 250, 100, 100, fg)
    BoarderRect(750, 250, 100, 100, fg)
    Hole((70, 200), 30, ball)


def level_6(fg, ball):
    add_frames(fg)
    BoarderRect(200, 280, 100, 300, fg)
    BoarderRect(600, 280, 100, 300, fg)
    BoarderRect(250, 140, 400, 50, fg)
    BoarderRect(70, 460, 130, 40, fg)
    BoarderRect(700, 460, 130, 40, fg)
    Hole((420, 50), 30, ball)


def level_7(fg, ball):
    add_frames(fg)
    for sqx in range(110, 800, 150):
        for sqy in range(100, 500, 150):
            if sqx != 410 or sqy != 400:
                BoarderRect(sqx, sqy, 80, 80, fg)
    BoarderRect(260, 480, 40, 200, fg)
    BoarderRect(490, 100, 70, 15, fg)
    BoarderRect(340, 100, 70, 15, fg)
    BoarderRect(600, 480, 40, 200, fg)
    Hole((420, 30), 30, ball)


def level_8(fg, ball):
    add_frames(fg)
    BoarderRect(80, 350, 800, 20, fg)
    BoarderRect(80, 80, 20, 270, fg)
    BoarderRect(100, 80, 720, 20, fg)
    BoarderRect(800, 100, 20, 190, fg)
    BoarderRect(180, 270, 620, 20, fg)
    BoarderRect(160, 160, 20, 130, fg)
    BoarderRect(180, 160, 550, 20, fg)
    Hole((200, 195), 30, ball)


def level_9(fg, ball):
    add_frames(fg)
    BoarderRect(WIDTH // 2 - 10, HEIGHT // 2 - 120, 20, 150, fg)
    BoarderRect(300, 300, 140, 20, fg)
    BoarderRect(460, 300, 140, 20, fg)
    BoarderRect(150, 200, 20, 150, fg)
    BoarderRect(730, 200, 20, 150, fg)
    BoarderRect(300, 100, 20, 200, fg)
    BoarderRect(580, 100, 20, 200, fg)
    BoarderRect(300, 80, 110, 20, fg)
    BoarderRect(490, 80, 110, 20, fg)
    Hole((WIDTH // 2 - 30, HEIGHT // 2 - 200), 30, ball)


def level_10(fg, ball):
    add_frames(fg)
    BoarderRect(130, 150, 90, 30, fg)
    BoarderRect(220, 180, 30, 50, fg)
    BoarderRect(100, 180, 30, 200, fg)
    BoarderRect(130, 380, 90, 30, fg)
    BoarderRect(220, 300, 30, 80, fg)
    BoarderRect(170, 300, 50, 30, fg)
    BoarderRect(320, 180, 30, 200, fg)
    BoarderRect(440, 180, 30, 200, fg)
    BoarderRect(350, 380, 90, 30, fg)
    BoarderRect(350, 150, 90, 30, fg)
    BoarderRect(540, 180, 30, 230, fg)
    BoarderRect(500, 150, 110, 30, fg)
    BoarderRect(640, 150, 30, 100, fg)
    BoarderRect(670, 250, 70, 30, fg)
    BoarderRect(740, 150, 30, 230, fg)
    BoarderRect(670, 380, 70, 30, fg)
    BoarderRect(640, 340, 30, 40, fg)
    Hole((365, 250), 30, ball)
