class Deque:
   """
   Реализована стурктура данных дек.
   Эта структура позволяет и добавлять, и извлекать
   элементы с обоих концов.
   В реализации используется кольцевой буфер, который устанавливает
   максимальный размер дека.

   Реализован следующий интерфейс:
   1. deque - сам массив данных, с длиной n
   2. head - начало дека
   3. tail - конец дека
   4. max_n - максимальная длина дека
   5. size - текущий размер дека
   6. is_empty - проверяет дек на пустоту
   7. push/pop back/front - добавляет либо извлекает элементы
   в конец или начало дека, со смещением начала или хвоста.

   -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
   Имея начало и конец дека, вставка и удаление происходит за O(1), то есть
   мы не передвигаем все элементы на одну позицию.

   -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
   В данной реализации используется кольцевой буфер, который предполагает
   наличие n элементов, при инициализации создается список из n элементов,
   значит сложность составляет O(n)
   """
   def __init__(self, n):
      self.deque = [None] * n
      self.head = 0
      self.tail = 1
      self.max_n = n
      self.size = 0

   def is_empty(self):
      return self.size == 0

   def push_back(self, value):
      if self.size != self.max_n:
         self.deque[self.tail] = value
         self.tail = (self.tail + 1) % self.max_n
         self.size += 1
      else:
         print('error')

   def push_front(self, value):
      if self.size != self.max_n:
         self.deque[self.head] = value
         self.head = (self.head - 1) % self.max_n
         self.size += 1
      else:
         print('error')

   def pop_front(self):
      if self.is_empty():
         print('error')
         return
      self.head = (self.head + 1) % self.max_n
      value = self.deque[self.head]
      self.deque[self.head] = None
      self.size -= 1
      print(value)

   def pop_back(self):
      if self.is_empty():
         print('error')
         return
      self.tail = (self.tail - 1) % self.max_n
      value = self.deque[self.tail]
      self.deque[self.tail] = None
      self.size -= 1
      print(value)


def main():
   amount = int(input())
   max_size = int(input())
   d = Deque(max_size)
   for _ in range(amount):
      m, *arg = input().split()
      if arg:
         arg = map(int, arg)
      getattr(d, m)(*arg)


if __name__ == "__main__":
   main()
