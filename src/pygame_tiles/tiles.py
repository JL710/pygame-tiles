import pygame
import os


class Tile(pygame.sprite.Sprite):
    def __init__(self, img, rel_x, rel_y):
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rel_x = rel_x
        self.rel_y = rel_y

    def update(self, x, y):
        self.rect.x = self.image.get_height() * self.rel_x + x
        print("check1")


class Tilelayer:
    def __init__(self, tile_images, tile_placing):
        self.tile_images_path = tile_images
        self.tiles = pygame.sprite.Group()
        for file in os.listdir(self.tile_images_path):
            my_tile = Tile(file, 1, 1)
            self.tiles.add(my_tile)
            pass

    def draw(self, display, x, y):
        self.tiles.update(x, y)
        self.tiles.draw(display)

