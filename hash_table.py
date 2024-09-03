""" 
Принцип работы: 
В данной реализации для разрешения коллизий используется метод цепочек, 
то есть в случае коллизии элементы добавляются в список той же ячейки. 
Задано максимальное возможное к-во объектов - простое число, 
слегка большее 10^5, чтобы хеш равномерно высчитывался. 
Хеш вычисляется путем взятия остатка от деления ключа на размер таблицы. 
 
Временная сложность 
Вставка, получение и удаление значений производится за O(1) в среднем случае, 
а в худшем O(n), где n - количество элементов в ячейке при условии, что все элементы будут 
добавлены в одну ячейку. 
 
Пространственная сложность 
Для инициализации хеш-таблицы используется константа 100003, 
значит пространственная сложность составляет O(n), где n - количество 
элементов. 
""" 


class HashTable: 
    def __init__(self, size=100003): 
        self.size = size 
        self.table = [[] for _ in range(size)] 
 
    def hash(self, key): 
        return key % self.size 
 
    def put(self, key, value): 
        index = self.hash(key) 
        bucket = self.table[index] 
 
        for i, (k, v) in enumerate(bucket): 
            if k == key: 
                bucket[i] = (key, value) 
                return 
 
        bucket.append((key, value)) 
 
    def get(self, key): 
        index = self.hash(key) 
        bucket = self.table[index] 
 
        for k, v in bucket: 
            if k == key: 
                print(v)
                return
 
        print(None)
 
    def delete(self, key): 
        index = self.hash(key) 
        bucket = self.table[index] 
 
        for i, (k, v) in enumerate(bucket): 
            if k == key: 
                value = bucket.pop(i)[1] 
                print(value)
                return
 
        print(None)
 
 
def main(): 
    n = int(input()) 
    hash_table = HashTable() 
    for _ in range(n): 
        command = input().split() 
        operation = command[0] 
        
        getattr(hash_table, operation)(
            *map(int, command[1:])
        )


if __name__ == "__main__": 
    main() 
