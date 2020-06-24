import uuid
import datetime

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///../data/sochi_athletes.sqlite3"
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = sa.Column(sa.String(36), primary_key=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.Float)


class Athlete(Base):
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
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()


# TODO Напишите модуль find_athlete.py поиска ближайшего к пользователю атлета. Логика работы модуля такова:
# запросить идентификатор пользователя;
# если пользователь с таким идентификатором существует в таблице user, то вывести на экран двух атлетов: ближайшего по дате рождения к данному пользователю и ближайшего по росту к данному пользователю;
# если пользователя с таким идентификатором нет, вывести соответствующее сообщение.

def find_athlete(session):
    query = session.query(Athlete, User).filter(Athlete.height.between(User.height + '0.1', User.height - '0.1')).filter(Athlete.birthdate.between(User.birthdate + '2', User.birthdate - '2'))
    athletes_count = query.count()
    athletes_ids = [athlete_id for athlete_id in query.all()]
    print(query)
    return (athletes_ids, athletes_count)


def user_exist(id, session):
    if session.query(User).filter(User.id == id).count() == 1:
        return True
    else:
        return False


def print_users_list(athlete_ids, count):
    if athlete_ids:
        print("Найдено атлетов: ", count)
        for athlete_id in athlete_ids:
            print("{}".format(athlete_id))
    else:
        print("Атлетов, примерно подходящих по параметрам, не найдено.")


def main():
    session = connect_db()
    user_id = input("Введите id пользователя: ")
    user_exist(user_id, session)
    if user_exist(user_id, session):
        athlete_ids, count = find_athlete(session)
        print_users_list(athlete_ids, count)
    else:
        print(f"Пользователя с идентификатором {user_id} не найдено.")


if __name__ == "__main__":
    main()
