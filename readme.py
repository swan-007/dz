documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def people():
    comanda_1 = input("Введите номер документа - ")
    for x in documents:
        if comanda_1 == x["number"]:
            print("Документ пренадлежит :", x["name"])


def shelf():
    com_2 = input("Введите номер документа-")
    for key, val in directories.items():
        if com_2 in val:
            print(f"Номер находится на полке - {key}")


def ne_list():
    print("Список всех документов:")
    for val in documents:
        print(f'{val["type"]} "{val["number"]}" "{val["name"]}"')


def add():
    tip = input("Введите тип документа-")
    nomer = input("Введите номер документа-")
    ima = input("Введите имя владельца-")
    polka = input("На какую полку положить-")
    dic_1 = {"type": tip, "number": nomer, "name": ima}
    documents.append(dic_1)
    directories[polka] = directories.get(polka, []) + [nomer]
    print(f"Данные добавленны в каталог, номер документа добавлен на {polka} ю полку")
    print(documents)
    print(directories)


def request():
    while True:
        Command_Request = input("Какой командой вы бы хотели воспользоваться : p , s, i, a - ")

        if Command_Request == "p":
            people()
        elif Command_Request == "s":
            shelf()
        elif Command_Request == "i":
            ne_list()
        elif Command_Request == "a":
            add()
        break


request()

#ffffffffffffffff

