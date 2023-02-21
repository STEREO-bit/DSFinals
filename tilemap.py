import pygame as pg
import pytmx
from settings import *

class TiledMap:
    # Initilizes the dimensions of the map
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True) 
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    # Render the map per tile
    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tileheight, 
                                            y * self.tmxdata.tilewidth))

    # Return the whole map and display to the screen
    def makemap(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface     

class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        
        self.width = width
        self.height = height

    # Apply the camera to the player
    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    # Move the camera when the player moves
    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)

    # Update the position of the camera
    def update(self, target):
        x = -target.rect.x + int(WIDTH/2)
        y = -target.rect.y + int(HEIGHT/2)

        x = min(0, x)
        y = min(0, y)

        x = max(-(self.width - WIDTH), x)
        y = max(-(self.height - HEIGHT), y)
        self.camera = pg.Rect(x, y, self.width, self.height)
