from importlib.resources import path
import pygame  # thư viện hệ thống
import sys
import time
from pygame.sprite import Sprite,Group
import os
class Button:
    def __init__(self, game, label):
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.width = 150
        self.height = 50
        self.color = 'CornflowerBlue'
        self.text_color = 'white'
        self.image = pygame.image.load('./image/start.png')
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.image_rect = self.image.get_rect()
        self.font = pygame.font.SysFont(None, 50)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.text = self.font.render(
            label, True, self.text_color, self.color
        )
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.screen_rect.center

    def draw(self):
        self.screen.fill(self.color,self.rect)
        self.screen.blit(self.text,self.text_rect)

