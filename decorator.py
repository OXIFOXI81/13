import datetime

def logger2(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            beg_time = datetime.datetime.now().strftime('%d-%m-%Y время %H:%M:%S')
            res = old_function(*args, **kwargs)

            with open(path, 'a', encoding='utf-8') as file:
                file.write(
                    f"вызов функции: {beg_time} имя функции: {old_function.__name__:15} атрибуты: {args} - {kwargs} результат: {res}\n")

            return res

        return new_function

    return __logger
