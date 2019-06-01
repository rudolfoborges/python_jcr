from loremipsum import generate_paragraph
from time import sleep
from uuid import uuid5, NAMESPACE_DNS
from datetime import datetime
from os.path import join

INPUT_PATH = './in'

def perform():
    while True:
        file_name = join(INPUT_PATH, str(uuid5(NAMESPACE_DNS, str(datetime.now()))) + '.txt')
        f = open(file_name, "w+")
        for item in range(100):
            _, _, paragraph = generate_paragraph()
            f.write(paragraph)
        f.close()
        print("Created: ", file_name)
        sleep(5)


if __name__ == "__main__":
    perform()