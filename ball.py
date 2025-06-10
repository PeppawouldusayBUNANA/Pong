from config import WIDTH, HEIGHT, BALL_RADIUS, BALL_SPEED, PADDLE_HEIGHT
import pygame
import random

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(
            WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS,
            BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.vel = [BALL_SPEED * random.choice((-1, 1)),
                    BALL_SPEED * random.choice((-1, 1))]

    def move(self):
        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.vel[1] *= -1

    def check_collision(self, paddle):
        if self.rect.colliderect(paddle.rect):
            self.vel[0] *= -1
            offset = (self.rect.centery - paddle.rect.centery) / (PADDLE_HEIGHT // 2)
            self.vel[1] += offset * 3

    def reset(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.vel = [BALL_SPEED * random.choice((-1, 1)),
                    BALL_SPEED * random.choice((-1, 1))]
