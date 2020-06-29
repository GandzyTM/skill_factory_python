import time
from tqdm import tqdm
class Decorator_avg:
    """B5.9 HW with * & **"""
    def __init__(self, num_exec):
        self.num_exec = num_exec

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __call__(self, function):
        def wrapper(*args):
            avg_time = 0
            for _ in tqdm(range(self.num_exec)):
                t0 = time.time()

                function(*args)

                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= self.num_exec
            return "Выполнение задания в среднем занимает %.3f секунд" % avg_time

        return wrapper


def fibonacci(n):
    if n < 3:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))


def avg_decorator(num_exec):
    """B5.9 HW Декоратор с аргументом num_exec для основного декоратора"""
    def avg_time_exec(function):
        def wrapper(arg1, arg2):
            avg_time = 0
            for _ in tqdm(range(num_exec)):
                t0 = time.time()

                function(arg1, arg2)

                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= num_exec
            return "Выполнение задания в среднем занимает %.3f секунд" % avg_time

        return wrapper

    return avg_time_exec


# @avg_decorator(5) # передаем количество проходов функции декоратору (как функция)
@Decorator_avg(5) # декоратор как класс
def find_fib_nums(max_num_of_range, max_num_of_end):
    result = 0
    for i in range(max_num_of_range):
        a = fibonacci(i)
        if a % 2 == 0:
            result += a
        if a >= max_num_of_end:
            break
    return result


def main():
    print(find_fib_nums(50, 10000000))
    # передаем 1 аргументом до какой цифры функция Фибоначчи будет проводить свои действия
    # 2 аргументом передается лимит суммы получающихся чисел


if __name__ == "__main__":
    main()
