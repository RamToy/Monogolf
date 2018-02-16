from settings import *
from ball import Ball
from slingshot import Slingshot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    slingshot = Slingshot((WIDTH // 2, HEIGHT // 4 * 3), 15, 10)

    running = True
    slingshot_active, slingshot_focus = True, False
    ball_move = False
    speed = 30

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

            if slingshot_active:
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1 and slingshot.capture_rect.collidepoint(e.pos):
                    slingshot_focus = True

                if slingshot_focus:
                    if e.type == pygame.MOUSEBUTTONUP:
                        slingshot_focus = False
                        if slingshot.capture_rect.collidepoint(e.pos):
                            slingshot.update()
                        else:
                            ball_move = True
                            ball = Ball(slingshot.center_pos, slingshot.cur_pos,
                                        slingshot.ball_r)
                            speed = ball.speed * 2 + 30
                    elif e.type == pygame.MOUSEMOTION:
                        slingshot.update(e.pos)

            else:
                if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                    slingshot.update()
                    slingshot_active = True
                    ball_move = False

        screen.fill(fg_color)
        pygame.draw.rect(screen, bg_color, (INDENT, INDENT, WIDTH - INDENT * 2, HEIGHT - INDENT * 2), 0)

        if ball_move:
            ball.move()
            ball.render(screen)
            if ball.y * ball.y_dir <= slingshot.y * ball.y_dir + slingshot.capture_rect.height and \
               ball.x * ball.x_dir <= slingshot.x * ball.x_dir + slingshot.capture_rect.width // 2:
                    slingshot.update(ball.cur_pos)
            else:
                slingshot_active = False

        if slingshot_active:
            slingshot.render(screen)

        clock.tick(speed)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
