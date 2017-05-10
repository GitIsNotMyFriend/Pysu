#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Imports
import os
import sys
import settings_parse
import pygame
import create_stage

# Constants
NAME = "Pysu!"
VERSION = "0.01-ALPHA"

# Directories of files
basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))
beatmaps = os.path.abspath(os.path.join(os.path.dirname(__file__), 'beatmaps'))

# Create dir if doesn't exist (used to generate default settings)
if not os.path.isdir(basedir): os.mkdir(basedir)

# Load normal key images and create image list
def loadKeyImages():
    image = []
    infoObject = pygame.display.Info()
    for i in xrange(4):
        file = create_stage.key_image_file(i)
        key_image = pygame.image.load(file)
        image.append(key_image)
    return image

# Main game init and loop
def main():
    # Get settings from file
    settings = settings_parse.parse(basedir)

    # Get keys from settings
    KEYS = [int(key) for key in settings['keys'].split(",")]

    # Init pygame module
    pygame.init()

    # Set game clock
    clock = pygame.time.Clock()

    # Set game display (determine fullscreen mode according to settings)
    infoObject = pygame.display.Info()
    if bool(int(settings["fullscreen"])):
        os.environ['SDL_VIDEO_WINDOW_POS'] = '1'
        game_display = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), pygame.NOFRAME)
    else:
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (infoObject.current_w/4,10)
        game_display = pygame.display.set_mode((int(settings["width"]),int(settings["height"])), pygame.NOFRAME)
    pygame.display.set_caption(NAME + " - " + VERSION)
    infoObject = pygame.display.Info()

    # Game run loop
    while 1:
        # Get key images list
        keyImages = loadKeyImages()

        # Check if players wants to leave game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Set repeat interval to 60 milliseconds
        pygame.key.set_repeat(60)

        # Get pressed keys and check if keys determined in settings were pressed
        for key in KEYS:
            if pygame.key.get_pressed()[key] == 1:
                # Change image to pressed button
                file = create_stage.keypressed_image_file(KEYS.index(key))
                keyImages[KEYS.index(key)] = pygame.image.load(file)

        # Draw images of keys
        for i, image in enumerate(keyImages):
            original_width, original_height = image.get_size()
            ratio = float(infoObject.current_h) / original_height
            image = pygame.transform.scale(image, (int(ratio * original_width), int(ratio * original_height)))
            game_display.blit(image, (infoObject.current_w / 2 - original_width * ratio * 4 / 2 + i * original_width * ratio, -50))

        # Update game and tick game
        pygame.display.update()
        pygame.display.flip()
        clock.tick(144)

# Call main
main()

