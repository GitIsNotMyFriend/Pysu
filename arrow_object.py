TOTAL_COL = 4
WIDTH = 512


class arrowObject(object):
    def __init__(self, x, y, time, hit_type, hit_end):
        self.x = x
        self.y = y
        self.time = time
        self.hit_type = hit_type
        self.hit_end = hit_end

    def get_column(self):
        xbase = WIDTH / TOTAL_COL
        minus = WIDTH / 2 / TOTAL_COL
        return (self.x + minus) / xbase

    def get_time(self):
        return self.time


def arrow_skin(column):
    if column == 1:
        file_open = "left"
    if column == 2:
        file_open = "down"
    if column == 3:
        file_open = "up"
    if column == 4:
        file_open = "right"

    return "data/noteskin/Arrownote/%s.png" % file_open
