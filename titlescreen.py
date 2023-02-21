from settings import *
import pygame as pg
from os import path
import os
game_folder = ""
snd_folder = path.join(game_folder, 'snd')
img_folder = path.join(game_folder, "img")

class TitleScreen():
    # Initializes the Title Screen
    def __init__(self, game):
        self.game = game
        self.title_bg = self.game.title_bg
        self.title_bg_rect = self.title_bg.get_rect()
        self.title_bg_rect.center = ((WIDTH/2), (HEIGHT/2))
        self.game.screen.blit(self.title_bg, self.title_bg_rect)

    # Loads the Title Screen
    def title_loader(self):
        self.game.all_sprites.empty()
        pg.mixer.music.stop()
        snd = pg.mixer.Sound(path.join(snd_folder, START))
        snd.play()
        print("title screen showed")
        
        self.title_logo = TitleLogo(self.game)

        self.game.screen.fill(BLACK)
        
        self.wait_for_key()
        self.game.levelloader.level_loader()

    # Waits for the space key
    def wait_for_key(self):
        waiting = True
        while waiting:
            self.title_bg = self.game.title_bg
            self.title_bg_rect = self.title_bg.get_rect()
            self.title_bg_rect.topleft = (0, 0)
            self.game.screen.blit(self.title_bg, self.title_bg_rect)  
            self.game.clock.tick(FPS)/1000
            self.game.all_sprites.update()
            self.game.all_sprites.draw(self.game.screen)
            self.game.draw_text("Press SPACE to continue", self.game.undertale_font, 25, WHITE, WIDTH/2, 477, align="center")    
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:   
                    self.game.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        waiting = False
                        return
                    
class TitleLogo(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = 2
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        
        self.current_frame = 0
        self.now = pg.time.get_ticks()
        self.last_update = self.now

        self.load_images()
        self.image = self.title_frame[0]
        self.rect = self.image.get_rect()
        self.rect.center = ((WIDTH/2), 150)

    def load_images(self):
        self.title_frame = self.game.title_frame

    def animate(self):
        self.now = pg.time.get_ticks()
        if self.now - self.last_update > 200:
            self.last_update = self.now
            self.current_frame = (self.current_frame + 1) % 8
            self.image = self.title_frame[self.current_frame]

    def update(self):
        self.animate()