import random
import sys

import pygame

from button import ImageButton

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Размеры экрана
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

# Шрифт
# FONT = pygame.font.Font(None, 36)

button = ImageButton(SCREEN_WIDTH/2 - (252/2), 100, 252, 74, " ", 
                     "media/button.png", "media/button.png", None)

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption("Cryptogram")

# Настройка времени:
clock = pygame.time.Clock()


class GameObject:
    """
    Родительский класс.
    - Определяет общие методы и свойства, которыми будут обладать все объекты игры.
    - Методы могут включать базовые функции для отрисовки объектов, 
    обработки событий и взаимодействия с другими объектами.
    """

    def __init__(self):
        pass

    def draw(self):
        """Отображает объект на экране."""
        raise NotImplementedError("Метод draw() должен быть переопределён.")

    def update(self):
        """Обновление состояния объекта."""
        raise NotImplementedError("Метод update() должен быть переопределён.")


class Cryptogram(GameObject):
    """ 
    - Главный игровой компонент, который управляет состоянием криптограммы:
        хранит зашифрованную фразу, исходную фразу и текущий прогресс игрока.
        Проверяет вводимые игроком символы и реагирует на изменение состояния криптограммы.
    """
    def pas(self):
        pass


class LetterBox(GameObject):
    """
    - Представляет собой отдельную ячейку для ввода одной буквы.
    - Содержит метод для проверки правильности введенной буквы и визуального
         отображения текущего состояния ячейки.

    """
    def pas(self):
        pass


class ScoreBoard(GameObject):
    """
    - Ведёт учёт статистики игры: количество попыток, оставшееся время, очки и прочее.
    - Выводит эту информацию на экран.
    """
    def pas(self):
        pass


def handel_event():
    """Обрабатывает нажатия клавиш в меню"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit


def main():
    """Главный цикл игры"""

    pygame.init()
    while True:
        clock.tick()
        handel_event()
        screen.fill(WHITE)
        button.draw(screen)
        pygame.display.update()
    pygame.quit()




if __name__ == '__main__':
    main()
