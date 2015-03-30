import sys


def read_file():
    if len(sys.argv) > 1:
        filename1 = sys.argv[1]
        filename2=sys.argv[2]
        text_file = open(filename, "r")
        text_file.close()

        return text_file.read()
    else:
        print("Give me a file to read!")
if __name__ == '__main__':
    print(read_file())
