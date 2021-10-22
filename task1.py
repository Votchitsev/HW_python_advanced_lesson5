import datetime


def logger_decorator(function):
    function()
    time = datetime.datetime.now()
    function_name = function.__name__
    log_information_for_writing = f"{function_name} {time}\n"
    with open('log_file.txt', 'a') as log_file:
        log_file.write(log_information_for_writing)


@logger_decorator
def random_function():
    print('Случайная функция вызвана')


@logger_decorator
def random_function_two():
    print('Другая функция для проверки')
