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

        if self.now - self.last_update > 1000:
            self.last_update = self.now
            self.timer -= 1
        
        if self.timer == 0:
            snd = pg.mixer.Sound(path.join(snd_folder, 'hurt.wav'))
            snd.play()
            print("ded")
            self.game.ded_screen("You ran out of time.")
            self.game.new()

    def update(self):
        self.tick()