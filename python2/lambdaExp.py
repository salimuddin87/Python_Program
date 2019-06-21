
def make_increment(n):
    return lambda x: x + n

if __name__ == '__main__':
    fun1 = make_increment(10)

    print fun1(1)
    print fun1(3)
    print fun1(5)
