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

    def drawGrid(self):
        for x in range(0, Config.WINDOW_WIDTH, Config.CELLSIZE):
            ''' Rysuje podział wertykalny '''
            pygame.draw.line(self.screen, Config.DARKGRAY, (x, 0),
                             (x, Config.WINDOW_HEIGHT))
        for y in range(0, Config.WINDOW_HEIGHT, Config.CELLSIZE):
            ''' Rysuje podział horyzontalny '''
            pygame.draw.line(self.screen, Config.DARKGRAY, (0, y),
                             (Config.WINDOW_WIDTH, y))

    def draw(self):
        self.screen.fill(Config.BG_COLOR)
        self.drawGrid()
        pygame.display.update()
        self.clock.tick(Config.FPS)

    def handleKeyEvents(self, event):
        if event.key == pygame.K_ESCAPE:
            pygame.quit()

    def resetGame(self):
        del self.snake
        del self.apple
        self.snake = Snake()
        self.apple = Apple()

        return True

    def isGameOver(self):
        if (self.snake.snakeCoords[self.snake.HEAD]['x'] == -1
                or self.snake.snakeCoords[self.snake.HEAD]['x']
                == Config.CELLWIDTH
                or self.snake.snakeCoords[self.snake.HEAD]['y'] == -1
                or self.snake.snakeCoords[self.snake.HEAD]['y']
                == Config.CELLWIDTH):
            return self.resetGame()

        for snakeBody in self.snake.snakeCoords[1:]:
            if snakeBody['x'] == self.snake.snakeCoords[self.snake.HEAD][
                    'x'] and snakeBody['y'] == self.snake.snakeCoords[
                        self.snake.HEAD]['y']:
                return self.resetGame()

    def run(self):
        while True:  # Main game loop
            for event in pygame.event.get(
            ):  # ta funkcja bierze i usuwa wiadomości z kolejki (można w argumencie funkcji zadać typ który jako jedyny ma być obsługiwany)
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    self.handleKeyEvents(event)

            self.snake.update(self.apple)
            self.draw()
            if self.isGameOver():
                break