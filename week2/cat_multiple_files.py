import sys


def read_file():
    if len(sys.argv) > 1:
        for arg in range(1, len(sys.argv)):
            filename = sys.argv[arg]
            a_file = open(filename, "r")
            content = a_file.read()
            print(content)
            a_file.close()
    else:
        print("Give me a file to read!")
if __name__ == '__main__':
    print(read_file())
