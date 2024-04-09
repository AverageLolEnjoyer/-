class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            index = (index + 1) % self.size
        self.keys[index] = key
        self.values[index] = value

    def search(self, key):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        return None

    def delete(self, key):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                return
            index = (index + 1) % self.size

# Пример использования
hash_table = HashTable(10)
hash_table.insert(5, "Coffee")
hash_table.insert(15, "Seven Seas Of Rhye")
hash_table.insert(25, "Polinomy")

print(hash_table.search(15))  # Выведет "Значение 2"
print(hash_table.search(5))   # Выведет "Значение 2"

print(hash_table.search(15))  # Выведет None

hash_table.delete(15)
print("----------------")
for i in range(10):
    print(hash_table.values[i])