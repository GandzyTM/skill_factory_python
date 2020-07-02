import album
from bottle import HTTPError
from bottle import route
from bottle import run


def make_end(number):
    # делаем нормальные окончания для числа альбомов и самого слова альбом
    if number % 10 in [2, 3, 4] and number % 100 not in [12, 13, 14]:
        return "{}-х альбомов".format(number)
    elif number % 10 == 0 or number % 10 in [5, 6, 7, 8, 9] or number % 100 in [11, 12, 13, 14]:
        return "{}-и альбомов".format(number)
    else:
        return "{}-го альбома".format(number)


@route("/albums/<artist>")
def albums(artist):
    """Веб-сервер принимает GET-запросы по адресу /albums/<artist> и выводит на экран сообщение
     с количеством альбомов исполнителя artist и списком названий этих альбомов."""
    albums_list = album.find(artist)
    if not albums_list:
        message = "Альбомов {} не найдено".format(artist)
        result = HTTPError(404, message)
    else:
        album_names = [album.album for album in albums_list]
        # количество и список альбомов, которые записал artist

        result = "Список из {} {}: <br>".format(make_end(len(albums_list)), artist)
        result += " <br>".join(album_names)
    return result


# def save_album(album_data):
#     artist = album_data["artist"]
#     album = album_data["album"]
#     filename = "{}-{}.json".format(artist, album)
#
#     with open(filename, "w") as fd:
#         json.dump(album_data, fd)
#     return filename


# @route("/albums/", method="POST")
# def album():
#     """Веб-сервер принимает POST-запросы по адресу /albums/ и сохраняет переданные пользователем
#     данные об альбоме. Данные передаются в формате веб-формы. Если пользователь пытается передать
#     данные об альбоме, который уже есть в базе данных, обработчик запроса отвечает HTTP-ошибкой 409
#     и выводит соответствующее сообщение."""
#     album_data = {
#         "artist": request.forms.get("artist"),
#         "genre": request.forms.get("genre"),
#         "album": request.forms.get("album")
#     }
#     resource_path = save_album(album_data)
#     print("User saved at: ", resource_path)
#
#     return "Данные успешно сохранены"


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
