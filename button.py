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
        self.image_path = pygame.image.load(image_path)
