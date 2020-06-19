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
    birthdate = sa.Column(sa.Date)
    height = sa.Column(sa.Float)


def connect_db():
    """
    Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии
    """
    # создаем соединение к базе данных
    engine = sa.create_engine(DB_PATH)
    # создаем описанные таблицы
    Base.metadata.create_all(engine)
    # создаем фабрику сессию
    session = sessionmaker(engine)
    # возвращаем сессию
    return session()


def find_athlete(session):
    user_id = input("Введите id пользователя: ")
    query_id = session.query(User).get(user_id)
    query = session.query(User).filter(User.id == user_id)
    users_cnt = query.count()
    user_ids = [user.id for user in query.all()]
    print(query_id)
    return users_cnt, user_ids


def main():
    find_athlete(connect_db())

if __name__ == "__main__":
    main()
