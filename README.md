# service_shop
Сервис, который принимает и отвечает на HTTP запросы
Функционал:
В случае успешной обработки сервис должен отвечать статусом 200,
в случае любой ошибки — статус 400.
Сохранение всех объектов в базе данных.
Запросы:
GET /city/ — получение всех городов из базы;
GET /city/<city_id>/street/ — получение всех улиц города; (city_id —
идентификатор города)
POST /shop/ — создание магазина; Данный метод получает json c
объектом магазина, в ответ возвращает id созданной записи.
GET /shop/?street=<street_id>&city=<city_id>&open=0/1 — получение
списка магазинов;
Метод принимает параметры для фильтрации. Параметры не
обязательны. В случае отсутствия параметров выводятся все
магазины, если хоть один параметр есть , то по нему
выполняется фильтрация.
Важно!: в объекте каждого магазина выводится название
города и улицы, а не id записей.
Параметр open: 0 - закрыт, 1 - закрыт. Данный статус
определяется исходя из параметров «Время открытия»,
«Время закрытия» и текущего времени сервера.
