def make_russian(number):
    if number % 10 in [2,3,4] and number % 100 not in [12,13,14]:
        return "{} студента".format(number)
    elif number % 10 == 0 or number % 10 in [5,6,7,8,9] or number % 100 in [11,12,13,14]:
        return "{} студентов".format(number)
    else:
        return "{} студент".format(number)

def make_end(number):
    if number % 10 in [2,3,4] and number % 100 not in [12,13,14]:
        return "{}-х альбомов".format(number)
    elif number % 10 == 0 or number % 10 in [5,6,7,8,9] or number % 100 in [11,12,13,14]:
        return "{}-и альбомов".format(number)
    else:
        return "{}-го альбома".format(number)


def main():

    # for i in range(30):
    #     print(make_russian(i))

    for i in range(111):
        print(make_end(i))

if __name__ == "__main__":
    main()