import os
import glob
import re
import arrow_object

class beatmap_data(object):

    def __init__(self, audio, title, artist, creator):
        self.audio = audio
        self.title = title
        self.artist = artist
        self.creator = creator
        self.arrows = []

    def add_arrow(self, arrow):
        self.arrows.append(arrow)

    def __repr__(self):
        return self.audio, self.title, self.artist, self.creator

def parse_metadata(folder):
    for file in glob.glob(folder + "/*.osu"):
        file_open = open(file, 'r')
        file_data = file_open.read()
        file_open.close()
        audio = re.search("AudioFilename: (.+\..+)", file_data).group(1)
        audio = os.path.join(os.path.abspath(folder), audio)
        title = re.search("Title:(.+)", file_data).group(1)
        artist = re.search("Artist:(.+)", file_data).group(1)
        creator = re.search("Creator:(.+)", file_data).group(1)

        beatmap = beatmap_data(audio, title, artist, creator)
        arrows_data = file_data[file_data.find("[HitObjects]") + 13: -1].split("\n")
        for arrow in arrows_data:
            arrow_data = tuple(arrow.split(","))
            x = int(arrow_data[0])
            y = int(arrow_data[1])
            time = int(arrow_data[2])
            hit_type = int(arrow_data[3])
            hit_end = arrow_data[4]
            new_arrow = arrow_object.arrowObject(x, y, 3000 + time, hit_type, hit_end)
            beatmap.add_arrow(new_arrow)

        return beatmap


def beatmap_list(folder):
    list = glob.glob(folder + "/*")
    return list


