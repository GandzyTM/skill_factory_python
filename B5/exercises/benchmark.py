def benchmark(function):
    import time

    def wrapper():
        start = time.time()
        function()
        end = time.time()
        print("Время выполнения составило: {} скунд".format(end - start))
        return wrapper

@benchmark
def fetch_webpage():
    import requests
    webpage = requests.get('http://info.cern.ch')

print(fetch_webpage())