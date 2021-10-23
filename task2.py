import datetime


def logger_decorator_with_params(p):

    def logger_decorator(function):

        def wrapper():
            function()
            time = datetime.datetime.now()
            function_name = function.__name__
            log_information_for_writing = f"{function_name} {time}\n"
            with open(f'{p}/log_file.txt', 'a') as log_file:
                log_file.write(log_information_for_writing)

        return wrapper

    return logger_decorator


path_to_logs = '/home/dmitry/PycharmProjects/HW_python_advanced_lesson5/logs'


@logger_decorator_with_params(path_to_logs)
def random_function():
    print('Случайная функция вызвана')


@logger_decorator_with_params(path_to_logs)
def random_function2():
    print('Случайная функция 2 вызвана.')


random_function2()

