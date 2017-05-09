#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os.path
import sys
import settings_parse
import pygame

NAME = "Pysu!"
VERSION = "0.01-ALPHA"

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))
beatmaps = os.path.abspath(os.path.join(os.path.dirname(__file__), 'beatmaps'))

if not os.path.isdir(basedir): os.mkdir(basedir)

def main():
    # Get settings from file
    settings = settings_parse.parse(basedir)

    # Init pygame module
    pygame.init()

    # Set game display
    game_display = pygame.display.set_mode((int(settings["width"]),int(settings["height"])))
    if bool(int(settings["fullscreen"])): game_display = pygame.display.set_mode((int(settings["width"]),int(settings["height"])), pygame.FULLSCREEN)
    pygame.display.set_caption(NAME + " - " + VERSION)

    # Game run loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Call main
main()

