import pygame
import os


class Tile(pygame.sprite.Sprite):
    def __init__(self, img: str, img_id: int, tile_width: int, tile_height: int, rel_x: int, rel_y: int):
        super().__init__()
        self.image = pygame.image.load(img)
        self.img_id = img_id
        self.image = pygame.transform.scale(self.image, (tile_width, tile_height))
        self.rect = self.image.get_rect()
        self.rel_x = rel_x
        self.rel_y = rel_y

    def update(self, x, y):
        self.rect.x = self.image.get_width() * self.rel_x + x
        self.rect.y = self.image.get_height() * self.rel_y + y


class Tilelayer:
    def __init__(self, tile_images, tile_width, tile_height, tile_placing):
        self.tile_images_path = tile_images
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.tiles = pygame.sprite.Group()
        image_files = os.listdir(self.tile_images_path)
        for index_y, y_layer in enumerate(tile_placing):
            for index_x, x_element in enumerate(y_layer):
                if x_element != " ":
                    my_tile = Tile(img= self.tile_images_path + "//" + image_files[int(x_element)],
                                   tile_width=self.tile_width, tile_height=self.tile_height, rel_x=index_x, rel_y=index_y,
                                   img_id=int(x_element))
                    self.tiles.add(my_tile)

    def colliderrect(self, rect, img_id: str) -> bool:
        for tile in self.tiles.sprites():
            if str(tile.img_id) == img_id:
                if tile.rect.colliderect(rect):
                    return True
        return False

    def spritecollide(self, sprite_group, img_id: str) -> bool:
        for tile in self.tiles.sprites():
            if str(tile.img_id) == img_id:
                if len(pygame.sprite.spritecollide(tile, sprite_group, False)) != 0:
                    return True
        return False

    def draw(self, display, x, y):
        self.tiles.update(x, y)
        self.tiles.draw(display)
