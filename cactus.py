import pygame as pg
import random


class Cactus(pg.sprite.Sprite):
    def __init__(self, enemy_group, move_speed):
        super(Cactus, self).__init__()

        # make an image list of all the cacti
        self.img_list = []

        # for 1,2,3,4,5 attach this to each cactus image
        for i in range(1, 6):
            self.img_list.append(pg.image.load(f"images/cactus{i}.png").convert_alpha())

        # pick a random cactus for an image
        self.image = self.img_list[random.randint(0, 4)]

        # masks the image to create better pixel collisions
        self.mask = pg.mask.from_surface(self.image)

        # set the rect boundaries and placement
        self.rect = pg.Rect(600, 208, self.image.get_width(), self.image.get_height())

        # set the move speed
        self.speed = move_speed
        # sets this sprite to be in an enemy group
        self.enemy_group = enemy_group

    def update(self, dt):
        """moves the cactus"""
        # moves the cactus at the given speed and multiply by the time passed
        self.rect.x -= self.speed * dt

        # if this rect's right edge is less than 0 kill the sprite
        if self.rect.right < 0:
            self.die()

    def setMoveSpeed(self, move_speed):
        """sets the move speed"""
        self.speed = move_speed

    def die(self):
        """kills the object"""
        self.kill()
        del self
