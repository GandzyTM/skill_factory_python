def main():
    import time

    # t0 = time.time()
    # for j in range(1000000):
    #     pass
    # t1 = time.time()
    # print("Выполнение заняло %.5f секунд" % (t1 - t0))

    import time

    NUM_RUNS = 10

    avg_time = 0
    for _ in range(NUM_RUNS):
        t0 = time.time()

        ### <<полезный>> код
        for j in range(1000000):
            pass

        t1 = time.time()
        avg_time += (t1 - t0)
    avg_time /= NUM_RUNS
    print("Выполнение заняло %.5f секунд" % avg_time)


if __name__ == "__main__":
    main()
