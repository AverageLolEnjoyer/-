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

    def insert(self, key, value):
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

# Пример использования
hash_table = HashTable(10)
hash_table.insert("key1", "apple")
hash_table.insert("key2", "banana")

print(hash_table.get("key1"))
print(hash_table.get("key2"))
hash_table.delete("key2")
print("-------------\n", hash_table.get("key2"))



