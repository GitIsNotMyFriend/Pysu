import re
import os.path

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))
def key_image_file(col):
    skin_file = open(basedir + "\\noteskin\\skin.ini", "r")
    data= skin_file.read()
    reg = re.compile(r"KeyImage%d: (\w+\\\w+)" % col, re.MULTILINE)
    result = reg.findall(data)
    key_image = result[0]

    return basedir + "\\noteskin\\" + key_image + ".png"
