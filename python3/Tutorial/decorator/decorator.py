"""
A Decorator takes in a function, add some functionality and return it.
Decorators add functionality to an existing code called metaprogramming.

"""

def outer(func):
    print("Inside outer function!")
    def inner():
        print("Inside inner function!")
    func()
    return inner()

def ordinary():
    print("I am ordinary function!")

if __name__ == '__main__':
    outer(ordinary)