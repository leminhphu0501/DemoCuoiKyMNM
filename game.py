from importlib.resources import path
import pygame  # thư viện hệ thống
import sys
import time
from pygame.sprite import Sprite,Group
import os
from classPhiThuyen import PhiThuyen
from classBangDiem import BangDiem
from classDan import Dan
from classQuaiVat import QuaiVat
from classButton import Button
from classVuNo import VuNo

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((850, 480))  # kích thước cửa sổ
        self.screen_rect = self.screen.get_rect()
        self.screen.fill((240, 230, 140))
        pygame.display.set_caption("Game Bắn Gà")  # đặt tiêu đề
        self.image = pygame.image.load('./image/background.jpg')  # nền
        self.image = pygame.transform.scale(self.image, (850, 540))
        # khởi tạo phi thuyền
        self.phithuyen = PhiThuyen(self)
        # Khởi tạo viên đạn
        self.dan = pygame.sprite.Group()
        #khai báo thuộc tính vụ nổ group
        self.vu_no = pygame.sprite.Group()
        # Khởi tạo quái vật
        self.quaivat = pygame.sprite.Group()
        tam = QuaiVat(self)
        self.soquaivat = self.screen.get_width() // (tam.rect.width*2)
        self.sohang = (self.screen.get_height()//2) // (tam.rect.height*2)
        self.so_phi_thuyen = 3
        self.nut_bam = Button(self, f'Play')
        self.dang_choi = False
        self.clock = pygame.time.Clock()
        self.diem = 0
        self.ky_luc = 0
        self.bang_diem = BangDiem(self)
        # Âm thanh
        pygame.mixer.music.load('./sound/bg-music.mp3')
        pygame.mixer.music.play(-1)
        # Hiệu ứng âm thanh
        self.ban = pygame.mixer.Sound('./sound/shot.wav')
        self.no = pygame.mixer.Sound('./sound/explosion.wav')
    def taoquaivat(self):
        for i in range(self.soquaivat):
            for j in range(self.sohang):
                # Tạo 1 quái vật
                quaivat = QuaiVat(self)
                quaivat.rect.x = quaivat.rect.width + i*quaivat.rect.width*2
                quaivat.rect.y = 20 + quaivat.rect.height + j*quaivat.rect.height*2
                self.quaivat.add(quaivat)
    def kiem_tra(self):
        for quaivat in self.quaivat.sprites():
            if quaivat.rect.bottom >= self.screen_rect.bottom:
                self.quaivat.empty()
                self.dan.empty()
                self.phithuyen.rect.midbottom = self.screen_rect.midbottom
                self.so_phi_thuyen -= 1
                #Hiển thị số mạng
                self.bang_diem.tinh_so_mang(self)
                time.sleep(0.5)
                #Xử lý như quái vật va chạm phi thuyen
    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # Bắt sự kiện nút trái phải
                elif event.type == pygame.KEYDOWN:
                    # Nút phải
                    if event.key == pygame.K_RIGHT:
                        self.phithuyen.phai = True
                        self.phithuyen.quay_phai = False
                    # Nút trái
                    elif event.key == pygame.K_LEFT:
                        self.phithuyen.trai = True
                        self.phithuyen.quay_phai = True
                    # Nút lên
                    elif event.key == pygame.K_UP:
                        self.phithuyen.len = True

                    # Nút xuống
                    elif event.key == pygame.K_DOWN:
                        self.phithuyen.xuong = True

                    elif event.key == pygame.K_SPACE:
                        if self.dang_choi is True:
                            n = self.phithuyen.so_tia_dan
                            for i in range(n):
                                dan = Dan(self)
                                w = dan.rect.width
                                dan.rect.x += (-1)**i*w * \
                                    ((i+n %2)//2+((n+1)%2)*1/2)
                                self.dan.add(dan)
                            pygame.mixer.Sound.play(self.ban)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.phithuyen.phai = False
                    elif event.key == pygame.K_LEFT:
                        self.phithuyen.trai = False
                    elif event.key == pygame.K_UP:
                        self.phithuyen.len = False
                    elif event.key == pygame.K_DOWN:
                        self.phithuyen.xuong = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    # Nếu click chuột vào nút play
                    clicked = self.nut_bam.rect.collidepoint(mouse)
                    if clicked and not self.dang_choi:
                        self.dang_choi = True
                        self.so_phi_thuyen = 3
                        self.bang_diem.tinh_so_mang(self)
            self.screen.blit(self.image, (0, 0))
            self.kiem_tra()
            if not self.dang_choi:

                self.nut_bam.draw()
            # Vẽ phi thuyền
            self.phithuyen.draw()
            #Vẽ bảng điểm
            self.bang_diem.draw()
            # self.kiem_tra()
            # Vẽ viên đạn
            for dan in self.dan.sprites():
                dan.draw()
            # Va chạm giữa đạn và quái vật
            va_cham = pygame.sprite.groupcollide(self.dan, self.quaivat, True, True)
            if va_cham:
                for quai_vat in va_cham.values():
                    self.diem += 10 * len(quai_vat)
                #Thêm hiệu ứng nổ
                vu_no = VuNo(self)
                for vacham in va_cham:
                    vu_no.rect.center = vacham.rect.center
                    self.vu_no.add(vu_no)
                pygame.mixer.Sound.play(self.no)
            for vuno in self.vu_no.sprites():
                vuno.draw()
                if vuno.xoa is True:
                    self.vu_no.remove(vuno) 
                    self.bang_diem.tinh_diem(self)
                    self.bang_diem.kiem_tra_ky_luc(self)
            #Cập nhật vụ nổ
            self.vu_no.update()
            # sau khi giết quái sẽ tạo thêm quái mơi
            if not self.quaivat:
                self.taoquaivat()
                self.dan.empty()
            # Va chạm giữa quái vật là phi thuyền
            # pygame.sprite.groupcollide(
            #    self.quaivat,self.phithuyen,False,True)
            if pygame.sprite.spritecollideany(self.phithuyen, self.quaivat):
                # print('Phi thuyền đã bị đụng trúng bởi quái vật!!!')
                self.quaivat.empty()
                self.dan.empty()
                self.phithuyen.rect.midbottom = self.screen_rect.midbottom
                self.so_phi_thuyen -= 1
                self.bang_diem.tinh_so_mang(self)
                time.sleep(1)
            if self.so_phi_thuyen == 0:
                self.dang_choi = False
                self.diem =0
                self.bang_diem.tinh_diem(self)
                #print('Bạn đã thua! Dừng trò chơi :) ')
                #Tính điểm
                for quai_vat in va_cham.values():
                    self.diem += 10 * len(quai_vat)
                self.bang_diem.tinh_diem(self)
                self.bang_diem.kiem_tra_ky_luc(self)
            # self.taoquaivat()
            # Vẽ quái vật
            for quaivat in self.quaivat.sprites():
                quaivat.draw()
            # Cập nhật vị trí
            if self.dang_choi:
                self.phithuyen.update()
                self.dan.update()
                self.quaivat.update()
            for dan in self.dan.sprites():
                if dan.rect.bottom <= 0:
                    self.dan.remove(dan)

            # Giới hạn di chuyển trong màn hình của quái vật
            for quaivat in self.quaivat.sprites():
                if quaivat.rect.right >= self.screen_rect.right:
                    quaivat.phai = False
                    quaivat.trai = True
                    quaivat.rect.y += quaivat.rect.height
                if quaivat.rect.left <= 0:
                    quaivat.phai = True
                    quaivat.trai = False
                    quaivat.rect.y += quaivat.rect.height
                if quaivat.rect.top >= self.screen_rect.top:
                    quaivat.top = False
                    quaivat.bot = True
                if quaivat.rect.bottom <= 0:
                    quaivat.top = True
                    quaivat.bot = False
            pygame.display.flip()
            self.clock.tick(60)
if __name__ == '__main__':
    game = Game()
    game.main()
