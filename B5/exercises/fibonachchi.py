def fibonacci(n):
    if n < 3:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))


def time_this(function):
    import time

    def wrapper():
        start = time.time()
        function()
        end = time.time()
        print("Время выполнения составило: {} скунд".format(end - start))

    return wrapper


@time_this
def main():
    result = 0
    for i in range(50):
        a = fibonacci(i)
        if a % 2 == 0:
            result += a
        if a >= 10000000:
            break

    print(result)


if __name__ == "__main__":
    main()
