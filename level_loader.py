from settings import *
import pygame as pg
from tilemap import *
import os
from os import path
vec = pg.math.Vector2

game_folder = ""
snd_folder = path.join(game_folder, 'snd')
img_folder = os.path.join(game_folder, "img")

class LevelLoader():
    def __init__(self, game):
        self.game = game

    def level_loader(self):
        print("picking level...")
        for sprite in self.game.all_sprites:
            sprite.kill()
        self.game.all_sprites.empty()
        self.level_floor = TiledMap(path.join(game_folder, 'lvl\\level.tmx'))
        self.level_floor_img = self.level_floor.makemap()
        self.level_floor_rect = self.level_floor_img.get_rect()
        self.game.level_tiles = pg.sprite.Group()

        level = 0
        for tile_object in self.level_floor.tmxdata.objects:
            if tile_object.name == 'player':
                self.game.player = LevelPlayer(self.game, tile_object.x, tile_object.y)
            if tile_object.name == 'level':
                Levels(self.game, tile_object.x, tile_object.y, level)

                level += 1

        self.game.camera = Camera(self.level_floor.width, self.level_floor.height)
        self.level_load_update_loop()

    def level_load_update_loop(self):
        self.picking = True
        while self.picking:
            self.draw_level_sprites()
            self.game.clock.tick(FPS)/1000
            pg.display.flip()
            self.game.all_sprites.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:   
                    self.game.quit()

    def draw_level_sprites(self):
        self.game.screen.blit(self.level_floor_img, self.game.camera.apply_rect(self.level_floor_rect))
        self.game.draw_text(f"Select a level.", self.game.title_font, 20, RED, WIDTH/2 , HEIGHT - 100, align="center")
        if self.game.player.on_block == True:
            self.game.draw_text(f"Not yet unlocked!", self.game.title_font, 30, RED, WIDTH/2, HEIGHT - 150, align="center")
        for sprite in self.game.all_sprites:
            self.game.screen.blit(sprite.image, self.game.camera.apply(sprite))

class LevelPlayer(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = 2
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.walking = False
        self.facing = "south"
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.on_block = False

        self.image = self.stand_frame
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.pos = vec(x, y)

    def load_images(self):
        self.stand_frame = self.game.player_stand_frame

        self.walk_north_frame = self.game.player_walk_north_frame

        self.walk_south_frame = self.game.player_walk_south_frame

        self.walk_west_frame  = self.game.player_walk_west_frame

        self.walk_east_frame  = self.game.player_walk_east_frame 

        self.lives_img        = self.game.player_lives_img

    def get_keys(self):
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vel.x = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vel.x = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel.y = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel.y = PLAYER_SPEED

    def animate(self):
        now = pg.time.get_ticks()
        self.walking = False
        if self.vel.x != 0 or self.vel.y != 0:
            self.walking = True

        if self.walking:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % 4
                if self.vel.x > 0:
                    self.image = self.walk_east_frame [self.current_frame]
                    self.facing = "east"
                elif self.vel.x < 0:
                    self.image = self.walk_west_frame [self.current_frame]
                    self.facing = "west"
                elif self.vel.y > 0:
                    self.image = self.walk_south_frame[self.current_frame]
                    self.facing = "south"
                elif self.vel.y < 0:
                    self.image = self.walk_north_frame[self.current_frame]
                    self.facing = "north"

        if not self.walking:
            if self.facing == "east":
                self.image = self.walk_east_frame[0]
            elif self.facing == "west":
                self.image = self.walk_west_frame[0]
            elif self.facing == "south":
                self.image = self.walk_south_frame[0]
            elif self.facing == "north":
                self.image = self.walk_north_frame[0]

    def collision_with_level(self):
        hits = pg.sprite.spritecollide(self, self.game.level_tiles, False)
        if hits:
            if int(self.game.highestlevel[0]) < hits[0].level and not self.on_block:
                self.on_block = True
                snd = pg.mixer.Sound(path.join(snd_folder, NOPE))
                snd.play()
            elif not self.on_block:
                self.game.picking = False
                self.game.level = hits[0].level
                print(f"****level {hits[0].level}****")
                pg.mixer.music.load(path.join(snd_folder, BGM))
                pg.mixer.music.play(loops=-1) 
                self.game.new()
                
        if not hits:
            self.on_block = False

    def update(self):
        self.animate()
        self.get_keys()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

        self.collision_with_level()

class Levels(pg.sprite.Sprite):
    def __init__(self, game, x, y, level):
        self._layer = 1
        self.groups = game.all_sprites, game.level_tiles
        pg.sprite.Sprite.__init__(self, self.groups)

        self.game = game
        self.level = level
        self.image = pg.image.load(path.join(img_folder, f'level{self.level}.png'))
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y