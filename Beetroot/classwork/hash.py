# # # Python program to demonstrate working of HashTable
# #
# # hashTable = [[], ] * 10
# #
# #
# # def checkPrime(n):
# #     if n == 1 or n == 0:
# #         return 0
# #
# #     for i in range(2, n // 2):
# #         if n % i == 0:
# #             return 0
# #
# #     return 1
# #
# #
# # def getPrime(n):
# #     if n % 2 == 0:
# #         n = n + 1
# #
# #     while not checkPrime(n):
# #         n += 2
# #
# #     return n
# #
# #
# # def hashFunction(key):
# #     capacity = getPrime(10)
# #     return key % capacity
# #
# #
# # def insertData(key, data):
# #     index = hashFunction(key)
# #     hashTable[index] = [key, data]
# #
# #
# # def removeData(key):
# #     index = hashFunction(key)
# #     hashTable[index] = 0
# #
# #
# # insertData(123, "apple")
# # insertData(432, "mango")
# # insertData(213, "banana")
# # insertData(654, "guava")
# #
# # print(hashTable)
# #
# # removeData(123)
# #
# # print(hashTable)
#
# class HashTable:
#     def __init__(self, size):
#         self.size = size
#         self.keys = [None] * self.size
#         self.values = [None] * self.size
#
#     def _hash_function(self, key):
#         return hash(key) % self.size
#
#     def put(self, key, value):
#         index = self._hash_function(key)
#         while self.keys[index] is not None:
#             if self.keys[index] == key:
#                 self.values[index] = value  # Оновлюємо значення, якщо ключ вже існує
#                 return
#             index = (index + 1) % self.size
#         self.keys[index] = key
#         self.values[index] = value
#
#     def get(self, key):
#         index = self._hash_function(key)
#         while self.keys[index] is not None:
#             if self.keys[index] == key:
#                 return self.values[index]
#             index = (index + 1) % self.size
#         return None
#
# # Приклад використання
#
# # Створення хеш-таблиці
# hash_table = HashTable(10)
#
# # Додавання елементів
# hash_table.put("key1", "value1")
# hash_table.put("key2", "value2")
# hash_table.put("key3", "value3")
#
# # Отримання значень
# print(hash_table.get("key1"))  # Виведе: value1
# print(hash_table.get("key2"))  # Виведе: value2
# print(hash_table.get("key3"))  # Виведе: value3
# print(hash_table.get("key4"))  # Виведе: None
#
# a = "100"
# print(hash(a))

class HashTable:
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for i, (existing_key, existing_value) in enumerate(bucket):
            if existing_key == key:
                # Оновлюємо значення, якщо ключ вже існує
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for existing_key, existing_value in bucket:
            if existing_key == key:
                return existing_value
        return None

    def remove(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for i, (existing_key, existing_value) in enumerate(bucket):
            if existing_key == key:
                del bucket[i]
                return

    def display(self):
        for i, bucket in enumerate(self.buckets):
            print(f'Bucket {i}:')
            for key, value in bucket:
                print(f'  {key}: {value}')


# Приклад використання
hash_table = HashTable(10)

hash_table.put('apple', 'A sweet fruit')
hash_table.put('banana', 'A delicious fruit')
hash_table.put('cat', 'A furry animal')

print(hash_table.get('apple'))  # Виведе: A sweet fruit
print(hash_table.get('banana'))  # Виведе: A delicious fruit
print(hash_table.get('cat'))  # Виведе: A furry animal

hash_table.display()
print(hash(hash_table.get('apple')))
