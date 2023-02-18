from settings import *
import pygame as pg
from os import path
import time
game_folder = ""
snd_folder = path.join(game_folder, 'snd')
img_folder = path.join(game_folder, "img")

prologue =   [["One night, a young", "programmer was coding", "his latest creation."],
              ["Debugging all night, he", "was becoming frustrated", "with errors he's seeing."],
              ["Desperate, he wished he", "could enter his computer", "and fix them from the inside."],
              ["Suddenly...", "", ""],
              ["A bright light appeared", "on his computer screen.", ""],
              ["To find his way back to", "the real world, he must solve", "some tricky math problems..."],]

epilogue =  [["As the young programmer", "dodged all the mobs while", "solving complex arithmetics..."],
             ["...he managed to escape", "the digital world!", ""],
             ["When he woke up, he finds", "himself in his own room.", ""],
             ["Checking his source code,", "the errors on his creation", "have finally vanished!"]]

class Story():
    def __init__(self, game):
        self.game = game
        self.current_frame = 0
        self.story_line = []
        self.file_name = ""

    def story_loader(self, story):
        if story == "prologue":
            self.story_line = prologue
            self.file_name = "prologue"
        if story == "epilogue":
            self.story_line = epilogue
            self.file_name = "epilogue"

        pg.mixer.music.load(path.join(snd_folder, f'{self.file_name}.ogg'))
        pg.mixer.music.play()

        self.draw_story()
        self.story_update_loop()

    def story_update_loop(self):
        self.reading = True
        while self.reading:
            self.game.clock.tick(FPS)/1000
            pg.display.flip()
            self.game.all_sprites.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:   
                    self.game.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        self.current_frame += 1
                        self.draw_story()

    def draw_story(self):
        if self.current_frame >= len(self.story_line):
            self.reading = False
            self.game.draw_text("Press SPACE to continue", self.game.undertale_font, 15, WHITE, WIDTH/2, HEIGHT - 75, align="center") 
            return
        self.game.screen.fill(BLACK)
        test = pg.image.load(path.join(img_folder, f"{self.file_name}_{self.current_frame}.png"))
        test_rect = test.get_rect()
        test_rect.center = ((WIDTH/2), 250)
        self.game.screen.blit(test, test_rect)

        string = ""
        i = 0
        snd = pg.mixer.Sound(path.join(snd_folder, 'txt.wav'))
        for lines in self.story_line[self.current_frame]:
            self.game.clock.tick(FPS)/1000
            time.sleep(0.1)
            for char in self.story_line[self.current_frame][i]:
                self.game.screen.fill(BLACK)
                self.game.screen.blit(test, test_rect)
                snd.stop()
                self.game.clock.tick(FPS)/1000
                string = string + char
                if i == 0:
                    self.game.draw_text(string, self.game.undertale_font, 30, WHITE, 175, 425, align="w") 
                if i == 1:
                    self.game.draw_text(self.story_line[self.current_frame][0], self.game.undertale_font, 30, WHITE, 175, 425, align="w") 
                    self.game.draw_text(string, self.game.undertale_font, 30, WHITE, 175, 465, align="w") 
                if i == 2:
                    self.game.draw_text(self.story_line[self.current_frame][0], self.game.undertale_font, 30, WHITE, 175, 425, align="w") 
                    self.game.draw_text(self.story_line[self.current_frame][1], self.game.undertale_font, 30, WHITE, 175, 465, align="w") 
                    self.game.draw_text(string, self.game.undertale_font, 30, WHITE, 175, 505, align="w")
                snd.play()
                time.sleep(0.05)
                pg.display.flip()
                for event in pg.event.get():
                    if event.type == pg.QUIT:   
                        self.game.quit()
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_SPACE:
                            self.draw_skip()
                            self.current_frame += 1
                            self.draw_story()
                            return
            i += 1
            string = ""
        waiting = True
        last_update = pg.time.get_ticks()
        while waiting:
            now = pg.time.get_ticks()
            if now - last_update > 3000:
                self.current_frame += 1
                waiting = False
                self.draw_story()
                return
            self.game.clock.tick(FPS)/1000
            for event in pg.event.get():
                if event.type == pg.QUIT:   
                    self.game.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        self.draw_skip()
                        self.current_frame += 1
                        self.draw_story()
                        return

        self.draw_skip()

    def draw_skip(self):
        self.game.draw_text(self.story_line[self.current_frame][0], self.game.undertale_font, 30, WHITE, 175, 425, align="w") 
        self.game.draw_text(self.story_line[self.current_frame][1], self.game.undertale_font, 30, WHITE, 175, 465, align="w") 
        self.game.draw_text(self.story_line[self.current_frame][2], self.game.undertale_font, 30, WHITE, 175, 505, align="w") 

    def ded_screen(self, reason):
        self.game.playing = False
        pg.mixer.music.stop()

        snd = pg.mixer.Sound(path.join(snd_folder, BSOD))
        snd.play(loops=-1)
        print("ded screen showed")

        self.game.screen.fill(WIN10BLUE)
        self.game.draw_text(f":", self.game.undertale_font, 200, WHITE, 0, 135, align="w")    
        self.game.draw_text(f"(", self.game.undertale_font, 200, WHITE, 50, 150, align="w")    
        self.game.draw_text(f"A fatal exception has occured at \"Bug TIME Rush.exe\". The ", self.game.undertale_font, 20, WHITE, 30, 300, align="w")
        self.game.draw_text(f"current application will be terminated.", self.game.undertale_font, 20, WHITE, 30, 325, align="w")    
        self.game.draw_text(f"Stop code: {reason}", self.game.undertale_font, 20, WHITE, 30, 400, align="w")    
        self.game.draw_text("Press SPACE to terminate the application.", self.game.undertale_font, 20, WHITE, WIDTH/2, 550, align="center") 
        pg.display.flip()
        self.wait_for_key()

        raise Exception("PlayerNotFound: The player has escaped the simulation.")
        
    def wait_for_key(self):
        waiting = True
        while waiting:
            self.game.clock.tick(FPS)/1000
            for event in pg.event.get():
                if event.type == pg.QUIT:   
                    waiting = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        waiting = False
                        return
                    