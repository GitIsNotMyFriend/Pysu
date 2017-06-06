#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import beatmap_metadata
import settings_parse
import pygame
import create_stage
import arrow_object
import random
import time

NAME = "Pysu!"
VERSION = "0.01-ALPHA"
SCROLL_SPEED = 13

# Directories of files
basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))
beatmaps = os.path.abspath(os.path.join(os.path.dirname(__file__), 'beatmaps'))

# Choose a random beatmap
beatmap_list = beatmap_metadata.beatmap_list(beatmaps)
chosen_beatmap = os.path.join(beatmaps, os.path.abspath(random.choice(beatmap_list)))
beatmap_data = beatmap_metadata.parse_metadata(chosen_beatmap)

ARROWS = beatmap_data.arrows




# Create dir if doesn't exist (used to generate default settings)
if not os.path.isdir(basedir):
    os.mkdir(basedir)


def draw_arrows(arrows):
    """Draw arrows to screen"""
    arrow_images = []
    for i, arrow in enumerate(arrows):
        arrow_y = 595 - 192 * arrow.get_time() / 1000.0 * SCROLL_SPEED + pygame.time.get_ticks() / 1000.0 * SCROLL_SPEED * 592.0 / 192.0
        image_dir = os.path.abspath(arrow_object.arrow_skin(arrow.get_column()))
        arrow_image = pygame.image.load(image_dir)
        arrow_images.append([i, arrow_image])
    return arrow_images


# Load normal key images and create image list
def loadKeyImages():
    image = []
    info_object = pygame.display.Info()
    for i in xrange(4):
        fileunpressed = create_stage.key_image_file(i)
        filepressed = create_stage.keypressed_image_file(i)
        keyunpressed_image = pygame.image.load(fileunpressed)
        keypressed_image = pygame.image.load(filepressed)
        image.append((keyunpressed_image, keypressed_image))
    return image


# Main game init and loop
def main():
    # Get settings from file
    settings = settings_parse.parse(basedir)

    # Get keys from settings
    KEYS = [int(key) for key in settings['keys'].split(",")]

    # Init pygame module
    pygame.init()

    # Init pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(beatmap_data.audio)

    # Set game display (determine fullscreen mode according to settings)
    global info_object
    info_object = pygame.display.Info()
    if bool(int(settings["fullscreen"])):
        os.environ['SDL_VIDEO_WINDOW_POS'] = '1'
        game_display = pygame.display.set_mode((info_object.current_w, info_object.current_h), pygame.NOFRAME)
    else:
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (info_object.current_w/4,10)
        game_display = pygame.display.set_mode((int(settings["width"]),int(settings["height"])), pygame.NOFRAME)
    pygame.display.set_caption(NAME + " - " + VERSION)
    info_object = pygame.display.Info()

    i = 0
    keyImages = loadKeyImages()
    arrow_images = draw_arrows(ARROWS)
    pygame.mixer.music.play(-1)
    t = time.clock()
    # Game run loop
    while 1:
        game_display.fill((0, 0, 0))

        original_height, original_width, ratio = 0, 0, 0
        # Check if players wants to leave game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return



        # Draw images of keys

        for i in xrange(len(keyImages)):
            image = keyImages[i][pygame.key.get_pressed()[KEYS[i]]]
            original_width, original_height = image.get_size()
            ratio = float(info_object.current_h) / original_height
            image = pygame.transform.smoothscale(image, (int(ratio * original_width), int(ratio * original_height)))
            game_display.blit(image, (info_object.current_w / 2 - original_width * ratio * 4 / 2 + i * original_width * ratio, -50))

        for arrow in arrow_images:
            arrow_image = arrow[1]
            arrow_index = arrow[0]
            width, height = arrow_image.get_size()
            arrow_y = 595 + 192 * (pygame.time.get_ticks() - ARROWS[arrow_index].get_time()) / 1000.0 * SCROLL_SPEED / (info_object.current_h / 512.0)
            if abs(pygame.time.get_ticks() - ARROWS[arrow_index].get_time()) > 1500: continue
            arrow_x = 5 + info_object.current_w / 2 - original_width * ratio * 2 + original_width * ratio * (ARROWS[arrow[0]].get_column() - 1)
            arrow_image = pygame.transform.smoothscale(arrow_image, (int(width * ratio * 0.8), int(height * ratio * 0.8)))
            game_display.blit(arrow_image, (arrow_x,arrow_y))

        # Update game and tick game
        pygame.display.update()
        pygame.display.flip()
        pygame.time.delay(1000/60)

# Call main
if __name__ == '__main__':
    main()
