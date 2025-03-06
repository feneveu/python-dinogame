import pygame as pg


class Bird(pg.sprite.Sprite):
    """creates a bird sprite"""
    def __init__(self, enemy_group, move_speed):
        super(Bird, self).__init__()

        # converting to alpha allows for masking purposes
        self.img_list = [pg.image.load("images/bird1.png").convert_alpha(),
                         pg.image.load("images/bird2.png").convert_alpha()]

        # set the initial image of the bird to bird1
        self.image = self.img_list[0]

        # create a mask so there is detailed pixel collision
        self.mask = pg.mask.from_surface(self.image)

        # this places the rect at 600,180 and the image width and height
        self.rect = pg.Rect(600, 180, self.image.get_width(), self.image.get_height())

        # the anim_counter almost acts as a frame rate, per 8 it changes images
        self.anim_counter = 0

        # the movement speed starts at 250
        self.speed = move_speed

        # shows that this sprite is an enemy
        self.enemy_group = enemy_group

        # next image switch is to image 1
        self.image_switch = 1

    def update(self, dt):
        """update the image of the bird"""

        # if the counter has hit 8 change the image
        if self.anim_counter == 8:
            # switch the image to the next in the list
            self.image = self.img_list[self.image_switch]

            # make the image switch a different value
            if self.image_switch == 0:
                self.image_switch = 1
            else:
                self.image_switch = 0

            # reset from 0 to 8
            self.anim_counter = 0
        # add a count per cycle
        self.anim_counter += 1

        # now move the x value of the bird at a speed * time
        self.rect.x -= self.speed * dt

        # if the right edge of the rectangle is less than - the dino dies
        if self.rect.right < 0:
            self.die()

    def setMoveSpeed(self, move_speed):
        """changes the move speed"""
        self.speed = move_speed

    def die(self):
        """kills the bird"""
        self.kill()
        del self
