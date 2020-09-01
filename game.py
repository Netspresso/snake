from config import Config
from snake import Snake
from apple import Apple
import pygame
import sys


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
        pygame.display.set_caption('Snake')
        self.apple = Apple()
        self.snake = Snake()

    def run(self):
        while True:  # Main game loop
            for event in pygame.event.get(
            ):  # ta funkcja bierze i usuwa wiadomości z kolejki (można w argumencie funkcji zadać typ który jako jedyny ma być obsługiwany)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            self.screen.fill(
                (255, 255, 255)
            )  # funkcją display utworzyłem obiekt Surface - fill to metoda dla obiektu Surface która wypełnia powierzchnię okna jednolitym kolorem

            pygame.display.update(
            )  # metoda która odświeża wyświetlane okno - w mojej pętli będzie odświeżana za każdym zdarzeniem
            self.clock.tick(
                60
            )  # ustala ilość cyknięć w milisekundach, w moim przypadku determinuje to że gra będzie działać w 60 klatkach na sekundę