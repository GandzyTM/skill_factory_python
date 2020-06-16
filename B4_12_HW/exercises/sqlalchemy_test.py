import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///../../data/b4_7.sqlite3"
Base = declarative_base()

class Album(Base):
    """Описывает структуру таблицы album для хранения записей музыкальной библиотеки"""
    __tablename__ = "album"
    id = sa.Column(sa.INTEGER, primary_key=True)
    year = sa.Column(sa.INTEGER)
    artist = sa.Column(sa.TEXT)
    genre = sa.Column(sa.TEXT)
    album = sa.Column(sa.TEXT)

def parse_connection_string(connection_string):
    """Принимает на вход строку соединения connection_string и возвращает словарь с ее составными частями"""




def main():
    engine = sa.create_engine(DB_PATH)
    Sessions = sessionmaker(engine)
    session = Sessions()
    albums = session.query(Album).all()
    # print(len(albums))
    for album in albums:
        print(f"Группа {album.artist} записала альбом {album.album} в {album.year} году.")

if __name__ == "__main__":
    main()