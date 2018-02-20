import pygame


class GUI:
    def __init__(self):
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def render(self, surface):
        for element in self.elements:
            render = getattr(element, "render", None)
            if callable(render):
                element.render(surface)

    def update(self):
        for element in self.elements:
            update = getattr(element, "update", None)
            if callable(update):
                element.update()

    def get_event(self, event):
        for element in self.elements:
            get_event = getattr(element, "get_event", None)
            if callable(get_event):
                element.get_event(event)

    def clear(self):
        self.elements.clear()


class Label:
    def __init__(self, rect, rect_color, text, font_color):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.rect_color = rect_color
        self.font_color = font_color
        self.font = pygame.font.Font(None, self.rect.height - 4)
        self.rendered_text = None
        self.rendered_rect = None

    def render(self, surface):
        if self.rect_color != -1:
            surface.fill(self.rect_color, self.rect)
        self.rendered_text = self.font.render(self.text, 1, self.font_color)
        self.rendered_rect = self.rendered_text.get_rect(x=self.rect.x + 2, centery=self.rect.centery, width=2)
        surface.blit(self.rendered_text, self.rendered_rect)


class Button(Label):
    def __init__(self, rect, rect_color, text=None, font_color=None, image=None):
        super().__init__(rect, rect_color, text, font_color)
        self.image = image
        self.pressed = False

    def render(self, surface):
        surface.fill(self.rect_color, self.rect)
        if self.text:
            self.rendered_text = self.font.render(self.text, 1, self.font_color)
        if not self.pressed:
            color1 = pygame.Color("white")
            color2 = pygame.Color("black")
            if self.text:
                self.rendered_rect = self.rendered_text.get_rect(x=self.rect.x + 5, centery=self.rect.centery)
            elif self.image:
                self.rendered_rect = self.image.get_rect(x=self.rect.x + 20, centery=self.rect.centery)
        else:
            color1 = pygame.Color("black")
            color2 = pygame.Color("white")
            if self.text:
                self.rendered_rect = self.rendered_text.get_rect(x=self.rect.x + 7, centery=self.rect.centery + 2)
            elif self.image:
                self.rendered_rect = self.image.get_rect(x=self.rect.x + 22, centery=self.rect.centery + 2)

        pygame.draw.rect(surface, color1, self.rect, 2)
        pygame.draw.line(surface, color2, (self.rect.right - 1, self.rect.top),
                         (self.rect.right - 1, self.rect.bottom), 2)
        pygame.draw.line(surface, color2, (self.rect.left, self.rect.bottom - 1),
                         (self.rect.right, self.rect.bottom - 1), 2)
        if self.text:
            surface.blit(self.rendered_text, self.rendered_rect)
        elif self.image:
            surface.blit(self.image, self.rendered_rect)

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.pressed = self.rect.collidepoint(*event.pos)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.pressed = False
            
            
class TextBox(Label):
    def __init__(self, rect, rect_color, font_color, text=''):
        super().__init__(rect, rect_color, text, font_color)
        self.password = ''
        self.active = True
        self.done = False

    def get_event(self, event):
        if event.type == pygame.KEYDOWN and self.active:
            if self.done:
                self.done = False
                self.password = ''
            if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                self.done = True
                self.text = ''
            elif event.key == pygame.K_BACKSPACE:
                if len(self.text) > 0:
                    self.text = self.text[:-1]
                    self.password = self.password[:-1]
            elif len(self.text) < 4:
                self.text += '*'
                self.password += event.unicode

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.active = self.rect.collidepoint(*event.pos)
            self.text, self.password = '', ''
