from importlib.resources import path
import pygame  # thư viện hệ thống
import sys
import time
from pygame.sprite import Sprite,Group
import os
class VuNo(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.danh_sach_anh = []
        for _, _, files in os.walk('./no'):
            for file in files:
                img = pygame.image.load('./no/' + file)
                img = pygame.transform.scale(img, (75, 75))
                self.danh_sach_anh.append(img)
        self.index = 0
        self.image = self.danh_sach_anh[self.index]
        self.rect = self.image.get_rect()
        self.xoa = False

    def draw(self):
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        self.index += 1
        if self.index == len(self.danh_sach_anh) - 1:
            self.xoa = True
        self.image = self.danh_sach_anh[self.index]