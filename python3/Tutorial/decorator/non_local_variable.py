def outer_function():
    a = 5

    def inner_function():
        a = 10  # nonlocal a
        print("Inner function a : ", a)
    inner_function()
    print("Outer function a : ", a)


if __name__ == '__main__':
    outer_function()
