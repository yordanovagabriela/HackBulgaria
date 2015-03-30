from random import randint

import sys


def generate_integers():
    number = int(sys.argv[2])
    text_file = sys.argv[1]
    f = open(text_file, "w")
    lst = []
    for i in range(1, number):
        lst.append(randint(1, number))
    f.write(",".join(map(str, lst)))
    f.close()

if __name__ == '__main__':
    generate_integers()
