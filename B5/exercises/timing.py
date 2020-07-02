# func_runtimes = {}
# def profile(method):
#     import time
#     """ Profiling decorator. """
#     def wrapper(*args, **kw):
#         start_time = time.time()
#
#         result = method(*args, **kw)
#
#         elapsed_time = time.time() - start_time
#         func_runtimes.setdefault(method.__name__, []).append(elapsed_time)
#         return result
#     return wrapper  # Decorated method (need to return this).
#
# def print_stats(method_name):
#     if method_name not in func_runtimes:
#         print("{!r} wasn't profiled, nothing to display.".format(method_name))
#     else:
#         runtimes = func_runtimes[method_name]
#         total_runtime = sum(runtimes)
#         average = total_runtime / len(runtimes)
#         print('Stats for method: {!r}'.format(method_name))
#         print('  run times: {}'.format(runtimes))
#         print('  total run time: {}'.format(total_runtime))
#         print('  average run time: {}'.format(average))


def avg_time_exec(num_runs):
    import time
    from tqdm import tqdm

    NUM_RUNS = num_runs

    avg_time = 0
    for _ in tqdm(range(NUM_RUNS)):
        t0 = time.time()

        ### <<полезный>> код
        for j in range(1000000):
            pass

        t1 = time.time()
        avg_time += (t1 - t0)
        # print(t1 - t0)
    avg_time /= NUM_RUNS
    print("Выполнение задания в среднем занимает %.5f секунд" % avg_time)


def main():

    avg_time_exec(10)


if __name__ == "__main__":
    main()
