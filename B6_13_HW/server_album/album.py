import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

try:
    # способ соединения с БД
    DB_PATH = "sqlite:///albums.sqlite3"
except FileNotFoundError as err:
    print('Файл базы данных не найден', err)

# описываем базовый класс моделей таблиц
Base = declarative_base()

class Album(Base):
    """
    Описывает структуру таблицы album для хранения записей музыкальной библиотеки
    """
    # задаем название таблицы
    __tablename__ = "album"
    # задаем необходимые колонки
    id = sa.Column(sa.INTEGER, primary_key=True)
    year = sa.Column(sa.INTEGER)
    artist = sa.Column(sa.TEXT)
    genre = sa.Column(sa.TEXT)
    album = sa.Column(sa.TEXT)


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


def find(artist):
    """
    Находит все альбомы в базе данных по заданному артисту
    """
    # создаем сессию
    session = connect_db()
    # делаем запрос в БД типа (select * from album where artist=?)
    albums = session.query(Album).filter(Album.artist == artist).all()
    # возвращаем список
    return albums

def add(year, artist, genre, album):
    """Добавляет альбом и данные о нем в БД"""
    # создаем сессию
    session = connect_db()
    # если такой альбом существует в списке, который нам передает функция find то возвращаем False
    if album in find(artist):
        return False
    else:
        # в противном случае (True) создаем объект Album
        add_album = Album(year=year, artist=artist, genre=genre, album=album)
        # добавляем объект Album в БД
        session.add(add_album)
        # записываем изменения
        session.commit()
        return True