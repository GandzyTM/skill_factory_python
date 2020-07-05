import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, validates

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
    artist = sa.Column(sa.String)
    genre = sa.Column(sa.TEXT)
    album = sa.Column(sa.TEXT)

    def __init__(self, year, artist, genre, album):
        self.year = year
        self.artist = artist
        self.genre = genre
        self.album = album

    @validates('year')
    # проводим валидацию передаваемых данных в поле year перед записью в БД
    def validate_year(self, key, year):
        if not year:
            raise AssertionError("Год не может быть пустым")
        if len(year) < 4 or len(year) > 4 or not isinstance(int(year), int):
            raise AssertionError("Неверно указан год")
        return year

    @validates('artist')
    # проводим валидацию передаваемых данных в поле artist перед записью в БД
    def validate_artist(self, key, artist):
        if not artist:
            raise AssertionError("Поле артист не может быть пустым")
        return artist

    @validates('album')
    # проводим валидацию передаваемых данных в поле album перед записью в БД
    def validate_album(self, key, album):
        if not album:
            raise AssertionError("Поле альбом не может быть пустым")
        if not isinstance(album, str):
            raise AssertionError("Поле альбом принимает только строковые значения")
        return album


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
    Находит все альбомы в базе данных по заданному полю artist
    """
    # создаем сессию
    session = connect_db()
    # делаем запрос в БД типа (select * from album where artist=? or album=?)
    albums = session.query(Album.album).filter(Album.artist == artist).all()
    # возвращаем список
    return albums

def find_album_artist(album, artist):
    session = connect_db()
    albums_artist = session.query(Album).filter(Album.artist == artist, Album.album == album).all()
    return albums_artist


def add(year, artist, genre, album):
    """Добавляет альбом и данные о нем в БД"""
    # проверяем валидность типов данных
    assert isinstance(year, int)
    assert isinstance(artist, str)
    assert isinstance(genre, str)
    assert isinstance(album, str)

    # создаем сессию
    session = connect_db()
    album_exists = session.query(Album).filter(Album.album == album).first()
    if album_exists is not None:
        raise Exception("Альбом {} уже существует в БД".format(album))

    # если такой альбом существует в списке, который нам передает функция find то возвращаем False
    if len(find_album_artist(album, artist)) > 0:
        return False
    else:
        # в ином случае (True) создаем объект Album
        add_album = Album(year=year, artist=artist, genre=genre, album=album)
        # добавляем объект Album в БД
        session.add(add_album)
        # записываем изменения
        session.commit()
        return True