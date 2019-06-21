def outer_function():
    a = 5
    def inner_function():
        #nonlocal a
        a = 10
        print "Inner function a : ", a
    inner_function()
    print "Outer function a : ", a

outer_function()
