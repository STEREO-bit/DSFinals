import pygame as pg
import sys
import traceback
from os import path
from settings import *
from sprites import *
from tilemap import *
from gameclock import *
from level_loader import *

game_folder = ""
snd_folder = path.join(game_folder, 'snd')
img_folder = os.path.join(game_folder, "img")

class Game:
    # Initiate pygame program
    def __init__(self):
        print("initializing pygame...")
        pg.init()
        pg.mixer.init()
        pg.font.init()
        self.load_images()
        self.title_font = path.join(img_folder, FONT)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.dt = self.clock.tick(FPS)/1000
        self.running = True
        self.level = 0
        self.collected_numbers = 0

        self.all_sprites = pg.sprite.LayeredUpdates()
        self.symbols = ['+', '-', 'X', 'D']
        self.highestlevel = 0
        pg.mixer.music.set_volume(0.5)
        self.levelloader = LevelLoader(self)

        self.highestlevel = []
        if os.path.isfile(path.join(game_folder, "currentlvl")):
            with open(path.join(game_folder, 'currentlvl'), 'rt') as f:
                for line in f:
                    self.highestlevel.append(line.strip())
            f.close()
        else:
            f = open(path.join(game_folder, 'currentlvl'), "w+")
            f.write('0')
            self.highestlevel.append(0)
            f.close()

    # Load every single image in one go.
    def load_images(self):
        print("loading images")
        self.player_stand_frame = pg.image.load(path.join(img_folder, PLAYER_STAND))

        self.player_walk_north_frame = [pg.image.load(path.join(img_folder, PLAYER_WALK_N_0)), 
                                        pg.image.load(path.join(img_folder, PLAYER_WALK_N_1)), 
                                        pg.image.load(path.join(img_folder, PLAYER_WALK_N_2)), 
                                        pg.image.load(path.join(img_folder, PLAYER_WALK_N_3))]

        self.player_walk_south_frame = [pg.image.load(path.join(img_folder, PLAYER_WALK_S_0)), 
                                        pg.image.load(path.join(img_folder, PLAYER_WALK_S_1)), 
                                        pg.image.load(path.join(img_folder, PLAYER_WALK_S_2)), 
                                        pg.image.load(path.join(img_folder, PLAYER_WALK_S_3))]

        self.player_walk_west_frame =  [pg.image.load(path.join(img_folder, PLAYER_WALK_W_0)), 
                                        pg.image.load(path.join(img_folder, PLAYER_WALK_W_1)), 
                                        pg.image.load(path.join(img_folder, PLAYER_WALK_W_2)), 
                                        pg.image.load(path.join(img_folder, PLAYER_WALK_W_3))] 

        self.player_walk_east_frame =  [pg.image.load(path.join(img_folder, PLAYER_WALK_E_0)), 
                                        pg.image.load(path.join(img_folder, PLAYER_WALK_E_1)), 
                                        pg.image.load(path.join(img_folder, PLAYER_WALK_E_2)), 
                                        pg.image.load(path.join(img_folder, PLAYER_WALK_E_3))]

        self.player_lives_img        = [pg.image.load(path.join(img_folder, LIVES3)),
                                        pg.image.load(path.join(img_folder, LIVES2)),
                                        pg.image.load(path.join(img_folder, LIVES1)),
                                        pg.image.load(path.join(img_folder, MORELIVES))]

        self.zombie_stand_frame = pg.image.load(path.join(img_folder, ZOMBIE_STAND))

        self.zombie_walk_north_frame = [pg.image.load(path.join(img_folder, ZOMBIE_WALK_N_0)), 
                                        pg.image.load(path.join(img_folder, ZOMBIE_WALK_N_1)), 
                                        pg.image.load(path.join(img_folder, ZOMBIE_WALK_N_2)), 
                                        pg.image.load(path.join(img_folder, ZOMBIE_WALK_N_3))]

        self.zombie_walk_south_frame = [pg.image.load(path.join(img_folder, ZOMBIE_WALK_S_0)), 
                                        pg.image.load(path.join(img_folder, ZOMBIE_WALK_S_1)), 
                                        pg.image.load(path.join(img_folder, ZOMBIE_WALK_S_2)), 
                                        pg.image.load(path.join(img_folder, ZOMBIE_WALK_S_3))]

        self.zombie_walk_west_frame =  [pg.image.load(path.join(img_folder, ZOMBIE_WALK_W_0)), 
                                        pg.image.load(path.join(img_folder, ZOMBIE_WALK_W_1)), 
                                        pg.image.load(path.join(img_folder, ZOMBIE_WALK_W_2)), 
                                        pg.image.load(path.join(img_folder, ZOMBIE_WALK_W_3))] 

        self.zombie_walk_east_frame =  [pg.image.load(path.join(img_folder, ZOMBIE_WALK_E_0)), 
                                        pg.image.load(path.join(img_folder, ZOMBIE_WALK_E_1)), 
                                        pg.image.load(path.join(img_folder, ZOMBIE_WALK_E_2)), 
                                        pg.image.load(path.join(img_folder, ZOMBIE_WALK_E_3))]

        self.turret_stand_frame = pg.image.load(path.join(img_folder, TURRET_STAND))

        self.bullet_img         = pg.image.load(path.join(img_folder, BULLET_IMG))

        self.arithmetictiles        =  [pg.image.load(path.join(img_folder, PLUS)), 
                                        pg.image.load(path.join(img_folder, MINUS)), 
                                        pg.image.load(path.join(img_folder, CROSS)), 
                                        pg.image.load(path.join(img_folder, OBELUS))]

        self.numbertiles            =  [pg.image.load(path.join(img_folder, ZERO)), 
                                        pg.image.load(path.join(img_folder, ONE)), 
                                        pg.image.load(path.join(img_folder, TWO)), 
                                        pg.image.load(path.join(img_folder, THREE)), 
                                        pg.image.load(path.join(img_folder, FOUR)), 
                                        pg.image.load(path.join(img_folder, FIVE)), 
                                        pg.image.load(path.join(img_folder, SIX)), 
                                        pg.image.load(path.join(img_folder, SEVEN)), 
                                        pg.image.load(path.join(img_folder, EIGHT)), 
                                        pg.image.load(path.join(img_folder, NINE)), 
                                        pg.image.load(path.join(img_folder, TEN)),]

        self.block_img = pg.image.load(path.join(img_folder, BLOCK))

        self.chest_img = pg.image.load(path.join(img_folder, CHEST))

        self.key_img   = pg.image.load(path.join(img_folder, KEY))

        self.finish_locked_img = pg.image.load(path.join(img_folder, FINISH_LOCKED))

        self.finish_opened_img = pg.image.load(path.join(img_folder, FINISH_OPENED))

        self.flashlight_img = pg.image.load(path.join(img_folder, FLASHLIGHT))

    # Loads the level's data
    def load_data(self, level):
        print("loading data...")
        try:
            print("loading map")
            self.map = TiledMap(path.join(game_folder, level))
        except:
            self.throw_exception(f"FileNotFoundException: No .tmx file has been provided for level {self.level}.")

        self.game_details = []
        with open(path.join(game_folder, 'lvl\\level_details'), 'rt') as f:
            for line in f:
                split = line.split(',')
                self.game_details.append(split)   
        f.close()

        try:
            print(f"game details: {self.game_details[self.level]}")
            self.sum = self.game_details[self.level][0]
            self.seconds = self.game_details[self.level][1]
        except:
            self.throw_exception(f"IndexError: Some level details has not been provided for level {self.level}.")

        if not self.sum.isnumeric():
            self.throw_exception(f"ValueError: {self.sum} is not an integer.")
        if int(self.sum) == 0:
            self.throw_exception("ZeroException: Sum cannot be 0.")

        self.map_img = self.map.makemap()
        self.map_rect = self.map_img.get_rect()

        print(f"total needed: {self.sum}")
        print(f"clock: {self.seconds}")

        # self.map = Map(path.join(game_folder, level))
        
    # This creates new level
    def new(self):
        print("creating new level...")
        self.all_sprites.empty()
        
        self.load_data("lvl\\" + str(self.level) + ".tmx")
        self.mobs = pg.sprite.Group()
        self.turrets = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.boxes = pg.sprite.Group()
        self.buttons = pg.sprite.Group()
        self.numbers = pg.sprite.Group()
        self.sign = pg.sprite.Group()
        self.finish = pg.sprite.Group()

        i = 0
        j = 0
        has_player = False
        has_chest = False
        has_finish = False

        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'player':
                self.player = Player(self, tile_object.x, tile_object.y)
                has_player = True
            if tile_object.name == 'zombie':
                Zombie(self, tile_object.x, tile_object.y)
            if tile_object.name == 'turret':
                Turret(self, tile_object.x, tile_object.y)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height, i)
                i += 1
            if tile_object.name == 'block':
                Box(self, tile_object.x, tile_object.y, j)
                j += 1
            if tile_object.name == 'chest':
                self.chest = Chest(self, tile_object.x, tile_object.y)
                has_chest = True
            if tile_object.name == 'finish':
                self.finish = Finish(self, tile_object.x, tile_object.y)
                has_finish = True
            if tile_object.name == 'flashlight':
                self.flashlight = Flashlight(self, tile_object.x, tile_object.y)
            if tile_object.name in self.symbols:
                Sign(self, tile_object.x, tile_object.y, tile_object.name)
            if str(tile_object.name).isnumeric():
                Numbers(self, tile_object.x, tile_object.y, int(tile_object.name))

        if not has_player:
            self.throw_exception(f"PlayerObjectException: No player object has been provided on {self.level}.tmx.")
        if not has_chest:
            self.throw_exception(f"ChestObjectException: No chest object has been provided on {self.level}.tmx.")
        if not has_finish:
            self.throw_exception(f"FinishObjectException: No finish object has been provided on {self.level}.tmx.")

        self.gameclock = GameClock(self, int(self.seconds))
        self.camera = Camera(self.map.width, self.map.height)
        self.run()

    # This will run the level
    def run(self):
        print("running...")
        self.playing = True
        while self.playing:
            # Tick clock according to how many frames per seconds
            self.dt = self.clock.tick(FPS)/1000
            self.events()
            self.update()
            self.draw_sprites()
        print("unrunning...")

    # This will update which sprite's data changed
    def update(self):
        self.gameclock.update()
        self.all_sprites.update()
        self.camera.update(self.player)

    # Then draw them after it updates
    def draw_sprites(self):
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        self.draw_hud() 
        pg.display.flip()

    # Draws the HUD of the game
    def draw_hud(self):
        self.player.draw_player_health()
        self.player.draw_current_sign()
        self.draw_text("total needed:", self.title_font, 20, RED, WIDTH - 10, HEIGHT - 65, align="se")
        self.draw_text(str(f"{self.player.collected_numbers}/{self.sum}"), self.title_font, 50, RED, WIDTH - 10, HEIGHT - 10, align="se")
        self.draw_text(str(self.gameclock.timer), self.title_font, 50, RED, WIDTH - 10  , 10, align="ne")
        if self.player.on_finish == True:
            self.draw_text("You don't have the key!", self.title_font, 50, RED, WIDTH/2, HEIGHT/2, align="center")
        
    # This creates and draws texts
    def draw_text(self, text, font_name, size, color, x, y, align="nw"):
        font = pg.font.Font(font_name, size)    
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "nw":
            text_rect.topleft = (x, y)
        if align == "ne":
            text_rect.topright = (x, y)
        if align == "sw":
            text_rect.bottomleft = (x, y)
        if align == "se":
            text_rect.bottomright = (x, y)
        if align == "n":
            text_rect.midtop = (x, y)
        if align == "s":
            text_rect.midbottom = (x, y)
        if align == "e":
            text_rect.midright = (x, y)
        if align == "w":
            text_rect.midleft = (x, y)
        if align == "center":
            text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    # Catch events here
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.pause_screen()
                if event.key == pg.K_n:
                    self.level += 1
                    print(f"****next level = {self.level}****")
                    self.new()
                if event.key == pg.K_b:
                    self.level -= 1
                    print(f"****previous level = {self.level}****")
                    self.new()
                if event.key == pg.K_F5:
                    print(f"****reset level = {self.level}****")
                    self.new()
                if event.key == pg.K_END:
                    self.ded_screen("A mysterious god took your soul.")
                    self.new()

    # Displays the Start Screen
    def start_screen(self):
        pg.mixer.music.load(path.join(snd_folder, TITLEBGM))
        pg.mixer.music.play(loops=-1)
        print("title screen showed")

        self.screen.fill(BLACK)
        self.draw_text(TITLE, self.title_font, 80, WHITE, WIDTH/2, 200, align="center")
        self.draw_text("Press SPACE to continue!", self.title_font, 48, WHITE, WIDTH/2, HEIGHT/2, align="center")    
        pg.display.flip()
        self.wait_for_key()
        self.levelloader.level_loader()

    # Display the Ded Screen
    def ded_screen(self, reason):
        pg.mixer.music.stop()
        snd = pg.mixer.Sound(path.join(snd_folder, BSOD))
        snd.play()
        print("ded screen showed")

        self.screen.fill(BLUE)
        square = pg.Surface((100, 20))
        square.fill(WHITE)
        square_rect = square.get_rect()
        square_rect.center = ((WIDTH/2), (HEIGHT/2 - 100))
        self.screen.blit(square, square_rect)
        self.draw_text("GLaDOS", self.title_font, 20, BLUE, WIDTH/2, HEIGHT/2 - 100, align="center")
        self.draw_text(f"A fatal exception has occured at level {self.level}. The current player", self.title_font, 20, WHITE, 30, 275, align="w")    
        self.draw_text(f"will be eliminated.", self.title_font, 20, WHITE, 30, 300, align="w")    
        self.draw_text(f"Traceback: {reason}", self.title_font, 20, WHITE, 30, 365, align="w")    
        self.draw_text("Press SPACE to retry the level.", self.title_font, 20, WHITE, WIDTH/2, 450, align="center")  
        self.draw_text("Press ESC to reboot.", self.title_font, 20, WHITE, WIDTH/2, 475, align="center")  
        pg.display.flip()
        self.wait_for_key()

        snd.stop()
        pg.mixer.music.load(path.join(snd_folder, BGM))
        pg.mixer.music.play(loops=-1) 

    # Displays the Pause Screen
    def pause_screen(self):
        snd = pg.mixer.Sound(path.join(snd_folder, PAUSE))
        snd.play()
        self.dim_screen = pg.Surface(self.screen.get_size()).convert_alpha()
        self.dim_screen.fill((0,0,0,155))
        self.screen.blit(self.dim_screen, (0, 0))
        self.draw_text("Paused", self.title_font, 48, WHITE, WIDTH/2, HEIGHT/2, align="center")    
        self.draw_text("Press SPACE to resume.", self.title_font, 20, WHITE, WIDTH/2, 450, align="center")  
        self.draw_text("Press F5 to retry the level.", self.title_font, 20, WHITE, WIDTH/2, 475, align="center")  
        self.draw_text("Press ESC to go to title screen.", self.title_font, 20, WHITE, WIDTH/2, 500, align="center")  
        pg.display.flip()
        self.wait_for_key()
        snd.stop()

    # Throw exceptions
    def throw_exception(self, exception):
        # this is too much effort for a throw_exception() screen. thank you toby fox.
        pg.mixer.music.load("snd\\throw.ogg")
        pg.mixer.music.play(loops=-1)

        self.screen.fill(BLACK)
        self.draw_text(exception, self.title_font, 15, RED, WIDTH/2, HEIGHT - 100, align="center")
        self.draw_text("Press SPACE to crash the game and save the traceback.txt file.", self.title_font, 15, RED, WIDTH/2, HEIGHT - 50, align="center")
        self.draw_text("Press ESC to return to title screen.", self.title_font, 15, RED, WIDTH/2, HEIGHT - 25, align="center")
        dog = pg.image.load(path.join(game_folder, "img\\annoyingdog.png"))
        dog_rect = dog.get_rect()
        dog_rect.center = ((WIDTH/2), (HEIGHT/2))
        self.screen.blit(dog, dog_rect)
        pg.display.flip()
        self.wait_for_key()

        with open('traceback.txt', 'w+') as f:
            traceback.print_exc(file=f)

        raise Exception(exception)

    # Waits for the user keypress
    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)/1000
            for event in pg.event.get():
                if event.type == pg.QUIT:   
                    self.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        waiting = False
                    if event.key == pg.K_F5:
                        waiting = False
                        self.load_data("lvl\\" + str(self.level) + ".tmx")
                        self.new()
                    if event.key == pg.K_ESCAPE:
                        waiting = False
                        pg.mixer.stop()
                        self.start_screen()
                
    # Call function if the user wants to quit the game
    def quit(self):
        pg.quit()
        sys.exit()

# Starts the game
g = Game()
g.start_screen()

while g.running:
    g.new()