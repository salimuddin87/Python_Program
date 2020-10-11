
def smart_divide(func):
    def inner(a, b):
        print("Divide ",a , "by", b, " : ")
        if b == 0:
            print("oh! Cannot divide!")
            return
        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    return a / b

if __name__ == '__main__':
    print(divide(5, 2))

    # The other way to do same thing
    # divide = smart_divide(divide)
    # print(divide(10, 3))