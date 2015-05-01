import sys


def read_file():
    if len(sys.argv) > 1:
        f = open(sys.argv[1], "r")
        contents = f.read()
        f.close
        return contents
    else:
        print("Give me a file to read!")
if __name__ == '__main__':
    print(read_file())
