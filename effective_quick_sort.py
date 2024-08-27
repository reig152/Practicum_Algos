class Members:
    """
    Создан класс участников, который хранит в себе
    информацию: логин, к-во задач, к-во штрафов
    Переопределен метод сравнения "меньше чем" для
    того, чтобы сравнение по количеству задач происходило
    в порядке убывания для правильной сортировки.
    """
    def __init__(self, login, tasks, penalties):
        self.login = login
        self.tasks = int(tasks)
        self.penalties = int(penalties)
    
    def key(self):
        return (
            -self.tasks, self.penalties, self.login
        )

    def __lt__(self, another: 'Members'):
        return self.key() < another.key()

    def __str__(self):
        return self.login


def partition(array, start, end):
    """
    Функция partition, которая разделяет массив
    Не используется дополнительная память, что
    делает сортировку "эффективной". Для этого
    изначальный массив делится на отрезки, а в качестве
    результата возвращается индекс элемента, на котором
    правый и левый указатели встретились.
    Принял решение приравнять опорный элемент к значению правого
    указателя, так как опорный элемент будет переставлен при
    соблюдении условий функции.
    """
    pivot = array[end]
    while start != end:
        if array[start] < pivot:
            start += 1
        else:
            if array[end] > pivot:
                end -= 1
            else:
                array[start], array[end] = array[end], array[start]

    return start


def quick_sort(
    array, start = 0,
    end = None
):
    """
    Функция быстрой сортировки. Временная сложность
    быстрой сортировки O(n log n), в худшем случае n**2.
    Пространственная сложность O(n) в худшем случае, в лучшем
    O(log n) для стека вызовов рекурсии.
    """

    if end is None:
        # устанавливается правый указатель
        end = len(array) - 1
    if start > end:
        # базовый случай рекурсии
        # если левый указатель больше правого,
        # тогда отрезок отсортирован
        return

    index_pivot = partition(array, start, end)
    quick_sort(array, start, index_pivot - 1)
    quick_sort(array, index_pivot + 1, end)


def main():
    amount = int(input())
    members = []
    for _ in range(amount):
        members.append(Members(*input().split()))
    
    quick_sort(members)
    print(*members, sep='\n')


if __name__ == '__main__':
    main()
