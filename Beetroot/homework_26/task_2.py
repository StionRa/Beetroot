class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Create an empty hash table with buckets

    def __contains__(self, key):
        index = self._hash(key)  # Calculate the key hash
        bucket = self.table[index]  # Getting a segment that may contain the key
        for item in bucket:
            if item[0] == key:  # Check if the key matches
                return True
        return False

    def __len__(self):
        count = 0
        for bucket in self.table:
            count += len(bucket)  # Count the number of elements in each segment
        return count

    def __setitem__(self, key, value):
        index = self._hash(key)  # Calculate the key hash
        bucket = self.table[index] # Getting the segment to add an element to
        for item in bucket:
            if item[0] == key:  # Check if the key already exists in the segment
                item[1] = value  # Replace value if key is already present
                return
        bucket.append((key, value))  # Add a new key-value to a segment

    def _hash(self, key):
        return hash(key) % self.size  # Calculating a key hash using a modular operation


my_table = HashTable(10)
my_table['key1'] = 'value1'
my_table['key2'] = 'value2'
my_table['key4'] = 'value3'
my_table['key5'] = 'value4'
my_table['key6'] = 'value5'
my_table['key3'] = 'value7'

print('key1' in my_table)  # True
print('key3' in my_table)  # False
print(len(my_table))  # 2
print(my_table.table)
