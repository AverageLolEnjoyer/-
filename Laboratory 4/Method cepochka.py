class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return

# Пример использования
hash_table = HashTable(10)
hash_table.insert(5, "apple")
hash_table.insert(15, "banana")
hash_table.insert(25, "cherry")
hash_table.insert(26,"strawberry")

for i in hash_table.table:
    print(i)
print(hash_table.search(5))  # Вывод: apple
print(hash_table.search(15))  # Вывод: banana
hash_table.delete(5)
print(hash_table.search(5))  # Вывод: None

