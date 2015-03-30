import sys


def read_file():
    if len(sys.argv) > 1:
        for arg in range(1, len(sys.argv)):
            filename = sys.argv[arg]
            file = open(filename, "r")
            content = file.read()
            print(content)
            file.close()
    else:
        print("Give me a file to read!")
if __name__ == '__main__':
    print(read_file())
