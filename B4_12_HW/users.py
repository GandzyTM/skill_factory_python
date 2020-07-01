import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# расположение БД может быть другим
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


def request_data():
    print("Привет! Я запишу твои данные!")
    first_name = input("Введите своё имя: ")
    last_name = input("А теперь фамилию: ")
    gender = input("Ваш пол: ")
    email = input("Мне еще понадобится адрес твоей электронной почты: ")
    birthdate = input("Введите вашу дату рождения в формате гггг-мм-дд: ")
    # birthdate = datetime.datetime.strptime(birthdate_text, '%Y-%m-%d')
    height = input("Введите ваш рост в метрах: ")
    user = User(
        # id=user_id,
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        email=email,
        birthdate=birthdate,
        height=height

    )
    return user


def connect_db():
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()


def main():
    session = connect_db()
    mode = input("Выбери режим.\n1 - найти пользователя по имени\n2 - ввести данные нового пользователя\n")
    if mode == "1":
        name = input("Введи имя пользователя для поиска: ")
        # users_cnt, user_ids, log = find(name, session)
        # print_users_list(users_cnt, user_ids, log)
    elif mode == "2":
        user = request_data()
        session.add(user)
        session.commit()
        print("Спасибо, данные сохранены!")
    else:
        print("Некорректный режим:(")


if __name__ == "__main__":
    main()
