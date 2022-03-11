from email.mime import image
from importlib.resources import path
import pygame  # thư viện hệ thống
import sys
import time
from pygame.sprite import Sprite,Group
import os
class PhiThuyen(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load('./di_chuyen/0.png')
        # self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.phai = False
        self.trai = False
        self.len = False
        self.xuong = False
        self.so_tia_dan = 2
        self.qua_phai = []
        self.qua_trai = []
        self.danh_sach_anh_phai=[]
        self.danh_sach_anh_trai =[]
        self.quay_phai = False
        self.index = 0

    def update(self):
        if self.phai is True and self.rect.right < self.screen_rect.right:
            self.rect.x += 10
        if self.trai is True and self.rect.left > 0:
            self.rect.x -= 10
        if self.len is True and self.rect.top > self.screen_rect.top:
            self.rect.y -= 10
        if self.xuong is True and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 10
        self.animation()
    def lay_anh(self, path):
        danh_sach_anh_phai = []
        danh_sach_anh_trai = []
        for _, _, files in os.walk(path):
            for file in files:
                image = pygame.image.load(path + file)
                danh_sach_anh_phai.append(image)
                image = pygame.transform.flip(image, True, False)
                danh_sach_anh_trai.append(image)
        return danh_sach_anh_phai, danh_sach_anh_trai
    def animation(self):
        self.danh_sach_anh_phai,self.danh_sach_anh_trai = self.lay_anh('./di_chuyen/')
        if self.quay_phai is False:
            if self.phai is True:
                self.image = self.danh_sach_anh_phai[self.index]
                self.index += 1
                if self.index == len(self.danh_sach_anh_phai):
                    self.index -= 1
            else:
                self.can_bang()
        else:
            if self.trai is True:
                self.image = self.danh_sach_anh_trai[self.index]
                self.index += 1
                if self.index == len(self.danh_sach_anh_trai):
                    self.index -= 1
            else:
                self.can_bang()
    def can_bang(self):
        while self.index >=0:
            self.image = self.danh_sach_anh_trai[self.index]
            self.index -= 1
        self.index = 0
    def draw(self):
        self.screen.blit(self.image, self.rect)