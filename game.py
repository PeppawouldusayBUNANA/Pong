# game.py
# Contains the main game loop and handles the game logic.
import pygame
from config import WIDTH, HEIGHT, BLACK, DARK_GREY, LIGHT_BLUE, WHITE
from paddle import Paddle
from ball import Ball

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pong")

pygame.font.init()
SCORE_FONT = pygame.font.SysFont("arial", 40)

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.left_score = 0
        self.right_score = 0
        self.left_paddle = Paddle(30, HEIGHT // 2 - 50)
        self.right_paddle = Paddle(WIDTH - 30 - 12, HEIGHT // 2 - 50, is_ai=True)
        self.ball = Ball()

    def draw(self):
        WIN.fill(BLACK)
        for y in range(0, HEIGHT, 30):
            pygame.draw.rect(WIN, DARK_GREY, (WIDTH // 2 - 2, y, 4, 20))

        pygame.draw.rect(WIN, LIGHT_BLUE, self.left_paddle.rect)
        pygame.draw.rect(WIN, WHITE, self.right_paddle.rect)
        pygame.draw.ellipse(WIN, WHITE, self.ball.rect)

        left_text = SCORE_FONT.render(str(self.left_score), 1, LIGHT_BLUE)
        right_text = SCORE_FONT.render(str(self.right_score), 1, WHITE)
        WIN.blit(left_text, (WIDTH // 4 - left_text.get_width() // 2, 20))
        WIN.blit(right_text, (WIDTH * 3 // 4 - right_text.get_width() // 2, 20))

        pygame.display.update()

    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.left_paddle.move(keys[pygame.K_w], keys[pygame.K_s])

    def check_score(self):
        if self.ball.rect.left <= 0:
            self.right_score += 1
            self.ball.reset()
        elif self.ball.rect.right >= WIDTH:
            self.left_score += 1
            self.ball.reset()

    def run(self):
        run = True
        while run:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.handle_input()

            if self.right_paddle.is_ai:
                self.right_paddle.ai_move(self.ball)

            self.ball.move()
            self.ball.check_collision(self.left_paddle)
            self.ball.check_collision(self.right_paddle)

            self.check_score()
            self.draw()

        pygame.quit()
