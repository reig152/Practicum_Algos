def broken_search(nums, target):
    """
    В описании задачи было указано соблюсти
    сложность за O(log n), так что был взят принцип
    бинарного поиска с дополнительной проверкой, которая
    осуществляет сдвиг. Пространственная сложность алгоритма
    O(1).
    """
    left = 0
    right = len(nums) - 1

    # цикл продолжается до тех пор, пока возможно
    # осуществлять сдвиг границ отрезка, это означает, что диапазон
    # поиска сузился до нуля, и все возможные места для поиска целевого элемента были проверены.
    while left <= right:
        mid = (left + right) // 2

        # если искомый элемент равен элементу середины массива,
        # то он является искомым числом
        if target == nums[mid]:
            return mid

        # если левая часть массива отсортирована, то выполняется проверка
        if nums[left] <= nums[mid]:
            # если целевой элемент находится в левой части массива,
            # то осуществляется сдвиг влево
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            # в противном случае сдвиг вправо
            else:
                left = mid + 1
        else:
            # аналогичное поведение, если правя часть отсортирована
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


test()
