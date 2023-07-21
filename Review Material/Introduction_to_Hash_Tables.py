class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ': ', val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for items in self.data_map[index]:
                if items[0] == key:
                    return items[1]
        return None
    
    def keys(self):
        all_keys = []
        for data in self.data_map:
            if data is not None:
                for items in data:
                    all_keys.append(items[0])
        return all_keys

my_ht = HashTable()
my_ht.set_item('washers', 200)
my_ht.set_item('screws', 1800)
my_ht.set_item('hammers', 20)
my_ht.set_item('bolts', 500)
# my_ht.print_table()
# print(my_ht.get_item('screws'))
print(my_ht.keys())