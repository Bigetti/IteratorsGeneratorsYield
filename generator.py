import types
import os
import datetime




def logger(old_function):

    func_name = old_function.__name__
    print(f"-------Была вызвана Функция {func_name} и для нее будет добавлена запись в лог, ")

    def new_function(*args, **kwargs):

        func_name = old_function.__name__
        print(f"Вызвана функция {func_name}")
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Функция {func_name} была вызвана в {current_time}")

        args_str = ', '.join(map(str, args))
        kwargs_str = ', '.join(f'{k}={v!r}' for k, v in kwargs.items())

        with open('main.log', 'a') as f:
            f.write(f" была вызвана функция {func_name} в {current_time}\n")
            f.write(f'Аргументы: {args_str}, {kwargs_str}\n')

            result = old_function(*args, **kwargs)
            f.write(f'Результат: {result}\n')

        return result

    return new_function


def flat_generator(list_of_lists):

    for i in range(len(list_of_lists)):

        for j in range(len(list_of_lists[i])):

            yield list_of_lists[i][j]


    ...

@logger
def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_generator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_generator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
