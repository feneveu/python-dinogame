import pygame as pg


class Dino(pg.sprite.Sprite):
    def __init__(self):
        super(Dino, self).__init__()

        # creates a list of dino moves made up of dino1 and dino2
        self.dino_run_list = [pg.image.load("images/dino1.png").convert_alpha(),
                              pg.image.load("images/dino2.png").convert_alpha()]

        # creates a list of dino crouches
        self.dino_crouch_list = [pg.image.load("images/dino_crouch1.png").convert_alpha(),
                                 pg.image.load("images/dino_crouch2.png").convert_alpha()]

        # set the image to the first fun image
        self.image = self.dino_run_list[0]

        # set good pixel collisions
        self.mask = pg.mask.from_surface(self.image)

        # start the dino off in a reset position
        self.resetDino()

        # the dino has gravity
        self.gravity = 10
        # the jump speed is set to 250
        self.jump_speed = 250

    def update(self, dt):
        """change the dino image"""

        # read the key executes
        keys = pg.key.get_pressed()

        # if it's the down button crouch the dino
        if keys[pg.K_DOWN]:
            self.crouch = True
        else:
            self.crouch = False

        # if the dino is touching the ground continue
        if self.is_on_ground:
            # if the anim count hits 5
            if self.anim_counter == 5:
                # check if crouch
                if self.crouch:
                    # set to crouch
                    self.image = self.dino_crouch_list[self.image_switch]
                    self.rect = pg.Rect(200, 220, self.image.get_width(), self.image.get_height())
                else:
                    # if it's not crouching its running
                    self.image = self.dino_run_list[self.image_switch]
                    self.rect = pg.Rect(200, 200, self.image.get_width(), self.image.get_height())
                self.mask = pg.mask.from_surface(self.image)

                # switch the image counter
                if self.image_switch == 0:
                    self.image_switch = 1
                else:
                    self.image_switch = 0

                # reset the anim counter
                self.anim_counter = 0
            # add a count per repeat
            self.anim_counter += 1
        else:
            # to change the velocity, look at the gravity and multiply by time
            self.velocity_y += self.gravity * dt
            # change the y value of the dino by the velocity
            self.rect.y += self.velocity_y
            # if the y value is greater = to 200 then the dino is back on the ground
            if self.rect.y >= 200:
                self.is_on_ground = True
                self.rect.y = 200

    def jumpDino(self, dt):
        """makes the dino jump"""
        # dino can only jump if it's on the ground
        if self.is_on_ground:
            self.velocity_y = -self.jump_speed * dt
            self.is_on_ground = False

    def resetDino(self):
        """resets the dino's placement"""
        # set the rect to this position
        self.rect = pg.Rect(200, 200, self.image.get_width(), self.image.get_height())
        # set the image switch back to 1
        self.image_switch = 1
        # reset all other attributes
        self.anim_counter = 0
        self.crouch = False
        self.is_on_ground = True
        self.velocity_y = 0