"""A. Служба доставки. ID: 137902845."""


def min_platforms(data: list[int], max_weight: int):
    """
    Определяет минимальное количество транспортных платформ,
    необходимое для перевозки всех роботов, описанных в массиве."""
    # Сортируем масив чтобы воспользоваться методом двух указателей.
    sorted_data = sorted(data)
    result = 0
    # Используем метод двух указателей.
    left_pointer = 0
    right_pointer = len(sorted_data) - 1
    while right_pointer >= left_pointer:
        weight_sum = sorted_data[left_pointer] + sorted_data[right_pointer]
        if weight_sum <= max_weight:
            # Увеличиваем счётчик на 1, сумма этих элементов нам подходит.
            left_pointer += 1
        # Увеличиваем счётчик на 1, если число не подходит.
        result += 1
        right_pointer -= 1
    return result


if __name__ == '__main__':
    with open('input.txt', 'r') as file_in:
        data = [int(i) for i in file_in.readline().split()]
        max_weight = int(file_in.readline())
    with open('output.txt', 'w') as file_out:
        file_out.write(str(min_platforms(data, max_weight)))
