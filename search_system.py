"""
Принцип работы. 
На входе формируется хеш-таблица, хранящая информацию о
количестве вхождения слов в документах, что позволяет проверять
только те документы, где слова встречаются. Далее для каждого запроса
вычисляется релевантность документов. По итогу результат сортируется и
выводится.

Временная сложность.
create_hash_table - Обработка каждого документа занимает оценивается
через суммарный размер, так как количество слов может быть разным, таким
образом сложность составляет O(S), где S - сумма размеров документов.

calculate_relevancy - Перебор каждого слова в каждом запросе и получение
всех документов, где эти слова встречаются. Сложность составляет
O(Qmax * D), Qmax - максимальный размер запроса,
D - среднее количество документов, в которых встречается слово.

Пространственная сложность.
Создание первой хеш-таблицы занимает O(W * D), где
W - количество уникальных слов в документах, D - количество документов,
в которых встречаются слова.

Создание хеш-таблицы занимает O(n), так как
таблица создается для каждого документа.
"""

from typing import List, Dict
from collections import defaultdict, Counter
from heapq import nlargest


def create_hash_table(
    documents: List[str]
) -> Dict[str, Dict[int, int]]:
    """
    Создание хеш-таблицы, где ключи - это слова из документов, 
    а значения - словари с ключами в виде номера документа со значением 
    в виде количества вхождений слова в документ.  
    """ 
    hash_table = defaultdict(lambda: defaultdict(int)) 
    for doc_id, doc in enumerate(documents): 
        word_count = defaultdict(int) 
        for word in doc.split(): 
            word_count[word] += 1 
        for word, count in word_count.items(): 
            hash_table[word][doc_id] += count 
    return hash_table 


def calculate_relevancy(
    hash_table: Dict[str, Dict[int, int]], query: set
) -> Dict[int, int]:
    """
    Подсчет релевантности. Создается хеш-таблица
    с ключами в виде номера документа и значением в
    виде подсчитанной релевантности(количество вхождений
    слов из запроса в документе)
    """
    relevancies = Counter()
    for word in query:
        if word in hash_table:
            for doc_id, count in hash_table[word].items():
                relevancies[doc_id] += count
    return relevancies


def form_array(n: int) -> List[str]: 
    """ 
    Формирование входных данных. 
    """ 
    array = [] 
    for _ in range(n): 
        array.append(input())
    return array

def main(): 
    n = int(input()) 
    documents = form_array(n) 
    m = int(input()) 
    # формирование хеш-таблицы 
    hash_table = create_hash_table(documents) 
 
    for _ in range(m): 
        # подсчет релевантности 
        relevancies = calculate_relevancy(
            hash_table, set(input().split())
        ) 

        top_5_docs = nlargest(
            5, relevancies.items(), key=lambda x: (x[1], -x[0])
        )
 
        print(*[doc_id + 1 for doc_id, _ in top_5_docs]) 


if __name__ == "__main__": 
    main() 
