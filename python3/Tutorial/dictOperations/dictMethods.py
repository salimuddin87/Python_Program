
if __name__ == '__main__':
    # dict.clear()
    d = {'a': 10, 'b': 20, 'c': 30}
    d.clear()
    print("d.clear() : ", d)

    # d.get(<key> [, <default>])
    d = {'a': 10, 'b': 20, 'c': 30}
    print(d.get('b'))
    print(d.get('z', 0))

    # d.items() outut:- [('a', 10), ('c', 30), ('b', 20)]
    print(d.items())

    # d.keys() and d.values()
    print(d.keys())
    print(d.values())

    # d.pop(<key>[, <default>]) Removes a key from a dictionary,
    # if it is present, and returns its value.
    print("d.pop('a', -1) : ", d.pop('a', -1))

    # d.popitem() Removes a key-value pair from a dictionary.
    print("d.popitem() : ", d.popitem())
    print("d items: ", d)

    # d.update(<obj>) Merges a dictionary with another dictionary
    # or with an iterable of key-value pairs.
    d1 = {'a': 10, 'b': 20, 'c': 30}
    d2 = {'b': 200, 'd': 400}
    d1.update(d2)
    print("d1.update(d2) : ", d1)
