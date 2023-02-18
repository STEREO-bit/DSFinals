from settings import *
import pygame as pg
from os import path

game_folder = ""
snd_folder = path.join(game_folder, 'snd')

class GameClock:
    def __init__(self, game, timer):
        self.game = game
        self.now = pg.time.get_ticks()
        self.last_update = self.now
        self.timer = timer

    def tick(self):
        self.now = pg.time.get_ticks()

        if self.now - self.last_update > 100:
            self.last_update = self.now
            self.timer -= 0.1
        
        if self.timer < 0:
            snd = pg.mixer.Sound(path.join(snd_folder, 'hurt.wav'))
            snd.play()
            print("ded")
            self.game.ded_screen("CLOCK_PROCESS_TIMED_OUT")

        if self.timer < -1: 
            self.game.anti_cheat()

    def draw_clock(self):
        img = self.game.timer_hud
        img_rect = img.get_rect()
        img_rect.topleft = (620, 30)
        self.game.screen.blit(img, img_rect)
        self.game.draw_text(str("{:.1f}".format(self.timer)), self.game.lcd_font, 25, WHITE, 700, 55, align="center")

    def update(self):
        self.tick()