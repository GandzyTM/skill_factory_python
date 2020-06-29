def make_russian(number):
    if number % 10 in [2,3,4] and number % 100 not in [12,13,14]:
        return "{} студента".format(number)
    elif number % 10 == 0 or number % 10 in [5,6,7,8,9] or number % 100 in [11,12,13,14]:
        return "{} студентов".format(number)
    else:
        return "{} студент".format(number)


def main():

    for i in range(30):
        print(make_russian(i))


if __name__ == "__main__":
    main()