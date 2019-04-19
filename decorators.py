def outer(func):
    print "Inside outer function!"
    def inner():
        print "Inside inner function!"
    func()
    return inner()

def ordinary():
    print "I am ordinary function!"

outer(ordinary)
