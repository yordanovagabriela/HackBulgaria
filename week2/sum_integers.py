from sys import argv


def sum_integers():
    lst = []
    f = open(argv[1], "r")
    for line in f:
        for word in line.split():
            lst.append(int(word))
    print (sum(lst))

if __name__ == '__main__':
    sum_integers()
