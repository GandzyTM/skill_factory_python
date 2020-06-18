import json
import os
# Импортируем модуль стандартной библиотеки time
import time
import uuid

# путь к файлу с данными пользователей
USERS_DATA_FILE_PATH = "../../data/users.json"
# путь к файлу с данными о времени последнего посещения пользователя
LOG_DATA_FILE_PATH = "../../data/last_seen_log.json"


class Users:
    """
    Класс реализует логику для работы с данными о пользователях
    """

    def __init__(self):
        self.users = self.read()

    def read(self):
        """
        Читает JSON документ с диска
        """
        # проверяем наличие файла на диске
        if not os.path.exists(USERS_DATA_FILE_PATH):
            # возвращаем пустой список, если файл еще не создан
            return []

        # открываем файл на чтение
        with open(USERS_DATA_FILE_PATH) as fd:
            # заргружаем JSON документ
            users = json.load(fd)
        # возвращаем список пользователей
        return users

    def save(self):
        """
        Сохраняет список пользователей JSON файле на диск
        """
        # открываем файл на запись
        with open(USERS_DATA_FILE_PATH, "w") as fd:
            # сохраняем список пользователей на диск
            json.dump(self.users, fd)

    def find(self, name):
        """
        Ищет среди списка всех зарегистированных пользователей пользователя
        с именем name и возвращает его идентификатор. Если пользователь не найден, возвращает None.
        """
        for user in self.users:
            # проверям совпадение имени
            if user["first_name"] == name:
                # если имя совпало, возвращаем идентификатор пользователя
                return user["id"]

    def add_user(self, user_data):
        """
        Добавляет данные пользователя user_data в список всех пользователей и сохраняет обновленный список
        """
        self.users.append(user_data)
        self.save()


def request_data():
    """
    Запрашивает у пользователя данные и добавляет их в список users
    """
    # выводим приветствие
    print("Привет! Я запишу твои данные!")
    # запрашиваем у пользователя данные
    first_name = input("Введи своё имя: ")
    last_name = input("А теперь фамилию: ")
    email = input("Мне еще понадобится адрес твоей электронной почты: ")
    # генерируем идентификатор пользователя и сохраняем его строковое представление
    user_id = str(uuid.uuid4())
    # создаем словарь пользователя
    user = {
        "id": user_id,
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }
    # возвращаем созданного пользователя
    return user


class LastSeenLog:
    """
    Класс хранит журнал последней активности пользователей
    """

    def __init__(self):
        self.log = self.read()

    def read(self):
        """
        Читает JSON документ с диска
        """
        # проверяем наличие файла на диске
        if not os.path.exists(LOG_DATA_FILE_PATH):
            # возвращаем пустой словарь, если файл еще не создан
            return {}

        # открываем файл на чтение
        with open(LOG_DATA_FILE_PATH) as fd:
            # заргружаем JSON документ
            log = json.load(fd)

        # возвращаем список пользователей
        return log

    def save(self):
        """
        Сохраняет журнал времени посещения пользователей
        """
        # открываем файл на запись
        with open(LOG_DATA_FILE_PATH, "w") as fd:
            # сохраняем список пользователей на диск
            json.dump(self.log, fd)

    def update_timestamp(self, user_id):
        """
        Обновляет время последнего посещения
        """
        # получаем текущее значение времени с помощью функции time
        current_timestamp = time.time()
        # сохраняем его в журнал для данного пользователя
        self.log[user_id] = current_timestamp
        # сохраняем журнал
        self.save()

    def find(self, user_id):
        """
        Возвращает время последнего визита пользователя с идентификатором user_id
        """
        # проверяем наличие пользователя с заданным идентификатором
        if user_id in self.log:
            # если такой пользователь есть в журнале, возвращаем время его последней активности
            return self.log[user_id]


def main():
    """
    Осуществляет взаимодействие с пользователем, обрабатывает пользовательский ввод
    """
    users = Users()
    last_seen_log = LastSeenLog()
    # просим пользователя выбрать режим
    mode = input(
        "Выбери режим.\n1 - найти пользователя по имени\n2 - ввести данные нового пользователя\n")
    # проверяем режим
    if mode == "1":
        # выбран режим поиска, запускаем его
        name = input("Введи имя пользователя для поиска: ")
        user_id = users.find(name)
        if user_id:
            last_seen = last_seen_log.find(user_id)
            print("Найден пользователь с идентификатором: ", user_id)
            print("Timestamp последней активности пользователя: ", last_seen)
        else:
            print("Такого пользователя нет.")
    elif mode == "2":
        user_data = request_data()
        # добавляем нового пользователя в список всех пользователей
        users.add_user(user_data)
        # обновляем время последнего визита для этого пользователя
        last_seen_log.update_timestamp(user_data["id"])
        print("Спасибо, данные сохранены!")
    else:
        print("Некорректный режим:(")


if __name__ == "__main__":
    main()
