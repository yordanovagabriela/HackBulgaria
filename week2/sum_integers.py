from sys import argv


def sum_integers():
    list_of_integers = []
    f = open(argv[1], "r")
    for line in f:
        for word in line.split():
            if word != ' ' and word != '\n':
                list_of_integers.append(int(word))
    print (sum(list_of_integers))

if __name__ == '__main__':
    sum_integers()
