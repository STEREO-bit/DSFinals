from settings import *
import pygame as pg
import os
import math
import random
from os import path
vec = pg.math.Vector2

game_folder = ""
snd_folder = path.join(game_folder, 'snd')
img_folder = os.path.join(game_folder, "img")

def collision_with_walls(sprite, group, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(sprite, group, False)
            if hits:
                if sprite.vel.x > 0:
                    sprite.pos.x = hits[0].rect.left - sprite.rect.width
                if sprite.vel.x < 0:
                    sprite.pos.x = hits[0].rect.right
                sprite.vel.x = 0
                sprite.rect.x = sprite.pos.x
                # print(f"{sprite} hits wall #{hits[0].name}")

        if dir == 'y':
            hits = pg.sprite.spritecollide(sprite, group, False)
            if hits:
                if sprite.vel.y > 0:
                    sprite.pos.y = hits[0].rect.top - sprite.rect.height
                if sprite.vel.y < 0:
                    sprite.pos.y = hits[0].rect.bottom
                sprite.vel.y = 0
                sprite.rect.y = sprite.pos.y
                # print(f"{sprite} hits wall #{hits[0].name}")

def collision_with_box(sprite, group, dir, vel):
        if dir == 'x':
            hits = pg.sprite.spritecollide(sprite, group, False)
            if hits:
                hits[0].vel.x = vel
                if sprite.vel.x > 0:
                    sprite.pos.x = hits[0].rect.left - sprite.rect.width 
                if sprite.vel.x < 0:
                    sprite.pos.x = hits[0].rect.right
                sprite.rect.x = sprite.pos.x

        if dir == 'y':
            hits = pg.sprite.spritecollide(sprite, group, False)
            if hits:
                hits[0].vel.y = vel
                if sprite.vel.y > 0:
                    sprite.pos.y = hits[0].rect.top - sprite.rect.height
                if sprite.vel.y < 0:
                    sprite.pos.y = hits[0].rect.bottom
                sprite.rect.y = sprite.pos.y

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = 2
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.walking = False
        self.facing = "south"
        self.current_frame = 0
        self.last_update = 0
        self.last_invulnerable_update = 0
        self.load_images()

        self.current_sign = '+'
        self.collected_numbers = 0
        self.holding_key = False
        self.vulnerable = True
        self.lives = 3

        self.image = self.stand_frame
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.on_finish = False

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

    def collision_with_finish(self):
        hits = pg.sprite.collide_rect(self, self.game.finish)
        if hits and not self.on_finish:
            if self.holding_key:
                self.game.level += 1
                snd = pg.mixer.Sound(path.join(snd_folder, NEXT))
                snd.play()
                self.kill()

                if int(self.game.highestlevel[0]) < self.game.level:
                    self.game.highestlevel[0] = self.game.level
                    f = open(path.join(game_folder, 'currentlvl'), "w")
                    f.write(str(f"{self.game.level}"))
                    f.close()

                print(f"*****proceeding to next level = {self.game.level}*****")
                self.game.load_data("lvl\\" + str(self.game.level) + ".tmx")
                self.game.new()
            else:
                snd = pg.mixer.Sound(path.join(snd_folder, NOPE))
                snd.play()
                print(f"{self.holding_key}")
            self.on_finish = True
        if not hits and self.on_finish:
            self.on_finish = False

    def check_match(self):
        if int(self.collected_numbers) == int(self.game.sum):
            for sprite in self.game.numbers:
                sprite.kill()
            for sprite in self.game.sign:
                sprite.kill()
            Key(self.game, self.game.chest.pos.x, self.game.chest.pos.y)
            self.game.chest.kill()
            print("key spawned")
            snd = pg.mixer.Sound(path.join(snd_folder, KEYSPAWNED))
            snd.play()

    def check_vulnerability(self):
        now = pg.time.get_ticks()
        if not self.vulnerable:
            if now - self.last_invulnerable_update > 2000:
                self.vulnerable = True
                print("now vulnerable")

    def draw_player_health(self):
        if self.lives == 3:
            img = self.lives_img[0]
        if self.lives == 2:
            img = self.lives_img[1]
        if self.lives == 1:
            img = self.lives_img[2]
        if self.lives > 3 or self.lives < 0:
            img = self.lives_img[3]
        img_rect = img.get_rect()
        img_rect.topleft = (10, 20)
        self.game.screen.blit(img, img_rect)

    def draw_current_sign(self):
        if self.current_sign == '+':
            img = self.game.arithmetictiles[0]
        if self.current_sign == '-':
            img = self.game.arithmetictiles[1]
        if self.current_sign == 'X':
            img = self.game.arithmetictiles[2]
        if self.current_sign == 'D':
            img = self.game.arithmetictiles[3]
        img_rect = img.get_rect()
        img_rect.topleft = (10, HEIGHT - 45)
        self.game.screen.blit(img, img_rect) 

    def update(self):
        self.animate()
        self.get_keys()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        collision_with_walls(self, self.game.walls, 'x')
        collision_with_walls(self, self.game.turrets, 'x')
        collision_with_box(self, self.game.boxes, 'x', self.vel.x)
        self.rect.y = self.pos.y
        collision_with_walls(self, self.game.walls, 'y')
        collision_with_walls(self, self.game.turrets, 'y')
        collision_with_box(self, self.game.boxes, 'y', self.vel.y)

        self.collision_with_finish()
        self.check_vulnerability()

class Zombie(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = 2
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.facing = "south"
        self.image = game.zombie_stand_frame

        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.last_movement_update = 0
        self.moving = False

        self.radius = ZOMBIE_RADIUS
        self.offset = random.randint(-15, 15)
        self.rotation = 0
        self.distance = [0, 0]
        self.displacement = 0
        self.rect.center = self.pos

    def load_images(self):
        self.stand_frame = self.game.zombie_stand_frame

        self.walk_north_frame = self.game.zombie_walk_north_frame

        self.walk_south_frame = self.game.zombie_walk_south_frame

        self.walk_west_frame =  self.game.zombie_walk_west_frame

        self.walk_east_frame =  self.game.zombie_walk_east_frame

    def animate(self):
        self.now = pg.time.get_ticks()

        if self.moving:
            if self.now - self.last_update > 200:
                self.last_update = self.now
                self.current_frame = (self.current_frame + 1) % 4
                if abs(self.vel.x) > abs(self.vel.y):
                    if self.vel.x < 0:
                        self.image = self.walk_west_frame[self.current_frame]
                        self.facing = "west"
                    else:
                        self.image = self.walk_east_frame[self.current_frame]
                        self.facing = "east"
                else:
                    if self.vel.y < 0:
                        self.image = self.walk_north_frame[self.current_frame]
                        self.facing = "north"
                    else:
                        self.image = self.walk_south_frame[self.current_frame]
                        self.facing = "south"
        if not self.moving:
            self.image = self.stand_frame

    def movement(self):
        self.now = pg.time.get_ticks()
        self.distance = (self.game.player.pos - self.pos)
        self.displacement = math.sqrt((self.distance[0] ** 2) + (self.distance[1] ** 2))

        if self.displacement < self.radius:
            if not self.moving:
                snd = pg.mixer.Sound(path.join(snd_folder, DETECT))
                snd.play()
            self.moving = True

        if self.now - self.last_movement_update > 500:
            self.last_movement_update = self.now
            self.rotation = -self.distance.angle_to(vec(1, 0)) + self.offset

            if self.moving:
                self.vel = vec(ZOMBIE_SPEED, 0).rotate(self.rotation)

        if self.displacement > self.radius:
            self.moving = False
            self.vel = vec(0, 0)

    def collision_with_player(self):
        player = self.game.player

        now = pg.time.get_ticks()   
        hits = pg.sprite.collide_rect(self, player)
        if hits and player.vulnerable:
            snd = pg.mixer.Sound(path.join(snd_folder, HURT))
            snd.play()
            player.vulnerable = False
            player.last_invulnerable_update = now
            player.lives -= 1
            print("invulnerable for 2 seconds.")
            if player.lives == 0:
                print("ded")
                self.game.ded_screen("You have been infested with a virus.")
                self.game.new()
                

    def update(self):
        self.movement()
        self.animate()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        collision_with_walls(self, self.game.walls, 'x')
        collision_with_box(self, self.game.boxes, 'x', self.vel.x)
        self.rect.y = self.pos.y
        collision_with_walls(self, self.game.walls, 'y')
        collision_with_box(self, self.game.boxes, 'y', self.vel.y)

        self.collision_with_player()

class Turret(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = 3
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.now = pg.time.get_ticks()

        self.current_frame = 0
        self.last_firing_update = 0
        self.last_fired = 0
        self.facing = "south"

        self.image = game.turret_stand_frame
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.target = vec(0, 0)
        self.firing = False
        self.shots_fired = 0

        self.radius = TURRET_RADIUS
        self.rotation = 0
        self.distance = [0, 0]
        self.displacement = 0
        self.rect.center = self.pos
        TurretHitbox(game, self.rect)

    def fire(self):
        self.now = pg.time.get_ticks()
        self.distance = (self.game.player.pos - self.pos)
        self.displacement = math.sqrt((self.distance[0] ** 2) + (self.distance[1] ** 2))

        if self.displacement < self.radius:
            if not self.firing:
                snd = pg.mixer.Sound(path.join(snd_folder, DETECT))
                snd.play()
            self.firing = True

        if self.now - self.last_firing_update > 2000:
            self.last_firing_update = self.now
            self.shots_fired = 0
                
        if self.firing and (self.shots_fired < BULLETS_PER_TICK):
            if self.now - self.last_fired > SHOOT_EVERY:
                self.last_fired = self.now
                self.rotation = -self.distance.angle_to(vec(1, 0))
                self.target = vec(1, 0).rotate(self.rotation)

                Bullet(self.game, self.pos, self.target)
                snd = pg.mixer.Sound(path.join(snd_folder, SHOOT))
                snd.play()
                self.shots_fired += 1

        if self.displacement > self.radius:
            self.firing = False

    def update(self):
        self.fire()

class TurretHitbox(pg.sprite.Sprite):
    def __init__(self, game,  rect):
        self.groups = game.all_sprites  
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((12, 13))
        self.rect = self.image.get_rect()

        self.rect.center = rect.center
        self.rect.bottom = rect.bottom

class Bullet(pg.sprite.Sprite):
    def __init__(self, game, pos, dir):
        self.groups = game.all_sprites, game.bullets, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        
        self.game = game
        self.image = game.bullet_img
        self.rect = self.image.get_rect()
        self.pos = vec(pos)
        self.rect.center = pos

        self.vel = dir * BULLET_SPEED

        self.spawn_time = pg.time.get_ticks()

    def collision_with_player(self):
        player = self.game.player

        now = pg.time.get_ticks()   
        hits = pg.sprite.collide_rect(self, player)
        if hits and player.vulnerable:
            snd = pg.mixer.Sound(path.join(snd_folder, HURT))
            snd.play()
            player.vulnerable = False
            player.last_invulnerable_update = now
            player.lives -= 1
            print("invulnerable for 2 seconds.")
            if player.lives == 0:
                print("ded")
                self.game.ded_screen("You have been shot.")
                self.game.new()

    def update(self):
        now = pg.time.get_ticks()

        self.pos += self.vel * self.game.dt
        self.rect.center = self.pos
        if now - self.spawn_time > BULLET_SPAN:
            self.kill()
        hits = pg.sprite.spritecollide(self, self.game.walls, False)
        if hits:
            self.kill()
        self.collision_with_player()

class Flashlight(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = 3
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.now = pg.time.get_ticks()

        self.image = game.flashlight_img
        self.rect = self.image.get_rect()

        self.rect.center = self.game.player.rect.center

    def update(self):
        self.rect.center = self.game.player.rect.center

class Obstacle(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h, name):
        self.groups = game.walls 
        pg.sprite.Sprite.__init__(self, self.groups)

        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.name = name

class Box(pg.sprite.Sprite):
    def __init__(self, game, x, y, name):
        self.groups = game.all_sprites, game.boxes
        pg.sprite.Sprite.__init__(self, self.groups)

        self.game = game

        self.image = game.block_img
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.name = name

    def collision_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x
                print(f"box #{self.name} hits something")

        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y
                print(f"box #{self.name} hits something")

    def update(self):
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        collision_with_walls(self, self.game.walls, 'x')
        self.rect.y = self.pos.y
        collision_with_walls(self, self.game.walls, 'y')
        self.vel = vec(0, 0)

class Chest(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)

        self.game = game

        self.image = game.chest_img
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

class Key(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = 1
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)

        self.game = game

        self.image = game.key_img
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

    def collision_with_player(self):
        hits = pg.sprite.collide_rect(self, self.game.player)
        if hits:
            print("got key!")
            self.game.player.holding_key = True
            self.kill()
            self.game.finish.image = self.game.finish_opened_img
            snd = pg.mixer.Sound(path.join(snd_folder, KEYGET))
            snd.play()
    
    def update(self):
        self.collision_with_player()

class Numbers(pg.sprite.Sprite):
    def __init__(self, game, x, y, number):
        self._layer = 1
        self.groups = game.all_sprites, game.numbers
        pg.sprite.Sprite.__init__(self, self.groups)

        self.game = game
        self.image = game.numbertiles[number]
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.number = number
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
    
    def collected_number(self):
        hits = pg.sprite.collide_rect(self, self.game.player)
        if hits:
            self.calculate(self.number, self.game.player.current_sign)
            self.game.gameclock.timer += 5
            snd = pg.mixer.Sound(path.join(snd_folder, PICK))
            snd.play()
            self.game.player.check_match()
            self.kill()
            print(f"collected {self.number}")

    def calculate(self, number, sign):
        if sign == '+':
            self.game.player.collected_numbers += number
        if sign == '-':
            self.game.player.collected_numbers -= number
        if sign == 'X':
            self.game.player.collected_numbers *= number
        if sign == 'D':
            if number == 0:
                snd = pg.mixer.Sound(path.join(snd_folder, EXPLODE))
                snd.play()
                self.game.ded_screen("The universe has torn apart.")
                self.game.new()
                return
            self.game.player.collected_numbers = int(self.game.player.collected_numbers/number)

    def update(self):
        self.collected_number()

class Sign(pg.sprite.Sprite):
    def __init__(self, game, x, y, sign):
        self._layer = 1
        self.groups = game.all_sprites, game.sign
        pg.sprite.Sprite.__init__(self, self.groups)

        self.game = game
        i = 0

        for symbols in self.game.symbols:
            if symbols == sign:
                self.image = self.game.arithmetictiles[i]
                break
            i += 1
        
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.sign = sign
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

    def collected_sign(self):
        hits = pg.sprite.collide_rect(self, self.game.player)
        if hits:
            self.game.player.current_sign = self.sign
            self.game.gameclock.timer += 3
            snd = pg.mixer.Sound(path.join(snd_folder, SIGN))
            snd.play()
            self.kill()
            print(f"collected {self.sign}")
        
    def update(self):
        self.collected_sign()

class Finish(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = 1
        self.groups = game.all_sprites, game.finish
        self._layer
        pg.sprite.Sprite.__init__(self, self.groups)

        self.game = game
        self.image = game.finish_locked_img
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y