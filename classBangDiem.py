from importlib.resources import path
import pygame  # thư viện hệ thống
import sys
import time
from pygame.sprite import Sprite,Group
import os
from classPhiThuyen import PhiThuyen
class BangDiem:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.font = pygame.font.Font(None, 50)
        self.color = (255,255,255)
        #Tùy chọn: self.bg_color = (0,0,0)
        self.tinh_diem(game)
        self.tinh_ky_luc(game)
        self.tinh_so_mang(game)
    def tinh_diem(self,game):
        self.text = self.font.render(str(game.diem),True,self.color)
        self.text_rect = self.text.get_rect()
        self.text_rect.left = 5
        self.text_rect.top = 5
    def tinh_ky_luc(self,game):
        self.text_ky_luc = self.font.render(str(game.ky_luc),True,self.color)
        self.text_ky_luc_rect = self.text.get_rect()
        self.text_ky_luc_rect.midtop =game.screen_rect.midtop
    def kiem_tra_ky_luc(self,game):
        if game.diem > game.ky_luc:
         game.ky_luc = game.diem
         self.tinh_ky_luc(game)
    def draw(self):
        self.screen.blit(self.text,self.text_rect)
        self.screen.blit(self.text_ky_luc,self.text_ky_luc_rect)
        self.phi_thuyen.draw(self.screen)
    def tinh_so_mang(self,game):
        self.phi_thuyen = Group()
        for i in range(game.so_phi_thuyen):
            phi_thuyen = PhiThuyen(game)
            phi_thuyen.rect.bottomright = game.screen_rect.bottomright
            phi_thuyen.rect.x -= i * phi_thuyen.rect.width
            self.phi_thuyen.add(phi_thuyen)