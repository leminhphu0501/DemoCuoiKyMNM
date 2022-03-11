from importlib.resources import path
import pygame  # thư viện hệ thống
import sys
import time
from pygame.sprite import Sprite,Group
import os
class Dan(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.image = pygame.image.load('./image/dan.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = game.phithuyen.rect.midtop

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        # cập nhật lại để toạ độ Y để viên đạn bay lên
        self.rect.y -= 10
