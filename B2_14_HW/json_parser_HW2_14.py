import json
import collections

FILE_NAME1 = "data/data_3000.json"
counter = collections.Counter()


def json_filter():
    """ Исключаем ключи detectedDuplicate и detectedCorruption """
    for line in listLines:
        line = json.loads(line)
        if not line["detectedDuplicate"] and not line["detectedCorruption"]:
            json_list.append(line)


json_file = open(FILE_NAME1, encoding='utf-8')
listLines = json_file.readlines()
json_list = []
json_filter()
json_file.close()

# число различных браузеров среди всех клиентов
listJson = []
for line in json_list:
    listJson.append(line["userAgentName"])
print("Count browsers: {}".format(len(collections.Counter(listJson))))

# Сумма всех item_price у событий itemBuyEvent
sum_item_price = 0
for listLine in json_list:
    if listLine["eventType"] == "itemBuyEvent":
        sum_item_price += listLine["item_price"]
print("Sum item_price = {}".format(sum_item_price))

# Найдите число уникальных значений для поля item_id у событий itemFavEvent
for line in json_list:
    if line['eventType'] == 'itemFavEvent':
        counter[line['item_id']] += 1
print("Count unique elements for itemFavEvent: {}".format(len(counter)))

# Укажите уникальный item_id товара лайкнутого 1359 раз
print("Most likely: ")
for agent, count in counter.most_common():
    print("{} --> {}".format(agent, count))

print("Most unlikely: ")
for agent, count in counter.most_common()[:-10-1:-1]:
    print("{} --> {}".format(agent, count))
