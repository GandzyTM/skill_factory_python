import collections


def main():

    # TODO Сколько запросов к серверу сделано с IP адреса 79.136.245.135?
    import collections
    FILENAME = "../data/dummy-access.log"
    ipCounter = collections.Counter()
    fp = open(FILENAME)
    for line in fp:
        line_list = line.split()
        line_first = line_list[0]
        ipCounter[line_first] += 1
    print("Count IP: {}".format(ipCounter["79.136.245.135"]))
    print(ipCounter.most_common()[:-10-1:-1]) # минимальное

    dict_ipCounter = dict(ipCounter.most_common())
    print(dict_ipCounter.keys())
    print(round(sum(dict_ipCounter.values()) / len(dict_ipCounter.keys())))

    # print(ip_addr[0])


if __name__ == "__main__":
    main()