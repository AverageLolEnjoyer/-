import random

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        # Простейшая хеш-функция для примера
        return hash(key) % self.size

    def rehash(self, key, index):
        # Генерация псевдослучайного числа для рехэширования
        return (index + random.randint(1, self.size-1)) % self.size

    def add(self, key, value):
        index = self.hash_function(key)

        while self.table[index] is not None:
            index = self.rehash(key, index)

        self.table[index] = (key, value)

    def delete(self, key):
        index = self.hash_function(key)

        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return
            index = self.rehash(key, index)
    def get(self, key):
        index = self.hash_function(key)

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = self.rehash(key, index)

        return None
    def resize(self):
        new_capacity = self.capacity * 2  # увеличиваем емкость вдвое
        new_buckets = [None] * new_capacity  # создаем новую таблицу с увеличенной емкостью
        # перехешируем все элементы из старой таблицы в новую
        for i in range(self.capacity):
            node = self.buckets[i]
            while node:
                index = hash(node.key) % new_capacity
                if new_buckets[index]:
                    new_node = new_buckets[index]
                    while new_node.next:
                        new_node = new_node.next
                    new_node.next = Node(node.key, node.value)
                else:
                    new_buckets[index] = Node(node.key, node.value)
                node = node.next
        self.capacity = new_capacity
        self.buckets = new_buckets
# Пример использования
hash_table = HashTable(10)
hash_table.insert("key1", "apple")
hash_table.insert("key2", "banana")

print(hash_table.get("key1"))
print(hash_table.get("key2"))
hash_table.delete("key2")
print("-------------\n", hash_table.get("key2"))



