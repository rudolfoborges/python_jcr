from os import listdir, stat
from os.path import isfile, join
from datetime import datetime, timedelta
import shutil

INPUT_PATH = './in'
OUTPUT_PATH = './out'

def move():
    limited = datetime.now() - timedelta(minutes = 2)
    files = [f for f in listdir(INPUT_PATH) if isfile(join(INPUT_PATH, f))]
    
    for file in files:
        statinfo = stat(join(INPUT_PATH, file))
        dt_object = datetime.fromtimestamp(statinfo.st_mtime)
        print('Arquivo: ', file, ' | ', dt_object, dt_object <= limited)
        if dt_object <= limited:
            shutil.move(join(INPUT_PATH, file), join(OUTPUT_PATH, file))

if __name__ == "__main__":
    move()