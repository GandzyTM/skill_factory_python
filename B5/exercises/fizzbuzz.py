def main():
    # for number in range(1, 101):
    #     if number % 3 == 0 and number % 5 == 0:
    #         print ("FizzBuzz")
    #     elif number % 3 == 0:
    #         print("Fizz")
    #     elif number % 5 == 0:
    #         print("Buzz")
    #     else:
    #         print(number)
    #
    # print("-----------------------")
    #
    sum = 0
    for number in range(1, 10000):
        # % returns the remainder so if there
        # is no remainder...
        if not number % 105:
            sum = number + sum
            print("FizzBuzz")
        elif not number % 3:
            sum = number + sum
            print("Fizz")
        elif not number % 5:
            sum = number + sum
            print("Buzz")
        elif not number % 7:
            sum = number + sum
        else:
            print(number)
    print(sum)
    #
    # print("-----------------------")
    #
    # for i in range(1, 101):
    #     print("FizzBuzz"[i * i % 3 * 4:8 - -i ** 4 % 5] or i)
    #
    # print("-----------------------")
    # sum = 0
    # for x in range(1, 1000):
    #     print("Fizz"[x % 3 * 4:] + "Buzz"[x % 5 * 4:])
    #     if x % 3 == 0 and x % 5 == 0:
    #         sum =  x + sum
    # print(sum)



if __name__ == "__main__":
    main()