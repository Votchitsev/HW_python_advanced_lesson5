import datetime


def logger_decorator_with_params(p):
    def logger_decorator(function):
        def wrapper(*args):
            time = datetime.datetime.now()
            function_name = function.__name__
            log_information_for_writing = f"{function_name} {time}\n"
            with open(f'{p}/log_file.txt', 'a') as log_file:
                log_file.write(log_information_for_writing)
            return function(*args)
        return wrapper

    return logger_decorator


path_to_logs = '/home/dmitry/PycharmProjects/HW_python_advanced_lesson5/logs'


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


@logger_decorator_with_params(path_to_logs)
def get_people(doc_num):
    for i in documents:
        if i["number"] == doc_num:
            print(i["name"])


@logger_decorator_with_params(path_to_logs)
def get_shelf(doc_num):
    list_of_documents = [x['number'] for x in documents]
    if doc_num not in list_of_documents:
        print('Такого документа нет!')
    else:
        for i, j in directories.items():
            if doc_num in j:
                print(i)


@logger_decorator_with_params(path_to_logs)
def show_list():
    for i in documents:
        type = i['type']
        number = i['number']
        name = i['name']
        print(f'{type} "{number}" "{name}"')


@logger_decorator_with_params(path_to_logs)
def add_document(type, number, name, shell):
    if shell not in directories.keys():
        print('Такой полки нет!')
    else:
        new_doc = {'type': type, 'number': number, 'name': name}
        documents.append(new_doc)
        directories[shell].append(new_doc['number'])


@logger_decorator_with_params(path_to_logs)
def del_document(doc_num):
    list_of_documents = [x['number'] for x in documents]
    if doc_num not in list_of_documents:
        print('Такого документа нет!')
    else:
        for i in documents:
            if doc_num in i['number']:
                documents.remove(i)
                for i, j in directories.items():
                    if doc_num in j:
                        j.remove(doc_num)


@logger_decorator_with_params(path_to_logs)
def move_document(doc_num, new_shelf):
    list_of_documents = [x['number'] for x in documents]
    if doc_num not in list_of_documents:
        print('Такого документа нет!')
    elif new_shelf not in directories.keys():
        print('Указана несуществующая полка!')
    else:
        for i, j in directories.items():
            if doc_num in j:
                j.remove(doc_num)
        directories[new_shelf].append(doc_num)


@logger_decorator_with_params(path_to_logs)
def add_shelf(num_shelf):
    if num_shelf in directories.keys():
        print('Такая полка уже есть!')
    else:
        directories[num_shelf] = []


@logger_decorator_with_params(path_to_logs)
def main_menu(comand):
    if comand == 'p':
        get_people(input('Введите номер документа: '))
    elif comand == 's':
        get_shelf(input('Введите номер документа: '))
    elif comand == 'l':
        show_list()
    elif comand == 'a':
        add_document(
            input('Введите тип документа: '),
            input('Введите номер документа: '),
            input('Введите имя и фамилию: '),
            input('Введите номер полки: ')
            )

    elif comand == 'd':
        del_document(input('Введите номер документа: '))
    elif comand == 'm':
        move_document(input('Введите номер документа: '),
                        input('Введите полку, на которую нужно переместить документ: ')
                          )
    elif comand == 'as':
        add_shelf(input('Введите номер полки, которую хотите добавить: '))
    print(documents)
    print(directories)


while True:
    main_menu(input('Введите команду: '))
