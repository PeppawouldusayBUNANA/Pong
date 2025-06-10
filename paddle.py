from config import PADDLE_WIDTH, PADDLE_HEIGHT, PLAYER_VEL, AI_VEL, HEIGHT
import pygame

class Paddle:
    def __init__(self, x, y, is_ai=False):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.is_ai = is_ai

    def move(self, up, down):
        if up and self.rect.top > 0:
            self.rect.y -= PLAYER_VEL
        if down and self.rect.bottom < HEIGHT:
            self.rect.y += PLAYER_VEL

    def ai_move(self, ball):
        if self.rect.centery < ball.rect.centery:
            self.rect.y += AI_VEL
        elif self.rect.centery > ball.rect.centery:
            self.rect.y -= AI_VEL

        # Clamp to screen
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
