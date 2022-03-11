from importlib.resources import path
import pygame  # thư viện hệ thống
import sys
import time
from pygame.sprite import Sprite,Group
import os
class QuaiVat(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('./image/chicken.png')
        self.rect = self.image.get_rect()
        # Điều chỉnh toạ độ
        self.rect.midtop = self.screen_rect.midtop
        # self.rect.y = 10
        self.phai = True
        self.trai = False

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.phai is True:
            self.rect.x += 6
        elif self.trai is True:
            self.rect.x -= 6