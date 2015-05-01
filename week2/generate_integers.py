from random import randint

import sys


def generate_integers():
    number = int(sys.argv[2])
    text_file = sys.argv[1]
    f = open(text_file, "w")
    contents = []
    for i in range(1, number):
        contents.append(randint(1, number))
    f.write(",".join(map(str, contents)))
    f.write("\n")
    f.close()

if __name__ == '__main__':
    generate_integers()
