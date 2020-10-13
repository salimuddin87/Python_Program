class Dog:
    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance


if __name__ == '__main__':
    d = Dog('Fido')
    e = Dog('Buddy')

    # shared by all dogs instance
    print(d.kind)  # 'canine'
    print(e.kind)  # 'canine'

    # Unique to each instance
    print(d.name)  # 'Fido'
    print(e.name)  # 'Buddy'
