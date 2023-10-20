class FlatIterator:

    def __init__(self, list_of_lists):
        self.data = list_of_lists

    def __iter__(self):
        print("Starting cycle")
        self.outer_index = 0  # Индекс текущего внешнего списка
        self.inner_index = 0  # Индекс текущего элемента во внутреннем списке
        return self

    def __next__(self):
        if self.outer_index<len(self.data):
            if self.inner_index < len(self.data[self.outer_index]):
                # Возвращаем текущий элемент из внутреннего списка
                result = self.data[self.outer_index][self.inner_index]
                self.inner_index +=1
                return result
            else:
                # Переходим к следующему внешнему списку
                self.outer_index +=1
                self.inner_index = 0
                return  next(self)
        else:  # Если все элементы исчерпаны, вызываем исключение StopIteration
            raise StopIteration

        return item

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    # Создаем итератор FlatIterator, который будет использоваться для итерации по списку списков list_of_lists_1.
    # Созданный итератор предоставит доступ к элементам вложенных списков в плоском порядке.
    iterator = FlatIterator(list_of_lists_1)

    # Создаем список ожидаемых значений, которые мы сравним с тем, что возвращает итератор.
    expected_values = ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    # Используем функцию zip, чтобы объединить элементы итератора с ожидаемыми значениями.
    # Теперь у нас есть пары (iterator_value, expected_value).
    # Например, (первый элемент из итератора, 'a') и так далее.
    zipped_values = zip(iterator, expected_values)

    # Теперь мы используем цикл for для итерации по парам значений.
    # На каждой итерации flat_iterator_item будет содержать текущий элемент из итератора,
    # и check_item будет содержать соответствующий ожидаемый элемент.
    for flat_iterator_item, check_item in zipped_values:
        # Мы используем оператор assert, чтобы проверить, что элемент из итератора (flat_iterator_item)
        # равен ожидаемому элементу (check_item).
        assert flat_iterator_item == check_item

    # Если на каждой итерации assert не вызовет исключение AssertionError,
    # это означает, что итератор вернул ожидаемые значения в правильном порядке.


if __name__ == '__main__':
    test_1()