import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///../../data/b4_7.sqlite3"
Base = declarative_base()


class Album(Base):
    __tablename__ = "album"
    id = sa.Column(sa.INTEGER, primary_key=True)
    year = sa.Column(sa.INTEGER)
    artist = sa.Column(sa.TEXT)
    genre = sa.Column(sa.TEXT)
    album = sa.Column(sa.TEXT)



def parse_connection_string(connection_string):
    """Принимает на вход строку соединения connection_string и возвращает словарь с ее составными частями"""
    # dialect+driver://username:password@host:port/database
    dict_connection = {'dialect': "", 'driver':"",'username':"", 'password':"", 'host':"", 'port':"", 'database':"" }
    # dialect + driver
    if connection_string.split(":", maxsplit=1)[0].find("+") != -1:
        dict_connection["dialect"] = connection_string.split("+")[0]
        dict_connection["driver"] = connection_string.split("+")[1].split(":", maxsplit=1)[0]
    else:
        dict_connection["dialect"] = connection_string.split(":", maxsplit=1)[0]
    # database + username + password + host + port
    uphpd = connection_string.split("//")[1]
    if uphpd.find(":") != -1:
        if uphpd.find("@") != -1:
            dict_connection["username"] = uphpd.split("@")[0].split(":")[0]
            dict_connection["password"] = uphpd.split("@")[0].split(":")[1]
            if uphpd.split("@")[1].find(":") != -1:
                dict_connection["host"] = uphpd.split("@")[1].split("/")[0].split(":")[0]
                dict_connection["port"] = uphpd.split("@")[1].split("/")[0].split(":")[1]
            else:
                dict_connection["host"] = uphpd.split("@")[1].split("/")[0].split(":")[0]
            dict_connection["database"] = uphpd.split("@")[1].split("/")[1]
        else:
            dict_connection["username"] = uphpd.split(":")[0]
            dict_connection["password"] = uphpd.split(":")[1].split("/")[0]
            dict_connection["database"] = uphpd.split(":")[1].split("/")[1]
    else:
        dict_connection["database"] = connection_string.split("///")[1]
    # print(dict_connection)
    return dict_connection


def main():
    engine = sa.create_engine(DB_PATH)
    Sessions = sessionmaker(engine)
    session = Sessions()
    albums = session.query(Album).all()
    # bionic = Album(year=2010, artist="Christina Aguilera", genre="Rhythm and blues", album="Bionic")
    # heaven_and_earth = Album(year=2010, artist="Kamasi Washington", genre="Jazz", album="Heaven and Earth")
    # session.add(bionic)
    # session.add(heaven_and_earth)
    # session.commit()
    for album in albums:
        print(f"Группа {album.artist} записала альбом {album.album} в {album.year} году.")

    # parse_connection_string("sqlite3:///b4_7.sqlite33")
    # parse_connection_string("postgresql+psycopg22://admin2:12342@localhost2:22/b4_72")
    # parse_connection_string("postgresql+psycopg2://admin:1234@localhost/b4_7")
    # parse_connection_string("m2sql://a2dmin:21234/b24_7")
    # parse_connection_string("m2sql+mmm://admin:1234@localhost:112233/b4_7")
    # parse_connection_string("dialect+driver://username:password@host:port/database")

if __name__ == "__main__":
    main()