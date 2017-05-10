#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import settings_parse
import pygame
import create_stage

NAME = "Pysu!"
VERSION = "0.01-ALPHA"

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))
beatmaps = os.path.abspath(os.path.join(os.path.dirname(__file__), 'beatmaps'))

if not os.path.isdir(basedir): os.mkdir(basedir)
def loadKeyImages():
    image = []
    infoObject = pygame.display.Info()
    for i in xrange(4):
        file = create_stage.key_image_file(i)
        key_image = pygame.image.load(file)
        original_width, original_height = key_image.get_size()
        ratio = float(infoObject.current_h) / original_height
        key_image = pygame.transform.scale(key_image, (int(ratio * original_width), int(ratio * original_height)))
        image.append(key_image)
    return image

def main():
    # Get settings from file
    settings = settings_parse.parse(basedir)

    # Init pygame module
    pygame.init()

    # Set game display
    infoObject = pygame.display.Info()
    native_width = infoObject.current_w
    native_height = infoObject.current_h
    os.environ['SDL_VIDEO_WINDOW_POS'] = '1'
    game_display = pygame.display.set_mode((int(settings["width"]),int(settings["height"])))
    if bool(int(settings["fullscreen"])): game_display = pygame.display.set_mode((native_width, native_height), pygame.NOFRAME)
    pygame.display.set_caption(NAME + " - " + VERSION)

    # Game run loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keyImages = loadKeyImages()
        for i, image in enumerate(keyImages):
            original_width, original_height = image.get_size()
            game_display.blit(image, (native_width / 2 - original_width * 4 / 2 + i * original_width, -50))
        pygame.display.update()
        pygame.display.flip()

# Call main
main()

