"""
Design a new data structure where we can perform following operation:
    insert: add x in data structure if x is not present.
    remove: delete x from data structure if x is present.
    search: perform search on data structure and return True if available.
    pickRandom: return a random item from data structure.
"""


class NewDs:
    key = -1
    x_list = []
    x_dict = {}

    def get_key_from_value(self, x):
        for key, value in self.x_dict.items():
            if x == value:
                return key
        return -1

    def insert(self, x):
        if x not in self.x_dict.values():
            self.key += 1
            self.x_list.append(self.key)
            self.x_dict[self.key] = x
        else:
            print("{} is present in ds".format(x))

    def remove(self, x):
        if x in self.x_dict.values():
            key = self.get_key_from_value(x)
            self.x_list.remove(key)
            print('{} is being deleted'.format(self.x_dict.pop(key)))
        else:
            print('{} is not found in ds'.format(x))

    def display(self):
        print('Items: {}'.format(self.x_dict.values()))


if __name__ == '__main__':
    obj = NewDs()
    # insert some data in data structure
    for i in [5, 4, 2, 7]:
        obj.insert(i)
    obj.display()

    obj.insert(4)
    obj.remove(4)
    obj.remove(4)
