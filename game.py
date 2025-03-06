import pygame as pg
import sys
import time
from dino import Dino
from bird import Bird
from cactus import Cactus
import random

# initializes pygame
pg.init()


class Game:
    def __init__(self):

        # screen settings
        self.width = 600
        self.height = 300
        self.window = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()

        # ground images
        self.ground1 = pg.image.load("images/ground.png").convert_alpha()
        self.ground1_rect = self.ground1.get_rect(center=(300, 250))

        self.ground2 = pg.image.load("images/ground.png").convert_alpha()
        self.ground2_rect = self.ground2.get_rect()
        self.ground2_rect = self.ground2.get_rect(center=(900, 250))

        # Import the font
        self.font = pg.font.Font("pixel_font.ttf", 20)

        # Creates the score counter
        self.label_score = self.font.render("Score: 0", True, (0, 0, 0))
        self.label_score_rect = self.label_score.get_rect(center=(500, 20))

        # Other Labels
        self.label_restart = self.font.render("Restart Game", True, (0, 0, 0))
        self.label_restart_rect = self.label_restart.get_rect(center=(300, 150))

        # create the dino on the window
        self.dino = Dino()

        # game hasn't been lost yet
        self.game_lost = False

        # sets the dinos movement speed
        self.move_speed = 250

        # enemy information
        self.enemy_counter = 0
        self.spawn_time = 80
        self.score = 0
        self.enemy_group = pg.sprite.Group()

        self.gameLoop()


    def checkCollisions(self):
        """checks if the dino has collided with an enemy"""
        # check if sprite collides and if so, stop game
        if pg.sprite.spritecollide(self.dino, self.enemy_group, False, pg.sprite.collide_mask):
            self.stopGame()

    def stopGame(self):
        """ set the game lost attribute to False"""
        self.game_lost = True

    def restart(self):
        """restart the game"""
        # set the game to lost
        self.game_lost = False
        # score resets to 0
        self.score = 0
        # there are no enemies
        self.enemy_counter = 0
        # speed is set to 250
        self.move_speed = 250
        self.label_score = self.font.render("Score: 0", True, (0, 0, 0))
        self.dino.resetDino()

        # kill all enemies in the group
        for enemy in self.enemy_group:
            enemy.die()

    def gameLoop(self):
        """actual game loop"""
        last_time = time.time()
        # compare time

        while True:
            # creates a new time
            new_time = time.time()
            # the difference between last and now
            dt = new_time - last_time

            # set the new time to the last time
            last_time = new_time

            for event in pg.event.get():
                # check all the keys pressed for an action
                # if mode is quit, end game
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                # if it's a key down or space it's an action
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    # if the game hasn't been lost the dino jumps
                    if not self.game_lost:
                        self.dino.jumpDino(dt)
                    else:
                        # otherwise the dino lost and resets
                        self.restart()

            # fill the window with white
            self.window.fill((255, 255, 255))

            # if the game isn't lost move the ground towrd the dino
            if not self.game_lost:
                self.ground1_rect.x -= int(self.move_speed * dt)
                self.ground2_rect.x -= int(self.move_speed * dt)

                # if its off screen reset it
                if self.ground1_rect.right < 0:
                    self.ground1_rect.x = 600
                if self.ground2_rect.right < 0:
                    self.ground2_rect.x = 600

                # increase the score
                self.score += 0.1
                # render the score
                self.label_score = self.font.render(f"Score: {int(self.score)}", True, (0, 0, 0))
                # update hte dino and update all enemies
                self.dino.update(dt)
                self.enemy_group.update(dt)

                # create a random enemy
                if self.enemy_counter == self.spawn_time:
                    # randomly assign a bird or a cactus
                    if random.randint(0, 1) == 0:
                        self.enemy_group.add(Bird(self.enemy_group, self.move_speed))
                    else:
                        self.enemy_group.add(Cactus(self.enemy_group, self.move_speed))
                    # reset enemy to 0
                    self.enemy_counter = 0
                # add an enemy
                self.enemy_counter += 1

                # increase speed per 30 points
                if int(self.score) % 30 == 0:
                    self.move_speed += 5
                    for enemy in self.enemy_group:
                        enemy.setMoveSpeed(self.move_speed)

                #draw the dino image, and rect to the screen
                self.window.blit(self.dino.image, self.dino.rect)
                # add each enemy to the screen
                for enemy in self.enemy_group:
                    self.window.blit(enemy.image, enemy.rect)
                # check if there are any collisions
                self.checkCollisions()
            else:
                # draw the labels
                self.window.blit(self.label_restart, self.label_restart_rect)

            # add the ground/scores
            self.window.blit(self.ground1, self.ground1_rect)
            self.window.blit(self.ground2, self.ground2_rect)
            self.window.blit(self.label_score, self.label_score_rect)
            pg.display.update()
            self.clock.tick(60)


game = Game()
