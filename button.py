import pygame

class ImageButton:
    """Кнопки меню"""
    def __init__(self, x, y, wigth, height, text,
                  image_path, hover_image=None, sound_path=None) -> None:
        self.x = x
        self.y = y
        self.wigth = wigth
        self.height = height
        self.text = text

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (wigth, height))
        self.hover_image = self.image
        if hover_image:
            self.hover_image = pygame.image.load(hover_image)
            self.hover_image = pygame.transform.scale(self.hover_image, (wigth, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = None
        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path)
        self.is_hover = False

    def draw(self, screen):
        current = self.hover_image if self.is_hover else self.image
        screen.blit(current, self.rect.topleft)

        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hover = self.rect.collidepoint(mouse_pos)


    def handel_event(self, event):
        """Обрабатывает нажатия клавиш в меню"""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hover:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
