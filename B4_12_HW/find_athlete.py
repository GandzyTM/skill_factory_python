import datetime

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///../data/sochi_athletes.sqlite3"
Base = declarative_base()


class User(Base):
    """
    Описываем структуру таблицы USER
    """
    __tablename__ = 'user'
    id = sa.Column(sa.String(36), primary_key=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.Float)


class Athlete(Base):
    """
    Описываем структуру таблицы ATHLETE
    """
    __tablename__ = 'athelete'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    age = sa.Column(sa.Integer)
    birthdate = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    height = sa.Column(sa.Float)
    name = sa.Column(sa.Text)
    weight = sa.Column(sa.Integer)
    gold_medals = sa.Column(sa.Integer)
    silver_medals = sa.Column(sa.Integer)
    bronze_medals = sa.Column(sa.Integer)
    total_medals = sa.Column(sa.Integer)
    sport = sa.Column(sa.Text)
    country = sa.Column(sa.Text)


def connect_db():
    """
    Коннект к БД
    """
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()


def find_athlete(user, session):
    """
    Производит поиск атлета, ближайшего по дате рождения к данному пользователю
    и атлета, ближайшего по росту к данному пользователю.
    Возвращает список с именами и целевыми значениями найденных спортсменов
    :param user:
    :param session:
    :return:
    """
    height_list = [athlete.height for athlete in session.query(Athlete).all()]
    list_of_height_absolute = []
    for height in height_list:
        if isinstance(height, float):  # проверяем валидность данных
            list_of_height_absolute.append(abs(user[1] - height))
        else:
            list_of_height_absolute.append(200)
    result_index = list_of_height_absolute.index(min(list_of_height_absolute))
    target_h = height_list[result_index]
    athlete_near_user_height = []
    session.query(Athlete)
    athlete_temp = session.query(Athlete).filter(Athlete.height == target_h).first()
    athlete_near_user_height.append(athlete_temp.name)
    athlete_near_user_height.append(athlete_temp.height)
    birthdate_list = [athlete.birthdate for athlete in session.query(Athlete).all()]
    user_bd = datetime.datetime.strptime(user[2], '%Y-%m-%d')
    list_of_birthdate_absolute = [abs(user_bd - datetime.datetime.strptime(birthdate, '%Y-%m-%d')) for birthdate in
                                  birthdate_list]
    result_index = list_of_birthdate_absolute.index(min(list_of_birthdate_absolute))
    target_bd = birthdate_list[result_index]
    athlete_temp = session.query(Athlete).filter(Athlete.birthdate == target_bd).first()
    athlete_near_user_height.append(athlete_temp.name)
    athlete_near_user_height.append(athlete_temp.birthdate)
    return athlete_near_user_height


def find_user(id, session):
    """
        Производит поиск пользователя в таблице user по заданному идентифекатору.
    :param id:
    :param session:
    :return:
    """
    user = []
    for id, height, birthdate in session.query(User.id, User.height, User.birthdate).filter(User.id == id):
        user.append(id)
        user.append(height)
        user.append(birthdate)
    if user:
        result = find_athlete(user, session)
        return f'Пользователь с идентификатором {user[0]}. Ближайший к пользователю спортсмен по росту: {result[0]}, его рост {result[1]}. ' \
               f'Ближайший к пользователю спортсмен по дню рождения: {result[2]}, его день рождения {result[3]}'
    else:
        return f"Пользователь с идетификатором {id} не найден."


def main():
    session = connect_db()
    mode = input("Выбери режим.\n1 - поиск ближайшего к пользователю атлета\n")
    if mode == "1":
        user_id = input("Введите id пользователя: ")
        text = find_user(user_id, session)
        print(text)
    else:
        print("Некорректный режим")


if __name__ == "__main__":
    main()
