
def record(name, *args, **kwargs):
    print("\nName : ", name)

    print("\nargs type : ", type(args))
    for item in args:
        print(item, end=", ")

    print("\nkwargs type : ", type(kwargs))
    for key, value in kwargs.items():
        print(key, value)


if __name__ == '__main__':
    record("salim", 34, 23, 89, 111, address='venkatagiri', phone='2222222222')
