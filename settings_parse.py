#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os.path

def parse(dir):
    settings = {}
    if not os.path.isfile(dir + "\settings.data"):
        default_data(dir + "\settings.data")

    settings_file = open(dir + "\settings.data", 'r')

    for line in settings_file.readlines():
        line = line.replace("\n", "")
        field, value = tuple(line.split(": "))
        settings[field] = value

    settings_file.close()
    return settings


def default_data(file):
    settings_file = open(dir + "\settings.data" , 'w')
    settings_file.write("fullscreen: True")

    settings_file.close()
