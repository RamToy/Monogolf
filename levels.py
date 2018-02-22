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
    BoarderRect(160, 300, 30, 130, fg)
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
    BoarderRect(580, 500, 40, 180, fg)
    BoarderRect(580, 400, 300, 40, fg)
    BoarderRect(675, 500, 50, 50, fg)
    BoarderRect(775, 500, 50, 50, fg)
    BoarderRect(675, 600, 50, 50, fg)
    BoarderRect(775, 600, 50, 50, fg)
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
    BoarderRect(110, 100, 80, 80, fg)
    BoarderRect(110, 250, 80, 80, fg)
    BoarderRect(110, 400, 80, 80, fg)
    BoarderRect(260, 100, 80, 80, fg)
    BoarderRect(260, 250, 80, 80, fg)
    BoarderRect(260, 400, 80, 80, fg)
    BoarderRect(410, 100, 80, 80, fg)
    BoarderRect(410, 250, 80, 80, fg)
    BoarderRect(560, 100, 80, 80, fg)
    BoarderRect(560, 250, 80, 80, fg)
    BoarderRect(560, 400, 80, 80, fg)
    BoarderRect(710, 100, 80, 80, fg)
    BoarderRect(710, 250, 80, 80, fg)
    BoarderRect(710, 400, 80, 80, fg)
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
    BoarderRect(440, 230, 20, 150, fg)
    BoarderRect(300, 300, 140, 20, fg)
    BoarderRect(460, 300, 140, 20, fg)
    BoarderRect(150, 200, 20, 150, fg)
    BoarderRect(730, 200, 20, 150, fg)
    BoarderRect(300, 100, 20, 200, fg)
    BoarderRect(580, 100, 20, 200, fg)
    BoarderRect(300, 80, 110, 20, fg)
    BoarderRect(490, 80, 110, 20, fg)
    Hole((420, 150), 30, ball)


def level_10(fg, ball):
    add_frames(fg)
    BoarderRect(145, 150, 90, 30, fg)
    BoarderRect(235, 180, 30, 50, fg)
    BoarderRect(115, 180, 30, 200, fg)
    BoarderRect(145, 380, 90, 30, fg)
    BoarderRect(235, 300, 30, 80, fg)
    BoarderRect(185, 300, 50, 30, fg)
    BoarderRect(335, 180, 30, 200, fg)
    BoarderRect(455, 180, 30, 200, fg)
    BoarderRect(365, 380, 90, 30, fg)
    BoarderRect(365, 150, 90, 30, fg)
    BoarderRect(555, 180, 30, 230, fg)
    BoarderRect(515, 150, 110, 30, fg)
    BoarderRect(655, 150, 30, 100, fg)
    BoarderRect(685, 250, 70, 30, fg)
    BoarderRect(755, 150, 30, 230, fg)
    BoarderRect(685, 380, 70, 30, fg)
    BoarderRect(655, 340, 30, 40, fg)
    Hole((380, 250), 30, ball)


level_list = [level_1, level_2, level_3, level_4, level_5,
              level_6, level_7, level_8, level_9, level_10]
